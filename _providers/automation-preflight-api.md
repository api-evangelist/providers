---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Automation Preflight Api Agentic Access
  operation_count: 5
  slug: automation-preflight-api-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 4
apis:
- description: The Acceptance Pack API from Automation Preflight API — 1 operation(s) for acceptance pack.
  name: Automation Preflight API Acceptance Pack API
  slug: automation-preflight-api-acceptance-pack-api
- description: The Analyze API from Automation Preflight API — 1 operation(s) for analyze.
  name: Automation Preflight API Analyze API
  slug: automation-preflight-api-analyze-api
- description: The Direct API from Automation Preflight API — 1 operation(s) for direct.
  name: Automation Preflight API Direct API
  slug: automation-preflight-api-direct-api
- description: The Health API from Automation Preflight API — 1 operation(s) for health.
  name: Automation Preflight API Health API
  slug: automation-preflight-api-health-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TinyOps Automation Integration Preflight Acceptance Pack API
  slug: open-automation-preflight-api-acceptance-pack-api
- collection_type: open
  name: TinyOps Automation Integration Preflight Analyze API
  slug: open-automation-preflight-api-analyze-api
- collection_type: open
  name: TinyOps Automation Integration Preflight - Access Direct API
  slug: open-automation-preflight-api-direct-api
- collection_type: open
  name: Automation Preflight Health API
  slug: open-automation-preflight-api-health-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/automation-preflight-api-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/automation-preflight-api-direct-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/automation-preflight-api-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/automation-preflight-api-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/automation-preflight-api-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tinyopsstudio.com/product
- group: operate
  title: ''
  type: Support
  url: https://tinyopsstudio.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tinyopsstudio
- group: commercial
  title: ''
  type: Pricing
  url: https://api.market/store/tinyopsstudio/automation-preflight
- group: start
  title: ''
  type: SignUp
  url: https://tinyopsstudio.gumroad.com/l/automation-preflight-api-500
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tinyopsstudio.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tinyopsstudio.com/privacy
- group: other
  title: ''
  type: AgentCard
  url: a2a/automation-preflight-api-a2a.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/automation-preflight-api-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/automation-preflight-api-llms.txt
- group: agent
  title: ''
  type: LLMsTxt Source
  url: https://tinyopsstudio.com/llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/automation-preflight-api-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/automation-preflight-api-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/automation-preflight-api-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/automation-preflight-api-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/automation-preflight-api-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/automation-preflight-api-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/automation-preflight-api-plans.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/automation-preflight-api-sandbox.yml
- group: build
  title: ''
  type: Examples
  url: examples/automation-preflight-api-analyze-example.json
- group: build
  title: ''
  type: Examples
  url: examples/automation-preflight-api-health-and-errors-example.json
created: '2026-07-29'
description: 'A self-serve REST API by TinyOps Studio LLC that inspects a public URL and returns deterministic, bounded JSON integration-readiness evidence across reachability, integration surface, and readiness scoring. It rejects private/credential-bearing targets, honors robots exclusions, bounds redirects and response sizes, does not execute JavaScript, and does not return raw HTML. Three operations are published: an open POST /analyze that answers without a key, a metered POST /direct/analyze authenticated with a Gumroad license key, and POST /acceptance-pack which returns launch gates, acceptance tests, and a prioritized remediation backlog. Sold as a $19 pack of 500 analyses, as pay-as-you-go units on API.market, and per-run on AgenticTrade.'
examples:
- key_count: 4
  name: Automation Preflight Api Analyze Example
  slug: automation-preflight-api-analyze-example
- key_count: 2
  name: Automation Preflight Api Health And Errors Example
  slug: automation-preflight-api-health-and-errors-example
image: https://tinyopsstudio.com/assets/tinyops-logo-mark-v4.png
layout: provider
mcp_servers:
- description: ''
  name: automation-preflight-api-mcp.yml
  slug: automation-preflight-api-mcpyml
modified: '2026-08-09'
name: Automation Preflight API
nav: Providers
network: true
overview: 'Automation Preflight API publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Acceptance Pack API, Analyze API, Direct API, and 1 more. Tagged areas include automation, integration, developer-tools, readiness, and testing.


  Automation Preflight API''s developer surface includes authentication, support, pricing, signup flow, sandbox, code examples, and 21 more developer resources.'
plans:
- name: Automation Preflight Api Plans
  plan_count: 4
  slug: automation-preflight-api-plans
random_paper: 74
rate_limits:
- limit_count: 2
  name: Automation Preflight Api Rate Limits
  slug: automation-preflight-api-rate-limits
score:
  band: developing
  composite: 48.6
  delta: 0.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 54.3
    developer_ergonomics: 34.2
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 26.3
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Automation Preflight Api Authentication
  slug: automation-preflight-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Automation Preflight Api Domain Security
  slug: automation-preflight-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: automation-preflight-api
tags:
- automation
- integration
- developer-tools
- readiness
- testing
- url-analysis
- web-scraping
- agent-tools
- quality-assurance
- site-audit
website: https://tinyopsstudio.com/product
---
