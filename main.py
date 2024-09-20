''' pdf to text extractor'''
import sys
import os
from PyPDF2 import PdfReader
from PyQt5.QtWidgets import (QApplication,QMainWindow,QFileDialog,QPushButton,QTextEdit,QVBoxLayout,QWidget)

class PDFTextExtractor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pdf_path = None
        self.initui()
        
    def initui(self):
        self.setGeometry(100,100,800,600)
        self.setWindowTitle("PDF TEXT EXTRACTOR")
        
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        
        self.btn_open_pdf = QPushButton("OPEN PDF FILE",self)
        self.btn_open_pdf.clicked.connect(self.openPDF)
        
        self.btn_extract_text = QPushButton("EXTRACT TEXT",self)
        self.btn_extract_text.clicked.connect(self.extractText)
        
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.btn_open_pdf)
        layout.addWidget(self.btn_extract_text)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
    def openPDF(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        pdf_file, _ = QFileDialog.getOpenFileName(self,"OPEN PDF FILE","","PDF FILES (*.pdf);ALL FILES(*)",options = options)
        if pdf_file:
            self.pdf_path = pdf_file
    
    def extractText(self,pdf_path):
        if not self.pdf_path:
            self.text_edit.setPlainText("NO PDF FILE SELECTED")
            return  
        text = self.extractTextFromPDF(self.pdf_path)
        self.text_edit.setPlainText(text)
        
    def extractTextFromPDF(self,pdf_path):
        pdf_text = ""
        pdf_reader = PdfReader(pdf_path)
        for page in pdf_reader.pages:
            pdf_text += page.extract_text()
        return pdf_text
    
def main():
    app =QApplication(sys.argv)
    window = PDFTextExtractor()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    
            