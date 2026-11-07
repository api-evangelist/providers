---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: EasyGerber provides a manufacturing API accessed via MCP endpoint, but no public OpenAPI or other machine‑readable contract is available.
  name: EasyGerber API
  slug: easygerber-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/easygerber-com/plans/easygerber-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/easygerber-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/easygerber-com/mcp/easygerber-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/easygerber-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/easygerber-com/well-known/easygerber-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/easygerber-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/easygerber-com/hosts/easygerber-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/easygerber-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/easygerber-com/vendors/easygerber-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/easygerber-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.easygerber.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.easygerber.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.easygerber.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.easygerber.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EasyGerber
- group: auth
  href: https://artifacts.apis.io/easygerber-com/security/easygerber-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/easygerber-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://easygerber.com/
coverage:
  checked: '2026-11-06'
  detail: Pricing page https://www.easygerber.com/pricing returns HTML but no OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts are published.
  evidence:
  - status: 200
    url: https://www.easygerber.com/pricing
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: 'easygerber-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
layout: provider
mcp_servers:
- description: Remote MCP server at www.easygerber.com.
  name: EasyGerber MCP Server
  slug: easygerber-com-mcp-yml
modified: '2026-11-06'
name: EasyGerber
nav: Providers
network: true
overview: 'EasyGerber is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include PCB Design, AI Design, Parts Library, and Manufacturing files.


  EasyGerber''s developer surface includes pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Easygerber Com Plans Pricing
  plan_count: 2
  slug: easygerber-com-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 28.0
    catalog_earned_first_party: 8.0
    catalog_gap: 87.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 36.7
    operational_transparency: 5.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Easygerber Com Domain Security
  slug: easygerber-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: easygerber-com
tags:
- PCB Design
- AI Design
- Parts Library
- Manufacturing files
website: https://easygerber.com/
---
