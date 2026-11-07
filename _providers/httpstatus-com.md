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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP server exposing developer tools via API for AI assistants, providing programmatic access to status checks and diagnostics.
  name: HttpStatus MCP
  slug: httpstatus-mcp
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/httpstatus-com/hosts/httpstatus-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/httpstatus-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/httpstatus-com/vendors/httpstatus-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/httpstatus-com-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.httpstatus.com/
- group: auth
  href: https://artifacts.apis.io/httpstatus-com/security/httpstatus-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/httpstatus-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://httpstatus.com/
- group: docs
  title: ''
  type: APIReference
  url: https://httpstatus.com/mcp/
- group: start
  title: ''
  type: GettingStarted
  url: https://httpstatus.com/status-responder/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://httpstatus.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://httpstatus.com/privacy/
coverage:
  checked: '2026-10-31'
  detail: The provider's website serves HTML pages for spec URLs (e.g., https://httpstatus.com/openapi.json) with content-type text/html, providing no machine‑readable contract.
  evidence:
  - status: 200
    url: https://httpstatus.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: HttpStatus.com provides a comprehensive reference of all HTTP status codes, from 100 to 511, along with free developer tools such as a URL status checker, redirect tracer, security headers scanner, CORS tester, DNS lookup, JWT decoder, Base64 encoder/decoder, and JSON formatter. It also offers an MCP server that exposes these tools via an API for AI assistants like Claude and Cursor, enabling programmatic access to status checks and diagnostics. The site is privacy‑first, open‑source, and does not require sign‑up to use its tools.
image: https://httpstatus.com/icon.svg?38a5c38ac34e89bc
layout: provider
modified: '2026-10-30'
name: httpstatus-com
nav: Providers
network: true
overview: 'httpstatus-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, HTTP, Status-Codes, Developer Tools, and Open Source.


  httpstatus-com''s developer surface includes engineering blog, API reference, getting-started guide, and 6 more developer resources.'
random_paper: 0
scopes:
- name: Httpstatus Com Scopes
  scope_count: 0
  slug: httpstatus-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 15.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/httpstatus-com/httpstatus-com-2026-11-03T133507.png
security:
- kind: authentication
  name: Httpstatus Com Authentication
  slug: httpstatus-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Httpstatus Com Domain Security
  slug: httpstatus-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: httpstatus-com
tags:
- Company
- HTTP
- Status-Codes
- Developer Tools
- Open Source
website: https://httpstatus.com/
---
