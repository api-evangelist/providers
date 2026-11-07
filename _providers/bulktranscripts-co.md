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
    mcp_server: documented
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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: YouTube transcripts, search, and channel/playlist listings API.
  name: BulkTranscripts API
  slug: bulktranscripts-api
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/bulktranscripts-co/changelog/bulktranscripts-co-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bulktranscripts-co-changelog.yml
- group: design
  href: https://artifacts.apis.io/bulktranscripts-co/conformance/bulktranscripts-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bulktranscripts-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bulktranscripts-co/llms/bulktranscripts-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bulktranscripts-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/bulktranscripts-co/well-known/bulktranscripts-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bulktranscripts-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/bulktranscripts-co/hosts/bulktranscripts-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bulktranscripts-co-hosts.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://bulktranscripts.co/changelog
- group: auth
  href: https://artifacts.apis.io/bulktranscripts-co/security/bulktranscripts-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bulktranscripts-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bulktranscripts.co/
- group: docs
  title: ''
  type: Documentation
  url: https://bulktranscripts.co/docs
- group: docs
  title: ''
  type: APIReference
  url: https://bulktranscripts.co/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://bulktranscripts.co/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bulktranscripts.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bulktranscripts.co/privacy
- group: company
  title: ''
  type: About
  url: https://bulktranscripts.co/about
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://bulktranscripts.co/openapi.json
  - status: 401
    url: https://bulktranscripts.co/mcp
  - status: 200
    url: https://bulktranscripts.co/
  reason: partner-login
  state: gated
created: '2026-11-03'
description: Bulk Transcripts is an independent, one‑person product that downloads every available transcript from YouTube channels, playlists, or videos in bulk. It offers a REST API, an MCP server, and an agent skill, enabling AI agents to retrieve transcripts in formats like JSON, Markdown, CSV, and more. Built by @attenisalluneed since July 2026, the service provides free access to up to 30 transcripts and paid plans for larger volumes, targeting developers, podcasters, and content creators who need large‑scale transcript extraction.
image: https://bulktranscripts.co/og-image.png
layout: provider
modified: '2026-11-03'
name: Bulk Transcripts
nav: Providers
network: true
overview: 'Bulk Transcripts is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Transcripts, YouTube, Artificial Intelligence, MCP, and Developer Tools.


  Bulk Transcripts'' developer surface includes changelog, documentation, API reference, pricing, and 10 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 66.1
    operational_transparency: 7.9
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bulktranscripts Co Domain Security
  slug: bulktranscripts-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bulktranscripts-co
tags:
- Transcripts
- YouTube
- Artificial Intelligence
- MCP
- Developer Tools
website: https://bulktranscripts.co/
---
