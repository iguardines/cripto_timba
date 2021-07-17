
app = Flask(__name__)

DEBUG = True
timberes = ["Nacho", "Cris", "Valen"]
@app.errorhandler(404)
def not_found(error):
	return "Not Found"


@app.route('/agregar_timbero', methods=['POST'])
def index():
    timbero = request.args.get("timbero", "nadie")
    timberes.append(timbero)
    return f"timbero {timbero} agregado safisfactoriamente"


@app.route('/la_persona_criptotimbera_del_mes', methods=['GET'])
def timbier_of_the_month():
    return random.choice(timberes)

@app.route('/criptotimberes', methods=['GET'])
def criptotimberes():
    return {"timberos" :timberes}

if __name__ == "__main__":
	app.run()
