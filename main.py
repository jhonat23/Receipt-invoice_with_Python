from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
#A4 size: 595.2 witdh and 841.8 height (points used to place doc objects)
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from datetime import datetime
w, h = A4
ylisti = h - 215 #value for grid

#Example data
data = ['John', 'Doe', '111111111', '310310310', '5555 W Nice Street', 'Nashville, Tennesse, USA', 'myemail@email.com']# test list

#begin file creation
c = canvas.Canvas("Receipt No. XXX.pdf")

#------------------Header
c.setFont("Times-Roman", 12)
c.drawString(50, h-100, "¡Hola! Este es tu recibo en el cual puedes ver el detalle de tu venta:")
c.line(w-580, h-110, w-15, h-110)
c.line(w-580, h-105, w-15, h-105)
c.drawImage("C:\image\Company-logo.png", 50, h - 80, width=100, height=80)
c.rect(40, h - 195, 320, 80)
c.rect(400, h - 180, 160, 60)

#------------------customer data
c.setFont("Times-Roman", 9)
c.drawString(50, h-130, "Name:")
c.drawString(180, h-130, data[0])
c.drawString(50, h-140, "Last Name:")
c.drawString(180, h-140, data[1])
c.drawString(50, h-150, "ID number:")
c.drawString(180, h-150, data[2])
c.drawString(50, h-160, "Telephone:")
c.drawString(180, h-160, data[3])
c.drawString(50, h-170, "Address:")
c.drawString(180, h-170, data[4])
c.drawString(50, h-180, "City/State:")
c.drawString(180, h-180, data[5])
c.drawString(50, h-190, "Email:")
c.drawString(180, h-190, data[6])
c.drawString(455, h-130, "Date & Hour")
c.drawString(425, h-140, datetime.now().isoformat())
c.drawString(455, h-160, "Receipt No.")
c.setFont("Times-Roman", 12)
c.drawString(460, h-170, "XXX")

c.line(w-580, h-200, w-15, h-200)
c.line(w-580, h-205, w-15, h-205)

#------------------Item's table
xlist = [w-580, 60, 300, 370, 440, 510, w-15]
ylistrot = [h - 215, h - 240]
c.drawString(25, h-230, "Ítem")
c.drawString(155, h-230, "Description")
c.drawString(320, h-230, "Units")
c.drawString(380, h-230, "Unit Cost")
c.drawString(450, h-230, "Total Cost")
c.drawString(520, h-230, "Taxes")
c.grid(xlist, ylistrot)
ylist = list(range(int(h) - 220 - (16*20),int(h)-245, 20))
ylist.reverse()
ylist.insert(0, int(ylisti))
c.grid(xlist, ylist)

#------------------Grid for data product
yitem = list(range(1, 16))
ygrid = list(range(235, 585, 20))
xgrid = list(range(375, int(w)-20, 3))

for p in yitem:
    if len(str(p))==1:
        c.drawString(35, h-ygrid[p], str(p))
    else:
        c.drawString(31, h-ygrid[p], str(p))

#------------------Totals
c.drawString(410, h-570, "Total Cost")
c.drawString(410, h-590, "Total Taxes")
c.drawString(410, h-610, "Total")
xt = [400 , 500 , w-15]
yt = [h-555, h-575, h-595, h-615]
c.grid(xt,yt)

c.line(w-580, h-700, w-15, h-700)
c.line(w-580, h-695, w-15, h-695)

#------------------ Final headers
c.drawString(170, h-710, "Preserve this document in case of warranty or leverage")
text = c.beginText(0, h-800)
text.setFont("Times-Roman", 9)
text.moveCursor(230, 0)
text.textLine("Company address, state and country")
text.moveCursor(30, 0)
text.textLine("Company email")
text.moveCursor(0, 0)
text.textLine("Contact Number")
text.moveCursor(12, 0)
text.textLine("web page")
c.drawText(text)

#Save document
c.save()
