---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Marketing intelligence and creative production API
  name: StackEnhance API
  slug: stackenhance-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/stackenhance-com/plans/stackenhance-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stackenhance-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/stackenhance-com/security/stackenhance-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/stackenhance-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/stackenhance-com/llms/stackenhance-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stackenhance-com-llms.txt
- group: build
  href: https://artifacts.apis.io/stackenhance-com/mcp/stackenhance-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/stackenhance-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/stackenhance-com/mcp/stackenhance-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/stackenhance-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/stackenhance-com/well-known/stackenhance-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stackenhance-com-security.txt
- group: agent
  href: https://artifacts.apis.io/stackenhance-com/well-known/stackenhance-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stackenhance-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/stackenhance-com/hosts/stackenhance-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stackenhance-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/stackenhance-com/vendors/stackenhance-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stackenhance-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stackenhance
- group: auth
  href: https://artifacts.apis.io/stackenhance-com/security/stackenhance-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/stackenhance-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/stackenhance-com/security/stackenhance-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stackenhance-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stackenhance.com/
- group: docs
  title: ''
  type: Documentation
  url: https://stackenhance.com/help
- group: operate
  title: ''
  type: Support
  url: https://stackenhance.com/help
- group: company
  title: ''
  type: Blog
  url: https://stackenhance.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://stackenhance.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stackenhance.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stackenhance.com/privacy
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec found on the provider's hosts.
  evidence:
  - status: 200
    url: https://stackenhance.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: StackEnhance provides a marketing intelligence platform that captures competitors' email campaigns and scores them using AI (Signal), and a creative production tool that enriches product feeds and generates on‑brand ads across channels (Studio). The service offers free access to a limited number of competitors, early‑access pricing for Studio, and a unified login for both products. It targets marketers, product teams, and advertisers seeking data‑driven insights and automated ad creation.
image: https://stackenhance.com/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at stackenhance.com.
  name: stackenhance-com MCP Server
  slug: stackenhance-com-mcp-yml
modified: '2026-10-30'
name: stackenhance-com
nav: Providers
network: true
overview: 'stackenhance-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, AI, Competitive-Intelligence, and Advertising.


  stackenhance-com''s developer surface includes documentation, support, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Stackenhance Com Plans Pricing
  plan_count: 4
  slug: stackenhance-com-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 56.7
    operational_transparency: 15.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Stackenhance Com Domain Security
  slug: stackenhance-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Stackenhance Com Vulnerability Disclosure
  slug: stackenhance-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: stackenhance-com
tags:
- Company
- Marketing
- AI
- Competitive-Intelligence
- Advertising
- SaaS
website: https://stackenhance.com/
---
