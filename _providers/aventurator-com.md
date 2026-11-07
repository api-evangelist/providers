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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides MCP tools for searching restaurants and retrieving menus via Aventurator Gastro.
  name: Aventurator API
  slug: aventurator-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/aventurator-com/llms/aventurator-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aventurator-com-llms.txt
- group: build
  href: https://artifacts.apis.io/aventurator-com/mcp/aventurator-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aventurator-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aventurator-com/mcp/aventurator-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aventurator-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/aventurator-com/hosts/aventurator-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aventurator-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aventurator-com/vendors/aventurator-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aventurator-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aventurator.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aventurator.com/privacy
- group: auth
  href: https://artifacts.apis.io/aventurator-com/security/aventurator-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aventurator-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aventurator.com/
created: '2026-11-02'
description: Aventurator is a travel-focused web application that helps users discover and navigate points of interest in the Canary Islands, especially Lanzarote. It provides a card feed of places, allows users to stamp visited locations with photos, and generates a personalized trophy poster of their journey. The service is open to all for browsing, with optional accounts for saving trips and accessing premium features like Aventurator Gastro QR menus for partner restaurants.
examples:
- key_count: 3
  name: Aventurator Com Mcp Tools
  slug: aventurator-com-mcp-tools
image: https://www.aventurator.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.aventurator.com.
  name: Aventurator MCP Server
  slug: aventurator-com-mcp-yml
modified: '2026-11-02'
name: Aventurator
nav: Providers
network: true
overview: Aventurator is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Adventure, Navigation, Mobile App, and CanaryIslands.
random_paper: 15
rate_limits:
- limit_count: 0
  name: Aventurator Com Rate Limits
  slug: aventurator-com-rate-limits
scopes:
- name: Aventurator Com Scopes
  scope_count: 0
  slug: aventurator-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 12.0
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aventurator Com Authentication
  slug: aventurator-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aventurator Com Domain Security
  slug: aventurator-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aventurator-com
tags:
- Travel
- Adventure
- Navigation
- Mobile App
- CanaryIslands
website: https://aventurator.com/
---
