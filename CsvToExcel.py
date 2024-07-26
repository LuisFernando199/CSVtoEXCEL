# TRANSFORMADOR DE CSV A XLSX Y VICEVERSA # http://localhost:5000/convert 

# PASO 1: Dale a la carpeta de archivos 📁 (logeate con google) y arrastra un csv o un xlsx.
# PASO 2: En la variable nombre_archivo cambia Catalog_v2.csv por el nombre de tu archivo.
# PASO 3: Ejecuta esta pestaña de código, luego la siguiente y dale a actualizar


from flask import Flask, request, send_file, render_template
import pandas as pd
import os

from flask import Flask, request, send_file, render_template
import pandas as pd
import os

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_file():
    file = request.files['file']
    filename, extension = os.path.splitext(file.filename)
    if extension == '.csv':
        output_file = f'{filename}.xlsx'
        df = pd.read_csv(file)
        df.to_excel(output_file, index=False)
    elif extension == '.xlsx':
        output_file = f'{filename}.csv'
        df = pd.read_excel(file)
        df.to_csv(output_file, index=False, header=True)
    return send_file(output_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
