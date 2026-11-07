---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for accessing LEGO data via the Model Context Protocol (MCP) as documented in the MCP Setup guide.
  name: Brick Directory API
  slug: brick-directory-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/brick-directory/authentication/brick-directory-authentication.yml
  title: ''
  type: Authentication
  url: authentication/brick-directory-authentication.yml
- group: agent
  href: https://artifacts.apis.io/brick-directory/well-known/brick-directory-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brick-directory-well-known.yml
- group: other
  href: https://artifacts.apis.io/brick-directory/hosts/brick-directory-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brick-directory-hosts.yml
- group: other
  href: https://artifacts.apis.io/brick-directory/vendors/brick-directory-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brick-directory-vendors.yml
- group: auth
  href: https://artifacts.apis.io/brick-directory/security/brick-directory-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brick-directory-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brick.directory/
- group: docs
  title: ''
  type: Documentation
  url: https://brick.directory/docs/about.html
- group: docs
  title: ''
  type: APIReference
  url: https://brick.directory/docs/mcp-setup.html
- group: start
  title: ''
  type: GettingStarted
  url: https://brick.directory/docs/mcp-setup.html
- group: operate
  title: ''
  type: Support
  url: https://brick.directory/docs/contact.html
- group: company
  title: ''
  type: Blog
  url: https://brick.directory/blog.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brick.directory/docs/terms-of-service.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brick.directory/docs/privacy-policy.html
coverage:
  checked: '2026-11-03'
  detail: Provider documentation exists but no public OpenAPI, GraphQL, or MCP spec is accessible without authentication.
  evidence:
  - status: 404
    url: https://api.brick.directory/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Brick Directory provides an AI-powered LEGO assistant that connects to comprehensive LEGO data via the Model Context Protocol (MCP). Users can access LEGO sets, parts, minifigures, and pricing through Claude, ChatGPT, and Gemini, enabling free AI-driven LEGO chat and information retrieval. The service offers a web interface and integrates with major AI platforms to deliver real-time LEGO data and insights.
image: https://brick.directory/assets/logo-1024-transparent.png
layout: provider
modified: '2026-11-03'
name: Brick Directory
nav: Providers
network: true
overview: 'Brick Directory is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, LEGO, Assistant, and MCP.


  Brick Directory''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, and 7 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
- kind: authentication
  name: Brick Directory Authentication
  slug: brick-directory-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Brick Directory Domain Security
  slug: brick-directory-domain-security
  summary_line: TLSv1.3
slug: brick-directory
tags:
- Company
- Artificial Intelligence
- LEGO
- Assistant
- MCP
website: https://brick.directory/
---
