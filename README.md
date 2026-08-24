# AIS Standards Explorer — Python / Flask

Python/Flask version of the AIS Standards Explorer. The UI uses a JSW-inspired red, blue and white palette.

## Local

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## GitHub

```bash
git add .
git commit -m "Convert AIS Explorer to Python Flask"
git push
```

## Vercel

The project includes `vercel.json` and `api/index.py` for Vercel's Python runtime. Import the GitHub repository into Vercel and deploy.

## Important

Calculator formulas are based on the supplied Excel workbooks/screenshots. Validate against controlled/current AIS publications before certification or regulatory submission.
