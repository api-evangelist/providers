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
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/paladindrones-io/hosts/paladindrones-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/paladindrones-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/paladindrones-io/vendors/paladindrones-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/paladindrones-io-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paladindrones.io/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.paladindrones.io/press
- group: auth
  href: https://artifacts.apis.io/paladindrones-io/security/paladindrones-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/paladindrones-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.paladindrones.io/
- group: company
  title: ''
  type: Blog
  url: https://www.paladindrones.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PaladinDrones
coverage:
  checked: '2026-10-29'
  detail: All attempted OpenAPI spec URLs on api.paladindrones.io returned 404, and dashboard.paladindrones.io served only HTML pages, providing no machine‑readable contract.
  evidence:
  - status: 404
    url: https://api.paladindrones.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Paladin autonomously deploys drones to emergency incidents, delivering real-time aerial intelligence before the first unit arrives. Built as infrastructure any department can use, regardless of city size, the platform integrates with dispatch workflows to provide immediate situational awareness and support community-led public safety operations.
image: https://cdn.prod.website-files.com/6704475e037f03d37c7ba3ca/69de96ce499d0c5ffefbcb12_Open%20Graph%20Image.avif
layout: provider
modified: '2026-10-29'
name: Paladin
nav: Providers
network: true
overview: 'Paladin is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Drone, Public Safety, Emergency Response, Aerial Intelligence, and First Responder.


  Paladin''s developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Paladindrones Io Plans
  plan_count: 0
  slug: paladindrones-io-plans
random_paper: 9
rate_limits:
- limit_count: 0
  name: Paladindrones Io Rate Limits
  slug: paladindrones-io-rate-limits
scopes:
- name: Paladindrones Io Scopes
  scope_count: 0
  slug: paladindrones-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 49.1
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.9
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/paladindrones-io/paladindrones-io-2026-11-03T140857.png
security:
- kind: authentication
  name: Paladindrones Io Authentication
  slug: paladindrones-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Paladindrones Io Domain Security
  slug: paladindrones-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paladindrones-io
tags:
- Drone
- Public Safety
- Emergency Response
- Aerial Intelligence
- First Responder
website: https://www.paladindrones.io/
---
