---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/mypinpal-com/authentication/mypinpal-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mypinpal-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/mypinpal-com/scopes/mypinpal-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/mypinpal-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/mypinpal-com/errors/mypinpal-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mypinpal-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mypinpal-com/conformance/mypinpal-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mypinpal-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mypinpal-com/llms/mypinpal-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mypinpal-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/mypinpal-com/well-known/mypinpal-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mypinpal-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/mypinpal-com/hosts/mypinpal-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mypinpal-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/mypinpal-com/security/mypinpal-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mypinpal-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mypinpal.com/
- group: operate
  title: ''
  type: Support
  url: https://mypinpal.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mypinpal.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mypinpal.com/terms
- group: docs
  title: ''
  type: Documentation
  url: https://mypinpal.com/llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://mypinpal.com/learn
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable spec found at any discovered host.
  evidence:
  - status: 404
    url: https://mypinpal.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Pinpal, built by Portfoliobox Stockholm AB, offers simple AI‑enabled note‑taking, project, and to‑do apps hosted in the EU. Founded in 2012 in Stockholm, the company serves about 30,000 paying customers, emphasizing privacy, plain‑Markdown data, and no AI training on user content.
image: https://mypinpal.com/og/pinpal.png
layout: provider
modified: '2026-10-29'
name: mypinpal-com
nav: Providers
network: true
overview: 'mypinpal-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Productivity, Notes, Project, and Sweden.


  mypinpal-com''s developer surface includes authentication, support, documentation, getting-started guide, and 10 more developer resources.'
random_paper: 14
scopes:
- name: Mypinpal Com Scopes
  scope_count: 1
  slug: mypinpal-com-scopes
  summary_line: 1 scope
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 55.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.1
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
screenshot: https://apis.io/screenshots/mypinpal-com/mypinpal-com-2026-11-03T135940.png
security:
- kind: authentication
  name: Mypinpal Com Authentication
  slug: mypinpal-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mypinpal Com Domain Security
  slug: mypinpal-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mypinpal-com
tags:
- Artificial Intelligence
- Productivity
- Notes
- Project
- Sweden
website: https://mypinpal.com/
---
