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
    mcp_server: documented
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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides a bounty board API accessed via MCP at https://bounty.brelsfordsoftware.com/mcp.
  name: Brelsford Software API
  slug: brelsford-software-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/brelsfordsoftware-com/llms/brelsfordsoftware-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brelsfordsoftware-com-llms.txt
- group: build
  href: https://artifacts.apis.io/brelsfordsoftware-com/mcp/brelsfordsoftware-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/brelsfordsoftware-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/brelsfordsoftware-com/mcp/brelsfordsoftware-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/brelsfordsoftware-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/brelsfordsoftware-com/hosts/brelsfordsoftware-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brelsfordsoftware-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/brelsfordsoftware-com/vendors/brelsfordsoftware-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brelsfordsoftware-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/brelsfordsoftware-com/security/brelsfordsoftware-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brelsfordsoftware-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brelsfordsoftware.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://brelsfordsoftware.com/developer-portal
- group: docs
  title: ''
  type: Documentation
  url: https://brelsfordsoftware.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://brelsfordsoftware.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://brelsfordsoftware.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://brelsfordsoftware.com/support
- group: company
  title: ''
  type: Blog
  url: https://brelsfordsoftware.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jasonbrelsford
- group: operate
  title: ''
  type: Roadmap
  url: https://brelsfordsoftware.com/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://brelsfordsoftware.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://brelsfordsoftware.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brelsfordsoftware.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brelsfordsoftware.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://brelsfordsoftware.com/postman
coverage:
  checked: '2026-10-30'
  detail: The provider's public site offers a bounty board API via MCP but no machine‑readable OpenAPI, GraphQL, or AsyncAPI specification is published.
  evidence:
  - status: 200
    url: https://brelsfordsoftware.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Brelsford Software LLC builds agent infrastructure, computational immunogenetics tooling, and quiet games. It provides a directory of projects, each published as structured data for automated enumeration, and offers APIs for agents to interact with its services.
image: https://brelsfordsoftware.com/favicon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at bounty.brelsfordsoftware.com.
  name: brelsfordsoftware-com MCP Server
  slug: brelsfordsoftware-com-mcp-yml
modified: '2026-10-29'
name: brelsfordsoftware-com
nav: Providers
network: true
overview: 'brelsfordsoftware-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Infrastructure, Immunogenetics, Games, Directory, and Open Data.


  brelsfordsoftware-com''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 13 more developer resources.'
random_paper: 18
scopes:
- name: Brelsfordsoftware Com Scopes
  scope_count: 0
  slug: brelsfordsoftware-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 66.7
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 28.2
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/brelsfordsoftware-com/brelsfordsoftware-com-2026-11-03T122544.png
security:
- kind: authentication
  name: Brelsfordsoftware Com Authentication
  slug: brelsfordsoftware-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Brelsfordsoftware Com Domain Security
  slug: brelsfordsoftware-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: brelsfordsoftware-com
tags:
- Infrastructure
- Immunogenetics
- Games
- Directory
- Open Data
website: https://brelsfordsoftware.com/
---
