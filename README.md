# House price pipeline

A small linear regression that predicts the price of a house (thousand €) from
its size, rooms and age, with a GitHub Actions pipeline that tests, trains,
checks and releases it.

| File | What it does |
|---|---|
| `data/houses.csv` | 400 synthetic houses: the training data |
| `train.py` | trains the model, measures it on 20% of the houses, saves `model.joblib` and `metrics.json` |
| `check_quality.py` | the quality gate: fails if the error is too large or no better than the baseline |
| `tests/` | tests on the data and on the model's answers |
| `.github/workflows/ml-pipeline.yml` | the pipeline GitHub runs on every push |

## Run it on your computer

Use Python 3.13, the same version as the pipeline. First create a virtual
environment (venv): a folder, `.venv`, with its own copy of Python and its own
libraries, so that the versions in `requirements.txt` do not mix with anything
else installed on your computer. `.gitignore` keeps `.venv` out of the repository.

Windows (PowerShell or Command Prompt):

```
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m pytest -v
.venv\Scripts\python train.py
.venv\Scripts\python check_quality.py
```

macOS or Linux:

```
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -v
.venv/bin/python train.py
.venv/bin/python check_quality.py
```

Each command calls the Python inside `.venv` directly, so there is nothing to
activate. On GitHub, the pipeline does not need a venv: every run starts on a
new, empty computer that is erased afterwards.

The data is synthetic: generated from a known formula with noise, for learning only.
