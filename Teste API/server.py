from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

operadoras_df = pd.read_csv("C:\\Users\\User\\Documents\\TesteDeNivelamento\\Relatorio_cadop.csv", encoding="utf8", delimiter=';')


@app.route("/api/operadoras", methods=["GET"])
def search_operadoras():
    query = request.args.get("q", "").lower()
    
    if query:
        filtered = operadoras_df[operadoras_df.apply(lambda row: query in row.to_string().lower(), axis=1)]
    else:
        filtered = operadoras_df

    result = filtered.to_dict(orient="records")
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
