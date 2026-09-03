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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Bikky provides push-button API integrations with leading POS, online ordering, loyalty, and marketing providers, sending data in real time for most POS and ordering sources and nightly for reservation
  name: Bikky Integrations
  slug: rest-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bikky-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bikky-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.bikky.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/bikky-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bikky-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bikky-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bikky-llms.txt
- group: company
  title: ''
  type: Website
  url: https://bikky.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bikky.com/integrations
- group: start
  title: ''
  type: Login
  url: https://app.bikky.com
- group: operate
  title: ''
  type: Support
  url: https://www.bikky.com/learn-more
- group: company
  title: ''
  type: Blog
  url: https://www.bikky.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bikky.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bikky.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bikky-inc
coverage:
  checked: '2026-08-13'
  detail: Bikky markets "push-button API integrations" and a live API host is running — api.bikky.com is an AWS load balancer that answers on every request — but no reference, spec or key-issuance path is published anywhere, and the integrations page routes data access through "our sales and engineering team" before a contract is signed.
  evidence:
  - status: 404
    url: https://api.bikky.com/openapi.json
  - status: 404
    url: https://www.bikky.com/developers
  - status: 200
    url: https://www.bikky.com/integrations
  - status: 404
    url: https://www.bikky.com/pricing
  reason: sales-gate
  state: gated
created: '2026-06-02'
description: Bikky is a New York-based Customer Data Platform (CDP) built exclusively for large, multi-unit restaurant brands, serving thousands of locations for companies such as Bojangles, MOD Pizza, Dave's Hot Chicken, and Long John Silver's. By integrating with point-of-sale, online ordering, payment, and loyalty systems, Bikky builds a single source of truth on guests, cleaning, standardizing, and de-duplicating data to reveal behavior, frequency, lifetime value, and menu performance across channels. Bikky offers push-button API integrations with leading ordering, loyalty, and marketing providers, plus Snowflake data shares, SFTP, and CSV import for data exchange. It does not appear to publish a public, self-service developer API or documentation; integration and data access are arranged directly with Bikky.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bikky.png
layout: provider
modified: '2026-08-13'
name: Bikky
nav: Providers
network: true
overview: 'Bikky publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Restaurant, Customer Data Platform, Guest Analytics, Integration, and Marketing.


  Bikky''s developer surface includes documentation, support, engineering blog, and 12 more developer resources.'
plans:
- name: Bikky Plans Pricing
  plan_count: 0
  slug: bikky-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Bikky Rate Limits
  slug: bikky-rate-limits
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 20.9
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bikky/refs/heads/main/screenshots/bikky-2026-06-20T173237.png
security:
- kind: domain-security
  name: Bikky Domain Security
  slug: bikky-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bikky Trust Center
  slug: bikky-trust-center
  summary_line: SOC 2
slug: bikky
tags:
- Restaurant
- Customer Data Platform
- Guest Analytics
- Integration
- Marketing
- Loyalty
website: https://bikky.com/
---
