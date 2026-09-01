---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
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
- description: REST API for EU and UK VAT compliance including VAT rate lookups by country, VAT number validation against VIES and HMRC, currency conversion rates from HMRC and ECB, and generation of VAT-compliant i
  name: VAT API v2
  slug: vat-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vatapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vatapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vatapi.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://vatapi.onfastspring.com/
- group: company
  title: ''
  type: Blog
  url: https://vatapi.com/news
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/infolution
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/vatapi/refs/heads/main/plans/vatapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/vatapi/refs/heads/main/rate-limits/vatapi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/vatapi/refs/heads/main/finops/vatapi-finops.yml
- group: company
  title: ''
  type: BlogPosts
  url: https://raw.githubusercontent.com/api-evangelist/vatapi/refs/heads/main/blogs/blogs.json
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/vatapi/refs/heads/main/json-ld/vatapi.json
created: '2026-06-13'
description: EU and UK VAT compliance REST API providing VAT rate retrieval, VAT number validation via the European Commission VIES system and UK HMRC, currency conversion, and VAT-compliant invoice generation. Operated by Eventured Ltd and launched in 2015, it connects directly to authoritative EU and HMRC sources to deliver audit-ready consultation numbers and real-time rate data.
finops:
- name: Vatapi Finops
  service_category: ''
  slug: vatapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vatapi.png
layout: provider
modified: '2026-06-13'
name: VAT API
nav: Providers
network: true
overview: 'VAT API publishes 1 API on the [APIs.io](https://apis.io/) network: v2. Tagged areas include VAT, Tax, EU, UK, and Compliance.


  VAT API''s developer surface includes documentation, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Vatapi Plans Pricing
  plan_count: 4
  slug: vatapi-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Vatapi Rate Limits
  slug: vatapi-rate-limits
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 24.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vatapi/refs/heads/main/screenshots/vatapi-2026-06-20T200828.png
security:
- kind: domain-security
  name: Vatapi Domain Security
  slug: vatapi-domain-security
  summary_line: TLSv1.2 · DMARC
slug: vatapi
tags:
- VAT
- Tax
- EU
- UK
- Compliance
- Invoice
- VIES
- Business Verification
website: https://vatapi.com/
---
