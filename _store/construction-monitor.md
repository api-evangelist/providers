---
aid: construction-monitor
name: Construction Monitor
url: https://raw.githubusercontent.com/api-evangelist/construction-monitor/refs/heads/main/apis.yml
tags:
  - Construction
  - Contractors
  - Lead Generation
  - Permits
  - Real Estate
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-08'
modified: '2026-04-29'
position: Consumer
specificationVersion: '0.19'
x-type: company
description: Construction Monitor aggregates building-permit data from county and municipal sources nationwide and resells it as construction leads, contractor intelligence, and historical permit research. Programmatic access is offered through a REST + JSON API backed by Elasticsearch and a weekly data-dump option delivered over secure FTP. Both channels are account-managed; partners receive credentials and a documented endpoint contract directly from Construction Monitor.
apis:
  - aid: construction-monitor:permits-api
    name: Construction Monitor Permits API
    tags:
      - Elasticsearch
      - JSON
      - Permits
      - REST
    humanURL: https://www.constructionmonitor.com/data
    properties:
      - url: https://www.constructionmonitor.com/data
        type: Documentation
    description: REST + JSON service backed by Elasticsearch that lets partners search building permits, retrieve full permit detail records, and pull delta updates on a polling schedule. Authentication is handled with a simple API-key scheme provisioned per customer. Used to drive lead-generation pipelines, populate CRM and BI tools, and power downstream construction analytics.
  - aid: construction-monitor:weekly-ftp
    name: Construction Monitor Weekly Data Dump (SFTP)
    tags:
      - Bulk
      - Data Dump
      - Permits
      - SFTP
    humanURL: https://www.constructionmonitor.com/data
    properties:
      - url: https://www.constructionmonitor.com/data
        type: Documentation
    description: Weekly bulk delivery of permit records over secure FTP for partners that prefer batch ingestion to live API polling. Suitable for warehousing millions of permits without operating a live integration.
common:
  - type: Website
    url: https://www.constructionmonitor.com
  - type: Data Products
    url: https://www.constructionmonitor.com/data
  - type: Contact / API Access
    url: https://www.constructionmonitor.com/contact
  - type: Blog
    url: https://www.constructionmonitor.com/blog
  - type: Privacy Policy
    url: https://www.constructionmonitor.com/privacy-policy
  - type: Terms of Service
    url: https://www.constructionmonitor.com/terms-of-use
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
