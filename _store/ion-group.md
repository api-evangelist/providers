---
aid: ion-group
name: Ion Group
description: ION Group is a visionary innovator delivering mission-critical trading and workflow automation software to financial institutions, corporations, central banks, and governments. ION helps customers improve decision-making, simplify complex processes, and empower people through automation.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Financial
  - Financial Services
  - Trading
url: https://raw.githubusercontent.com/api-evangelist/ion-group/refs/heads/main/apis.yml
created: '2024-04-14'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: ion-group:acuris-entities-api
    name: Ion Group Acuris Entities API
    description: The Acuris Entities API allows you to search over 1 million records of private and public companies, firms, assets, and private investors.
    humanURL: https://api.acuris.com/entities/docs/api
    baseURL: https://api.acuris.com
    tags:
      - Companies
      - Financial Data
      - Investors
    properties:
      - url: https://api.acuris.com/entities/docs/api
        type: Documentation
      - url: openapi/ion-group-openapi.yml
        type: OpenAPI
  - aid: ion-group:dealogic-analytics-spac-api
    name: Ion Group Dealogic Analytics SPAC API
    description: Detailed profiling of Special Purpose Acquisition Companies (SPACs). Gain access to real-time content and analytics covering the full spectrum of the SPAC market, from IPO Filing/Pricing, additional fundraising via PIPEs, through to the M&A de-SPAC.
    humanURL: https://iongroup.com/analytics/data-portal/apis-data-feeds/spac-api/documentation/
    tags:
      - Analytics
      - Financial Data
      - SPAC
    properties:
      - url: https://iongroup.com/analytics/data-portal/apis-data-feeds/spac-api/documentation/
        type: Documentation
common:
  - type: Website
    url: https://iongroup.com/
  - type: Portal
    url: https://iongroup.com/analytics/data-portal/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
