# NER Evaluation

## Transformer Result

The saved evaluation report for the DNRTI transformer NER model records:

| Metric | Value |
|---|---:|
| Evaluation loss | 0.2059 |
| Precision | 0.7614 |
| Recall | 0.8020 |
| F1 | 0.7812 |
| Token accuracy | 0.9376 |

These values describe one recorded evaluation run at epoch 1.0. They are model-evaluation evidence, not a claim about end-to-end production detection accuracy.

## Sklearn Fallback Result

The tracked fallback model reported entity F1 of 0.5654 on validation and 0.6379 on the test split. Its purpose is resilient local execution when the preferred transformer checkpoint is unavailable.

## Interpretation

The transformer result supports the use of the trained model as the preferred NER backend. Production readiness would still require additional validation, drift monitoring, source-quality analysis, error review by entity type, and end-to-end evaluation across collection, classification, extraction, correlation, and export.
