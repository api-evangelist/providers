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
  score: 0.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Assetize MCP JSON-RPC tool interface providing Maximo knowledge queries.
  name: Assetize MCP
  slug: assetize-mcp
artifact_total: 3
common:
- group: operate
  href: https://artifacts.apis.io/assetize-com-au/changelog/assetize-com-au-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/assetize-com-au-changelog.yml
- group: agent
  href: https://artifacts.apis.io/assetize-com-au/llms/assetize-com-au-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/assetize-com-au-llms.txt
- group: build
  href: https://artifacts.apis.io/assetize-com-au/mcp/assetize-com-au-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/assetize-com-au-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/assetize-com-au/mcp/assetize-com-au-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/assetize-com-au-mcp.yml
- group: other
  href: https://artifacts.apis.io/assetize-com-au/hosts/assetize-com-au-hosts.yml
  title: ''
  type: Hosts
  url: hosts/assetize-com-au-hosts.yml
- group: other
  href: https://artifacts.apis.io/assetize-com-au/vendors/assetize-com-au-vendors.yml
  title: ''
  type: Vendors
  url: vendors/assetize-com-au-vendors.yml
- group: auth
  href: https://artifacts.apis.io/assetize-com-au/security/assetize-com-au-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/assetize-com-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://assetize.com.au/
- group: company
  title: ''
  type: Blog
  url: https://assetize.com.au/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://assetize.com.au/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.assetize.com.au/maximo/login?next=%2Fmaximo%2Fui%2F
- group: docs
  title: ''
  type: Documentation
  url: https://assetize.com.au/mxh/docs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://assetize.com.au/privacy
- group: operate
  title: ''
  type: Roadmap
  url: https://assetize.com.au/roadmap
- group: start
  title: ''
  type: Sandbox
  url: https://assetize.com.au/ui/playground
- group: operate
  title: ''
  type: Support
  url: https://assetize.com.au/ui/help
created: '2026-11-01'
description: Assetize provides free tools and intelligence for IBM Maximo users, offering the MXH upgrade assessment workbench, data loading utilities, and a suite of resources to explore IBM’s roadmap, design workflows, test scripts, and assess your own system. Users can run MXH assessments on their own exports, access a knowledge base, and leverage free consulting links, all without fees or licenses.
image: https://assetize.com.au/api/og/clock/2026-11-02.png
layout: provider
mcp_servers:
- description: Remote MCP server at assetize.com.au.
  name: Assetize MCP Server
  slug: assetize-com-au-mcp-yml
modified: '2026-11-01'
name: Assetize
nav: Providers
network: true
overview: 'Assetize is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Asset Management, IBM Maximo, Upgrade Tools, Free, and Assessment.


  Assetize''s developer surface includes changelog, engineering blog, documentation, sandbox, support, and 11 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 65.0
    operational_transparency: 10.5
  previous_composite: 17.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Assetize Com Au Domain Security
  slug: assetize-com-au-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: assetize-com-au
tags:
- Asset Management
- IBM Maximo
- Upgrade Tools
- Free
- Assessment
website: https://assetize.com.au/
---
