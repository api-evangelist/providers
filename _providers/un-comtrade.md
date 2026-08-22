---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Un Comtrade Agentic Access
  operation_count: 13
  slug: un-comtrade-agentic-access
  summary_line: 13 operations
api_count: 1
apis:
- description: REST API for extracting international merchandise and services trade statistics. Provides access to final trade data, tariffline data, data availability, metadata, live updates, and bulk file download
  name: UN Comtrade Data API
  slug: un-comtrade-data-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: UN Comtrade Data Bulk Download API
  slug: open-un-comtrade-bulk-download-api
- collection_type: open
  name: UN Comtrade Data Bulk Download Data Availability API
  slug: open-un-comtrade-data-availability-api
- collection_type: open
  name: UN Comtrade Data Bulk Download Final Trade Data API
  slug: open-un-comtrade-final-trade-data-api
- collection_type: open
  name: UN Comtrade Data Bulk Download Reference Data API
  slug: open-un-comtrade-reference-data-api
- collection_type: open
  name: UN Comtrade Data Bulk Download Tariffline Data API
  slug: open-un-comtrade-tariffline-data-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/un-comtrade-agentic-access.yml
created: '2026-06-13'
description: United Nations international trade statistics database with a REST API for accessing import/export data, commodity trade flows, and bilateral trade statistics. Covers over 200 reporting countries and territories with data spanning goods and services trade classified by HS, SITC, and other commodity codes.
examples:
- key_count: 4
  name: Check Data Availability
  slug: check-data-availability
- key_count: 4
  name: Get Bilateral Trade
  slug: get-bilateral-trade
- key_count: 4
  name: Preview Goods Exports
  slug: preview-goods-exports
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://comtradeplus.un.org/favicon.ico
json_schemas:
- name: UN Comtrade API Response Envelope
  property_count: 6
  slug: api-response
- name: UN Comtrade Trade Record
  property_count: 47
  slug: trade-record
layout: provider
modified: '2026-06-13'
name: UN Comtrade
nav: Providers
network: true
overview: 'UN Comtrade publishes 1 API on the [APIs.io](https://apis.io/) network: Data API. Tagged areas include Trade, International Trade, Import, Export, and Statistics.


  The UN Comtrade catalog on APIs.io includes 1 Spectral governance ruleset.'
plans:
- name: Plans
  plan_count: 6
  slug: plans
random_paper: 6
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: UN Comtrade API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: un-comtrade-jsonschema-spectral-rules
score:
  band: emerging
  composite: 24.2
  delta: -7.1
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 35.2
    developer_ergonomics: 0.0
    discoverability: 63.0
    governance: 9.8
    operational_transparency: 0.0
  previous_composite: 31.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/un-comtrade/refs/heads/main/screenshots/un-comtrade-2026-06-20T200015.png
security:
- kind: authentication
  name: Un Comtrade Authentication
  slug: un-comtrade-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Un Comtrade Domain Security
  slug: un-comtrade-domain-security
  summary_line: TLSv1.3 · DMARC
slug: un-comtrade
tags:
- Trade
- International Trade
- Import
- Export
- Statistics
- United Nations
- Economics
- Commodities
- Bilateral Trade
- HS Codes
- SITC
---
