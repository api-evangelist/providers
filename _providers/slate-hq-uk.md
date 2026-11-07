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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Connect AMBI to supported AI tools through remote MCP, explore the Mac CLI, or enquire about the AmbientOS partner API.
  name: AmbientOS Partner API
  slug: ambientos-partner-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/slate-hq-uk/well-known/slate-hq-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/slate-hq-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/slate-hq-uk/hosts/slate-hq-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/slate-hq-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/slate-hq-uk/vendors/slate-hq-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/slate-hq-uk-vendors.yml
- group: auth
  href: https://artifacts.apis.io/slate-hq-uk/security/slate-hq-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/slate-hq-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://slate-hq.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://slate-hq.uk/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://slate-hq.uk/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://slate-hq.uk/about/
- group: operate
  title: ''
  type: Support
  url: https://slate-hq.uk/contact/
- group: company
  title: ''
  type: Blog
  url: https://slate-hq.uk/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://slate-hq.uk/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://slate-hq.uk/terms/
- group: start
  title: ''
  type: SignUp
  url: https://slate-hq.uk/ambi-runtime-auth/
coverage:
  checked: '2026-10-29'
  detail: The provider's developer portal does not publish any machine‑readable API contract (no OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL) and only describes the partner API in prose.
  evidence:
  - status: 200
    url: https://slate-hq.uk/developers/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Slate HQ Ltd builds AmbientOS, AMBI, and the .slate format to enable contextual AI integration across personal and work data. Their platform offers developers APIs to connect AI tools, manage memory ambience, and integrate health and productivity services, emphasizing privacy and user control.
image: https://slate-hq.uk/wp-content/uploads/2026/10/slate-hq-wordmark-canva-20261010.png
layout: provider
modified: '2026-10-29'
name: slate-hq-uk
nav: Providers
network: true
overview: 'slate-hq-uk is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Productivity, AmbientOS, Privacy, and United Kingdom.


  slate-hq-uk''s developer surface includes documentation, getting-started guide, support, engineering blog, signup flow, and 8 more developer resources.'
random_paper: 12
scopes:
- name: Slate Hq Uk Scopes
  scope_count: 0
  slug: slate-hq-uk-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/slate-hq-uk/slate-hq-uk-2026-11-03T143331.png
security:
- kind: authentication
  name: Slate Hq Uk Authentication
  slug: slate-hq-uk-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Slate Hq Uk Domain Security
  slug: slate-hq-uk-domain-security
  summary_line: TLSv1.3 · DMARC
slug: slate-hq-uk
tags:
- Artificial Intelligence
- Productivity
- AmbientOS
- Privacy
- United Kingdom
website: https://slate-hq.uk/
---
