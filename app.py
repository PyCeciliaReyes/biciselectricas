from flask import Flask, render_template, send_file, url_for
import folium
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/mapa")
def mapa():
    #Crear un mapa centrado en la zona la gaeria, Asuncion Paraguay
    m = folium.Map(location=[-25.284702 , -57.563289], zoom_start=16)
    tooltip1 = 'Bicielectrica nro 1'
    tooltip2 = 'Bicielectrica nro 2'
    tooltip3 = 'Bicielectrica nro 3'
    tooltip4 = 'Bicielectrica nro 4'
    tooltip5 = 'Bicielectrica nro 5'
    # Agregar una etiqueta en la ubicación
    folium.Marker([-25.279847 , -57.5653], popup='Bicielectrica N° 1', tooltip=tooltip1).add_to(m)
    folium.Marker([-25.280945 , -57.563519], popup='Bicielectrica N° 2', tooltip=tooltip2).add_to(m)
    folium.Marker([-25.281229, -57.566843], popup='Bicielectrica N° 3', tooltip=tooltip3).add_to(m)
    folium.Marker([-25.286061,-57.561476], popup='Bicielectrica N° 4', tooltip=tooltip4).add_to(m)
    folium.Marker([-25.285949 ,-57.562356], popup='Bicielectrica N° 5', tooltip=tooltip5).add_to(m)

    #Agregar circulos a las ubicaciones
    folium.Circle(location=[-25.279847 ,-57.5653], tooltip='Bicielectrica 1' ,color='purple', fill_color= 'red', radius=20, weight=4, fill_opacity=0.5).add_to(m)
    folium.Circle(location=[-25.280945,-57.563519], tooltip= 'Bicielectrica 2',color='purple', fill_color= 'red', radius=20, weight=4, fill_opacity=0.5).add_to(m)
    folium.Circle(location=[-25.281229,-57.566843], tooltip='Bicielectrica 3', color='purple', fill_color= 'red', radius=20, weight=4, fill_opacity=0.5).add_to(m)
    folium.Circle(location=[-25.286061,-57.561476],tooltip='Bicielectrica 4', color='purple', fill_color= 'red', radius=20, weight=4, fill_opacity=0.5).add_to(m)
    folium.Circle(location=[-25.285949,-57.562356], tooltip='Bicielectrica 5' ,color='purple', fill_color= 'red', radius=20, weight=4, fill_opacity=0.5).add_to(m)

    map_html = m._repr_html_()

    return render_template('mapa_asuncion.html', map_html = map_html)


@app.route('/generate_qr/<data>')
def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img_buffer = BytesIO()
    img.save(img_buffer, 'PNG')
    img_buffer.seek(0)

    return send_file(img_buffer, mimetype='image/png')


if __name__== '__main__':
    app.run(debug=True)

   