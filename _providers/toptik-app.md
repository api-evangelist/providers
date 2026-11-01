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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.8
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Public TikTok data in one call — videos, creators, comments, search, hashtags, sounds, live streams, places, no-watermark downloads and real transcripts.
  name: TopTik API
  slug: toptik-api
- description: 'toptik-app API as documented publicly: 33 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: toptik-app API
  slug: toptik-app-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/toptik-app/rules/toptik-app-rules.yml
  title: ''
  type: Spectral
  url: rules/toptik-app-rules.yml
- group: design
  href: https://artifacts.apis.io/toptik-app/vocabulary/toptik-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/toptik-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/toptik-app/conventions/toptik-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/toptik-app-conventions.yml
- group: auth
  href: https://artifacts.apis.io/toptik-app/authentication/toptik-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/toptik-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/toptik-app/conformance/toptik-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/toptik-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/toptik-app/mcp/toptik-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/toptik-app-mcp.yml
- group: other
  href: https://artifacts.apis.io/toptik-app/hosts/toptik-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/toptik-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/toptik-app/vendors/toptik-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/toptik-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/toptik-app/security/toptik-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/toptik-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://toptik.app/
- group: docs
  title: ''
  type: Documentation
  url: https://toptik.app/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://toptik.app/docs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://toptik.app/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://toptik.app/privacy/
coverage:
  checked: '2026-10-31'
  detail: Docs are a JavaScript‑rendered SPA, so no machine‑readable spec could be fetched.
  evidence:
  - status: 200
    url: https://toptik.app/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: Public TikTok data in one call — videos, creators, comments, search, hashtags, sounds, live streams, places, no-watermark downloads and real transcripts. Subscribe on RapidAPI, run on Apify, or pay per call over MCP. The service offers 38 REST endpoints, 25 MCP tools, and 14 Apify Actors with >99% success.
image: https://toptik.app/opengraph-image.png?opengraph-image=0rjuialbvno3q.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.toptik.app.
  name: toptik-app MCP Server
  slug: toptik-app-mcp-yml
modified: '2026-10-31'
name: toptik-app
nav: Providers
network: true
overview: 'toptik-app is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, TikTok, Data, and Public.


  The toptik-app catalog on APIs.io includes 1 Spectral governance ruleset.


  toptik-app''s developer surface includes authentication, documentation, API reference, and 11 more developer resources.'
plans:
- name: Toptik App Plans Pricing
  plan_count: 0
  slug: toptik-app-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Toptik App Rate Limits
  slug: toptik-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: toptik-app API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: toptik-app-rules
scopes:
- name: Toptik App Scopes
  scope_count: 0
  slug: toptik-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 50.0
    catalog_earned_first_party: 0.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 70.9
    contract_quality: 38.0
    developer_ergonomics: 28.6
    discoverability: 56.7
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Toptik App Authentication
  slug: toptik-app-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Toptik App Domain Security
  slug: toptik-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: toptik-app
tags:
- Company
- API
- TikTok
- Data
- Public
website: https://toptik.app/
---
