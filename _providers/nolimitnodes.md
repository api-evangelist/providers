---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nolimitnodes Agentic Access
  operation_count: 1
  slug: nolimitnodes-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Provides private Solana RPC nodes, gRPC streams, Shredstream, and Geyser plugin hosting for high‑frequency traders and indexers.
  name: Solana RPC API
  slug: solana-rpc-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/nolimitnodes/agentic-access/nolimitnodes-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nolimitnodes-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/nolimitnodes/plans/nolimitnodes-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nolimitnodes-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/nolimitnodes/rules/nolimitnodes-rules.yml
  title: ''
  type: Spectral
  url: rules/nolimitnodes-rules.yml
- group: agent
  href: https://artifacts.apis.io/nolimitnodes/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/nolimitnodes/changelog/nolimitnodes-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/nolimitnodes-changelog.yml
- group: auth
  href: https://artifacts.apis.io/nolimitnodes/security/nolimitnodes-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/nolimitnodes-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/nolimitnodes/authentication/nolimitnodes-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nolimitnodes-authentication.yml
- group: design
  href: https://artifacts.apis.io/nolimitnodes/conformance/nolimitnodes-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nolimitnodes-conformance.yml
- group: agent
  href: https://artifacts.apis.io/nolimitnodes/llms/nolimitnodes-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nolimitnodes-llms.txt
- group: agent
  href: https://artifacts.apis.io/nolimitnodes/mcp/nolimitnodes-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/nolimitnodes-mcp.yml
- group: auth
  href: https://artifacts.apis.io/nolimitnodes/well-known/nolimitnodes-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nolimitnodes-security.txt
- group: agent
  href: https://artifacts.apis.io/nolimitnodes/well-known/nolimitnodes-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nolimitnodes-well-known.yml
- group: other
  href: https://artifacts.apis.io/nolimitnodes/hosts/nolimitnodes-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nolimitnodes-hosts.yml
- group: other
  href: https://artifacts.apis.io/nolimitnodes/vendors/nolimitnodes-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nolimitnodes-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nolimitnodes.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://nolimitnodes.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nolimitnodes.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://nolimitnodes.com/docs/changelog
- group: auth
  href: https://artifacts.apis.io/nolimitnodes/security/nolimitnodes-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/nolimitnodes-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/nolimitnodes/security/nolimitnodes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nolimitnodes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nolimitnodes.com/
- group: docs
  title: ''
  type: Documentation
  url: https://nolimitnodes.com/docs/api-reference/general/overview
- group: docs
  title: ''
  type: APIReference
  url: https://nolimitnodes.com/docs/api-reference/general/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://nolimitnodes.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://nolimitnodes.com/support
- group: company
  title: ''
  type: Blog
  url: https://nolimitnodes.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://nolimitnodes.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://nolimitnodes.com/talk-to-sales
coverage:
  checked: '2026-10-08'
  detail: OpenAPI spec endpoint requires an API key, returning 401 Unauthorized.
  evidence:
  - status: 401
    url: https://rpc.mainnet.solana.nolimitnodes.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-08'
description: NoLimitNodes provides private Solana RPC nodes, Yellowstone gRPC streams, Shredstream, and Geyser plugin hosting, along with a comprehensive catalog of pre‑parsed on‑chain events. Targeted at high‑frequency traders, MEV searchers, and indexers, the service offers schema‑stable data without the need for custom parsers, guaranteeing uptime and flat‑rate pricing. The platform includes extensive documentation, pricing details, a blog, and support channels, enabling developers to integrate Solana infrastructure quickly and reliably.
finops:
- has_sources: true
  method: derived
  name: Nolimitnodes Finops
  primary_unit: subscription
  service_category: ''
  slug: nolimitnodes-finops
  template: false
layout: provider
mcp_servers:
- description: Remote MCP server at nolimitnodes.com.
  name: NoLimitNodes MCP Server
  slug: nolimitnodes-mcp-yml
modified: '2026-10-08'
name: NoLimitNodes
nav: Providers
network: true
overview: 'NoLimitNodes is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Solana, RPC, Data Streams, and MEV.


  The NoLimitNodes catalog on APIs.io includes 1 Spectral governance ruleset.


  NoLimitNodes'' developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 21 more developer resources.'
plans:
- name: Nolimitnodes Plans Pricing
  plan_count: 3
  slug: nolimitnodes-plans-pricing
- name: Nolimitnodes Price Estimates
  plan_count: 0
  slug: nolimitnodes-price-estimates
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: NoLimitNodes API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: nolimitnodes-rules
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 49.5
    catalog_earned_first_party: 12.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 49.4
    discoverability: 53.3
    operational_transparency: 42.1
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Nolimitnodes Authentication
  slug: nolimitnodes-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Nolimitnodes Domain Security
  slug: nolimitnodes-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Nolimitnodes Vulnerability Disclosure
  slug: nolimitnodes-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: health-check
  slug: nolimitnodes-health
slug: nolimitnodes
tags:
- Company
- Solana
- RPC
- Data Streams
- MEV
- Infrastructure
website: https://nolimitnodes.com/
---
