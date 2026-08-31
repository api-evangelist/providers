---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    auth_clarity: bearer
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
  score: 5.0
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: REST API enabling independent insurance agencies to generate homeowners insurance quotes, bind policies, manage endorsements, and process renewals programmatically. Agencies can build custom interface
  name: Openly Quote & Bind API
  slug: openly-quote-bind-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.openly.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/openly-insurance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openlyllc
- group: company
  title: ''
  type: Blog
  url: https://openly.com/the-open-door
- group: commercial
  title: ''
  type: Pricing
  url: https://openly.com/homeowners
- group: operate
  title: ''
  type: StatusPage
  url: https://status.openly.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/openlyllc
- group: commercial
  title: ''
  type: Plans
  url: plans/openly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/openly-finops.yml
created: '2026-06-13'
description: Openly is an independent agent home insurance platform founded in 2017 and headquartered in Boston, Massachusetts. The company provides REST APIs for generating homeowners insurance quotes, binding policies, managing endorsements, and processing renewals. Openly operates as a general agency and program administrator, enabling tech-savvy independent agencies to build custom interfaces and plug into the Openly platform on the backend. The platform leverages actuarial science, machine learning, and advanced technology to provide fully underwritten quotes in seconds, supporting primary residences, secondary and seasonal homes, and landlord (rented-to-others) policies with coverage up to $5M guaranteed replacement cost.
finops:
- name: Openly Finops
  service_category: ''
  slug: openly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openly.png
layout: provider
modified: '2026-06-13'
name: Openly
nav: Providers
network: true
overview: 'Openly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Homeowners Insurance, Home Insurance, Quotes, and Bind.


  Openly''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Openly Plans Pricing
  plan_count: 2
  slug: openly-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Openly Rate Limits
  slug: openly-rate-limits
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 19.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openly/refs/heads/main/screenshots/openly-2026-06-20T191015.png
security:
- kind: domain-security
  name: Openly Domain Security
  slug: openly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openly
tags:
- Insurance
- Homeowners Insurance
- Home Insurance
- Quotes
- Bind
- Policy
- Endorsement
- Renewal
- InsurTech
website: https://openly.com/
---
