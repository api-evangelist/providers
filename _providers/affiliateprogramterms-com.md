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
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/affiliateprogramterms-com/llms/affiliateprogramterms-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/affiliateprogramterms-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/affiliateprogramterms-com/mcp/affiliateprogramterms-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/affiliateprogramterms-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/affiliateprogramterms-com/hosts/affiliateprogramterms-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/affiliateprogramterms-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/affiliateprogramterms-com/vendors/affiliateprogramterms-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/affiliateprogramterms-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://affiliateprogramterms.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://affiliateprogramterms.com/programs/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://affiliateprogramterms.com/privacy/
- group: company
  title: ''
  type: Blog
  url: https://affiliateprogramterms.com/blog/
- group: auth
  href: https://artifacts.apis.io/affiliateprogramterms-com/security/affiliateprogramterms-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/affiliateprogramterms-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://affiliateprogramterms.com/
coverage:
  checked: '2026-10-31'
  detail: The provider only offers an MCP JSON‑RPC endpoint at /mcp, which returns 405 to GET and requires POST, so no OpenAPI/AsyncAPI/GraphQL spec is publicly available.
  evidence:
  - status: 405
    url: https://affiliateprogramterms.com/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Affiliate Program Terms aggregates commission rates, cookie windows, payout minimums and network details for over 494 affiliate programs, sourcing each figure directly from vendor pages and dating them. The service provides free, downloadable CSV and PDF datasets, enabling marketers and affiliates to compare program terms accurately and transparently.
image: https://affiliateprogramterms.com/og.3afae275d8.png
layout: provider
mcp_servers:
- description: Remote MCP server at affiliateprogramterms.com.
  name: Affiliate Program Terms MCP Server
  slug: affiliateprogramterms-com-mcp-yml
modified: '2026-10-31'
name: Affiliate Program Terms
nav: Providers
network: true
overview: 'Affiliate Program Terms is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Affiliates, Data, Marketing, Software-as-a-Service, and Affiliate Programs.


  Affiliate Program Terms'' developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 10.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Affiliateprogramterms Com Domain Security
  slug: affiliateprogramterms-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: affiliateprogramterms-com
tags:
- Affiliates
- Data
- Marketing
- Software-as-a-Service
- Affiliate Programs
website: https://affiliateprogramterms.com/
---
