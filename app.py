from flask import Flask,request,jsonify,render_template,jsonify
from clickhouse_driver import Client
import pandas as pd
from flask_jsonpify import jsonpify
from werkzeug.exceptions import BadRequest

client = Client(host='34.70.65.12', user = "default", password = "lead#2019", database = "OrionLead")

app = Flask(__name__)


@app.route("/home", methods=['POST'])
def newscore():
   try:
      content = request.get_json(silent=True)

      user_id = str(content['UserId'])
      game_id = str(content['GameId'])
      new_score = str(content['Score'])
      
      client.execute('INSERT INTO SpilScoreboard(GameId,UserId,Score) VALUES',[(game_id,user_id,new_score)])
      res = {'Inserted New Score to the Database':True}
      return jsonify(res), 200
   except:
      raise BadRequest()

@app.route("/ranking",methods=["POST"])
def ranking(): 
  try:
      content = request.get_json(silent=True)
      game_id = str(content['GameId'])
      user_id = str(content['UserId'])
    
      ranking_query = """select *,rowNumberInBlock() + 1 as ranking from(select UserId from SpilScoreboard where GameId = '{}'order by toInt32(Score) desc )""".format(game_id)

      result, columns = client.execute(ranking_query, with_column_types=True)
      df = pd.DataFrame(result, columns=[tuple[0] for tuple in columns])
      rank = df.query('UserId=="{}"'.format(user_id)).iloc[0]
     
      data = {'your_ranking': int(rank[1])}#"Here is your Ranking!: {}".format(rank[1])
   
      return jsonify(data), 200
  except:
      raise BadRequest()
   



@app.route("/highscores", methods=['GET','POST'])
def highscores():
   try:
      content = request.get_json(silent=True)
      game_id = str(content['GameId'])
      highscores_query = "select UserId from SpilScoreboard where GameId = '{}'  order by toInt32(Score) desc limit 3".format(game_id)
      
      result, columns = client.execute(highscores_query, with_column_types=True)
      df = pd.DataFrame(result, columns=[tuple[0] for tuple in columns])
      
      if(content['GameId'] > 5):
         raise BadRequest()

      df_list = df.values.tolist() # This sends back the values as JSON 
      top_3 = jsonpify(df_list) # JSONPIFY

      response = {'first player_id': df_list[0],
                  'second player_id': df_list[1],
                  'third player_id': df_list[2]}

      return jsonify(response),200 #render_template('scoreboard.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)
   except:
      raise BadRequest()
  

   

@app.route("/", methods=['GET','POST'])
def hello():
   return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')