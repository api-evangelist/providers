---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 13
  name: Moirailabs Com Agentic Access
  operation_count: 36
  slug: moirailabs-com-agentic-access
  summary_line: 36 operations · 13 acting · 13 human-in-the-loop
api_count: 1
apis:
- description: A2A 1.0 agent ("A2A-compatible analytics and contract intelligence agent", version 0.1.0) with 11 skills — analytics.cohorts/metrics/methods/methods_by_cohorts/transactions, reports.daily/weekly/month
  name: Moirai Agents API (A2A + MCP)
  slug: moirai-agents-api
- baseURL: https://api.moirailabs.com/api/v1
  baseurl_source: declared
  description: The analytics-controller API from Moirai Labs — 7 operation(s) for analytics-controller.
  name: Moirai Labs Analytics Controller API
  slug: moirailabs-com-analytics-controller-api
- baseURL: https://api.moirailabs.com/api/v1
  baseurl_source: declared
  description: The analytics-invocation-controller API from Moirai Labs — 4 operation(s) for analytics-invocation-controller.
  name: Moirai Labs Analytics Invocation Controller API
  slug: moirailabs-com-analytics-invocation-controller-api
- baseURL: https://api.moirailabs.com/api/v1
  baseurl_source: declared
  description: The contract-info-controller API from Moirai Labs — 6 operation(s) for contract-info-controller.
  name: Moirai Labs Contract Info Controller API
  slug: moirailabs-com-contract-info-controller-api
- baseURL: https://api.moirailabs.com/api/v1
  baseurl_source: declared
  description: The functions-controller API from Moirai Labs — 1 operation(s) for functions-controller.
  name: Moirai Labs Functions Controller API
  slug: moirailabs-com-functions-controller-api
- baseURL: https://api.moirailabs.com/api/v1
  baseurl_source: declared
  description: The plan-controller API from Moirai Labs — 3 operation(s) for plan-controller.
  name: Moirai Labs Plan Controller API
  slug: moirailabs-com-plan-controller-api
- baseURL: https://api.moirailabs.com/api/v1
  baseurl_source: declared
  description: The report-controller API from Moirai Labs — 1 operation(s) for report-controller.
  name: Moirai Labs Report Controller API
  slug: moirailabs-com-report-controller-api
- baseURL: https://api.moirailabs.com/api/v1
  baseurl_source: declared
  description: The subscription-controller API from Moirai Labs — 2 operation(s) for subscription-controller.
  name: Moirai Labs Subscription Controller API
  slug: moirailabs-com-subscription-controller-api
- baseURL: https://api.moirailabs.com/api/v1
  baseurl_source: declared
  description: The user-info-controller API from Moirai Labs — 3 operation(s) for user-info-controller.
  name: Moirai Labs User Info Controller API
  slug: moirailabs-com-user-info-controller-api
- baseURL: https://api.moirailabs.com/api/v1
  baseurl_source: declared
  description: The wallet-profiling-controller API from Moirai Labs — 4 operation(s) for wallet-profiling-controller.
  name: Moirai Labs Wallet Profiling Controller API
  slug: moirailabs-com-wallet-profiling-controller-api
artifact_total: 23
common:
- group: other
  href: https://artifacts.apis.io/moirailabs-com/capabilities/moirailabs-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/moirailabs-com-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://moirailabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://moirailabs.com/a2a
- group: commercial
  title: ''
  type: Pricing
  url: https://moirailabs.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://moirailabs.com/auth
- group: start
  title: ''
  type: Login
  url: https://moirailabs.com/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moirailabs.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moirailabs.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://moirailabs.com/blog
- group: operate
  title: ''
  type: Support
  url: https://moirailabs.featurebase.app/en/help
- group: operate
  title: ''
  type: Roadmap
  url: https://moirailabs.featurebase.app/en/roadmap
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moirailabs
- group: agent
  href: https://artifacts.apis.io/moirailabs-com/llms/moirailabs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/moirailabs-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://moirailabs.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/moirailabs-com/well-known/moirailabs-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/moirailabs-com-well-known.yml
- group: auth
  href: https://artifacts.apis.io/moirailabs-com/well-known/moirailabs-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/moirailabs-com-security.txt
- group: other
  href: https://artifacts.apis.io/moirailabs-com/a2a/moirailabs-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/moirailabs-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/moirailabs-com/mcp/moirailabs-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/moirailabs-com-mcp.yml
- group: build
  href: https://artifacts.apis.io/moirailabs-com/mcp/moirailabs-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/moirailabs-com-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/moirailabs-com/authentication/moirailabs-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/moirailabs-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/moirailabs-com/conventions/moirailabs-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/moirailabs-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/moirailabs-com/conventions/moirailabs-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/moirailabs-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/moirailabs-com/errors/moirailabs-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/moirailabs-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/moirailabs-com/lifecycle/moirailabs-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/moirailabs-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/moirailabs-com/conformance/moirailabs-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/moirailabs-com-conformance.yml
