# Methodology

## Design Boundary

ACTIT separates model development from runtime intelligence processing. This avoids retraining models during ordinary ingestion and allows a missing local model to fail safely rather than crashing the complete pipeline.

## Offline NLP/ML Pipeline

1. Validate the DNRTI BIO/IOB dataset.
2. Prepare train, validation, and test splits.
3. Train and evaluate NER backends.
4. Save model artifacts and label maps.
5. Load the preferred local model at runtime, with an explicit fallback path.

## External Runtime Pipeline

1. Convert source-specific records into a normalized raw-record contract.
2. Clean and normalize text.
3. detect duplicates before expensive processing.
4. Classify unstructured documents before NER.
5. Allow trusted structured advisory sources to bypass general document classification only with explicit metadata.
6. Extract entities, IoCs, and rule-labeled relationships.
7. Build source-independent CTI objects.
8. Isolate record-level failures so one malformed input does not stop a batch.

## Internal Runtime Boundary

Structured telemetry such as Wazuh, Zeek, Suricata, firewall, and honeypot logs requires parsing, field extraction, session building, and anomaly analysis. It should not be forced through the same document-classification path used by security articles.

## Evidence Policy

Public artifacts use synthetic or reserved examples and omit credentials, internal identifiers, raw captures, private datasets, operational collection details, model weights, and full implementation code.
