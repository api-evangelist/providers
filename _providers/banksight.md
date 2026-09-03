---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://banksight.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.bottomline.com/us/digital-banking — a different registrable domain (banksight.com -> bottomline.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/banksight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://banksight.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/banksight
created: '2026-07-17'
description: BankSight Systems is a cloud banking software company founded in 2015 (San Francisco / Mumbai) that built an intelligent banking CRM and customer engagement platform for community banks, regional banks, and credit unions. The platform consolidated and analyzed customer data on top of Microsoft Azure and the Microsoft Power Platform, running a banking-specific data model with an open integration framework of pre-built connectors to core, LOS, and legacy banking systems, and delivered AI-driven "Next Best Conversation" recommendations to bankers and wealth managers. BankSight was acquired by Bottomline Technologies; its product now lives inside Bottomline's Commercial Digital Banking platform, and banksight.com 301-redirects to bottomline.com. This profile was surfaced as a Bloomberg Beta portfolio company (since exited) and added to the API Evangelist network for enrichment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/banksight.png
layout: provider
modified: '2026-07-18'
name: Banksight
nav: Providers
network: true
overview: Banksight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Financial-Services, CRM, and Customer Engagement.
random_paper: 10
score:
  band: minimal
  composite: 1.5
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 1.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/banksight/refs/heads/main/screenshots/banksight-2026-07-25T202348.png
security:
- kind: domain-security
  name: Banksight Domain Security
  slug: banksight-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: banksight
tags:
- Company
- Banking
- Financial-Services
- CRM
- Customer Engagement
- Digital Banking
- Fintech
- Cloud
website: https://banksight.com
---
