def log2dict(lines): #log 형식: [005930][Epoch 0001/1000] Epsilon:1.0000 #Expl.:248/248 #Buy:80 #Sell:70 #Hold:98 #Stocks:1867 PV:151,298,150 Loss:151572.202313 ET:0.4847
    ret_json = {}
    lines = lines.strip("'").split("\\n")
    for line in lines:
        line = line.strip().split(" ")
        try:
            name, epoch = " ".join(line[:2]).strip("[").strip("]").split("][")
        except:
            print(line)
        epoch = epoch.replace("/", "_").replace(" ", "_")[6:10]
        if not ret_json.get(name):
            ret_json[name] = {}
        ret_json[name]
        ret_json[name][epoch] = {}
        t_dict = ret_json[name][epoch]
        for chunk in line[2:]:
            k, v = chunk.split(":")
            t_dict[k] = v.replace(",", "")
    return ret_json

def lineparser(lines):
    stdout, log = lines.split("[--log--]")
    log = log.replace("', '", "")
    log = log.strip("'")
    return stdout.strip().strip("[").strip("]"), log.strip().strip("[").strip("]")

import pymysql
class db_controller:
  def __init__(self, host, user, pw, db):
    self.conn = pymysql.connect(host=host, user=user, password=pw, db=db, charset="utf8", cursorclass=pymysql.cursors.DictCursor)
    self.cur = self.conn.cursor()

  def get_cursor(self):
    return self.cur
  def get_conn(self):
    return self.conn