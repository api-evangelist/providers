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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fluentedi Agentic Access
  operation_count: 99
  slug: fluentedi-agentic-access
  summary_line: 99 operations
api_count: 1
apis:
- description: Stateless HTTP tool API. 50 paths and 99 operations in the served OpenAPI 3.1, no authentication. A failed call returns the tool parameter schema plus working example URLs.
  name: FluentEDI Tools API
  slug: fluentedi-tools-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fluentedi-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fluentedi-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fluentedi-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fluentedi-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fluentedi-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/fluentedi-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fluentedi-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://fluentedi.com/health
- group: design
  title: ''
  type: Conformance
  url: conformance/fluentedi-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fluentedi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fluentedi-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fluentedi-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fluentedi.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fluentedi.com/privacy
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mastermanas805/fluentedi-mcp
created: '2026-09-03'
description: 45 deterministic tools for AI agents, free and with no API key, signup or rate limit. Every tool is a single stateless GET or POST returning JSON, read-only and idempotent. Coverage runs deepest in retail EDI -- X12 850/856/810/855/997 parsing, generating an 856 with correct HL parent pointers and a fixed-width 106-character ISA, envelope validation, decoding a 997 acknowledgment into plain language, and GS1 check digits -- alongside timezone and delivery-window arithmetic, cron, exact maths, JSON repair with line/column error localisation, JSONPath, RFC 8785 canonical JSON with CIDv1, Ed25519/ECDSA/RSA signature verification, secret and PII scanning, link-liveness checking with retraction detection, endpoint assertion, and text position conversion.
image: https://fluentedi.com/favicon.svg
layout: provider
mcp_servers:
- description: ''
  name: FluentEDI MCP Server
  slug: fluentedi-mcp-server
- description: ''
  name: FluentEDI MCP Server
  slug: fluentedi-mcp-server-2
modified: '2026-09-03'
name: FluentEDI
nav: Providers
network: true
overview: 'FluentEDI publishes 1 API on the [APIs.io](https://apis.io/) network: Tools API. Tagged areas include EDI, X12, Retail EDI, AI Agents, and MCP.


  FluentEDI''s developer surface includes authentication, GitHub presence, and 14 more developer resources.'
plans:
- name: Fluentedi Plans Pricing
  plan_count: 1
  slug: fluentedi-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Fluentedi Rate Limits
  slug: fluentedi-rate-limits
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.0
    catalog_earned_first_party: 8.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 40.0
    developer_ergonomics: 39.9
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 13.2
  previous_composite: 35.7
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Fluentedi Authentication
  slug: fluentedi-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Fluentedi Domain Security
  slug: fluentedi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: fluentedi
tags:
- EDI
- X12
- Retail EDI
- AI Agents
- MCP
- Developer Tools
- JSON
- Cryptography
- Data Validation
- Supply Chain
website: https://fluentedi.com/
---
