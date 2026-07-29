---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Rtx Agentic Access
  operation_count: 3
  slug: rtx-agentic-access
  summary_line: 3 operations
api_count: 3
apis:
- description: Run analytics jobs and retrieve analysis results.
  name: RTX Analytics API
  slug: rtx-analytics-api
- description: Manage and query intelligence data sources.
  name: RTX Data Sources API
  slug: rtx-data-sources-api
- description: Generate and retrieve intelligence reports.
  name: RTX Reports API
  slug: rtx-reports-api
artifact_total: 16
collections:
- collection_type: open
  name: RTX EAGLE API
  slug: open-rtx-eagle-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rtx-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rtx-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rtx-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rtx
- group: company
  title: ''
  type: Website
  url: https://www.rtx.com/
- group: other
  title: ''
  type: Developer
  url: https://www.rtx.com/raytheon/eagle
- group: build
  title: ''
  type: GitHub
  url: https://github.com/raytheonbbn
- group: company
  title: ''
  type: Blog
  url: https://www.rtx.com/news
created: '2025-01-01'
description: 'RTX Corporation is a leading American aerospace and defense company comprising three market businesses: Collins Aerospace, Pratt & Whitney, and Raytheon. Raytheon develops the EAGLE (Enhanced Automated Graphical Logistics Environment) software platform for integrated logistics support and logistic support analysis across defense programs. RTX BBN Technologies (a Raytheon subsidiary) develops open-source software including SPARQL triple stores, NLP frameworks, and TAK ecosystem plugins for government and military situational awareness platforms.'
examples:
- key_count: 2
  name: Rtx List Data Sources Example
  slug: rtx-list-data-sources-example
finops:
- name: Rtx Finops
  service_category: Defense / Aerospace Software
  slug: rtx-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rtx.png
json_schemas:
- name: RTX EAGLE Data Source
  property_count: 7
  slug: rtx-data-source
json_structures:
- name: Rtx Eagle Structure
  property_count: 0
  slug: rtx-eagle-structure
jsonld:
- class_count: 4
  name: Rtx Context
  property_count: 8
  slug: rtx-context
layout: provider
modified: '2026-05-19'
name: RTX
nav: Providers
network: true
overview: 'RTX publishes 3 APIs on the [APIs.io](https://apis.io/) network: Analytics API, Data Sources API, and Reports API. Tagged areas include Defense, Aerospace, Government, Logistics, and Intelligence.


  The RTX catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  RTX''s developer surface includes authentication, GitHub presence, engineering blog, and 5 more developer resources.'
plans:
- name: Rtx Plans Pricing
  plan_count: 1
  slug: rtx-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 1
  name: Rtx Rate Limits
  slug: rtx-rate-limits
rules:
- name: RTX API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: rtx-jsonschema-spectral-rules
- name: RTX API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 7
  slug: rtx-spectral-rules
score:
  band: thin
  composite: 39.1
  delta: -4.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 56.8
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rtx/refs/heads/main/screenshots/rtx-2026-06-20T193244.png
security:
- kind: authentication
  name: Rtx Authentication
  slug: rtx-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rtx Domain Security
  slug: rtx-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: rtx
tags:
- Defense
- Aerospace
- Government
- Logistics
- Intelligence
- Military
website: https://www.rtx.com/
---
