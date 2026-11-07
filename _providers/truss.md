---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: operate
  href: https://artifacts.apis.io/truss/rate-limits/truss-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/truss-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/truss/sandbox/truss-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/truss-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trusspayments.com/security
- group: auth
  href: https://artifacts.apis.io/truss/authentication/truss-authentication.yml
  title: ''
  type: Authentication
  url: authentication/truss-authentication.yml
- group: agent
  href: https://artifacts.apis.io/truss/llms/truss-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/truss-llms.txt
- group: agent
  href: https://artifacts.apis.io/truss/well-known/truss-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/truss-well-known.yml
- group: other
  href: https://artifacts.apis.io/truss/hosts/truss-hosts.yml
  title: ''
  type: Hosts
  url: hosts/truss-hosts.yml
- group: other
  href: https://artifacts.apis.io/truss/vendors/truss-vendors.yml
  title: ''
  type: Vendors
  url: vendors/truss-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trusspayments.com/legal/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://trusspayments.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trusspayments.com/legal/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://trusspayments.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.trusspayments.com/guides/webhooks/setup-guide/index
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trusspayments.com/
- group: auth
  href: https://artifacts.apis.io/truss/security/truss-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/truss-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/truss/security/truss-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/truss-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trusspayments.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://trusspayments.com
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Truss provides banking services tailored for the construction industry, offering no monthly or account fees, fast payment processing for subcontractors and vendors, and expense management tools. Their platform enables construction businesses to get paid quickly via ACH and card payments, pay subs and vendors instantly, and manage finances without hidden costs, aiming to streamline financial operations in the building sector.
image: https://cdn.prod.website-files.com/67c6ba2c65db234784dea6b9/68001b2692988da1b13bba10_truss-og.avif
layout: provider
modified: '2026-10-21'
name: Truss
nav: Providers
network: true
overview: 'Truss is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Construction, Payments, and Fintech.


  Truss'' developer surface includes sandbox, authentication, engineering blog, getting-started guide, documentation, and 12 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 4
  name: Truss Rate Limits
  slug: truss-rate-limits
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 62.5
    operational_transparency: 36.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 27.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 14.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/truss/truss-2026-11-03T145117.png
security:
- kind: authentication
  name: Truss Authentication
  slug: truss-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Truss Domain Security
  slug: truss-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Truss Trust Center
  slug: truss-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018
slug: truss
tags:
- Company
- Banking
- Construction
- Payments
- Fintech
website: https://trusspayments.com
---
