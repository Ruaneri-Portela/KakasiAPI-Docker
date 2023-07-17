from flask import Flask, request
from flask_cors import CORS
import shlex
app = Flask(__name__)
CORS(app)
@app.route('/convert', methods=['POST'])
def convert_string():
    input_string = request.form.get('input')
    if input_string:
        converted_string = execute_command(shlex.quote(input_string))
        return converted_string
    else:
        return 'Erro: nenhuma entrada fornecida.'
def execute_command(input_string):
    import subprocess
    command = f"echo {input_string} | iconv -f utf8 -t eucjp | kakasi -i euc -w | kakasi -i euc -Ha -Ka -Ja -Ea -ka"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return f"Erro na execução do comando: {result.stderr}"
if __name__ == '__main__':
    app.run()
