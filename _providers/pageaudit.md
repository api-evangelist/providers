---
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-09-08'
agentic_access:
- acting_count: 16
  human_in_the_loop: 1
  name: Pageaudit Agentic Access
  operation_count: 38
  slug: pageaudit-agentic-access
  summary_line: 38 operations · 16 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: REST/HTTP API for one-shot technical SEO audits plus micro-tools, with a hosted MCP server, llms.txt, and OKF knowledge bundle. OpenAPI 3.1.0 covering 38 endpoints and 26 structures.
  name: PageAudit API
  slug: pageaudit-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://pageaudit.online/
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/pageaudit-tool-crosswalk.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pageaudit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://pageaudit.online/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pageaudit-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pageaudit-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pageaudit-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pageaudit-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/pageaudit-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pageaudit-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pageaudit-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/pageaudit-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/pageaudit-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pageaudit-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pageaudit-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pageaudit-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/pageaudit-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/pageaudit-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pageaudit-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pageaudit-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://pageaudit.online/api/billing
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pageaudit-rate-limits.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pageaudit.online/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pageaudit.online/privacy
created: '2026-09-05'
description: An agent-first technical SEO auditor that checks a page's search appearance, sharing previews and technical issues, prioritizes fixes, and delivers ready-to-apply patches for head tags, robots and sitemap. Every UI screen has an equivalent endpoint and every resource carries its own API URL.
image: https://pageaudit.online/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: PageAudit MCP Server
  slug: pageaudit-mcp-server
- description: ''
  name: PageAudit
  slug: pageaudit
modified: '2026-09-07'
name: PageAudit
nav: Providers
network: true
overview: 'PageAudit publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Technical SEO, SEO auditing, Developer Tools, Agent-native, and MCP.


  PageAudit''s developer surface includes authentication, pricing, and 23 more developer resources.'
plans:
- name: Pageaudit Plans Pricing
  plan_count: 3
  slug: pageaudit-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Pageaudit Rate Limits
  slug: pageaudit-rate-limits
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 35.2
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Pageaudit Authentication
  slug: pageaudit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pageaudit Domain Security
  slug: pageaudit-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Pageaudit Vulnerability Disclosure
  slug: pageaudit-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pageaudit
tags:
- Technical SEO
- SEO auditing
- Developer Tools
- Agent-native
- MCP
- x402
website: https://pageaudit.online/
---
