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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Lazybird Speech API lets you list available voices, generate MP3 speech from text or SSML, and create, edit and publish cloned voices.
  name: Lazybird Speech API
  slug: lazybird-speech-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/lazybird-app/conformance/lazybird-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lazybird-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lazybird-app/llms/lazybird-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lazybird-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/lazybird-app/well-known/lazybird-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lazybird-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/lazybird-app/hosts/lazybird-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lazybird-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/lazybird-app/vendors/lazybird-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lazybird-app-vendors.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://www.lazybird.app/roadmap
- group: start
  title: ''
  type: Login
  url: https://www.lazybird.app/studio/login
- group: auth
  href: https://artifacts.apis.io/lazybird-app/security/lazybird-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lazybird-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lazybird.app/
- group: docs
  title: ''
  type: Documentation
  url: https://www.lazybird.app/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.lazybird.app/docs/api-reference
- group: company
  title: ''
  type: Blog
  url: https://www.lazybird.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lazybird.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lazybird.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lazybird.app/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://www.lazybird.app/openapi.json
  - status: null
    url: https://lazybird.app/openapi.json
  - status: 401
    url: https://api.lazybird.app/mcp
  - status: 200
    url: https://lazybird.app/
  reason: partner-login
  state: gated
created: '2026-10-22'
description: Lazybird is an AI voiceover generator for creators, enabling realistic text‑to‑speech for videos, podcasts, audiobooks, courses, and product demos. Users can import scripts, select from a variety of AI voices, generate audio, and download it, with a free tier to start. The platform also offers multilingual support and customizable voice options, aiming to streamline content creation for creators and businesses alike.
image: https://www.lazybird.app/og/home
layout: provider
modified: '2026-10-22'
name: lazybird-app
nav: Providers
network: true
overview: 'lazybird-app is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Voiceover, Text-to-Speech, and Creator Tools.


  lazybird-app''s developer surface includes documentation, API reference, engineering blog, pricing, and 11 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lazybird App Domain Security
  slug: lazybird-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lazybird-app
tags:
- Company
- Artificial Intelligence
- Voiceover
- Text-to-Speech
- Creator Tools
- Multilingual
website: https://www.lazybird.app/
---
