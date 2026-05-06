---
aid: influxdb
name: InfluxDB
description: InfluxData is the company building InfluxDB, the open source time series database used by more than a million developers around the world. Their mission is to help developers build intelligent, real-time systems with their time series data, with offerings spanning open source InfluxDB Core and Enterprise, InfluxDB Cloud Serverless and Dedicated, and Telegraf for data collection.
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/influxdb/refs/heads/main/apis.yml
created: '2024-09-25'
modified: '2026-04-28'
specificationVersion: '0.20'
position: Consuming
access: 3rd-Party
tags:
  - Database
  - Time Series
  - Real-Time
  - Analytics
apis:
  - aid: influxdb:influxdb
    name: InfluxDB Cloud API
    description: InfluxDB Cloud v2 API for managing buckets, organizations, tasks, authorizations, dashboards, and writing and querying time series data. The API exposes the full surface of the InfluxDB Cloud platform including data ingestion, Flux query execution, task scheduling, alerting, and access control.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.influxdata.com/
    baseURL: https://cloud2.influxdata.com/api/v2
    tags:
      - Database
      - Time Series
      - Real-Time
      - Cloud
    properties:
      - type: Documentation
        url: https://docs.influxdata.com/influxdb/cloud/api/v2/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/influxdb/refs/heads/main/openapi/influxdb-openapi.yml
      - type: Authentication
        url: https://docs.influxdata.com/influxdb/cloud/api/v2/#tag/Authentication
      - type: Getting Started
        url: https://docs.influxdata.com/influxdb/cloud/api/v2/#tag/Quick-start
      - type: Pagination
        url: https://docs.influxdata.com/influxdb/cloud/api/v2/#tag/Pagination
      - type: Headers
        url: https://docs.influxdata.com/influxdb/cloud/api/v2/#tag/Headers
      - type: Source
        url: https://github.com/influxdata/openapi
    contact:
      - FN: InfluxData Support
        email: support@influxdata.com
        url: https://support.influxdata.com/
common:
  - type: Website
    url: https://www.influxdata.com/
  - type: Documentation
    url: https://docs.influxdata.com/
  - type: Getting Started
    url: https://docs.influxdata.com/influxdb/cloud/api/v2/#tag/Quick-start
  - type: Pricing
    url: https://www.influxdata.com/influxdb-pricing/
  - type: Use Cases
    url: https://www.influxdata.com/solutions/
  - type: Resources
    url: https://www.influxdata.com/_resources/?pg=1
  - type: Webinars
    url: https://www.influxdata.com/_resources/?pg=1&ct=webinar
  - type: White Papers
    url: https://www.influxdata.com/_resources/?pg=1&ct=tech_paper
  - type: Video
    url: https://www.influxdata.com/_resources/?pg=1&ct=video
  - type: Case Studies
    url: https://www.influxdata.com/_resources/?pg=1&ct=case_study
  - type: Events
    url: https://www.influxdata.com/events/
  - type: Glossary
    url: https://www.influxdata.com/glossary/
  - type: Integrations
    url: https://www.influxdata.com/products/integrations/
  - type: Issues
    url: https://github.com/influxdata/influxdb/issues/new/choose/
  - type: Support
    url: https://support.influxdata.com/
  - type: GitHub
    url: https://github.com/influxdata/influxdb
  - type: LinkedIn
    url: https://www.linkedin.com/company/influxdb/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
include: []
---
