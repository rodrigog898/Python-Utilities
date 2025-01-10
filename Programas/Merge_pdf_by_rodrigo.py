import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QLineEdit, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

class PDFMergerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Crear layout principal
        self.layout = QVBoxLayout()

        # Configurar estilos de la ventana
        self.setWindowTitle('PDF Merger - Desarrollado por Rodrigo Aravena')
        self.setGeometry(300, 300, 400, 250)
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
            }
            QPushButton {
                background-color: #4728C0;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #FFCE00;
                color: black;
            }
            QLabel {
                font-size: 14px;
                color: #333;
            }
        """)

        # Etiqueta para seleccionar archivos PDF
        self.label = QLabel('Selecciona archivos PDF para unir o dividir:', self)
        self.label.setFont(QFont('Arial', 12))
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        # Botón para seleccionar PDF a unir
        self.btnSelect = QPushButton('Seleccionar PDF para unir', self)
        self.btnSelect.clicked.connect(self.select_files)
        self.layout.addWidget(self.btnSelect)

        # Botón para unir PDFs
        self.btnMerge = QPushButton('Unir PDFs', self)
        self.btnMerge.clicked.connect(self.merge_pdfs)
        self.layout.addWidget(self.btnMerge)

        # Campo para seleccionar el PDF a dividir y la página de inicio
        self.btnSelectDivide = QPushButton('Seleccionar PDF para dividir', self)
        self.btnSelectDivide.clicked.connect(self.select_file_to_split)
        self.layout.addWidget(self.btnSelectDivide)

        # Campo para ingresar la página desde la cual dividir
        self.page_input = QLineEdit(self)
        self.page_input.setPlaceholderText('Ingresa la página desde donde dividir')
        self.layout.addWidget(self.page_input)

        # Botón para dividir el PDF
        self.btnSplit = QPushButton('Dividir PDF', self)
        self.btnSplit.clicked.connect(self.split_pdf)
        self.layout.addWidget(self.btnSplit)

        # Pie de página con los créditos
        footer = QLabel('Desarrollado por Rodrigo Aravena', self)
        footer_font = QFont('Arial', 10)
        footer_font.setItalic(True)
        footer.setFont(footer_font)
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("color: #555;")
        self.layout.addWidget(footer)

        # Aplicar layout
        self.setLayout(self.layout)

    def select_files(self):
        self.files, _ = QFileDialog.getOpenFileNames(self, "Selecciona PDFs", "", "PDF Files (*.pdf)")
        if self.files:
            self.label.setText("Archivos seleccionados:\n" + "\n".join(self.files))

    def merge_pdfs(self):
        if hasattr(self, 'files') and self.files:
            merger = PdfMerger()

            for pdf in self.files:
                merger.append(pdf)

            output_path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo unido", "", "PDF Files (*.pdf)")
            if output_path:
                merger.write(output_path)
                merger.close()
                self.label.setText(f'PDFs unidos y guardados en: {output_path}')
        else:
            self.label.setText('No se han seleccionado archivos para unir.')

    def select_file_to_split(self):
        self.file_to_split, _ = QFileDialog.getOpenFileName(self, "Selecciona el PDF para dividir", "", "PDF Files (*.pdf)")
        if self.file_to_split:
            self.label.setText(f'Archivo seleccionado para dividir: {self.file_to_split}')

    def split_pdf(self):
        if hasattr(self, 'file_to_split') and self.file_to_split:
            # Obtener la página desde la cual dividir
            try:
                split_page = int(self.page_input.text()) - 1  # Convertir a índice de página (comienza en 0)
                reader = PdfReader(self.file_to_split)
                writer = PdfWriter()

                # Validar que el número de página sea válido
                if split_page < 0 or split_page >= len(reader.pages):
                    self.label.setText('Número de página fuera de rango.')
                    return

                # Agregar páginas desde la seleccionada hasta el final
                for page_num in range(split_page, len(reader.pages)):
                    writer.add_page(reader.pages[page_num])

                # Guardar el nuevo archivo PDF
                output_path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo dividido", "", "PDF Files (*.pdf)")
                if output_path:
                    with open(output_path, 'wb') as output_file:
                        writer.write(output_file)
                    self.label.setText(f'PDF dividido y guardado en: {output_path}')
            except ValueError:
                self.label.setText('Por favor, ingresa un número válido.')
        else:
            self.label.setText('No se ha seleccionado un archivo para dividir.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PDFMergerApp()
    ex.show()
    sys.exit(app.exec_())
