# Automatic Licence Card Detection, Perspective Correction, and OCR

Initial scaffold for a Computer Vision course project that will detect a
licence card, correct its perspective, preprocess the image, and extract text
with OCR.

## Planned stack

- Python 3.10+
- OpenCV and NumPy
- Matplotlib
- EasyOCR (with Tesseract as an optional future backend)
- jiwer for OCR evaluation

## Project layout

- `src/detect.py` — card and corner detection
- `src/rectify.py` — corner ordering and perspective correction
- `src/preprocess.py` — grayscale, denoising, contrast, and thresholding
- `src/ocr.py` — OCR integration and field extraction
- `src/pipeline.py` — end-to-end pipeline and CLI
- `evaluate.py` — detection and OCR metrics
- `data/` — train, validation, test, and annotation data
- `samples/` — redacted or mock demonstration images
- `outputs/` — generated experiment outputs

## Setup

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

The implementation is intentionally not included in this initial scaffold.
Future pipeline usage will be documented here once the stages are implemented.

