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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Sandgarden does not publish a public API; the site provides a learning center for AI concepts.
  name: Sandgarden API
  slug: sandgarden-api
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/sandgarden/overlays/sandgarden-api.sandgarden.com_openapi.json-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sandgarden-api.sandgarden.com_openapi.json-overlay.yaml
- group: other
  href: https://artifacts.apis.io/sandgarden/hosts/sandgarden-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sandgarden-hosts.yml
- group: other
  href: https://artifacts.apis.io/sandgarden/vendors/sandgarden-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sandgarden-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sandgarden.com/privacy-off
- group: start
  title: ''
  type: Login
  url: https://www.sandgarden.com/archived/log-in
- group: auth
  href: https://artifacts.apis.io/sandgarden/security/sandgarden-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sandgarden-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sandgarden.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.sandgarden.com/learn
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.sandgarden.com/learn
- group: company
  title: ''
  type: Blog
  url: https://www.sandgarden.com/blog
- group: company
  title: ''
  type: About
  url: https://www.sandgarden.com/about
- group: operate
  title: ''
  type: Contact
  url: https://www.sandgarden.com/contact
coverage:
  checked: '2026-10-29'
  detail: No public API is documented; attempts to fetch OpenAPI specs on api.sandgarden.com and www.sandgarden.com returned 404 or failed.
  evidence:
  - status: failed
    url: https://api.sandgarden.com/openapi.json
  - status: 404
    url: https://www.sandgarden.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Sandgarden is an AI incubator that builds and launches AI‑powered products through a playbook‑driven approach. It operates as a capital‑efficient company‑making machine, creating and scaling startups such as Miranda, Featurette, Affiro, Doc Holiday, and Gloria. The incubator offers resources, mentorship, and product development expertise to turn ideas into market‑ready AI solutions while maintaining a focus on cost efficiency and rapid iteration.
image: https://cdn.prod.website-files.com/66dd653d079776ced5bd3a4a/6765a383b0f6fbc5ec1dd194_fullmark-color-p-500.png
layout: provider
modified: '2026-10-29'
name: Sandgarden
nav: Providers
network: true
overview: 'Sandgarden is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Incubator, Startups, and Technology.


  Sandgarden''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
random_paper: 15
scopes:
- name: Sandgarden Scopes
  scope_count: 0
  slug: sandgarden-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 57.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.2
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sandgarden/sandgarden-2026-11-03T142705.png
security:
- kind: authentication
  name: Sandgarden Authentication
  slug: sandgarden-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Sandgarden Domain Security
  slug: sandgarden-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sandgarden
tags:
- Company
- Artificial Intelligence
- Incubator
- Startups
- Technology
website: https://www.sandgarden.com/
---
