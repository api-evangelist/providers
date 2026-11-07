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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Machine Control Protocol (MCP) providing tool definitions for useSignal utilities.
  name: usesignal MCP
  slug: usesignal-mcp
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/usesignal-dev/mcp/usesignal-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/usesignal-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/usesignal-dev/hosts/usesignal-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usesignal-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/usesignal-dev/vendors/usesignal-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usesignal-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/usesignal-dev/security/usesignal-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usesignal-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usesignal.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://www.usesignal.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.usesignal.dev/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.usesignal.dev/
- group: operate
  title: ''
  type: Support
  url: https://www.usesignal.dev/support
- group: company
  title: ''
  type: Blog
  url: https://www.usesignal.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.usesignal.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usesignal.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usesignal.dev/privacy
- group: operate
  title: ''
  type: Roadmap
  url: https://www.usesignal.dev/roadmap
- group: build
  title: ''
  type: Postman
  url: https://www.usesignal.dev/postman
- group: start
  title: ''
  type: SignUp
  url: https://www.usesignal.dev/signup
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.usesignal.dev/
created: '2026-10-31'
description: useSignal offers a suite of free, browser‑based tools that require no registration. Users can download video or audio from URLs, record screen or voice, compress and merge PDF files, generate QR codes, and format or beautify JSON data. All tools run client‑side, ensuring privacy and quick results, and are accessible via a clean web interface at usesignal.dev.
image: https://www.usesignal.dev/og/usesignal.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at www.usesignal.dev.
  name: usesignal-dev MCP Server
  slug: usesignal-dev-mcp-yml
modified: '2026-10-31'
name: usesignal-dev
nav: Providers
network: true
overview: 'usesignal-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Free Tools, Video, Audio, PDF, and QR Codes.


  usesignal-dev''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 10 more developer resources.'
random_paper: 15
scopes:
- name: Usesignal Dev Scopes
  scope_count: 0
  slug: usesignal-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 65.0
    operational_transparency: 2.6
  previous_composite: 27.4
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Usesignal Dev Authentication
  slug: usesignal-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Usesignal Dev Domain Security
  slug: usesignal-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: usesignal-dev
tags:
- Free Tools
- Video
- Audio
- PDF
- QR Codes
- JSON
website: https://usesignal.dev/
---
