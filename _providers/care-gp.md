---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/care-gp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caregp.com.au/
- group: start
  title: ''
  type: Login
  url: https://agent.caregp.com.au/login
- group: commercial
  title: ''
  type: Pricing
  url: https://caregp.com.au/pricing
- group: auth
  title: ''
  type: Compliance
  url: https://caregp.com.au/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/caregp/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@CareGP-aus
created: '2026-07-17'
description: Care GP is a Sydney-based healthcare technology company (Y Combinator Summer 2026) building a suite of AI agents that automate the administrative and operational work of Australian general practice clinics. Its products include Samantha (medical document allocation that files inbound emails, faxes, and scans), Veronica (24/7 inbound and outbound phone and booking management), and a Billing beta for billing and debt-collection automation. Care GP states it is ISO 27001 certified with onshore Australian data storage, multi-factor authentication, and encryption, and reports serving 400+ clinic operators. As of this enrichment pass the company exposes a customer web application (agent.caregp.com.au) but no public developer portal, API documentation, or OpenAPI definition.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/care-gp.png
layout: provider
modified: '2026-07-18'
name: Care GP
nav: Providers
network: true
overview: 'Care GP is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Tech, Artificial Intelligence, and AI Agents.


  Care GP''s developer surface includes pricing, YouTube channel, and 5 more developer resources.'
random_paper: 71
score:
  band: minimal
  composite: 11.7
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/care-gp/refs/heads/main/screenshots/care-gp-2026-07-25T204525.png
security:
- kind: domain-security
  name: Care Gp Domain Security
  slug: care-gp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: care-gp
tags:
- Company
- Healthcare
- Health Tech
- Artificial Intelligence
- AI Agents
- Primary Care
- Medical Practice
- Automation
- Australia
- Y Combinator
website: https://caregp.com.au/
---
