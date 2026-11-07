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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Realised yields and USDC settlement cost data API.
  name: 402rates API
  slug: main-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/402rates-com/rules/402rates-com-rules.yml
  title: ''
  type: Spectral
  url: rules/402rates-com-rules.yml
- group: design
  href: https://artifacts.apis.io/402rates-com/vocabulary/402rates-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/402rates-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/402rates-com/conformance/402rates-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/402rates-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/402rates-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/402rates-com/errors/402rates-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/402rates-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/402rates-com/llms/402rates-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/402rates-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/402rates-com/mcp/402rates-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/402rates-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/402rates-com/hosts/402rates-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/402rates-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/402rates-com/vendors/402rates-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/402rates-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/402rates-com/security/402rates-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/402rates-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://402rates.com/
- group: docs
  title: ''
  type: APIReference
  url: https://402rates.com/basis-spec-v1/
- group: start
  title: ''
  type: GettingStarted
  url: https://402rates.com/integration/
- group: operate
  title: ''
  type: Support
  url: https://402rates.com/access/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://402rates.com/data-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://402rates.com/
created: '2026-10-29'
description: 402rates.com provides evidence‑backed tokenized treasury yields and measured cross‑chain USDC settlement costs. The platform aggregates and presents real‑time yield data, cost analyses, and methodological documentation, allowing developers and analysts to access transparent financial metrics. By publishing observations, sources, and methods, it aims to improve transparency in treasury finance and crypto settlement ecosystems.
image: https://402rates.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.402rates.com.
  name: 402rates-com MCP Server
  slug: 402rates-com-mcp-yml
modified: '2026-10-29'
name: 402rates-com
nav: Providers
network: true
overview: '402rates-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Data, Blockchain, and Treasury.


  The 402rates-com catalog on APIs.io includes 1 Spectral governance ruleset.


  402rates-com''s developer surface includes API reference, getting-started guide, support, and 13 more developer resources.'
plans:
- name: 402Rates Com Plans Pricing
  plan_count: 0
  slug: 402rates-com-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: 402Rates Com Rate Limits
  slug: 402rates-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: 402rates-com API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: 402rates-com-rules
scopes:
- name: 402Rates Com Scopes
  scope_count: 0
  slug: 402rates-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 42.0
    catalog_earned_first_party: 0.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 10.5
    contract_governance: 19.7
    contract_quality: 0.0
    developer_ergonomics: 27.9
    discoverability: 75.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.8
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/402rates-com/402rates-com-2026-11-03T120114.png
security:
- kind: authentication
  name: 402Rates Com Authentication
  slug: 402rates-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: 402Rates Com Domain Security
  slug: 402rates-com-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: 402rates-com-rwa
  slug: 402rates-com-rwa-skill
slug: 402rates-com
tags:
- Company
- Finance
- Data
- Blockchain
- Treasury
- USDC
website: https://402rates.com/
---
