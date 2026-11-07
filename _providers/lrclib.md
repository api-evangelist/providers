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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API for accessing lyrics data, supporting search, retrieval, and metadata endpoints. No authentication required.
  name: LRCLIB API
  slug: lrclib-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/lrclib/errors/lrclib-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lrclib-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/lrclib/llms/lrclib-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lrclib-llms.txt
- group: other
  href: https://artifacts.apis.io/lrclib/hosts/lrclib-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lrclib-hosts.yml
- group: other
  href: https://artifacts.apis.io/lrclib/vendors/lrclib-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lrclib-vendors.yml
- group: auth
  href: https://artifacts.apis.io/lrclib/security/lrclib-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lrclib-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lrclib.net/
- group: docs
  title: ''
  type: Documentation
  url: https://lrclib.net/docs/api.md
- group: docs
  title: ''
  type: APIReference
  url: https://lrclib.net/docs/api.md
- group: start
  title: ''
  type: GettingStarted
  url: https://lrclib.net/docs#quickstart
- group: agent
  title: ''
  type: llms
  url: https://lrclib.net/llms.txt
coverage:
  checked: '2026-10-28'
  detail: The provider offers only markdown documentation and returns a 404 HTML page for typical OpenAPI URLs (e.g., https://lrclib.net/openapi.json).
  evidence:
  - status: 404
    url: https://lrclib.net/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: LRCLIB provides a free and open lyrics database accessible via a public API. It offers endpoints to search for songs, retrieve lyrics, and obtain metadata such as artists and albums. The service is unauthenticated, CORS-enabled, and includes generous rate limits for anonymous users, with optional registration for higher limits. Documentation is available in Markdown and plain text formats.
image: https://lrclib.net/favicon.ico
layout: provider
modified: '2026-10-28'
name: LRCLIB
nav: Providers
network: true
overview: 'LRCLIB is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Lyrics, Music, and Open Source.


  LRCLIB''s developer surface includes documentation, API reference, getting-started guide, and 7 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 64.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lrclib/lrclib-2026-11-03T135109.png
security:
- kind: domain-security
  name: Lrclib Domain Security
  slug: lrclib-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lrclib
tags:
- Company
- Lyrics
- Music
- Open Source
website: https://lrclib.net/
---
