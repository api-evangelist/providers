---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 11.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Junct Dev Agentic Access
  operation_count: 4
  slug: junct-dev-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: Junct is the agent-readiness layer for web3. This API provides access to 28+ hosted MCP servers for DeFi protocols, exchanges, oracles, and data providers. Free to use, no authentication required.
  name: Junct API
  slug: junct-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/junct-dev/agentic-access/junct-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/junct-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/junct-dev/rules/junct-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/junct-dev-rules.yml
- group: agent
  href: https://artifacts.apis.io/junct-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/junct-dev/errors/junct-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/junct-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/junct-dev/conformance/junct-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/junct-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/junct-dev/llms/junct-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/junct-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/junct-dev/well-known/junct-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/junct-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/junct-dev/hosts/junct-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/junct-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/junct-dev/vendors/junct-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/junct-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/junct-dev/security/junct-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/junct-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://junct.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://junct.dev/docs
- group: docs
  title: ''
  type: Documentation
  url: https://junct.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://junct.dev/docs
- group: company
  title: ''
  type: Blog
  url: https://junct.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://junct.dev/pricing
- group: operate
  title: ''
  type: Roadmap
  url: https://junct.dev/roadmap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://junct.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://junct.dev/privacy
created: '2026-10-29'
description: Junct is an agent‑readiness platform that converts any API specification into ready‑to‑use tools for leading AI agent frameworks such as Claude, GPT, LangChain and five others. By uploading OpenAPI, contract ABI, llms.txt, or Etherscan URLs, users instantly receive generated tools—over 1,200 tools hosted across 30 MCP servers. The service simplifies integration of web APIs into AI agents, offering a one‑line configuration to turn APIs into actionable agents.
image: https://junct.dev/og.png
layout: provider
modified: '2026-10-29'
name: junct-dev
nav: Providers
network: true
overview: 'junct-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Agents, MCP, and API Tools.


  The junct-dev catalog on APIs.io includes 1 Spectral governance ruleset.


  junct-dev''s developer surface includes documentation, getting-started guide, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Junct Dev Plans Pricing
  plan_count: 0
  slug: junct-dev-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Junct Dev Rate Limits
  slug: junct-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: junct-dev API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: junct-dev-rules
scopes:
- name: Junct Dev Scopes
  scope_count: 0
  slug: junct-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 15.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.1
    discoverability: 73.2
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.2
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/junct-dev/junct-dev-2026-11-03T134244.png
security:
- kind: authentication
  name: Junct Dev Authentication
  slug: junct-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Junct Dev Domain Security
  slug: junct-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC
skill_count: 4
skills:
- name: get-llms-full-txt
  slug: junct-dev-get-llms-full-txt
- name: get-llms-txt
  slug: junct-dev-get-llms-txt
- name: get-server-details
  slug: junct-dev-get-server-details
- name: list-servers
  slug: junct-dev-list-servers
slug: junct-dev
tags:
- Company
- Artificial Intelligence
- Agents
- MCP
- API Tools
- Platform
website: https://junct.dev/
---
