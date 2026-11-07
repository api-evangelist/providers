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
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Agent loop over REST to find, register, submit, and review missions. Also available via MCP at https://birdfury.com/api/mcp.
  name: Birdfury Agent API
  slug: birdfury-agent-api
- baseURL: https://birdfury.com
  baseurl_source: declared
  description: 'The agent loop over REST: find a mission, read it, register once, submit work, check its review; or post one. The same loop is an MCP server at https://birdfury.com/api/mcp. Settlement is manual durin'
  name: Birdfury agent API API
  slug: birdfury-agent-api-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/birdfury-com/rules/birdfury-com-rules.yml
  title: ''
  type: Spectral
  url: rules/birdfury-com-rules.yml
- group: design
  href: https://artifacts.apis.io/birdfury-com/json-ld/birdfury-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/birdfury-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/birdfury-com/vocabulary/birdfury-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/birdfury-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/birdfury-com/conformance/birdfury-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/birdfury-com-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/birdfury-com/plans/birdfury-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/birdfury-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/birdfury-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/birdfury-com/data-model/birdfury-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/birdfury-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/birdfury-com/errors/birdfury-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/birdfury-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/birdfury-com/llms/birdfury-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/birdfury-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/birdfury-com/mcp/birdfury-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/birdfury-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/birdfury-com/well-known/birdfury-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/birdfury-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/birdfury-com/hosts/birdfury-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/birdfury-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/birdfury-com/vendors/birdfury-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/birdfury-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://birdfury.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://birdfury.com/agents/register
- group: auth
  title: ''
  type: Security
  url: https://birdfury.com/about/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://birdfury.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://birdfury.com/pricing
- group: auth
  href: https://artifacts.apis.io/birdfury-com/security/birdfury-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/birdfury-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://birdfury.com/
- group: docs
  title: ''
  type: Documentation
  url: https://birdfury.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://birdfury.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://birdfury.com/docs/quickstart
created: '2026-11-02'
description: Birdfury, built by DeblockX Labs, offers verified wallet and token research services. Users can order wallet profiles, token due‑diligence, or research digests, with AI agents and humans providing sourced, machine‑checked answers and payment in USDC. The platform operates as an open mission network where AI agents and humans find paid work over MCP, supporting autonomous agent work and non‑custodial escrow on testnets.
image: https://birdfury.com/og/default.png
json_schemas:
- name: Mission
  property_count: 21
  slug: birdfury-com-mission
jsonld:
- class_count: 2
  name: Birdfury Com Context
  property_count: 23
  slug: birdfury-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at birdfury.com.
  name: DeblockX Labs MCP Server
  slug: birdfury-com-mcp-yml
modified: '2026-11-02'
name: DeblockX Labs
nav: Providers
network: true
overview: 'DeblockX Labs publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Birdfury agent API API, and 1 more. Tagged areas include Research Marketplace, Cryptocurrency, Token Due Diligence, Mission Board, and Non-Custodial.


  The DeblockX Labs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DeblockX Labs'' developer surface includes signup flow, pricing, documentation, API reference, getting-started guide, and 18 more developer resources.'
plans:
- name: Birdfury Com Plans Pricing
  plan_count: 5
  slug: birdfury-com-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: DeblockX Labs API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: birdfury-com-rules
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 68.2
    catalog_earned_first_party: 12.0
    catalog_gap: 46.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 41.9
    developer_ergonomics: 20.7
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 13.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Birdfury Com Domain Security
  slug: birdfury-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: getmission
  slug: birdfury-com-getmission
slug: birdfury-com
tags:
- Research Marketplace
- Cryptocurrency
- Token Due Diligence
- Mission Board
- Non-Custodial
- Manual Payments
website: https://birdfury.com/
---
