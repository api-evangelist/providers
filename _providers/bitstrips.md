---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: OAuth2 (authorization code + PKCE) API for Bitmoji for Developers, providing access to a connected user's avatar ID, sticker packs, and sticker search. Served from bitmoji.api.snapchat.com/direct with
  name: Bitmoji Direct API
  slug: bitmoji-direct-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitstrips-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bitmoji.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Bitmoji/BitmojiForDevelopers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bitmoji
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitstrips-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bitstrips-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bitstrips-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bitstrips-well-known.yml
created: '2026-07-17'
description: 'Bitstrips was a Toronto-based consumer software company, founded in 2007 by Jacob "Ba" Blackstock, that created the personalized comic platform Bitstrips and the personal-avatar app Bitmoji. Snap Inc. acquired Bitstrips in March 2016, retired the original Bitstrips comic product, and now operates the technology as Bitmoji. The public developer surface today is the Bitmoji Direct API (Bitmoji for Developers): an OAuth2 authorization-code-with-PKCE flow via www.bitmoji.com/connect that grants third-party apps access to a user''s avatar ID, sticker packs, and sticker search, served from bitmoji.api.snapchat.com/direct. Note that Snap has deprecated the "Bitmoji For Identity" product; the standalone stickers and search integrations remain documented. This profile was surfaced as a Kleiner Perkins portfolio company and enriched from the public Bitmoji developer documentation.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bitstrips.png
layout: provider
modified: '2026-07-18'
name: Bitstrips
nav: Providers
network: true
overview: 'Bitstrips publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Avatars, Stickers, and Bitmoji.


  Bitstrips'' developer surface includes documentation, authentication, and 6 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.7
  provenance:
    conformance: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitstrips/refs/heads/main/screenshots/bitstrips-2026-07-25T203209.png
security:
- kind: authentication
  name: Bitstrips Authentication
  slug: bitstrips-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Bitstrips Domain Security
  slug: bitstrips-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bitstrips
tags:
- Company
- Consumer
- Avatars
- Stickers
- Bitmoji
- Messaging
- Image
- Authentication
- Social
website: https://www.bitmoji.com
---
