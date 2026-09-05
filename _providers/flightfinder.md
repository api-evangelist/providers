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
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: REST/JSON over the merged corpus. 17 paths / 18 operations in the served OpenAPI 3.0.3. Keyless GET tier, CORS open, RateLimit-* headers on every response, per-record licence and attribution.
  name: FlightFinder Aviation Safety Data API
  slug: flightfinder-aviation-safety-data-api
- description: First-party remote MCP server over Streamable HTTP (JSON-RPC 2.0, protocol 2025-06-18) exposing nine read tools over the same corpus. Anonymous — no key, no account, no install. Probed live on 2026-09
  name: FlightFinder Aviation Safety MCP Server
  slug: flightfinder-aviation-safety-mcp-server
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flightfinder-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flightfinder-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flightfinder-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/flightfinder-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flightfinder-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://himaxym.com/.well-known/api-catalog
- group: other
  title: ''
  type: ContentSignal
  url: https://himaxym.com/robots.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/flightfinder-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/flightfinder-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flightfinder-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/flightfinder-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/flightfinder-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flightfinder-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flightfinder-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/flightfinder-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/flightfinder-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flightfinder-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://himaxym.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://himaxym.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://himaxym.com/developers
- group: start
  title: ''
  type: SignUp
  url: https://himaxym.com/developers#dev-key-form
- group: operate
  title: ''
  type: Support
  url: https://himaxym.com/contact
- group: company
  title: ''
  type: Blog
  url: https://himaxym.com/aviation-news
- group: commercial
  title: ''
  type: Pricing
  url: https://himaxym.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://himaxym.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://himaxym.com/legal/privacy
- group: other
  title: ''
  type: X-Methodology
  url: https://himaxym.com/methodology
- group: other
  title: ''
  type: X-EditorialStandards
  url: https://himaxym.com/editorial-standards
- group: other
  title: ''
  type: X-AIContentPolicy
  url: https://himaxym.com/ai-content-policy
- group: other
  title: ''
  type: X-Attributions
  url: https://himaxym.com/legal/attributions
created: '2026-09-03'
description: 'Read-only JSON API over a merged aviation-safety corpus: 164,068 accident narratives aggregated from 130 official investigation authorities (NTSB, ATSB, AAIB, BEA, MAK and national agencies), deduplicated into one occurrence-level dataset, plus the FAA wildlife-strike, laser-incident and drone-sighting datasets and OurAirports reference data. Every record carries its source, attribution, licence and a deep link, and GET /sources returns the per-source licence and narrative policy. Keyless tier answers without an Authorization header at 100 requests/day/IP, and the same corpus is served to agents by an anonymous remote MCP server at https://himaxym.com/mcp with nine tools.'
image: https://himaxym.com/og-image.png?v=2
layout: provider
mcp_servers:
- description: FlightFinder operates a first-party, anonymous, remote MCP server over Streamable HTTP at https://himaxym.com/mcp. It is a projection of the same merged aviation-safety corpus the REST API serves — an
  name: FlightFinder MCP Server
  slug: flightfinder-mcp-server
modified: '2026-09-03'
name: FlightFinder
nav: Providers
network: true
overview: 'FlightFinder publishes 1 API on the [APIs.io](https://apis.io/) network: Aviation Safety Data API. Tagged areas include Aviation, Aviation Safety, Accident Data, Open Data, and Public Domain.


  FlightFinder''s developer surface includes authentication, sandbox, API reference, getting-started guide, signup flow, support, engineering blog, and 24 more developer resources.'
plans:
- name: Flightfinder Plans Pricing
  plan_count: 3
  slug: flightfinder-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Flightfinder Rate Limits
  slug: flightfinder-rate-limits
score:
  band: developing
  composite: 52.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 70.8
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 52.6
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: authentication
  name: Flightfinder Authentication
  slug: flightfinder-authentication
  summary_line: http/none · 2 schemes
- kind: domain-security
  name: Flightfinder Domain Security
  slug: flightfinder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flightfinder
tags:
- Aviation
- Aviation Safety
- Accident Data
- Open Data
- Public Domain
- Transportation
- Government Data
- Research
- Reference Data
- Agent Ready
website: https://himaxym.com/developers
---
