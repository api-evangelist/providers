---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: false
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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/farmo/llms/farmo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/farmo-llms.txt
- group: agent
  href: https://artifacts.apis.io/farmo/well-known/farmo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/farmo-well-known.yml
- group: other
  href: https://artifacts.apis.io/farmo/hosts/farmo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/farmo-hosts.yml
- group: other
  href: https://artifacts.apis.io/farmo/vendors/farmo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/farmo-vendors.yml
- group: auth
  href: https://artifacts.apis.io/farmo/security/farmo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/farmo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://farmo.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.farmo.com.au/pages/api-integration
- group: docs
  title: ''
  type: APIReference
  url: https://www.farmo.com.au/pages/api-integration
- group: start
  title: ''
  type: GettingStarted
  url: https://www.farmo.com.au/pages/api-integration
- group: operate
  title: ''
  type: Support
  url: https://www.farmo.com.au/pages/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.farmo.com.au/blogs/news
- group: commercial
  title: ''
  type: Pricing
  url: https://www.farmo.com.au/pages/farmo-pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.farmo.com.au/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.farmo.com.au/policies/privacy-policy
coverage:
  checked: '2026-10-28'
  detail: Farmo's GraphQL endpoint returns a generic Shopify schema, not a Farmo-specific contract.
  evidence:
  - status: 200
    url: https://farmo.com.au/api/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Farmo makes remote monitoring and automation simple and effective. We provide solutions for agriculture, industrial and smart city applications using mobile and satellite technologies. We deliver the data you need to take action and boost efficiency.
image: http://www.farmo.com.au/cdn/shop/files/Farmo_Brand_Photo_WR_1919dc56-e4be-41fd-96fa-a3048b183665.jpg?v=1759357874
layout: provider
modified: '2026-10-28'
name: Farmo
nav: Providers
network: true
overview: 'Farmo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Industrial, Smart City, Remote Monitoring, and Automation.


  Farmo''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Farmo Plans Pricing
  plan_count: 0
  slug: farmo-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Farmo Rate Limits
  slug: farmo-rate-limits
scopes:
- name: Farmo Scopes
  scope_count: 0
  slug: farmo-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 55.4
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/farmo/farmo-2026-11-03T131851.png
security:
- kind: authentication
  name: Farmo Authentication
  slug: farmo-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Farmo Domain Security
  slug: farmo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: farmo
tags:
- Agriculture
- Industrial
- Smart City
- Remote Monitoring
- Automation
website: https://farmo.com.au/
---
