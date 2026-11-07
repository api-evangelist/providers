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
    auth_clarity: bearer
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.agentdomains.co
  baseurl_source: declared
  description: 'AgentDomains API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AgentDomains API
  slug: agentdomains-co-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/agentdomains-co/plans/agentdomains-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentdomains-co-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentdomains-co/rules/agentdomains-co-rules.yml
  title: ''
  type: Spectral
  url: rules/agentdomains-co-rules.yml
- group: design
  href: https://artifacts.apis.io/agentdomains-co/json-ld/agentdomains-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentdomains-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentdomains-co/vocabulary/agentdomains-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentdomains-co-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentdomains-co/data-model/agentdomains-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentdomains-co-data-model.yml
- group: build
  href: https://artifacts.apis.io/agentdomains-co/cli/agentdomains-co-cli.yml
  title: ''
  type: CLI
  url: cli/agentdomains-co-cli.yml
- group: design
  href: https://artifacts.apis.io/agentdomains-co/conformance/agentdomains-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentdomains-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentdomains-co/llms/agentdomains-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentdomains-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentdomains-co/mcp/agentdomains-co-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentdomains-co-mcp.yml
- group: other
  href: https://artifacts.apis.io/agentdomains-co/hosts/agentdomains-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentdomains-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentdomains-co/vendors/agentdomains-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentdomains-co-vendors.yml
- group: build
  href: https://artifacts.apis.io/agentdomains-co/packages/agentdomains-co-packages.yml
  title: ''
  type: SDKs
  url: packages/agentdomains-co-packages.yml
- group: build
  href: https://artifacts.apis.io/agentdomains-co/packages/agentdomains-co-packages.yml
  title: ''
  type: Packages
  url: packages/agentdomains-co-packages.yml
- group: auth
  href: https://artifacts.apis.io/agentdomains-co/security/agentdomains-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentdomains-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentdomains.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agentdomains.co/
- group: commercial
  title: ''
  type: Pricing
  url: https://agentdomains.co/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.agentdomains.co/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agentdomains.co/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.agentdomains.co/api
created: '2026-10-31'
description: AgentDomains provides free subdomains under makes.fyi and agentdomains.co for AI agents and developers. Through a simple CLI or HTTP API, agents can claim, manage DNS records, set up forwarding, reverse proxy, and obtain SSL certificates automatically. The service is designed for automated workflows, offering 19 MCP tools and a fully documented HTTP API, enabling seamless integration into CI/CD pipelines and AI-driven site deployments.
image: https://agentdomains.co/og.png
json_schemas:
- name: PostRequest
  property_count: 4
  slug: agentdomains-co-post-request
- name: PostV1SubdomainsRequest
  property_count: 4
  slug: agentdomains-co-post-v1-subdomains-request
jsonld:
- class_count: 2
  name: Agentdomains Co Context
  property_count: 8
  slug: agentdomains-co-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.agentdomains.co.
  name: AgentDomains MCP Server
  slug: agentdomains-co-mcp-yml
modified: '2026-10-31'
name: AgentDomains
nav: Providers
network: true
overview: 'AgentDomains is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Domains, CLI, MCP, and DNS.


  The AgentDomains catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AgentDomains'' developer surface includes CLI, documentation, pricing, getting-started guide, API reference, and 15 more developer resources.'
plans:
- name: Agentdomains Co Plans Pricing
  plan_count: 2
  slug: agentdomains-co-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: AgentDomains API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: agentdomains-co-rules
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 64.8
    catalog_earned_first_party: 8.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 26.3
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 33.3
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 30.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentdomains Co Domain Security
  slug: agentdomains-co-domain-security
  summary_line: TLSv1.3
slug: agentdomains-co
tags:
- Artificial Intelligence
- Domains
- CLI
- MCP
- DNS
website: https://agentdomains.co/
---
