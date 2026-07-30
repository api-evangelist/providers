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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Searches a firm's extracted clauses and definitions across its connected contract database, with intelligent ranking by frequency, document type, and metadata, surfaced inside Microsoft Word and Outlo
  name: Henchman Clause and Definition Search
  slug: clause-and-definition-search
- description: Builds and maintains a searchable knowledge layer over a firm's precedent contracts by extracting clauses and definitions into a structured store (the base package plus an optional Dynamic Knowledge a
  name: Henchman Knowledge Base
  slug: knowledge-base
- description: Connects Henchman to document management and storage systems - iManage Cloud and On-Prem, NetDocuments, SharePoint, Microsoft OneDrive, Google Drive, and OpenText eDocs - to extract precedent contract
  name: Henchman Integrations
  slug: integrations
artifact_total: 8
collections:
- collection_type: open
  name: Henchman API
  slug: open-henchman
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/henchman-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/henchman-io
- group: company
  title: ''
  type: Website
  url: https://www.henchman.io
- group: docs
  title: ''
  type: Documentation
  url: https://help.henchman.io/home
- group: commercial
  title: ''
  type: Plans
  url: plans/henchman-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/henchman-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/henchman-finops.yml
created: '2026-06-21'
description: Henchman is a legal knowledge and contract-drafting AI platform that surfaces a firm's own past clauses and definitions from its document management system directly inside Microsoft Word, Outlook, and Copilot. It connects to legal DMS platforms (iManage, NetDocuments, SharePoint, OneDrive, Google Drive, OpenText eDocs), extracts and ranks clauses and definitions, and adds a secure multi-LLM AI clause assistant on top. Henchman was acquired by LexisNexis in 2024 and is being integrated into Lexis+ AI and Lexis Create+. Henchman is delivered primarily as add-ins and DMS connectors; it does not publish a public developer API.
finops:
- name: Henchman Finops
  service_category: Legal Technology
  slug: henchman-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/henchman.png
layout: provider
modified: '2026-06-21'
name: Henchman
nav: Providers
network: true
overview: 'Henchman publishes 3 APIs on the [APIs.io](https://apis.io/) network: Clause and Definition Search, Knowledge Base, and Integrations. Tagged areas include Legal, Legal Tech, Contract Drafting, Clause Search, and Knowledge Management.


  Henchman''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Henchman Plans Pricing
  plan_count: 3
  slug: henchman-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Henchman Rate Limits
  slug: henchman-rate-limits
score:
  band: emerging
  composite: 26.9
  delta: -3.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 32.3
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 30.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/henchman/refs/heads/main/screenshots/henchman-2026-07-25T220957.png
security:
- kind: domain-security
  name: Henchman Domain Security
  slug: henchman-domain-security
  summary_line: DNSSEC · DMARC
slug: henchman
tags:
- Legal
- Legal Tech
- Contract Drafting
- Clause Search
- Knowledge Management
- AI
website: https://www.henchman.io
---
