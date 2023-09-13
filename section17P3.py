import PyPDF2
import sys

inputs = sys.argv[1:]


def water_marker(pdf_list):
    file = 'wtr.pdf'
    # wm = PyPDF2.PdfFileReader(file)
    writer = PyPDF2.PdfFileWriter()
    for pdf in pdf_list:
        reader = PyPDF2.PdfFileReader(pdf)
        content_page = reader
        mediabox = content_page.mediabox
        reader_stamp = file

        image_page = reader_stamp.pages[0]
        image_page.merge_page(content_page)
        image_page.mediabox = mediabox
        writer.add_page(image_page)

    with open('result.pdf' "wb") as fp:
        writer.write(fp)


water_marker(inputs)


# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('super.pdf')
