---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ChargeZen provides payment processing APIs documented at https://chargezen.com/docs/spark/api/endpoints
  name: ChargeZen API
  slug: chargezen-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/chargezen-com/hosts/chargezen-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chargezen-com-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://chargezen.com/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chargezen.com/terms
- group: operate
  title: ''
  type: Support
  url: https://chargezen.com/help
- group: operate
  title: ''
  type: StatusPage
  url: https://chargezen.com/status
- group: auth
  title: ''
  type: Security
  url: https://chargezen.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chargezen.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://chargezen.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chargezen
- group: docs
  title: ''
  type: Documentation
  url: https://chargezen.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://chargezen.com/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://chargezen.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://chargezen.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://chargezen.com/subscriptions/getting-started
- group: auth
  href: https://artifacts.apis.io/chargezen-com/security/chargezen-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chargezen-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chargezen.com/
coverage:
  checked: '2026-10-29'
  detail: OpenAPI spec not found at https://api.chargezen.com/openapi.json (HTTP 0)
  evidence:
  - status: 0
    url: https://api.chargezen.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: 'chargezen-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://chargezen.com/og-default.png
layout: provider
modified: '2026-10-29'
name: chargezen-com
nav: Providers
network: true
overview: 'chargezen-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  chargezen-com''s developer surface includes support, pricing, documentation, changelog, engineering blog, getting-started guide, and 10 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.8
  facets:
    access_clarity: 19.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 23.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 27.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/chargezen-com/chargezen-com-2026-11-03T124016.png
security:
- kind: domain-security
  name: Chargezen Com Domain Security
  slug: chargezen-com-domain-security
  summary_line: DMARC
slug: chargezen-com
tags:
- Company
website: https://chargezen.com/
---
