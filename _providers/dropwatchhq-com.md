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
    mcp_server: verified
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
  score: 8.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Agent-payable live drop restock feed for retro game re-releases.
  name: Amiibo Drops API
  slug: amiibo-drops-api
- description: Agent-payable live drop restock feed for designer art toys.
  name: Art Toys Drops API
  slug: art-toys-drops-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/dropwatchhq-com/llms/dropwatchhq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dropwatchhq-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dropwatchhq-com/mcp/dropwatchhq-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dropwatchhq-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/dropwatchhq-com/hosts/dropwatchhq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dropwatchhq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dropwatchhq-com/vendors/dropwatchhq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dropwatchhq-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dropwatchhq-com/security/dropwatchhq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dropwatchhq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dropwatchhq.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dropwatchhq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dropwatchhq.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://dropwatchhq.com/contact
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, or GraphQL specifications found at standard endpoints on any discovered host.
  evidence:
  - status: 404
    url: https://dropwatchhq.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: DropWatch watches the shops you love and emails you the instant something drops or restocks — Pokémon & TCG, anime figures, Funko, LEGO, indie yarn, keyboards, vinyl, rare aquarium livestock, and US product recalls. DropWatch is a network of independent restock and drop alert sites for collectibles, craft and home.
image: https://dropwatchhq.com/og.svg
layout: provider
mcp_servers:
- description: Remote MCP server at amiibo.dropwatchhq.com over HTTP; 2 tools listed.
  name: RetroDrop
  slug: retrodrop
modified: '2026-10-29'
name: dropwatchhq-com
nav: Providers
network: true
overview: 'dropwatchhq-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Collectibles, Alerts, Restock, and E-Commerce.


  dropwatchhq-com''s developer surface includes support and 8 more developer resources.'
random_paper: 17
scopes:
- name: Dropwatchhq Com Scopes
  scope_count: 0
  slug: dropwatchhq-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 75.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.9
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
screenshot: https://apis.io/screenshots/dropwatchhq-com/dropwatchhq-com-2026-11-03T131049.png
security:
- kind: authentication
  name: Dropwatchhq Com Authentication
  slug: dropwatchhq-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Dropwatchhq Com Domain Security
  slug: dropwatchhq-com-domain-security
  summary_line: TLSv1.3
slug: dropwatchhq-com
tags:
- Company
- Collectibles
- Alerts
- Restock
- E-Commerce
- Community
website: https://dropwatchhq.com/
---
