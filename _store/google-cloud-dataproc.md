---
aid: google-cloud-dataproc
name: Google Cloud Dataproc
description: Google Cloud Dataproc is a fully managed and highly scalable service for running Apache Spark, Apache Hadoop, Apache Flink, Presto, and other open-source data processing frameworks. It enables batch processing, querying, streaming, and machine learning use cases with cluster management that takes seconds instead of minutes, along with per-second billing and autoscaling capabilities.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-dataproc/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Big Data
  - Data Processing
  - Google Cloud
  - Hadoop
  - Spark
apis:
  - name: Cloud Dataproc API
    description: The Cloud Dataproc API manages Hadoop-based clusters and jobs on Google Cloud. It provides programmatic access to create, configure, and delete clusters, submit and monitor Apache Spark, Hadoop, Hive, and Pig jobs, and manage workflow templates for orchestrating multi-step data processing pipelines. The API supports autoscaling policies, optional components, and integration with other Google Cloud services.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/dataproc/docs
    baseURL: https://dataproc.googleapis.com/v1
    tags:
      - Clusters
      - Hadoop
      - Jobs
      - Spark
    properties:
      - type: Documentation
        url: https://cloud.google.com/dataproc/docs/reference/rest
      - type: OpenAPI
        url: openapi/cloud-dataproc-openapi.yml
      - type: Authentication
        url: https://cloud.google.com/dataproc/docs/concepts/iam
      - type: Getting Started
        url: https://cloud.google.com/dataproc/docs/quickstarts
      - type: JSONSchema
        url: json-schema/cluster-schema.json
common:
  - type: Portal
    url: https://cloud.google.com/dataproc
  - type: Getting Started
    url: https://cloud.google.com/dataproc/docs/quickstarts
  - type: Documentation
    url: https://cloud.google.com/dataproc/docs
  - type: Authentication
    url: https://cloud.google.com/dataproc/docs/concepts/iam
  - type: Pricing
    url: https://cloud.google.com/dataproc/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/dataproc/docs/support
  - type: JSON-LD
    url: json-ld/google-cloud-dataproc-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
