def utility_processor():
  def tax(price):
    return ("コンテキスト・プロセッサ（tax()）：" + str(price * 1.1))
  
  def hello():
    return "コンテキスト・プロセッサ（hello()）：hello Flask"
  return dict(tax=tax, hello=hello)