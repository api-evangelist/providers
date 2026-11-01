---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Words into Music service.
  name: Words into Music API
  slug: words-into-music-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/wordsintomusic/plans/wordsintomusic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wordsintomusic-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/wordsintomusic/cli/wordsintomusic-cli.yml
  title: ''
  type: CLI
  url: cli/wordsintomusic-cli.yml
- group: auth
  href: https://artifacts.apis.io/wordsintomusic/authentication/wordsintomusic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wordsintomusic-authentication.yml
- group: design
  href: https://artifacts.apis.io/wordsintomusic/conformance/wordsintomusic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wordsintomusic-conformance.yml
- group: other
  href: https://artifacts.apis.io/wordsintomusic/overlays/wordsintomusic-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/wordsintomusic-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/wordsintomusic/llms/wordsintomusic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wordsintomusic-llms.txt
- group: agent
  href: https://artifacts.apis.io/wordsintomusic/well-known/wordsintomusic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wordsintomusic-well-known.yml
- group: other
  href: https://artifacts.apis.io/wordsintomusic/hosts/wordsintomusic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wordsintomusic-hosts.yml
- group: other
  href: https://artifacts.apis.io/wordsintomusic/vendors/wordsintomusic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wordsintomusic-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wordsintomusic.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wordsintomusic.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://wordsintomusic.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://wordsintomusic.com/sign-in/
- group: company
  title: ''
  type: Blog
  url: https://wordsintomusic.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://wordsintomusic.com/blog/mcp-setup-guide/
- group: docs
  title: ''
  type: APIReference
  url: https://wordsintomusic.com/developers/
- group: auth
  href: https://artifacts.apis.io/wordsintomusic/security/wordsintomusic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wordsintomusic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wordsintomusic.com
- group: docs
  title: ''
  type: Documentation
  url: https://wordsintomusic.com/developers
created: '2026-10-22'
description: Words into Music offers an AI-powered song generator that transforms user‑provided text or lyrics into downloadable music tracks. Users can describe an idea, select a sound style, and receive a custom song, showcasing the company’s blend of natural‑language processing and audio synthesis technologies. The service is accessible via a web interface and an API, enabling integration into creative workflows and applications.
image: https://wordsintomusic.com/api/og?path=%2F
layout: provider
modified: '2026-10-22'
name: Words into Music
nav: Providers
network: true
overview: 'Words into Music is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Music, Audio, and Generation.


  Words into Music''s developer surface includes CLI, authentication, pricing, engineering blog, getting-started guide, API reference, documentation, and 12 more developer resources.'
plans:
- name: Wordsintomusic Plans Pricing
  plan_count: 6
  slug: wordsintomusic-plans-pricing
random_paper: 10
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 73.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Wordsintomusic Authentication
  slug: wordsintomusic-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Wordsintomusic Domain Security
  slug: wordsintomusic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wordsintomusic
tags:
- Company
- AI
- Music
- Audio
- Generation
- API
website: https://wordsintomusic.com
---
