---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/domainkits-com/plans/domainkits-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/domainkits-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/domainkits-com/llms/domainkits-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/domainkits-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/domainkits-com/mcp/domainkits-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/domainkits-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/domainkits-com/well-known/domainkits-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/domainkits-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/domainkits-com/hosts/domainkits-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/domainkits-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/domainkits-com/vendors/domainkits-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/domainkits-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://domainkits.com/login
- group: auth
  href: https://artifacts.apis.io/domainkits-com/security/domainkits-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/domainkits-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://domainkits.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://domainkits.com/dev
- group: docs
  title: ''
  type: Documentation
  url: https://domainkits.com/dev/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://domainkits.com/dev/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://domainkits.com/dev
- group: commercial
  title: ''
  type: Pricing
  url: https://domainkits.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://domainkits.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://domainkits.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://domainkits.com/blog
created: '2026-11-05'
description: DomainKits provides a comprehensive domain lifecycle search platform, allowing users to search, filter, and analyze over 370 million domains across more than 1,200 extensions. It offers data on available, newly registered, active, expiring, and deleted domains, along with WHOIS and DNS lookup capabilities via its REST API and CLI tools. The service targets domain investors, marketers, and developers needing bulk domain intelligence and trend analysis.
image: https://domainkits.com/assets/images/domainkits-social-card.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.domainkits.com.
  name: DomainKits MCP Server
  slug: domainkits-com-mcp-yml
modified: '2026-11-05'
name: DomainKits
nav: Providers
network: true
overview: 'DomainKits is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Domain, Search, Data, Investment, and Marketing.


  DomainKits'' developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Domainkits Com Plans Pricing
  plan_count: 5
  slug: domainkits-com-plans-pricing
random_paper: 23
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Domainkits Com Domain Security
  slug: domainkits-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: domainkits-com
tags:
- Domain
- Search
- Data
- Investment
- Marketing
website: https://domainkits.com/
---
