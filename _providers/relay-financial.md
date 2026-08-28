---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Relay API
  slug: open-relay-financial
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/relay-financial-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/relayfi
- group: company
  title: ''
  type: Website
  url: https://relayfi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.relayfi.com/hc/en-us
- group: commercial
  title: ''
  type: Plans
  url: plans/relay-financial-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/relay-financial-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/relay-financial-finops.yml
- group: other
  title: ''
  type: ProductPage
  url: https://relayfi.com/integrations/
created: '2026-06-20'
description: Relay is an online business banking and cash-flow management platform for small and medium-sized businesses, offering up to 20-50 checking accounts, virtual and physical Visa debit/credit cards, accounts payable and bill pay, and one-way data integrations with accounting and payroll tools such as QuickBooks Online, Xero, and Gusto. Banking services are provided by Thread Bank, Member FDIC. Relay does not publish a public developer API; the surfaces below are product features and inbound integrations rather than developer-facing APIs.
finops:
- name: Relay Financial Finops
  service_category: Financial Services
  slug: relay-financial-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/relay-financial.png
layout: provider
modified: '2026-07-25'
name: Relay
nav: Providers
network: true
overview: 'Relay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Business Banking, Fintech, SMB, Cash Flow, and Bill Pay.


  Relay''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Relay Financial Plans Pricing
  plan_count: 3
  slug: relay-financial-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Relay Financial Rate Limits
  slug: relay-financial-rate-limits
score:
  band: emerging
  composite: 14.0
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 14.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/relay-financial/refs/heads/main/screenshots/relay-financial-2026-06-20T192825.png
security:
- kind: domain-security
  name: Relay Financial Domain Security
  slug: relay-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: relay-financial
tags:
- Business Banking
- Fintech
- SMB
- Cash Flow
- Bill Pay
website: https://relayfi.com/
---
