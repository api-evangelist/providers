---
aid: data-quality-standards
name: Data Quality Standards
description: Data Quality Standards is the landscape of frameworks, standards, and tools used to define and measure the accuracy, completeness, consistency, validity, uniqueness, and timeliness of data. It spans ISO/IEC 25012 and ISO 8000, the DAMA-DMBOK data quality dimensions, EDM Council DCAM, and open source and commercial tooling like Great Expectations, Soda, dbt tests, Monte Carlo, and Anomalo.
type: Topic
xType: topic
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Governance
  - Data Management
  - Data Quality
  - Data Quality Standards
  - Observability
  - Standards
created: '2025-01-01'
modified: '2026-04-30'
url: https://raw.githubusercontent.com/api-evangelist/data-quality-standards/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis: []
common:
  - url: https://www.iso.org/standard/35736.html
    name: ISO/IEC 25012
    type: Standard
    description: ISO standard defining a data quality model with 15 characteristics.
  - url: https://www.iso.org/standard/50798.html
    name: ISO 8000
    type: Standard
    description: ISO 8000 family for data quality, master data, and data quality management.
  - url: https://www.dama.org/cpages/body-of-knowledge
    name: DAMA-DMBOK
    type: Reference
    description: DAMA Data Management Body of Knowledge with the data quality dimensions.
  - url: https://edmcouncil.org/page/aboutdcamreview
    name: EDM Council DCAM
    type: Framework
    description: Data Management Capability Assessment Model.
  - url: https://www.iso.org/standard/82911.html
    name: ISO/IEC 25024
    type: Standard
    description: Measurement of data quality.
  - url: https://greatexpectations.io/
    name: Great Expectations
    type: Tool
    description: Open source data quality validation framework.
  - url: https://www.soda.io/
    name: Soda
    type: Tool
    description: Data quality and observability platform with SodaCL.
  - url: https://docs.getdbt.com/docs/build/data-tests
    name: dbt Tests
    type: Tool
    description: dbt's built-in data tests for transformations.
  - url: https://www.montecarlodata.com/
    name: Monte Carlo
    type: Tool
    description: Data observability platform for detecting data quality incidents.
  - url: https://www.anomalo.com/
    name: Anomalo
    type: Tool
    description: Data quality monitoring with automated anomaly detection.
  - url: https://elementary-data.com/
    name: Elementary
    type: Tool
    description: Open source data observability built on dbt.
  - url: https://github.com/awslabs/deequ
    name: Deequ
    type: Tool
    description: AWS Labs library for testing data quality on Spark.
  - url: vocabulary/data-quality-standards-vocabulary.yml
    name: Vocabulary
    type: Vocabulary
    description: Vocabulary of data quality dimensions and concepts.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