- group: operate
  href: https://artifacts.apis.io/moirailabs-com/rate-limits/moirailabs-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/moirailabs-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/moirailabs-com/plans/moirailabs-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/moirailabs-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/moirailabs-com/data-model/moirailabs-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/moirailabs-com-data-model.yml
- group: other
  href: https://artifacts.apis.io/moirailabs-com/overlays/moirailabs-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moirailabs-com-openapi-overlay.yaml
- group: build
  href: https://artifacts.apis.io/moirailabs-com/packages/moirailabs-com-packages.yml
  title: ''
  type: Packages
  url: packages/moirailabs-com-packages.yml
- group: agent
  href: https://artifacts.apis.io/moirailabs-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/moirailabs-com/agentic-access/moirailabs-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/moirailabs-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/moirailabs-com/security/moirailabs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moirailabs-com-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/moirailabs-com/security/moirailabs-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/moirailabs-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/moirailabs-com/security/moirailabs-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/moirailabs-com-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/moirailabs-com/regulatory/moirailabs-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/moirailabs-com-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://moirailabs.com/privacy
created: '2026-09-19'
description: 'Moirai Labs is a smart-contract analytics platform for Web3 teams that turns raw EVM chain data (Ethereum, Polygon, Arbitrum, Optimism, Base, Linea) into product-grade metrics: cohort retention, method-level call breakdowns, daily reports, product dashboards and wallet profiling. The same credit-metered core is exposed three ways — a bearer-JWT REST API described by an OpenAPI 3.0.1 document with 36 operations (including durable, idempotent asynchronous analytics invocations), an A2A 1.0 agent ("Moirai Agents API", 11 skills, registered in the A2A Registry) and an MCP bridge on the agent host — alongside an OpenAI ai-plugin.json manifest, llms.txt and an RFC 9116 security.txt. Subscription plans meter contracts under analysis per 30-day period; the plan catalog is served anonymously by the API.'
finops:
- has_sources: true
  method: derived
  name: Moirailabs Com Finops
  primary_unit: contracts
  service_category: ''
  slug: moirailabs-com-finops
  template: false
image: https://moirailabs.com/og-image.png
layout: provider
mcp_servers:
- description: 'Moirai Labs ships one remote MCP surface: an "MCP bridge" mounted on the A2A agent host at https://agent.moirailabs.com/a2a/v1/mcp, declared by the agent card as a vendor extension and by the /a2a pag'
  name: Moirai Labs MCP Server
  slug: moirailabs-com-mcp-yml
modified: '2026-09-19'
name: Moirai Labs
nav: Providers
network: true
overview: 'Moirai Labs publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics Controller API, Analytics Invocation Controller API, Contract Info Controller API, and 7 more. Tagged areas include Company, Blockchain, Smart Contracts, Web3, and Analytics.


  The Moirai Labs catalog on APIs.io includes 1 Spectral governance ruleset.


  Moirai Labs'' developer surface includes documentation, pricing, signup flow, engineering blog, support, authentication, and 31 more developer resources.'
plans:
- name: Moirailabs Com Plans Pricing
  plan_count: 5
  slug: moirailabs-com-plans-pricing
- name: Moirailabs Com Price Estimates
  plan_count: 0
  slug: moirailabs-com-price-estimates
random_paper: 7
rate_limits:
- limit_count: 5
  name: Moirailabs Com Rate Limits
  slug: moirailabs-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Moirai Labs API Rules
  rule_count: 53
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 5
  slug: moirailabs-com-rules
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 29
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 61.8
    contract_governance: 18.2
    contract_quality: 54.2
    developer_ergonomics: 22.0
    discoverability: 75.0
    operational_transparency: 47.4
  previous_composite: 52.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/moirailabs-com/moirailabs-com-2026-10-11T111210.png
security:
- kind: authentication
  name: Moirailabs Com Authentication
  slug: moirailabs-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Moirailabs Com Domain Security
  slug: moirailabs-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Moirailabs Com Vulnerability Disclosure
  slug: moirailabs-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: moirailabs-com-async-analytics-invocation
  slug: moirailabs-com-async-analytics-invocation
- name: moirailabs-com-cohort-and-method-report
  slug: moirailabs-com-cohort-and-method-report
- name: moirailabs-com-register-contract
  slug: moirailabs-com-register-contract
slug: moirailabs-com
tags:
- Company
- Blockchain
- Smart Contracts
- Web3
- Analytics
- cohort-analysis
- Wallet Profiling
- Ethereum
- AI Agents
- A2A
- MCP
- Agent-Native
website: https://moirailabs.com/
---
