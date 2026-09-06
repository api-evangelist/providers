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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 20
  human_in_the_loop: 1
  name: Meta Agent Tools Agentic Access
  operation_count: 42
  slug: meta-agent-tools-agentic-access
  summary_line: 42 operations · 20 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: REST/HTTP API for a registry of MCP servers, agent skills and plugins — public catalog search, publishing/editing listings, engagement (likes/comments/visits), accounts, MCP subregistry (Official Regi
  name: Meta Agent Tools API
  slug: meta-agent-tools-api
artifact_total: 8
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/meta-agent-tools-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/meta-agent-tools-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meta-agent-tools-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/meta-agent-tools-authentication.yml
- group: auth
  title: ''
  type: Security
  url: well-known/meta-agent-tools-security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/meta-agent-tools-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/meta-agent-tools-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/meta-agent-tools-api-catalog.json
- group: design
  title: ''
  type: Conformance
  url: conformance/meta-agent-tools-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/meta-agent-tools-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/meta-agent-tools-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/meta-agent-tools-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/meta-agent-tools-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/meta-agent-tools-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://agentalog.com/#precos
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://agentalog.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentalog.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentalog.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://agentalog.com/sobre
- group: start
  title: ''
  type: GettingStarted
  url: https://agentalog.com/como-anunciar
- group: start
  title: ''
  type: SignUp
  url: https://agentalog.com/
created: '2026-09-05'
description: A registry/catalog of MCP servers, agent skills and plugins. It aggregates MCP metadata from the Official MCP Registry, Smithery and Casdoor, and public skill dumps, exposing a REST/HTTP API, a hosted MCP server, an llms.txt agent guide and a public OpenAPI 3.1 contract. Portuguese-language service based in Brazil. Canonical host is agentalog.com — the originally submitted classificado.app.br permanently redirects (301) every path there.
image: https://agentalog.com/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: Meta Agent Tools
  slug: meta-agent-tools
modified: '2026-09-05'
name: Meta Agent Tools
nav: Providers
network: true
overview: 'Meta Agent Tools publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Developer Tools, API Registry, Agent Registry, MCP, and Agent Skills.


  Meta Agent Tools'' developer surface includes authentication, pricing, support, getting-started guide, signup flow, and 17 more developer resources.'
plans:
- name: Meta Agent Tools Plans Pricing
  plan_count: 3
  slug: meta-agent-tools-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Meta Agent Tools Rate Limits
  slug: meta-agent-tools-rate-limits
score:
  band: developing
  composite: 50.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 33.3
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
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
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: Meta Agent Tools Authentication
  slug: meta-agent-tools-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Meta Agent Tools Domain Security
  slug: meta-agent-tools-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Meta Agent Tools Vulnerability Disclosure
  slug: meta-agent-tools-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: meta-agent-tools
tags:
- Developer Tools
- API Registry
- Agent Registry
- MCP
- Agent Skills
- AI Agents
- Catalog
- Directory
- Search & Discovery
- x402
- Agent Payments
- Community
- UGC
website: https://agentalog.com/
---
