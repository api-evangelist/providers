---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: EZBiz services are accessible through multiple integration points depending on the product, with MCP servers as the primary API.
  name: EZBiz API
  slug: ezbiz-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/ezbizservices-com/plans/ezbizservices-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ezbizservices-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/ezbizservices-com/authentication/ezbizservices-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ezbizservices-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/ezbizservices-com/conformance/ezbizservices-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ezbizservices-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ezbizservices-com/llms/ezbizservices-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ezbizservices-com-llms.txt
- group: other
  href: https://artifacts.apis.io/ezbizservices-com/hosts/ezbizservices-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ezbizservices-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ezbizservices-com/vendors/ezbizservices-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ezbizservices-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ezbizservices-com/security/ezbizservices-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ezbizservices-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ezbizservices.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ezbizservices.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ezbizservices.com/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ezbizservices.com/
- group: company
  title: ''
  type: Blog
  url: https://ezbizservices.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ezbizservices.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ezbizservices.com/terms
- group: operate
  title: ''
  type: Support
  url: https://ezbizservices.com/contact
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ezbizservices.com/
coverage:
  checked: '2026-10-29'
  detail: Documentation is public but no OpenAPI/GraphQL/AsyncAPI spec is published.
  evidence:
  - status: 200
    url: https://docs.ezbizservices.com/api/overview
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: EZBiz is the AI receptionist and front office for service businesses, offering 24/7 AI call answering, texts, scheduling, and follow-ups for HVAC, plumbing, electrical, roofing, and more, starting at $149 per month.
image: https://ezbizservices.com/og-image.png
layout: provider
modified: '2026-10-29'
name: ezbizservices-com
nav: Providers
network: true
overview: 'ezbizservices-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Receptionist, Service Business, Automation, and Scheduling.


  ezbizservices-com''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, and 10 more developer resources.'
plans:
- name: Ezbizservices Com Plans Pricing
  plan_count: 5
  slug: ezbizservices-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Ezbizservices Com Rate Limits
  slug: ezbizservices-com-rate-limits
scopes:
- name: Ezbizservices Com Scopes
  scope_count: 0
  slug: ezbizservices-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 34.5
    discoverability: 64.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 33.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ezbizservices-com/ezbizservices-com-2026-11-03T131747.png
security:
- kind: authentication
  name: Ezbizservices Com Authentication
  slug: ezbizservices-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Ezbizservices Com Domain Security
  slug: ezbizservices-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ezbizservices-com
tags:
- Artificial Intelligence
- Receptionist
- Service Business
- Automation
- Scheduling
website: https://ezbizservices.com/
---
