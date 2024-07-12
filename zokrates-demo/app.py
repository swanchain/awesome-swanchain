from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/compute', methods=['POST'])
def compute():
    data = request.json
    a = data['a']
    b = data['b']
    c = data['c']

    # 写入 ZoKrates 输入文件
    with open('input.txt', 'w') as f:
        f.write(f"{a} {b} {c}")

    try:
        # 运行 ZoKrates 命令
        subprocess.run(["/usr/local/bin/zokrates", "compile", "-i", "addition.zok"], check=True)
        subprocess.run(["/usr/local/bin/zokrates", "setup"], check=True)
        subprocess.run(["/usr/local/bin/zokrates", "compute-witness", "-a", str(a), str(b), str(c)], check=True)
        subprocess.run(["/usr/local/bin/zokrates", "generate-proof"], check=True)
        result = subprocess.run(["/usr/local/bin/zokrates", "verify"], check=True, capture_output=True, text=True)

        return jsonify({"result": result.stdout.strip()})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
