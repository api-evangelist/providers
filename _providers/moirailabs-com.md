---
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.4
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 13
  human_in_the_loop: 13
  name: Moirailabs Com Agentic Access
  operation_count: 36
  slug: moirailabs-com-agentic-access
  summary_line: 36 operations · 13 acting · 13 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.moirailabs.com/api/v1
  baseurl_source: declared
  description: 'REST API for smart-contract analytics on EVM chains: register contracts and track indexer sync, run cohort / method / metrics / dashboard / token analytics synchronously or as durable asynchronous inv'
  name: Moirai Labs API
  slug: moirai-labs-api
- description: A2A 1.0 agent ("A2A-compatible analytics and contract intelligence agent", version 0.1.0) with 11 skills — analytics.cohorts/metrics/methods/methods_by_cohorts/transactions, reports.daily/weekly/month
  name: Moirai Agents API (A2A + MCP)
  slug: moirai-agents-api
artifact_total: 10
common:
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
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/llms/moirailabs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/moirailabs-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://moirailabs.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/well-known/moirailabs-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/moirailabs-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/well-known/moirailabs-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/moirailabs-com-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/a2a/moirailabs-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/moirailabs-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/mcp/moirailabs-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/moirailabs-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/mcp/moirailabs-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/moirailabs-com-tool-crosswalk.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/authentication/moirailabs-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/moirailabs-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/conventions/moirailabs-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/moirailabs-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/conventions/moirailabs-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/moirailabs-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/errors/moirailabs-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/moirailabs-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/lifecycle/moirailabs-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/moirailabs-com-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/conformance/moirailabs-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/moirailabs-com-conformance.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/rate-limits/moirailabs-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/moirailabs-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/plans/moirailabs-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/moirailabs-com-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/data-model/moirailabs-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/moirailabs-com-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/overlays/moirailabs-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moirailabs-com-openapi-overlay.yaml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/packages/moirailabs-com-packages.yml
  title: ''
  type: Packages
  url: packages/moirailabs-com-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/agentic-access/moirailabs-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/moirailabs-com-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/security/moirailabs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moirailabs-com-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/security/moirailabs-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/moirailabs-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/security/moirailabs-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/moirailabs-com-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moirailabs-com/refs/heads/main/regulatory/moirailabs-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/moirailabs-com-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://moirailabs.com/privacy
created: '2026-09-19'
description: 'Moirai Labs is a smart-contract analytics platform for Web3 teams that turns raw EVM chain data (Ethereum, Polygon, Arbitrum, Optimism, Base, Linea) into product-grade metrics: cohort retention, method-level call breakdowns, daily reports, product dashboards and wallet profiling. The same credit-metered core is exposed three ways — a bearer-JWT REST API described by an OpenAPI 3.0.1 document with 36 operations (including durable, idempotent asynchronous analytics invocations), an A2A 1.0 agent ("Moirai Agents API", 11 skills, registered in the A2A Registry) and an MCP bridge on the agent host — alongside an OpenAI ai-plugin.json manifest, llms.txt and an RFC 9116 security.txt. Subscription plans meter contracts under analysis per 30-day period; the plan catalog is served anonymously by the API.'
image: https://moirailabs.com/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: Moirai Labs MCP Server
  slug: moirai-labs-mcp-server
- description: ''
  name: MCP bridge endpoint (bearer-gated)
  slug: mcp-bridge-endpoint-bearer-gated
modified: '2026-09-19'
name: Moirai Labs
nav: Providers
network: true
overview: 'Moirai Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Smart Contracts, Web3, and Analytics.


  Moirai Labs'' developer surface includes documentation, pricing, signup flow, engineering blog, support, authentication, and 30 more developer resources.'
plans:
- name: Moirailabs Com Plans Pricing
  plan_count: 4
  slug: moirailabs-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Moirailabs Com Rate Limits
  slug: moirailabs-com-rate-limits
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 52.5
    developer_ergonomics: 30.4
    discoverability: 75.9
    operational_transparency: 52.6
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
