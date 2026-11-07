---
access_model:
  confidence: low
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: true
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
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/aisotools-com/plans/aisotools-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aisotools-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aisotools-com/llms/aisotools-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aisotools-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/aisotools-com/mcp/aisotools-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aisotools-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/aisotools-com/hosts/aisotools-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aisotools-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aisotools-com/vendors/aisotools-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aisotools-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://aisotools.com/category/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aisotools.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://aisotools.com/blog
- group: auth
  href: https://artifacts.apis.io/aisotools-com/security/aisotools-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aisotools-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aisotools.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://aisotools.com/pricing
- group: company
  title: ''
  type: About
  url: https://aisotools.com/about
coverage:
  checked: '2026-11-01'
  detail: The provider's site offers documentation but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts are publicly available.
  evidence:
  - status: 200
    url: https://aisotools.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AISO Tools is a curated directory of AI tools across 27 categories, helping users discover, compare, and evaluate the best AI solutions for tasks ranging from writing and coding to image generation and analytics. The platform offers free audits, pricing information, and a marketplace for tool providers, aiming to streamline AI tool selection for individuals and businesses.
layout: provider
mcp_servers:
- description: Remote MCP server at aisotools.com.
  name: AISO Tools MCP Server
  slug: aisotools-com-mcp-yml
modified: '2026-11-01'
name: AISO Tools
nav: Providers
network: true
overview: 'AISO Tools is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Tools, Directory, Marketplace, Comparison, and Free.


  AISO Tools'' developer surface includes engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Aisotools Com Plans Pricing
  plan_count: 6
  slug: aisotools-com-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 45.0
    operational_transparency: 5.3
  previous_composite: 16.1
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aisotools Com Domain Security
  slug: aisotools-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aisotools-com
tags:
- AI Tools
- Directory
- Marketplace
- Comparison
- Free
website: https://aisotools.com/
---
