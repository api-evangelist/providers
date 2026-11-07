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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/beheerjewp-nl/well-known/beheerjewp-nl-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beheerjewp-nl-well-known.yml
- group: other
  href: https://artifacts.apis.io/beheerjewp-nl/hosts/beheerjewp-nl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beheerjewp-nl-hosts.yml
- group: other
  href: https://artifacts.apis.io/beheerjewp-nl/vendors/beheerjewp-nl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beheerjewp-nl-vendors.yml
- group: auth
  href: https://artifacts.apis.io/beheerjewp-nl/security/beheerjewp-nl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beheerjewp-nl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beheerjewp.nl/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://beheerjewp.nl/wordpress-mcp
- group: docs
  title: ''
  type: Documentation
  url: https://beheerjewp.nl/wordpress-mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://beheerjewp.nl/start
- group: operate
  title: ''
  type: Support
  url: https://beheerjewp.nl/hulp
- group: company
  title: ''
  type: Blog
  url: https://beheerjewp.nl/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://beheerjewp.nl/prijzen
- group: start
  title: ''
  type: SignUp
  url: https://beheerjewp.nl/start
- group: start
  title: ''
  type: Login
  url: https://beheerjewp.nl/inloggen
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beheerjewp.nl/voorwaarden
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beheerjewp.nl/privacy
coverage:
  checked: '2026-11-02'
  detail: The provider website offers no public developer program or API documentation, and all spec discovery attempts returned 404 or no content.
  evidence:
  - status: 404
    url: https://beheerjewp.nl/openapi.json
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: Beheer je WP is a Dutch SaaS service that lets users manage their WordPress sites through AI chat assistants such as Claude, ChatGPT, Codex and Grok. Users can add a website, install a plugin, connect their preferred AI, and approve changes via natural language. The platform offers a free tier for one site and paid plans for multiple sites, emphasizing privacy and security. It is operated by Samautomation, a Dutch company (KvK 68369492) based in Wognum.
image: https://beheerjewp.nl/assets/beheerjewp-social-1200x630.png
layout: provider
modified: '2026-11-02'
name: Samautomation
nav: Providers
network: true
overview: 'Samautomation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include WordPress, Artificial Intelligence, ChatGPT, Claude, and Dutch.


  Samautomation''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, and 9 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beheerjewp Nl Domain Security
  slug: beheerjewp-nl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beheerjewp-nl
tags:
- WordPress
- Artificial Intelligence
- ChatGPT
- Claude
- Dutch
- Software-as-a-Service
website: https://beheerjewp.nl/
---
