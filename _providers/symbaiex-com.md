---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Symbaiex Com Agentic Access
  operation_count: 4
  slug: symbaiex-com-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 3
apis:
- description: Public discovery, Ed25519 authentication, quota, provenance reads, cited research jobs, bounded exports, and signed webhooks.
  name: Agent API
  slug: agent-api
- description: Credential-free, read-only endpoints backed only by deterministic synthetic fixtures.
  name: Sandbox API
  slug: sandbox-api
- baseURL: https://github.com/SYMBaiEX/docs
  baseurl_source: declared
  description: Complete Postman collection for the Eliza AI Framework REST API endpoints.
  name: Eliza AI Framework API
  slug: eliza-ai-framework-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/symbaiex-com/agentic-access/symbaiex-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/symbaiex-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/symbaiex-com/rate-limits/symbaiex-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/symbaiex-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/symbaiex-com/plans/symbaiex-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/symbaiex-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/symbaiex-com/rules/symbaiex-com-rules.yml
  title: ''
  type: Spectral
  url: rules/symbaiex-com-rules.yml
- group: design
  href: https://artifacts.apis.io/symbaiex-com/json-ld/symbaiex-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/symbaiex-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/symbaiex-com/vocabulary/symbaiex-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/symbaiex-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/symbaiex-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/symbaiex-com/data-model/symbaiex-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/symbaiex-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/symbaiex-com/cli/symbaiex-com-cli.yml
  title: ''
  type: CLI
  url: cli/symbaiex-com-cli.yml
- group: auth
  title: ''
  type: Security
  url: https://www.symbaiex.com/privacy
- group: auth
  href: https://artifacts.apis.io/symbaiex-com/authentication/symbaiex-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/symbaiex-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/symbaiex-com/scopes/symbaiex-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/symbaiex-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/symbaiex-com/lifecycle/symbaiex-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/symbaiex-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/symbaiex-com/errors/symbaiex-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/symbaiex-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/symbaiex-com/conformance/symbaiex-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/symbaiex-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/symbaiex-com/llms/symbaiex-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/symbaiex-com-llms.txt
- group: other
  href: https://artifacts.apis.io/symbaiex-com/a2a/symbaiex-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/symbaiex-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/symbaiex-com/mcp/symbaiex-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/symbaiex-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/symbaiex-com/well-known/symbaiex-com-symbaiex-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/symbaiex-com-symbaiex-security.txt
- group: auth
  href: https://artifacts.apis.io/symbaiex-com/well-known/symbaiex-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/symbaiex-com-security.txt
- group: auth
  href: https://artifacts.apis.io/symbaiex-com/well-known/symbaiex-com-forum-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/symbaiex-com-forum-security.txt
- group: agent
  href: https://artifacts.apis.io/symbaiex-com/well-known/symbaiex-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/symbaiex-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/symbaiex-com/hosts/symbaiex-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/symbaiex-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/symbaiex-com/vendors/symbaiex-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/symbaiex-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/symbaiex-com/packages/symbaiex-com-packages.yml
  title: ''
  type: SDKs
  url: packages/symbaiex-com-packages.yml
- group: build
  href: https://artifacts.apis.io/symbaiex-com/packages/symbaiex-com-packages.yml
  title: ''
  type: Packages
  url: packages/symbaiex-com-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.symbaiex.com/news
- group: start
  title: ''
  type: SignUp
  url: https://www.symbaiex.com/agent/signup
- group: auth
  href: https://artifacts.apis.io/symbaiex-com/security/symbaiex-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/symbaiex-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/symbaiex-com/security/symbaiex-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/symbaiex-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://symbaiex.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.symbaiex.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.symbaiex.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.symbaiex.com/api/agent
- group: start
  title: ''
  type: GettingStarted
  url: https://www.symbaiex.com/agent
- group: operate
  title: ''
  type: Support
  url: https://www.symbaiex.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.symbaiex.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.symbaiex.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.symbaiex.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.symbaiex.com/privacy
created: '2026-10-30'
description: SYMBaiEX is Austin Hamilton's public engineering and research publication platform, providing open-source software, AI system insights, agent infrastructure details, and source‑grounded research notes. It offers a public evidence API, documentation, pricing information, and community resources, all accessible without authentication, fostering transparent AI research and development.
image: https://www.symbaiex.com/opengraph-image?bc274934acf0b043
jsonld:
- class_count: 4
  name: Symbaiex Com Context
  property_count: 14
  slug: symbaiex-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.symbaiex.com.
  name: symbaiex-com MCP Server
  slug: symbaiex-com-mcp-yml
modified: '2026-10-30'
name: symbaiex-com
nav: Providers
network: true
overview: 'symbaiex-com is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Eliza AI Framework API, and 2 more. Tagged areas include Company, Artificial Intelligence, Research, OpenAPI, and Public Data.


  The symbaiex-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  symbaiex-com''s developer surface includes CLI, authentication, signup flow, documentation, API reference, getting-started guide, support, and 33 more developer resources.'
plans:
- name: Symbaiex Com Plans Pricing
  plan_count: 1
  slug: symbaiex-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Symbaiex Com Rate Limits
  slug: symbaiex-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: symbaiex-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: symbaiex-com-rules
scopes:
- name: Symbaiex Com Scopes
  scope_count: 1
  slug: symbaiex-com-scopes
  summary_line: 1 scope
score:
  band: developing
  composite: 46.9
  coverage:
    artifact_dirs: 31
    catalog_earned: 69.8
    catalog_earned_first_party: 16.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.1
  facets:
    access_clarity: 43.4
    contract_governance: 35.6
    contract_quality: 33.6
    developer_ergonomics: 55.2
    discoverability: 80.8
    operational_transparency: 26.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 57.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/symbaiex-com/symbaiex-com-2026-11-03T144221.png
security:
- kind: authentication
  name: Symbaiex Com Authentication
  slug: symbaiex-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Symbaiex Com Domain Security
  slug: symbaiex-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Symbaiex Com Vulnerability Disclosure
  slug: symbaiex-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: get-agent-api-manifest
  slug: get-agent-api-manifest
- name: request-agent-login-challenge
  slug: request-agent-login-challenge
slug: symbaiex-com
tags:
- Company
- Artificial Intelligence
- Research
- OpenAPI
- Public Data
website: https://symbaiex.com/
---
