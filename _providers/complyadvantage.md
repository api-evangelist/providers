---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Complyadvantage Agentic Access
  operation_count: 19
  slug: complyadvantage-agentic-access
  summary_line: 19 operations · 10 acting
api_count: 5
apis:
- description: ComplyAdvantage's newer Mesh platform API, authenticated with OAuth2 bearer tokens (24-hour validity). Covers the full customer lifecycle - customer creation and screening (sync or async), risk scorin
  name: ComplyAdvantage Mesh Platform API
  slug: complyadvantage-mesh-platform-api
- description: Comments, tags, assignment, and match status workflow on searches.
  name: ComplyAdvantage Case Management API
  slug: complyadvantage-case-management-api
- description: Ongoing monitoring of searches, change differences, and acknowledgement.
  name: ComplyAdvantage Monitored Searches API
  slug: complyadvantage-monitored-searches-api
- description: Create and manage AML screening searches against sanctions, PEP, warning, and adverse media data.
  name: ComplyAdvantage Searches API
  slug: complyadvantage-searches-api
- description: Users on your ComplyAdvantage account.
  name: ComplyAdvantage Users API
  slug: complyadvantage-users-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ComplyAdvantage Case Management API
  slug: open-complyadvantage-case-management-api
- collection_type: open
  name: ComplyAdvantage Case Management Monitored Searches API
  slug: open-complyadvantage-monitored-searches-api
- collection_type: open
  name: ComplyAdvantage Case Management Searches API
  slug: open-complyadvantage-searches-api
- collection_type: open
  name: ComplyAdvantage Case Management Users API
  slug: open-complyadvantage-users-api
- collection_type: open
  name: ComplyAdvantage API
  slug: open-complyadvantage
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/complyadvantage-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/complyadvantage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/complyadvantage-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/complyadvantage
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/complyadvantage
- group: company
  title: ''
  type: Website
  url: https://complyadvantage.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.complyadvantage.com
- group: commercial
  title: ''
  type: Pricing
  url: https://complyadvantage.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/complyadvantage-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/complyadvantage-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/complyadvantage-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://complyadvantage.com/insights/
created: '2026-07-11'
description: ComplyAdvantage provides AI-driven anti-money laundering (AML) and financial crime risk detection - screening people and companies against sanctions and watchlists, politically exposed persons (PEPs and RCAs), and adverse media, with ongoing monitoring that alerts you when a customer's risk profile changes. The REST API (api.complyadvantage.com, with US and APAC regional bases) exposes searches, monitored searches, case management, comments, tags, and users with api-key auth, plus webhooks for match and monitoring updates. The newer Mesh platform API adds customer lifecycle screening, cases and alerts, transaction monitoring, and fraud detection workflows. Used by banks, fintechs, payments, and crypto firms for KYC/AML compliance, sanctions screening, and fraud prevention.
finops:
- name: Complyadvantage Finops
  service_category: Security, Identity, and Compliance
  slug: complyadvantage-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/complyadvantage.png
layout: provider
modified: '2026-07-11'
name: ComplyAdvantage
nav: Providers
network: true
overview: 'ComplyAdvantage publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Case Management API, Monitored Searches API, Searches API, and 1 more. Tagged areas include Anti-Money Laundering, AML, Fraud Detection, Sanctions Screening, and Compliance.


  ComplyAdvantage''s developer surface includes authentication, documentation, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Complyadvantage Plans Pricing
  plan_count: 3
  slug: complyadvantage-plans-pricing
random_paper: 109
rate_limits:
- limit_count: 4
  name: Complyadvantage Rate Limits
  slug: complyadvantage-rate-limits
score:
  band: developing
  composite: 42.0
  delta: 0.2
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 61.4
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/complyadvantage/refs/heads/main/screenshots/complyadvantage-2026-07-25T210154.png
security:
- kind: authentication
  name: Complyadvantage Authentication
  slug: complyadvantage-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Complyadvantage Domain Security
  slug: complyadvantage-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: complyadvantage
tags:
- Anti-Money Laundering
- AML
- Fraud Detection
- Sanctions Screening
- Compliance
- PEP Screening
- Adverse Media
- KYC
- Watchlists
- Transaction Monitoring
- Financial Crime
- RegTech
website: https://complyadvantage.com
---
