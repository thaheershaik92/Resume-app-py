from flask import Flask, render_template, request, send_file
from fpdf import FPDF

app = Flask(__name__)

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Resume', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/resume', methods=['POST'])
def resume():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    profession = request.form['profession']
    experience = request.form['experience']
    education = request.form['education']
    skills = request.form['skills']

    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', size=12)
    pdf.cell(200, 10, txt="Name: " + first_name + " " + last_name, ln=True)
    pdf.cell(200, 10, txt="Profession: " + profession, ln=True)
    pdf.cell(200, 10, txt="Experience: " + experience, ln=True)
    pdf.cell(200, 10, txt="Education: " + education, ln=True)
    pdf.cell(200, 10, txt="Skills: " + skills, ln=True)

    pdf.output('resume.pdf')
    return send_file('resume.pdf')

if __name__ == '__main__':
    app.run(debug=True)
