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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/waypay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://waypay.ca
created: '2026-07-17'
description: WayPay was a cloud-based B2B payments and accounts-payable-automation fintech headquartered in Burlington, Ontario, Canada. Its platform let businesses pay any supplier by any method (EFT, cheque, credit card, wire) from a single dashboard, reconciling against accounting and ERP software to automate the accounts-payable workflow. Royal Bank of Canada (RBC) announced its acquisition of WayPay in July 2019, after which the independent brand was retired. As of this enrichment pass the domain waypay.ca resolves via DNS (behind Akamai, enterprise mail) but serves no public site (HTTP 503), and there is no reachable public developer portal, API, or documentation surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/waypay.png
layout: provider
modified: '2026-07-21'
name: WayPay
nav: Providers
network: true
overview: WayPay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fintech, Accounts Payable, and B2B.
random_paper: 16
score:
  band: minimal
  composite: 1.5
  coverage:
    artifact_dirs: 1
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
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Waypay Domain Security
  slug: waypay-domain-security
  summary_line: no transport/DNS hardening detected
slug: waypay
tags:
- Company
- Payments
- Fintech
- Accounts Payable
- B2B
- Canada
- Financial-Services
- Acquired
website: https://waypay.ca
---
