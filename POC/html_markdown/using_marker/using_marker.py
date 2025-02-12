from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered
import os

# Set up paths
# pdf_filename = "test_1.pdf"
# pdf_filename = "test-5_33-landscape.pdf"
pdf_filename = "test-5_33-landscape-pages.pdf"
# pdf_filename = "test-5_33-portrait.pdf"
pdf_path = os.path.join(os.getcwd(), "POC","html_markdown","using_marker", pdf_filename)

converter = PdfConverter(
    artifact_dict=create_model_dict(),
)
rendered = converter("FILEPATH")
text, _, images = text_from_rendered(rendered)