---
aid: bindbee
name: Bindbee
description: Bindbee provides a unified HRIS and ATS integration API that allows companies to connect with multiple HR systems through a single integration, simplifying workforce data access and HR automation.
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - ATS
  - HR Integration
  - HRIS
  - Workforce
url: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-21'
specificationVersion: '0.19'
apis:
  - aid: bindbee:bindbee-api
    name: Bindbee API
    description: Unified HRIS and ATS integration API for connecting with multiple HR systems through a single integration.
    humanURL: https://bindbee.dev/
    tags:
      - ATS
      - HR Integration
      - HRIS
    properties:
      - type: Documentation
        url: https://docs.bindbee.dev/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/openapi/bindbee-api.yaml
common:
  - type: Portal
    url: https://bindbee.dev/
  - type: Documentation
    url: https://docs.bindbee.dev/
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/rules/bindbee-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/vocabulary/bindbee-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/bindbee/refs/heads/main/capabilities/hr-integration.yaml
  - type: Features
    data:
      - name: Unified HRIS API
        description: Access employee data from BambooHR, Workday, ADP, and 50+ HRIS systems through one API.
      - name: Unified ATS API
        description: Access job listings and candidates from Greenhouse, Lever, Workable, and other ATS systems.
      - name: Data Normalization
        description: Consistent normalized schema across all connected HR systems.
      - name: Cursor Pagination
        description: Efficient cursor-based pagination for large employee datasets.
      - name: Connector Tokens
        description: Secure per-integration connector tokens for multi-tenant HR data access.
      - name: Real-Time Sync
        description: Webhooks and polling for real-time HR data synchronization.
  - type: UseCases
    data:
      - name: Employee Directory Integration
        description: Sync employee records from any HRIS into internal apps and directories.
      - name: Onboarding Automation
        description: Trigger onboarding workflows when new employees are added in the HRIS.
      - name: Recruiting Pipeline Visibility
        description: Track candidates across ATS stages in unified dashboards.
      - name: HRIS Migration
        description: Move between HRIS providers without rewriting integrations.
      - name: HR Analytics
        description: Aggregate people data from multiple HR systems for workforce analytics.
  - type: Integrations
    data:
      - name: BambooHR
        description: Sync employee data from BambooHR via Bindbee unified API.
      - name: Workday
        description: Access Workday employee and org data through normalized Bindbee API.
      - name: ADP
        description: Connect ADP Workforce Now employee records via Bindbee.
      - name: Greenhouse
        description: Access Greenhouse ATS job listings and candidates via Bindbee.
      - name: Lever
        description: Sync Lever ATS recruiting pipeline data through Bindbee.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
access: 3rd-Party
position: Consuming
---
