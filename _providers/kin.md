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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Kin Insurance platform provides data-driven home insurance services including property data enrichment, automated underwriting, online quote generation, policy binding, and claims management for h
  name: Kin Insurance Platform API
  slug: kin-insurance-platform
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kin.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.kin.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/kin-insurance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kin-insurance
- group: company
  title: ''
  type: Blog
  url: https://www.kin.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kin.com/homeowners-insurance/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kin.com
- group: other
  title: ''
  type: X
  url: https://x.com/kin
- group: commercial
  title: ''
  type: Plans
  url: plans/kin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kin-finops.yml
created: '2026-06-13'
description: Kin Insurance is a direct-to-consumer home insurance platform founded in 2016 that leverages data and artificial intelligence to provide homeowners insurance in high-risk coastal and weather-exposed markets. The platform uses thousands of property data points for automated underwriting, enabling online quote generation, policy binding, and claims management without the need for traditional agents. Kin offers homeowners, condo, flood, and auto insurance across multiple states with a focus on affordability and accessibility in markets traditionally underserved by major carriers.
finops:
- name: Kin Finops
  service_category: ''
  slug: kin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kin.png https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-06-13'
name: Kin Insurance
nav: Providers
network: true
overview: 'Kin Insurance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Home Insurance, InsureTech, Property Data, and Underwriting.


  Kin Insurance''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Kin Plans Pricing
  plan_count: 4
  slug: kin-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Kin Rate Limits
  slug: kin-rate-limits
score:
  band: emerging
  composite: 16.1
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
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 16.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kin/refs/heads/main/screenshots/kin-2026-06-20T184037.png
security:
- kind: domain-security
  name: Kin Domain Security
  slug: kin-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: kin
tags:
- Insurance
- Home Insurance
- InsureTech
- Property Data
- Underwriting
- Claims
- Direct to Consumer
website: https://www.kin.com
---
