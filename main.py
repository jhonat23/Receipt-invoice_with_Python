from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
#Una hoja A4 está constituida por 595.2 puntos de ancho (width) y 841.8 puntos de alto (height).
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from datetime import datetime
w, h = A4
ylisti = h - 215
lst = list()

#datos ejemplo
rot_cliente = ['Nombres', 'Apellidos', 'Documento', 'Teléfono', 'Dirección', 'Ciudad', 'e-mail']
data = ['John', 'Doe', '111111111', '310310310', '5555 W Nice Street', 'Nashville, Tennesse, USA', 'myemail@email.com']# test list
cliente = [rot_cliente,data]

#inicio creación de archivo
c = canvas.Canvas("Receipt No. XXX.pdf")

#------------------encabezado
c.setFont("Times-Roman", 12)
c.drawString(50, h-100, "¡Hola! Este es tu recibo en el cual puedes ver el detalle de tu venta:")
#c.setFillColorRGB(1, 0, 0)
c.line(w-580, h-110, w-15, h-110)
c.line(w-580, h-105, w-15, h-105)
c.drawImage("C:\image\Company-logo.png", 50, h - 80, width=100, height=80)
c.rect(40, h - 195, 320, 80)
c.rect(400, h - 180, 160, 60)

#------------------datos del cliente
c.setFont("Times-Roman", 9)
c.drawString(50, h-130, "Nombres:")
c.drawString(180, h-130, data[0])
c.drawString(50, h-140, "Apellidos:")
c.drawString(180, h-140, data[1])
c.drawString(50, h-150, "Documento:")
c.drawString(180, h-150, data[2])
c.drawString(50, h-160, "Telefóno:")
c.drawString(180, h-160, data[3])
c.drawString(50, h-170, "Dirección:")
c.drawString(180, h-170, data[4])
c.drawString(50, h-180, "Ciudad/Departamento:")
c.drawString(180, h-180, data[5])
c.drawString(50, h-190, "Correo:")
c.drawString(180, h-190, data[6])
c.drawString(455, h-130, "Fecha y hora")
c.drawString(425, h-140, datetime.now().isoformat())
c.drawString(455, h-160, "Recibo No.")
c.setFont("Times-Roman", 12)
c.drawString(460, h-170, "XXX")

c.line(w-580, h-200, w-15, h-200)
c.line(w-580, h-205, w-15, h-205)

#------------------Tabla de items
xlist = [w-580, 60, 300, 370, 440, 510, w-15]
ylistrot = [h - 215, h - 240]
c.drawString(25, h-230, "Ítem")
c.drawString(155, h-230, "Descripción")
c.drawString(310, h-230, "Cantidad")
c.drawString(380, h-230, "C. unitario")
c.drawString(455, h-230, "C. total")
c.drawString(520, h-230, "Impuestos")
c.grid(xlist, ylistrot)
#ylist = [h - 215, h - 245, h - 265, h - 285, h-305, h-325, h-345]
ylist = list(range(int(h) - 220 - (16*20),int(h)-245, 20))
ylist.reverse()
ylist.insert(0, int(ylisti))
#print(ylist)
c.grid(xlist, ylist)

#------------------información productos vendidos
yitem = list(range(1, 16))
ygrid = list(range(235, 585, 20))
xgrid = list(range(375, int(w)-20, 3))

for p in yitem:
    if len(str(p))==1:
        c.drawString(35, h-ygrid[p], str(p))
    #for a in range(len(xproduct)):
        #c.drawString(xgrid[a], h-ygrid[p], xproduct[a])
    else:
        c.drawString(31, h-ygrid[p], str(p))

#------------------Totales
c.drawString(410, h-570, "Total Bruto")
c.drawString(410, h-590, "Total impuestos")
c.drawString(410, h-610, "Total a pagar")
xt = [400 , 500 , w-15]
yt = [h-555, h-575, h-595, h-615]
c.grid(xt,yt)

c.line(w-580, h-700, w-15, h-700)
c.line(w-580, h-695, w-15, h-695)

#------------------ final documento
c.drawString(50, h-710, "Convserva este documento en caso de requerir un garantía")
text = c.beginText(0, h-800)
text.setFont("Times-Roman", 9)
text.moveCursor(180, 0)
text.textLine("Company address, state and country")
text.moveCursor(-3, 0)
text.textLine("company email")
text.moveCursor(80, 0)
text.textLine("Contact Number")
text.moveCursor(-18, 0)
text.textLine("web page")
c.drawText(text)
#Pasar a la siguiente página
c.showPage()

#Guardar o cerrar documento
c.save()
