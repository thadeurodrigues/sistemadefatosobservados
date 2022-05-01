from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
from reportlab.pdfgen import canvas


banco = mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="fo"
)

def exibir_mensagem():
    #if formulario.lineEdit.text == (""):
        #QMessageBox.about(formulario, "alerta", "Nenhum nome digitado")
    #elif formulario.lineEdit_2.text == (""):
        #QMessageBox.about(formulario,"alerta","Nenhum motivo digitado")
    #else:
        QMessageBox.about(formulario, "alerta", "Dados enviados")

def logar():
    login.label_6.setText("")
    nome_usuario = login.lineEdit.text()
    senha = login.lineEdit_3.text()
    if nome_usuario == "adm" and senha == "rondon":
        login.close()
        formulario.show()
    else:
        login.label_6.setText("Dados de Login incorretos")


def logout():
    formulario.close()
    login.show()
    login.lineEdit.setText("")
    login.lineEdit_3.setText("")




def gerar_pdf():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM fo"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("listafo.pdf")
    pdf.setFont("Times-Bold", 9)
    pdf.drawString(200,800, "Lista de Fatos Observados")
    pdf.setFont("Times-Bold", 9)

    pdf.drawString(10, 750, "Ordem")
    pdf.drawString(50, 750, "Graduação")
    pdf.drawString(100, 750, "Nome de Guerra")
    pdf.drawString(180, 750, "Data")
    pdf.drawString(250, 750, "Motivo")
    pdf.drawString(490, 750, "Fato Observado")

    for i in range(0, len(dados_lidos)):
        y = y + 10
        pdf.drawString(10, 750 - y, str(dados_lidos[i][0]))
        pdf.drawString(50, 750 - y, str(dados_lidos[i][1]))
        pdf.drawString(100, 750 - y, str(dados_lidos[i][2]))
        pdf.drawString(180, 750 - y, str(dados_lidos[i][3]))
        pdf.drawString(250, 750 - y, str(dados_lidos[i][4]))
        pdf.drawString(490, 750 - y, str(dados_lidos[i][5]))


    pdf.save()
    print("PDF GERADO COM SUCESSO!")


def funcao_principal():
    linha1 = formulario.comboBox.currentText()
    linha2 = formulario.lineEdit.text()
    linha3 = formulario.dateEdit.text()
    linha4 = formulario.lineEdit_2.text()

    Fato = ""
    print("Graduação:",linha1)
    print("Nome de Guerra:",linha2)
    print("Data da Obervação:",linha3)
    print("Motivo:",linha4)
    
    if formulario.radioButton.isChecked() :
        print("Fato Observado Positivo")
        Fato = "Fato Observado Positivo"
    elif formulario.radioButton_2.isChecked() :
        print("Fato Observado Negativo")
        Fato = "Fato Observado Negativo"


    cursor = banco.cursor()
    comando_SQL = "INSERT INTO fo (Graduação,Nome,Data,Fato,Motivo) VALUES (%s,%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3),str(Fato),str(linha4))
    cursor.execute(comando_SQL,dados)
    banco.commit()
    #formulario.comboBox.setText("Selecione")
    formulario.lineEdit.setText("")
    #formulario.dateEdit.setText("")
    formulario.lineEdit_2.setText("")
    #formulario.radioButton.setCheckable("")
    #formulario.radioButton_2.setCheckable(False)

def listarfo():
        lista.show()

        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM fo"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()

        lista.tableWidget.setRowCount(len(dados_lidos))
        lista.tableWidget.setColumnCount(6)

        for i in range(0, len(dados_lidos)):
            for j in range(0,6):
                lista.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))



app=QtWidgets.QApplication([])
formulario=uic.loadUi("fo.ui")
lista=uic.loadUi("lista.ui")
login=uic.loadUi("login.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(listarfo)
lista.pushButton.clicked.connect(gerar_pdf)
formulario.pushButton_4.clicked.connect(logout)
login.pushButton.clicked.connect(logar)
login.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
formulario.pushButton.clicked.connect(exibir_mensagem)

login.show()
#formulario.show()
app.exec()


#INSERT INTO fo (Graduação,descrição,data,fato_observado,motivo) VALUES ("cb","teste","29/09/1997","positivo","testando")
#tabela
    # create table fo (
    #     id INT NOT NULL AUTO_INCREMENT,
    #     Graduação VARCHAR(50),
    #     Nome VARCHAR(50),
    #     Data VARCHAR(20),
    #     Motivo VARCHAR(50),
    #     Fato VARCHAR(50),
    #     PRIMARY KEY (id)
    # );
