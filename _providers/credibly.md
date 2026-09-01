---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'REST API (V2) enabling approved broker and referral partners to submit loan applications, upload supporting documentation, receive webhook-based status updates, identify outstanding stipulations, and '
  name: Credibly Lender API
  slug: credibly-lender-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/credibly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.credibly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.credibly.com/where-you-can-find-our-financing/
- group: company
  title: ''
  type: Blog
  url: https://www.credibly.com/incredibly/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.credibly.com/working-capital-loans/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/credibly
- group: other
  title: ''
  type: X
  url: https://x.com/credibly360
- group: start
  title: ''
  type: PartnerPortal
  url: https://portal.credibly.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.credibly.com/contact/
- group: commercial
  title: ''
  type: Plans
  url: plans/credibly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/credibly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/credibly-finops.yml
created: '2026-06-13'
description: Credibly is a small business lending platform offering a REST API (API V2) for originating merchant cash advances, working capital loans, business lines of credit, equipment financing, and SBA loans through an approved broker and referral partner network. The API supports application submission, multi-part document uploads, stipulation identification, and webhook-based status notifications within a SOC 2-compliant environment.
finops:
- name: Credibly Finops
  service_category: ''
  slug: credibly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/credibly.png
layout: provider
modified: '2026-06-13'
name: Credibly
nav: Providers
network: true
overview: 'Credibly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Small Business Lending, Merchant Cash Advance, Working Capital, Business Loans, and Fintech.


  Credibly''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Credibly Plans Pricing
  plan_count: 7
  slug: credibly-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Credibly Rate Limits
  slug: credibly-rate-limits
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 7
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/credibly/refs/heads/main/screenshots/credibly-2026-06-20T175222.png
security:
- kind: domain-security
  name: Credibly Domain Security
  slug: credibly-domain-security
  summary_line: TLSv1.3 · DMARC
slug: credibly
tags:
- Small Business Lending
- Merchant Cash Advance
- Working Capital
- Business Loans
- Fintech
- Lending API
- Partner Integration
website: https://www.credibly.com/
---
