---
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.3
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Finn Tannlege Com Agentic Access
  operation_count: 11
  slug: finn-tannlege-com-agentic-access
  summary_line: 11 operations · 2 acting
api_count: 1
apis:
- baseURL: https://finn-tannlege.com/api/tannlege
  baseurl_source: declared
  description: 'Read-only JSON API over the clinic directory: list and filter clinics (free text, county, specialty, Helfo agreement, emergency duty, enrichment state, limit/offset), fetch one clinic by UUID, list th'
  name: Finn-tannlege REST API
  slug: finn-tannlege-rest-api
- description: 'The agent-to-agent surface: an anonymous A2A JSON-RPC 2.0 endpoint at https://finn-tannlege.com/a2a implementing message/send, described by a signed (EdDSA JWS, JWKS at /.well-known/jwks.json) agent c'
  name: Finn-tannlege A2A Agent
  slug: finn-tannlege-a2a-agent
- description: 'Model Context Protocol server in two shipped forms: a remote Streamable-HTTP endpoint at https://finn-tannlege.com/mcp (session-based - initialize first, then send the Mcp-Session-Id header) and the n'
  name: Finn-tannlege MCP Server
  slug: finn-tannlege-mcp-server
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://finn-tannlege.com/
- group: docs
  title: ''
  type: Documentation
  url: https://finn-tannlege.com/llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://finn-tannlege.com/hvordan-det-fungerer
- group: company
  title: ''
  type: About
  url: https://finn-tannlege.com/om
- group: operate
  title: ''
  type: Support
  url: https://finn-tannlege.com/kontakt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://finn-tannlege.com/personvern
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/slookisen/lokal/tree/main/mcp-server-dental
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://finn-tannlege.com/personvern
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/finn-tannlege-com/refs/heads/main/agentic-access/finn-tannlege-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/finn-tannlege-com-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/finn-tannlege-com/refs/heads/main/security/finn-tannlege-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/finn-tannlege-com-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/finn-tannlege-com/refs/heads/main/a2a/finn-tannlege-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/finn-tannlege-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/finn-tannlege-com/refs/heads/main/mcp/finn-tannlege-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/finn-tannlege-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/finn-tannlege-com/refs/heads/main/mcp/finn-tannlege-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/finn-tannlege-com-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/finn-tannlege-com/refs/heads/main/llms/finn-tannlege-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/finn-tannlege-com-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/finn-tannlege-com/refs/heads/main/well-known/finn-tannlege-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/finn-tannlege-com-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/finn-tannlege-com/refs/heads/main/packages/finn-tannlege-com-packages.yml
  title: ''
  type: Packages
  url: packages/finn-tannlege-com-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/finn-tannlege-com/refs/heads/main/authentication/finn-tannlege-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/finn-tannlege-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/finn-tannlege-com/refs/heads/main/conventions/finn-tannlege-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/finn-tannlege-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/finn-tannlege-com/refs/heads/main/errors/finn-tannlege-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/finn-tannlege-com-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/finn-tannlege-com/refs/heads/main/rate-limits/finn-tannlege-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/finn-tannlege-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/finn-tannlege-com/refs/heads/main/plans/finn-tannlege-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/finn-tannlege-com-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/finn-tannlege-com/refs/heads/main/conformance/finn-tannlege-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/finn-tannlege-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/finn-tannlege-com/refs/heads/main/lifecycle/finn-tannlege-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/finn-tannlege-com-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/finn-tannlege-com/refs/heads/main/data-model/finn-tannlege-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/finn-tannlege-com-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/finn-tannlege-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-19'
description: 'Finn-tannlege.com is an independent, free directory of Norwegian dental clinics (5,447 clinics on 2026-09-19) assembled from public sources - the Brønnøysund Register Centre (Brreg), the Norwegian Health Personnel Register (HPR), the Norwegian Dental Association (NTF) and the clinics'' own websites - and searchable by county (fylke), specialty, Helfo direct-billing agreement and emergency-duty (akuttvakt) availability. It is built for people and AI agents alike: an open, key-free REST API under /api/tannlege described by an OpenAPI 3.1 document, an A2A 1.0.0 agent card and JSON-RPC endpoint, a remote Streamable-HTTP MCP server plus an npm stdio package (finn-tannlege-mcp), an llms.txt and a ChatGPT Custom GPT. Operated by Daniel Fredriksen on the same Norwegian A2A agent platform as rettfrabonden.com and opplevagent.no; every clinic field is stored with its source and last-confirmed date, and the "Verified" badge is an editorially set status.'
image: https://finn-tannlege.com/favicon.svg
layout: provider
mcp_servers:
- description: Search and compare Norwegian dental clinics (5,447 on 2026-09-19) by free text, county (fylke), specialty, Helfo direct-billing agreement and emergency-duty (akuttvakt) availability, fetch a single cl
  name: Finn-tannlege MCP Server
  slug: finn-tannlege-mcp-server
modified: '2026-09-19'
name: Finn-tannlege
nav: Providers
network: true
overview: 'Finn-tannlege publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Dental, Healthcare, Directory, Norway, and Search.


  Finn-tannlege''s developer surface includes documentation, getting-started guide, support, authentication, and 21 more developer resources.'
plans:
- name: Finn Tannlege Com Plans Pricing
  plan_count: 1
  slug: finn-tannlege-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Finn Tannlege Com Rate Limits
  slug: finn-tannlege-com-rate-limits
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 43.4
    developer_ergonomics: 39.9
    discoverability: 75.9
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - norway
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 38.8
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
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Finn Tannlege Com Authentication
  slug: finn-tannlege-com-authentication
  summary_line: none/apiKey · 2 schemes
- kind: domain-security
  name: Finn Tannlege Com Domain Security
  slug: finn-tannlege-com-domain-security
  summary_line: TLSv1.3
slug: finn-tannlege-com
tags:
- Dental
- Healthcare
- Directory
- Norway
- Search
- Open Data
- A2A
- MCP
- AI Agents
- Clinics
website: https://finn-tannlege.com/
---
