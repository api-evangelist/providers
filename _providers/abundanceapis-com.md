---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Abundanceapis Com Agentic Access
  operation_count: 9
  slug: abundanceapis-com-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 1
apis:
- description: The CORS Proxy API from abundanceapis-com — 1 operation(s) for cors proxy.
  name: abundanceapis-com CORS Proxy API
  slug: abundanceapis-com-cors-proxy-api
- description: Health and meta endpoints.
  name: abundanceapis-com System API
  slug: abundanceapis-com-system-api
- description: The Tools API from abundanceapis-com — 6 operation(s) for tools.
  name: abundanceapis-com Tools API
  slug: abundanceapis-com-tools-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/abundanceapis-com/agentic-access/abundanceapis-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/abundanceapis-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/abundanceapis-com/rate-limits/abundanceapis-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/abundanceapis-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/abundanceapis-com/plans/abundanceapis-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/abundanceapis-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/abundanceapis-com/rules/abundanceapis-com-rules.yml
  title: ''
  type: Spectral
  url: rules/abundanceapis-com-rules.yml
- group: design
  href: https://artifacts.apis.io/abundanceapis-com/vocabulary/abundanceapis-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/abundanceapis-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/abundanceapis-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/abundanceapis-com/conformance/abundanceapis-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/abundanceapis-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/abundanceapis-com/llms/abundanceapis-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/abundanceapis-com-llms.txt
- group: build
  href: https://artifacts.apis.io/abundanceapis-com/mcp/abundanceapis-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/abundanceapis-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/abundanceapis-com/mcp/abundanceapis-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/abundanceapis-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/abundanceapis-com/hosts/abundanceapis-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/abundanceapis-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/abundanceapis-com/vendors/abundanceapis-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/abundanceapis-com-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://abundanceapis.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/abundanceapis-com/security/abundanceapis-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/abundanceapis-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://abundanceapis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://abundanceapis.com/guides
- group: operate
  title: ''
  type: Support
  url: https://abundanceapis.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://abundanceapis.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://abundanceapis.com/terms
- group: start
  title: ''
  type: GettingStarted
  url: https://abundanceapis.com/guides
created: '2026-10-30'
description: Abundance APIs offers a catalog of over 25 developer APIs covering web utilities, data validation, geolocation, finance math, text analysis, privacy tooling, and more. Each API runs on a hardened, stateless backend with typical latency under 100 ms. Design principles include no third‑party data resale, no scraping, and no per‑call upstream fees, keeping prices low. Billing and API keys are managed via RapidAPI, with free tiers of 1,000 requests per month and paid plans starting at $5/month. Uptime is monitored every 15 minutes with automated alerts.
image: https://abundanceapis.com/icon.png
layout: provider
mcp_servers:
- description: Remote MCP server at abundanceapis.com.
  name: abundanceapis-com MCP Server
  slug: abundanceapis-com-mcp-yml
modified: '2026-10-30'
name: abundanceapis-com
nav: Providers
network: true
overview: 'abundanceapis-com publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: CORS Proxy API, System API, and Tools API. Tagged areas include Developer Tools, Data Validation, Geolocation, Finance, and Utilities.


  The abundanceapis-com catalog on APIs.io includes 1 Spectral governance ruleset.


  abundanceapis-com''s developer surface includes API reference, documentation, support, getting-started guide, and 16 more developer resources.'
plans:
- name: Abundanceapis Com Plans Pricing
  plan_count: 2
  slug: abundanceapis-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Abundanceapis Com Rate Limits
  slug: abundanceapis-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 46
  extends:
  - spectral:oas
  name: abundanceapis-com API Rules
  rule_count: 5
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 1
  slug: abundanceapis-com-rules
scopes:
- name: Abundanceapis Com Scopes
  scope_count: 0
  slug: abundanceapis-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 53.8
    catalog_earned_first_party: 16.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 34.1
    developer_ergonomics: 23.1
    discoverability: 56.7
    operational_transparency: 21.1
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 26.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/abundanceapis-com/abundanceapis-com-2026-11-03T120143.png
security:
- kind: authentication
  name: Abundanceapis Com Authentication
  slug: abundanceapis-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Abundanceapis Com Domain Security
  slug: abundanceapis-com-domain-security
  summary_line: TLSv1.3
slug: abundanceapis-com
tags:
- Developer Tools
- Data Validation
- Geolocation
- Finance
- Utilities
website: https://abundanceapis.com/
---
