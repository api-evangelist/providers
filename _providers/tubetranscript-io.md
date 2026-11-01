---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: operate
  href: https://artifacts.apis.io/tubetranscript-io/rate-limits/tubetranscript-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tubetranscript-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tubetranscript-io/plans/tubetranscript-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tubetranscript-io-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/tubetranscript-io/changelog/tubetranscript-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tubetranscript-io-changelog.yml
- group: auth
  href: https://artifacts.apis.io/tubetranscript-io/authentication/tubetranscript-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tubetranscript-io-authentication.yml
- group: agent
  href: https://artifacts.apis.io/tubetranscript-io/llms/tubetranscript-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tubetranscript-io-llms.txt
- group: other
  href: https://artifacts.apis.io/tubetranscript-io/hosts/tubetranscript-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tubetranscript-io-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://tubetranscript.io/sign-in
- group: auth
  href: https://artifacts.apis.io/tubetranscript-io/security/tubetranscript-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tubetranscript-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tubetranscript.io/
- group: docs
  title: ''
  type: Documentation
  url: https://tubetranscript.io/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://tubetranscript.io/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://tubetranscript.io/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://tubetranscript.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tubetranscript.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tubetranscript.io/privacy
- group: operate
  title: ''
  type: Contact
  url: https://tubetranscript.io/contact
coverage:
  checked: '2026-10-30'
  detail: The provider's documentation pages are HTML only and no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found despite probing common spec endpoints.
  evidence:
  - status: 0
    url: https://api.tubetranscript.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: TubeTranscript.io provides a free YouTube transcript generator and related tools, allowing users to paste a YouTube link and instantly obtain the full transcript, subtitles, or timed JSON. The service offers multiple utilities such as timestamp removal, filler‑word cleaning, and transcript splitting for AI prompts, all accessible via a simple web interface and an API for developers.
image: https://tubetranscript.io/opengraph-image.jpg
layout: provider
modified: '2026-10-30'
name: tubetranscript-io
nav: Providers
network: true
overview: 'tubetranscript-io is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, YouTube, Transcript, FreeTool, and API.


  tubetranscript-io''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, and 10 more developer resources.'
plans:
- name: Tubetranscript Io Plans Pricing
  plan_count: 3
  slug: tubetranscript-io-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Tubetranscript Io Rate Limits
  slug: tubetranscript-io-rate-limits
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 51.0
    catalog_earned_first_party: 24.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 48.2
    operational_transparency: 47.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Tubetranscript Io Authentication
  slug: tubetranscript-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Tubetranscript Io Domain Security
  slug: tubetranscript-io-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tubetranscript-io
tags:
- Company
- YouTube
- Transcript
- FreeTool
- API
website: https://tubetranscript.io/
---
