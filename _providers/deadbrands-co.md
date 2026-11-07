---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
- description: Dead Brands provides ERP consulting APIs for SAP Business One and Odoo.
  name: Dead Brands API
  slug: dead-brands-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/deadbrands-co/security/deadbrands-co-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/deadbrands-co-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/deadbrands-co/llms/deadbrands-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deadbrands-co-llms.txt
- group: build
  href: https://artifacts.apis.io/deadbrands-co/mcp/deadbrands-co-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/deadbrands-co-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/deadbrands-co/mcp/deadbrands-co-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/deadbrands-co-mcp.yml
- group: auth
  href: https://artifacts.apis.io/deadbrands-co/well-known/deadbrands-co-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deadbrands-co-security.txt
- group: agent
  href: https://artifacts.apis.io/deadbrands-co/well-known/deadbrands-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deadbrands-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/deadbrands-co/hosts/deadbrands-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deadbrands-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/deadbrands-co/vendors/deadbrands-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deadbrands-co-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://deadbrands.co/blog/tag/trust/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deadbrands.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deadbrands.co/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://deadbrands.co/news/
- group: other
  title: ''
  type: Leadership
  url: https://deadbrands.co/team/
- group: company
  title: ''
  type: Blog
  url: https://deadbrands.co/blog/
- group: auth
  href: https://artifacts.apis.io/deadbrands-co/security/deadbrands-co-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/deadbrands-co-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/deadbrands-co/security/deadbrands-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deadbrands-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deadbrands.co/
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's hosts.
  evidence:
  - status: 200
    url: https://deadbrands.co/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Dead Brands, LLC revives dead brands and offers ERP consulting for small businesses, specializing in SAP Business One and Odoo solutions. They provide AI and automation services, and host the Shark Bite Biz podcast, delivering real talk and results for entrepreneurs seeking growth and technology integration.
image: https://deadbrands.co/assets/img/dead-brands-logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.deadbrands.co.
  name: Dead Brands, LLC MCP Server
  slug: deadbrands-co-mcp-yml
modified: '2026-11-05'
name: Dead Brands, LLC
nav: Providers
network: true
overview: 'Dead Brands, LLC is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include BrandRevival, ERPConsulting, AI Automation, Podcasts, and Small Business.


  Dead Brands, LLC''s developer surface includes engineering blog and 16 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 60.0
    operational_transparency: 10.5
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deadbrands Co Domain Security
  slug: deadbrands-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deadbrands Co Vulnerability Disclosure
  slug: deadbrands-co-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: deadbrands-co
tags:
- BrandRevival
- ERPConsulting
- AI Automation
- Podcasts
- Small Business
website: https://deadbrands.co/
---
