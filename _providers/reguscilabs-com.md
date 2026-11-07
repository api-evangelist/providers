---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Reguscilabs Com Agentic Access
  operation_count: 1
  slug: reguscilabs-com-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 2
apis:
- baseURL: https://www.reguscilabs.com
  baseurl_source: declared
  description: The Agent tools API from reguscilabs-com — 1 operation(s) for agent tools.
  name: reguscilabs-com Agent tools API
  slug: reguscilabs-com-agent-tools-api
- baseURL: https://www.reguscilabs.com
  baseurl_source: declared
  description: The Sandbox API from reguscilabs-com — 2 operation(s) for sandbox.
  name: reguscilabs-com Sandbox API
  slug: reguscilabs-com-sandbox-api
artifact_total: 17
common:
- group: design
  href: https://artifacts.apis.io/reguscilabs-com/data-model/reguscilabs-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/reguscilabs-com-data-model.yml
- group: agent
  href: https://artifacts.apis.io/reguscilabs-com/agentic-access/reguscilabs-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/reguscilabs-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/reguscilabs-com/rate-limits/reguscilabs-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/reguscilabs-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/reguscilabs-com/rules/reguscilabs-com-rules.yml
  title: ''
  type: Spectral
  url: rules/reguscilabs-com-rules.yml
- group: design
  href: https://artifacts.apis.io/reguscilabs-com/vocabulary/reguscilabs-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/reguscilabs-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/reguscilabs-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/reguscilabs-com/cli/reguscilabs-com-cli.yml
  title: ''
  type: CLI
  url: cli/reguscilabs-com-cli.yml
- group: design
  href: https://artifacts.apis.io/reguscilabs-com/conventions/reguscilabs-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/reguscilabs-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/reguscilabs-com/conventions/reguscilabs-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/reguscilabs-com-conventions.yml
- group: operate
  href: https://artifacts.apis.io/reguscilabs-com/lifecycle/reguscilabs-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/reguscilabs-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/reguscilabs-com/lifecycle/reguscilabs-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/reguscilabs-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/reguscilabs-com/errors/reguscilabs-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/reguscilabs-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/reguscilabs-com/conformance/reguscilabs-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/reguscilabs-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/reguscilabs-com/llms/reguscilabs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/reguscilabs-com-llms.txt
- group: build
  href: https://artifacts.apis.io/reguscilabs-com/mcp/reguscilabs-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/reguscilabs-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/reguscilabs-com/mcp/reguscilabs-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/reguscilabs-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/reguscilabs-com/well-known/reguscilabs-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/reguscilabs-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/reguscilabs-com/hosts/reguscilabs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/reguscilabs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/reguscilabs-com/vendors/reguscilabs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/reguscilabs-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/reguscilabs-com/packages/reguscilabs-com-packages.yml
  title: ''
  type: SDKs
  url: packages/reguscilabs-com-packages.yml
- group: build
  href: https://artifacts.apis.io/reguscilabs-com/packages/reguscilabs-com-packages.yml
  title: ''
  type: Packages
  url: packages/reguscilabs-com-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://www.reguscilabs.com/sandbox
- group: auth
  href: https://artifacts.apis.io/reguscilabs-com/security/reguscilabs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reguscilabs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://reguscilabs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.reguscilabs.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.reguscilabs.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.reguscilabs.com/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://www.reguscilabs.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.reguscilabs.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reguscilabs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reguscilabs.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reguscilabs.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reguscilabs.com/terms
created: '2026-10-30'
description: RegusciLabs is an innovation lab in Montevideo, Uruguay, turning difficult ideas in AI, software, hardware, and strategy into real‑world proof‑of‑concepts, offering consulting, prototyping, and training services.
image: https://reguscilabs.com/og-story-v2.png
jsonld:
- class_count: 1
  name: Reguscilabs Com Context
  property_count: 11
  slug: reguscilabs-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.reguscilabs.com.
  name: reguscilabs-com MCP Server
  slug: reguscilabs-com-mcp-yml
modified: '2026-10-30'
name: reguscilabs-com
nav: Providers
network: true
overview: 'reguscilabs-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Agent tools API and Sandbox API. Tagged areas include Innovation, Artificial Intelligence, Software, Hardware, and Uruguay.


  The reguscilabs-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  reguscilabs-com''s developer surface includes CLI, sandbox, documentation, API reference, support, engineering blog, pricing, and 26 more developer resources.'
plans:
- name: Reguscilabs Com Plans Pricing
  plan_count: 0
  slug: reguscilabs-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Reguscilabs Com Rate Limits
  slug: reguscilabs-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: reguscilabs-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: reguscilabs-com-rules
scopes:
- name: Reguscilabs Com Scopes
  scope_count: 0
  slug: reguscilabs-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 32
    catalog_earned: 58.8
    catalog_earned_first_party: 8.0
    catalog_gap: 56.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 15.8
    contract_governance: 35.6
    contract_quality: 50.1
    developer_ergonomics: 41.0
    discoverability: 75.0
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - uruguay
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
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
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/reguscilabs-com/reguscilabs-com-2026-11-03T142128.png
security:
- kind: authentication
  name: Reguscilabs Com Authentication
  slug: reguscilabs-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Reguscilabs Com Domain Security
  slug: reguscilabs-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 6
skills:
- name: get-latest-activity
  slug: reguscilabs-com-get_latest_activity
- name: get-latest-news
  slug: reguscilabs-com-get_latest_news
- name: read-information
  slug: reguscilabs-com-read_information
- name: search-information
  slug: reguscilabs-com-search_information
- name: submit-inquiry
  slug: reguscilabs-com-submit_inquiry
- name: subscribe-pulse
  slug: reguscilabs-com-subscribe_pulse
slug: reguscilabs-com
tags:
- Innovation
- Artificial Intelligence
- Software
- Hardware
- Uruguay
- Company
website: https://reguscilabs.com/
---
