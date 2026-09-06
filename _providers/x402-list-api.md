---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Public REST API (OpenAPI 3.1) providing access to the x402 services directory, uptime, pricing, facilitator volumes, networks, stats, rankings, and change events. Free reads (rate-limited), with x402 '
  name: x402 List API
  slug: x402-list-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/x402-list-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/x402-list-api-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/x402-list-api-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://x402-list.com/.well-known/api-catalog
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/x402-list-api-security.txt
- group: auth
  title: ''
  type: Security
  url: security/x402-list-api-vulnerability-disclosure.yml
- group: other
  title: ''
  type: ContentSignal
  url: https://x402-list.com/robots.txt
- group: other
  title: ''
  type: APIsJSON
  url: https://x402-list.com/.well-known/apis.json
- group: build
  title: ''
  type: Packages
  url: packages/x402-list-api-packages.yml
- group: company
  title: ''
  type: Blog
  url: https://x402-list.com/blog
- group: operate
  title: ''
  type: Support
  url: https://x402-list.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://x402-list.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://x402-list.com/privacy
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/mcccsm/x402-list-mcp
created: '2026-09-02'
description: An open, machine-readable, live-monitored directory of services that accept x402 protocol payments (HTTP 402 Payment Required). Self-described as agent-first, it exposes service listings, uptime metrics, pricing, facilitator settlement data, and rankings as JSON for autonomous agents, aggregators, and integrations.
image: https://x402-list.com/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: x402 List API MCP Server
  slug: x402-list-api-mcp-server
- description: 'x402 List ships a first-party MCP server in both shapes: a hosted Streamable HTTP endpoint at https://mcp.x402-list.com/mcp that answers tools/list anonymously, and a local stdio build published to np'
  name: x402 List API MCP Server
  slug: x402-list-api-mcp-server-2
modified: '2026-09-02'
name: x402 List API
nav: Providers
network: true
overview: 'x402 List API publishes 1 API on the [APIs.io](https://apis.io/) network: x402 List API. Tagged areas include x402, crypto, 402, agentic-payments, and API directory.


  The x402 List API catalog on APIs.io includes 1 Spectral governance ruleset.


  x402 List API''s developer surface includes engineering blog, support, and 12 more developer resources.'
plans:
- name: X402 List Api Plans Pricing
  plan_count: 2
  slug: x402-list-api-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: X402 List Api Rate Limits
  slug: x402-list-api-rate-limits
rules:
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: x402 List API API Rules
  rule_count: 5
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 2
  slug: x402-list-api-spectral
score:
  band: strong
  composite: 56.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 68.0
    catalog_earned_first_party: 16.0
    catalog_gap: 47.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 50.0
    contract_quality: 33.3
    developer_ergonomics: 58.9
    discoverability: 87.0
    governance: 50.0
    operational_transparency: 68.4
  previous_composite: 56.6
  provenance:
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: X402 List Api Authentication
  slug: x402-list-api-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: X402 List Api Domain Security
  slug: x402-list-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: X402 List Api Vulnerability Disclosure
  slug: x402-list-api-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: x402-list-api
tags:
- x402
- crypto
- '402'
- agentic-payments
- API directory
- registry
- AI agents
- blockchain
- developer tools
- uptime monitoring
---
