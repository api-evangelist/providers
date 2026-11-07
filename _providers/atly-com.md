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
  band: agent-ready
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Atly provides place recommendation API accessed via MCP tools endpoint.
  name: Atly API
  slug: atly-api
artifact_total: 6
common:
- group: auth
  href: https://artifacts.apis.io/atly-com/security/atly-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/atly-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/atly-com/llms/atly-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atly-com-llms.txt
- group: build
  href: https://artifacts.apis.io/atly-com/mcp/atly-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/atly-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/atly-com/mcp/atly-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/atly-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/atly-com/well-known/atly-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atly-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/atly-com/hosts/atly-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atly-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/atly-com/vendors/atly-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atly-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.atly.com/news
- group: auth
  href: https://artifacts.apis.io/atly-com/security/atly-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/atly-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/atly-com/security/atly-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atly-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atly.com/
- group: company
  title: ''
  type: Blog
  url: https://www.atly.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atly.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atly.com/terms
created: '2026-11-01'
description: Atly provides context‑aware place recommendations, turning fragmented local signals into structured, explainable place intelligence. Users can specify intents such as "quiet café for work" or "dog‑friendly spot" and receive ranked matches with scores and reasons. The platform powers personal discovery today and enables partners—travel, hospitality, and marketplace services—to embed intelligent location insights into their products. Atly’s API offers place scoring, intent parsing, and rich attribute data, supporting AI assistants, travel planners, and location‑based applications.
image: https://www.atly.com/top/images/logos/logo-blue.svg
layout: provider
mcp_servers:
- description: Remote MCP server at agentic-api.atly.com requiring OAuth.
  name: Atly MCP Server
  slug: atly-com-mcp-yml
modified: '2026-11-01'
name: Atly
nav: Providers
network: true
overview: 'Atly is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Location, Recommendations, Artificial Intelligence, Mapping, and Personalization.


  Atly''s developer surface includes engineering blog and 13 more developer resources.'
random_paper: 14
scopes:
- name: Atly Com Scopes
  scope_count: 0
  slug: atly-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 24.0
    developer_ergonomics: 1.2
    discoverability: 65.8
    operational_transparency: 10.5
  previous_composite: 21.4
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Atly Com Authentication
  slug: atly-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Atly Com Domain Security
  slug: atly-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Atly Com Vulnerability Disclosure
  slug: atly-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: atly-com
tags:
- Location
- Recommendations
- Artificial Intelligence
- Mapping
- Personalization
website: https://www.atly.com/
---
