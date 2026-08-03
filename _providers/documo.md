---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Documo Agentic Access
  operation_count: 13
  slug: documo-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 4
apis:
- description: Read account profile and settings.
  name: Documo Account API
  slug: documo-account-api
- description: Send, resend, retrieve, list, and download faxes.
  name: Documo Fax API
  slug: documo-fax-api
- description: Search, provision, list, and release inbound fax numbers.
  name: Documo Numbers API
  slug: documo-numbers-api
- description: Manage webhook subscriptions for fax and number events.
  name: Documo Webhooks API
  slug: documo-webhooks-api
artifact_total: 12
collections:
- collection_type: open
  name: Documo API
  slug: open-documo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/documo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/documo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/documo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/documo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/documo
- group: company
  title: ''
  type: Website
  url: https://www.documo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.documo.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/documo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/documo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/documo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.documo.com/blog/feed/
created: '2026-06-21'
description: Documo (mFax) is a cloud fax and document delivery platform. The Documo REST API lets developers send and receive faxes, provision and manage fax numbers, subscribe to delivery events via webhooks, and manage account resources over a JSON/HTTPS interface secured with an API key.
finops:
- name: Documo Finops
  service_category: Communications and Document Delivery
  slug: documo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/documo.png
layout: provider
modified: '2026-06-21'
name: Documo
nav: Providers
network: true
overview: 'Documo publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Fax API, Numbers API, and 1 more. Tagged areas include Fax, Cloud Fax, Document Delivery, HIPAA, and Communications.


  Documo''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Documo Plans Pricing
  plan_count: 5
  slug: documo-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 4
  name: Documo Rate Limits
  slug: documo-rate-limits
score:
  band: thin
  composite: 41.2
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 63.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/documo/refs/heads/main/screenshots/documo-2026-07-25T212222.png
security:
- kind: authentication
  name: Documo Authentication
  slug: documo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Documo Domain Security
  slug: documo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Documo Trust Center
  slug: documo-trust-center
  summary_line: SOC 2, HIPAA
slug: documo
tags:
- Fax
- Cloud Fax
- Document Delivery
- HIPAA
- Communications
website: https://www.documo.com/
---
