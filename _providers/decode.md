---
agent_readiness:
  band: human-only
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Decode offers a whiteboard platform with an API for integrating AI agents and code tools.
  name: Decode API
  slug: decode-api
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/decode/hosts/decode-hosts.yml
  title: ''
  type: Hosts
  url: hosts/decode-hosts.yml
- group: other
  href: https://artifacts.apis.io/decode/vendors/decode-vendors.yml
  title: ''
  type: Vendors
  url: vendors/decode-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://decode.dev/changelog
- group: auth
  href: https://artifacts.apis.io/decode/security/decode-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/decode-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://decode.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://decode.dev/developer
- group: docs
  title: ''
  type: Documentation
  url: https://decode.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://decode.dev/api
- group: start
  title: ''
  type: GettingStarted
  url: https://decode.dev/getting-started
- group: operate
  title: ''
  type: Support
  url: https://decode.dev/support
- group: company
  title: ''
  type: Blog
  url: https://decode.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/decode
- group: operate
  title: ''
  type: Roadmap
  url: https://decode.dev/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://decode.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://decode.dev/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://decode.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://decode.dev/privacy
- group: build
  title: ''
  type: Postman
  url: https://decode.dev/postman
coverage:
  checked: '2026-10-29'
  detail: Documentation pages exist but no machine‑readable OpenAPI, AsyncAPI, GraphQL or gRPC specifications were found.
  evidence:
  - status: 200
    url: https://docs.decode.dev/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Decode provides a collaborative visual canvas where developers and AI agents can plan, prototype, and iterate on applications. Users can integrate code from Claude Code, Codex, Cursor, or any MCP agent, and see live previews of every screen. The platform aims to streamline the development workflow by unifying design, code, and AI assistance in a single whiteboard, enabling teams to build faster and more efficiently.
image: https://decode.dev/images/decode-og.png
layout: provider
modified: '2026-10-29'
name: Decode
nav: Providers
network: true
overview: 'Decode is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Collaboration, DeveloperTools, and LowCode.


  Decode''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 11 more developer resources.'
random_paper: 12
scopes:
- name: Decode Scopes
  scope_count: 0
  slug: decode-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Decode Authentication
  slug: decode-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Decode Domain Security
  slug: decode-domain-security
  summary_line: TLSv1.3 · DMARC
slug: decode
tags:
- Company
- AI
- Collaboration
- DeveloperTools
- LowCode
- Whiteboard
website: https://decode.dev
---
