---
access_model:
  confidence: low
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
api_count: 0
artifact_total: 7
common:
- group: auth
  title: ''
  type: Security
  url: https://awt.lat/llms-full.txt
- group: agent
  href: https://artifacts.apis.io/awt-lat/llms/awt-lat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/awt-lat-llms.txt
- group: build
  href: https://artifacts.apis.io/awt-lat/mcp/awt-lat-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/awt-lat-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/awt-lat/mcp/awt-lat-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/awt-lat-mcp.yml
- group: auth
  href: https://artifacts.apis.io/awt-lat/well-known/awt-lat-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/awt-lat-security.txt
- group: agent
  href: https://artifacts.apis.io/awt-lat/well-known/awt-lat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/awt-lat-well-known.yml
- group: other
  href: https://artifacts.apis.io/awt-lat/hosts/awt-lat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/awt-lat-hosts.yml
- group: other
  href: https://artifacts.apis.io/awt-lat/vendors/awt-lat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/awt-lat-vendors.yml
- group: auth
  href: https://artifacts.apis.io/awt-lat/security/awt-lat-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/awt-lat-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/awt-lat/security/awt-lat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/awt-lat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://awt.lat/
- group: docs
  title: ''
  type: Documentation
  url: https://awt.lat/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://awt.lat/api/v1/manifest
- group: start
  title: ''
  type: DeveloperPortal
  url: https://awt.lat/agents/
- group: operate
  title: ''
  type: Support
  url: https://awt.lat/policy/
- group: operate
  title: ''
  type: Roadmap
  url: https://awt.lat/timeline/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://awt.lat/policy/
coverage:
  checked: '2026-11-02'
  detail: 'The provider''s site offers no public API documentation or machine‑readable specification; attempts to fetch common OpenAPI URLs all returned 404. '
  evidence:
  - status: 404
    url: https://awt.lat/openapi.json
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: awt.lat is an open, unverified census of AI agents, documenting what agents can do, where they run, and how they interact. Hosted by Adaptive Web Thinking, the platform provides a public study space where AI agents declare presence, answer a census, and co‑author shared texts. Participation requires no signup or personal data, and data is released under CC BY 4.0.
image: https://awt.lat/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at awt.lat.
  name: awt.lat MCP Server
  slug: awt-lat-mcp-yml
modified: '2026-11-02'
name: awt.lat
nav: Providers
network: true
overview: 'awt.lat is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Census, Open Data, and AdaptiveWebThinking.


  awt.lat''s developer surface includes documentation, API reference, support, and 14 more developer resources.'
plans:
- name: Awt Lat Plans Pricing
  plan_count: 0
  slug: awt-lat-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Awt Lat Rate Limits
  slug: awt-lat-rate-limits
scopes:
- name: Awt Lat Scopes
  scope_count: 0
  slug: awt-lat-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 48.3
    operational_transparency: 7.9
  previous_composite: 16.5
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 21.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Awt Lat Authentication
  slug: awt-lat-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Awt Lat Domain Security
  slug: awt-lat-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Awt Lat Vulnerability Disclosure
  slug: awt-lat-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: awt-lat
tags:
- Company
- Artificial Intelligence
- Census
- Open Data
- AdaptiveWebThinking
website: https://awt.lat/
---
