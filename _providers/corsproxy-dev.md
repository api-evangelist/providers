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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Corsproxy Dev Agentic Access
  operation_count: 6
  slug: corsproxy-dev-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.corsproxy.dev
  baseurl_source: declared
  description: The health API from corsproxy-dev — 1 operation(s) for health.
  name: corsproxy-dev Health API
  slug: corsproxy-dev-health-api
- baseURL: https://api.corsproxy.dev
  baseurl_source: declared
  description: Remote MCP server for AI assistants and agents.
  name: corsproxy-dev MCP API
  slug: corsproxy-dev-mcp-api
- baseURL: https://api.corsproxy.dev
  baseurl_source: declared
  description: The Proxy API from corsproxy-dev — 2 operation(s) for proxy.
  name: corsproxy-dev Proxy API
  slug: corsproxy-dev-proxy-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/corsproxy-dev/agentic-access/corsproxy-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/corsproxy-dev-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/corsproxy-dev/rate-limits/corsproxy-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/corsproxy-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/corsproxy-dev/plans/corsproxy-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/corsproxy-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/corsproxy-dev/rules/corsproxy-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/corsproxy-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/corsproxy-dev/vocabulary/corsproxy-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/corsproxy-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/corsproxy-dev/conventions/corsproxy-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/corsproxy-dev-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://corsproxy.dev/blog/cors-proxy-security
- group: auth
  href: https://artifacts.apis.io/corsproxy-dev/authentication/corsproxy-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/corsproxy-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/corsproxy-dev/lifecycle/corsproxy-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/corsproxy-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/corsproxy-dev/errors/corsproxy-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/corsproxy-dev-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/corsproxy-dev/llms/corsproxy-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/corsproxy-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/corsproxy-dev/mcp/corsproxy-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/corsproxy-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/corsproxy-dev/well-known/corsproxy-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/corsproxy-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/corsproxy-dev/well-known/corsproxy-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/corsproxy-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/corsproxy-dev/hosts/corsproxy-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/corsproxy-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/corsproxy-dev/vendors/corsproxy-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/corsproxy-dev-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.corsproxy.dev`
- group: auth
  href: https://artifacts.apis.io/corsproxy-dev/security/corsproxy-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/corsproxy-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/corsproxy-dev/security/corsproxy-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/corsproxy-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://corsproxy.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://corsproxy.dev/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://corsproxy.dev/openapi.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://corsproxy.dev/docs/
- group: company
  title: ''
  type: Blog
  url: https://corsproxy.dev/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/melihbirim
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corsproxy.dev/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corsproxy.dev/legal/privacy/
- group: operate
  title: ''
  type: Support
  url: https://corsproxy.dev/about/
- group: start
  title: ''
  type: SignUp
  url: https://app.corsproxy.dev/auth/login
- group: build
  title: ''
  type: Postman
  url: https://corsproxy.dev/corsproxy.postman_collection.json
- group: commercial
  title: ''
  type: Pricing
  url: https://corsproxy.dev/compare/
- group: operate
  title: ''
  type: StatusPage
  url: https://corsproxy.dev/status/
created: '2026-10-30'
description: corsproxy.dev provides a managed CORS relay service that enables browsers to call third‑party APIs without building their own proxy infrastructure. It offers API keys, rate limits, request logs, a dashboard, and an open‑source self‑hosted relay. Free tier gives 500 requests per day, with paid plans for higher volume and enterprise features. The service includes documentation, status page, blog, and open source code on GitHub.
image: https://corsproxy.dev/logo-mark.svg
layout: provider
mcp_servers:
- description: Remote MCP server at api.corsproxy.dev requiring an API key.
  name: corsproxy-dev MCP Server
  slug: corsproxy-dev-mcp-yml
modified: '2026-10-30'
name: corsproxy-dev
nav: Providers
network: true
overview: 'corsproxy-dev publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Health API, MCP API, and Proxy API. Tagged areas include Company, CORS, Proxy, Developer Tools, and Open Source.


  The corsproxy-dev catalog on APIs.io includes 1 Spectral governance ruleset.


  corsproxy-dev''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, signup flow, and 25 more developer resources.'
plans:
- name: Corsproxy Dev Plans Pricing
  plan_count: 1
  slug: corsproxy-dev-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Corsproxy Dev Rate Limits
  slug: corsproxy-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: corsproxy-dev API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 1
  slug: corsproxy-dev-rules
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 58.8
    catalog_earned_first_party: 16.0
    catalog_gap: 56.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.2
  facets:
    access_clarity: 43.4
    contract_governance: 17.4
    contract_quality: 48.0
    developer_ergonomics: 36.9
    discoverability: 65.0
    operational_transparency: 36.8
  previous_composite: 55.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/corsproxy-dev/corsproxy-dev-2026-11-03T125358.png
security:
- kind: authentication
  name: Corsproxy Dev Authentication
  slug: corsproxy-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Corsproxy Dev Domain Security
  slug: corsproxy-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Corsproxy Dev Vulnerability Disclosure
  slug: corsproxy-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: corsproxy-dev
tags:
- Company
- CORS
- Proxy
- Developer Tools
- Open Source
website: https://corsproxy.dev/
---
