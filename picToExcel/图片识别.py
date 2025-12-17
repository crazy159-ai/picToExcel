from paddleocr import PaddleOCR
from openpyxl import Workbook


def image_to_excel(image_path, output_path,col):
    
    ocr = PaddleOCR(
    use_doc_orientation_classify=False, 
    use_doc_unwarping=False, 
    use_textline_orientation=True) 

    result = ocr.predict(image_path)    
    texts = result[0]['rec_texts']

    wb = Workbook()
    ws = wb.active
    
    row_index = 1
    for i in range(round(len(texts)/col)-1):
        for j in range(col):
            ws.cell(row=row_index, column=j+1, value=texts[5*i+j])
        row_index += 1
 
     
    wb.save(output_path)
 
if __name__ == "__main__":
    img_path = "pic/1.png"
    out_path = "output.xlsx"
    image_to_excel(img_path, out_path,5)