---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Tyton MCP (Meta Conversions API) provides endpoints for free audit and setup at mcp.usetyton.com, supporting tools like begin_audit, audit_site, read_audit, record_audit_context, and record_audit.
  name: Tyton MCP API
  slug: tyton-mcp-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/usetyton-com/llms/usetyton-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usetyton-com-llms.txt
- group: build
  href: https://artifacts.apis.io/usetyton-com/mcp/usetyton-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/usetyton-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/usetyton-com/mcp/usetyton-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/usetyton-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/usetyton-com/well-known/usetyton-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/usetyton-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/usetyton-com/hosts/usetyton-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usetyton-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/usetyton-com/vendors/usetyton-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usetyton-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/usetyton-com/packages/usetyton-com-packages.yml
  title: ''
  type: SDKs
  url: packages/usetyton-com-packages.yml
- group: build
  href: https://artifacts.apis.io/usetyton-com/packages/usetyton-com-packages.yml
  title: ''
  type: Packages
  url: packages/usetyton-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/usetyton-com/security/usetyton-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usetyton-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usetyton.com/
- group: docs
  title: ''
  type: Documentation
  url: https://usetyton.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://usetyton.com/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://usetyton.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://usetyton.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usetyton.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usetyton.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://usetyton.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usetyton
coverage:
  checked: '2026-10-31'
  detail: Documentation references an API at mcp.usetyton.com but no OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found.
  evidence:
  - status: 200
    url: https://usetyton.com/docs/markdown/agents/tools
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Tyton is a Meta Pixel and Conversions API management platform that connects to AI agents to automate the setup, testing, and monitoring of Facebook tracking. It offers a free tier for one site with up to 10,000 events per month and paid plans for larger volumes, providing a dashboard, email support, and tools such as a Pixel checker. The service is operated by Kitra LLC under the brand Tyton and is hosted at usetyton.com.
image: https://usetyton.com/tyton-social-preview.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.usetyton.com requiring OAuth.
  name: usetyton-com MCP Server
  slug: usetyton-com-mcp-yml
modified: '2026-10-31'
name: usetyton-com
nav: Providers
network: true
overview: 'usetyton-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Meta Pixel, Conversions API, and Marketing.


  usetyton-com''s developer surface includes documentation, getting-started guide, pricing, signup flow, engineering blog, and 13 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 65.0
    operational_transparency: 2.6
  previous_composite: 22.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Usetyton Com Domain Security
  slug: usetyton-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: usetyton-com
tags:
- Company
- Artificial Intelligence
- Meta Pixel
- Conversions API
- Marketing
- Automation
website: https://usetyton.com/
---
