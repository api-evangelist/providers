---
aid: airflow
name: Airflow
description: >-
  Airflow API. All endpoints located under /api/v2 can be used safely, are
  stable and backward compatible. Endpoints located under /ui are dedicated to
  the UI and are subject to breaking change depending on the need of the
  frontend. Users should not rely on those but use the public ones instead. 
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API
created: '2026-01-02'
modified: '2026-01-02'
url: >-
  https://raw.githubusercontent.com/api-evangelist/airflow/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: airflow:airflow
    name: Airflow
    description: >-
      Airflow API. All endpoints located under /api/v2 can be used safely, are
      stable and backward compatible. Endpoints located under /ui are dedicated
      to the UI and are subject to breaking change depending on the need of the
      frontend. Users should not rely on those but use the public ones instead. 
    humanURL: ' https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html'
    tags:
      - API
    properties:
      - type: Documentation
        url: ' https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html'
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---