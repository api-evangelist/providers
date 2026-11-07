---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Casuyi provides a suite of lightweight, privacy‑first mobile applications designed for everyday life.
  name: Casuyi Apps
  slug: casuyi-apps
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/casuyi-com/hosts/casuyi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/casuyi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/casuyi-com/vendors/casuyi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/casuyi-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/casuyi-com/security/casuyi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/casuyi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://casuyi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://casuyi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://casuyi.com/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://casuyi.com/developer
- group: company
  title: ''
  type: Blog
  url: https://casuyi.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://casuyi.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://casuyi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://casuyi.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://casuyi.com/support
- group: build
  title: ''
  type: Postman
  url: https://casuyi.com/postman
coverage:
  checked: '2026-10-30'
  detail: The public documentation pages (e.g., https://casuyi.com/docs) contain no machine‑readable OpenAPI, GraphQL, AsyncAPI, or other contract.
  evidence:
  - status: 200
    url: https://casuyi.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Casuyi provides a suite of lightweight, privacy‑first mobile applications designed for everyday life, including protein tracking, QR discount code scanning, bill and payment management, price history lookup, package pickup coordination, AI‑generated complaint drafting, and subscription tracking. All apps operate offline, require no user account, and prioritize user privacy.
image: https://casuyi.com/og-image.png
layout: provider
modified: '2026-10-29'
name: casuyi-com
nav: Providers
network: true
overview: 'casuyi-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobile App, Privacy, Productivity, and Health.


  casuyi-com''s developer surface includes documentation, API reference, engineering blog, pricing, support, and 8 more developer resources.'
plans:
- name: Casuyi Com Plans Pricing
  plan_count: 0
  slug: casuyi-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Casuyi Com Rate Limits
  slug: casuyi-com-rate-limits
scopes:
- name: Casuyi Com Scopes
  scope_count: 0
  slug: casuyi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 21.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/casuyi-com/casuyi-com-2026-11-03T123502.png
security:
- kind: authentication
  name: Casuyi Com Authentication
  slug: casuyi-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Casuyi Com Domain Security
  slug: casuyi-com-domain-security
  summary_line: TLSv1.3
slug: casuyi-com
tags:
- Company
- Mobile App
- Privacy
- Productivity
- Health
- Finance
website: https://casuyi.com/
---
