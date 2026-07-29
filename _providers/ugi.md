---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: UGI International manages LPG and natural gas distribution operations across Europe, primarily through Flaga, AvantiGas, and other regional brands serving 17 European countries with liquid petroleum g
  name: UGI International
  slug: ugi-international
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ugi-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ugi-corporation
- group: operate
  title: ''
  type: Contact
  url: https://www.ugi.com
- group: operate
  title: ''
  type: Contact
  url: https://www.amerigas.com
- group: operate
  title: ''
  type: Contact
  url: https://ugies.com
created: '2026-05-03'
description: 'UGI Corporation is a Fortune 500 international energy distribution and services company headquartered in King of Prussia, Pennsylvania. UGI distributes natural gas, liquid propane, and electricity primarily through four business segments: UGI Utilities (natural gas and electric distribution in Pennsylvania), AmeriGas Propane (largest US propane marketer), Midstream and Marketing, and UGI International (European energy distribution). No public developer API has been identified; the company primarily uses EDI and utility industry standards for B2B data exchange.'
finops:
- name: Ugi Finops
  service_category: Utility / Energy
  slug: ugi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ugi.png
json_schemas:
- name: UGI Energy Account
  property_count: 8
  slug: ugi-energy-account
json_structures:
- name: Ugi Structure
  property_count: 0
  slug: ugi-structure
jsonld:
- class_count: 5
  name: Ugi Context
  property_count: 13
  slug: ugi-context
layout: provider
modified: '2026-07-25'
name: UGI Corporation
nav: Providers
network: true
overview: 'UGI Corporation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Utilities, Natural Gas, Propane, and Electric.


  The UGI Corporation catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Ugi Plans Pricing
  plan_count: 1
  slug: ugi-plans-pricing
press:
- date: '2026-05-25'
  title: UGI Energy Services and Prime Data Centers Forge ...
  url: https://www.ugicorp.com/news-releases/news-release-details/ugi-energy-services-and-prime-data-centers-forge-strategic
- date: '2026-05-25'
  title: UGI Energy Services, Prime Data Centers Announce $100 ...
  url: https://www.facebook.com/PaEnvironmentDigest/posts/ugi-energy-services-prime-data-centers-announce-100-million-partnership-to-devel/1534293588657129/
- date: '2026-05-25'
  title: UGI to build gas pipeline for Prime data center in ...
  url: https://www.investing.com/news/company-news/ugi-to-build-gas-pipeline-for-prime-data-center-in-pennsylvania-93CH-4665359
- date: '2026-05-25'
  title: UGI Energy Services Blog | artificial intelligence
  url: https://blog.ugies.com/topic/artificial-intelligence
- date: '2026-05-25'
  title: 'Press Release: UGI Selects IntelliShift for Vehicle AI Video ...'
  url: https://intellishift.com/resources/blog/press-release-ugi-selects-intellishift-for-vehicle-ai-video-deployment/
random_paper: 9
rate_limits:
- limit_count: 1
  name: Ugi Rate Limits
  slug: ugi-rate-limits
rules:
- name: UGI Corporation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ugi-jsonschema-spectral-rules
score:
  band: emerging
  composite: 24.2
  delta: -6.4
  facets:
    commercial_clarity: 28.9
    contract_quality: 17.7
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 30.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 14.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ugi/refs/heads/main/screenshots/ugi-2026-06-20T195955.png
security:
- kind: domain-security
  name: Ugi Domain Security
  slug: ugi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ugi
tags:
- Energy
- Utilities
- Natural Gas
- Propane
- Electric
- Fortune 500
- Pennsylvania
---
