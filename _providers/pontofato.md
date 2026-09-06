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
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 29.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Pontofato Agentic Access
  operation_count: 18
  slug: pontofato-agentic-access
  summary_line: 18 operations · 3 acting
api_count: 1
apis:
- description: REST/JSON API for CEP-to-CNEFE point resolution, address search, proximity/radius queries, and Receita Federal business lookups. Includes a hosted MCP server and agent-native discovery artifacts.
  name: PontoFato API
  slug: pontofato-api
artifact_total: 9
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pontofato-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pontofato-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pontofato-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://pontofato.com/.well-known/security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pontofato-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/pontofato-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pontofato-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pontofato-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/pontofato-security.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/pontofato-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/pontofato-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pontofato-problem-types.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pontofato-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pontofato-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pontofato-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pontofato-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pontofato-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://pontofato.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://pontofato.com/#agentes
- group: commercial
  title: ''
  type: Pricing
  url: https://pontofato.com/#precos
- group: operate
  title: ''
  type: Support
  url: https://pontofato.com/#contato
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pontofato.com/termos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pontofato.com/privacidade
created: '2026-09-05'
description: Brazilian address/location-intelligence API mapping CEP (postal code) or address to IBGE CNEFE census points with latitude/longitude, joined with Receita Federal business establishments. Offers proximity/radius search, full-text street search, and companies-at-location lookups. Agent-first provider with a hosted MCP server and llms.txt.
image: https://pontofato.com/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: PontoFato MCP Server
  slug: pontofato-mcp-server
- description: ''
  name: PontoFato
  slug: pontofato
modified: '2026-09-05'
name: PontoFato
nav: Providers
network: true
overview: 'PontoFato publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Brazilian CEP, address geocoding, IBGE CNEFE, geospatial, and latitude/longitude.


  PontoFato''s developer surface includes authentication, getting-started guide, pricing, support, and 20 more developer resources.'
plans:
- name: Pontofato Plans Pricing
  plan_count: 3
  slug: pontofato-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Pontofato Rate Limits
  slug: pontofato-rate-limits
score:
  band: developing
  composite: 48.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: Pontofato Authentication
  slug: pontofato-authentication
  summary_line: none/http-bearer/x402-payment · 4 schemes
- kind: domain-security
  name: Pontofato Domain Security
  slug: pontofato-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Pontofato Vulnerability Disclosure
  slug: pontofato-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pontofato
tags:
- Brazilian CEP
- address geocoding
- IBGE CNEFE
- geospatial
- latitude/longitude
- CNPJ
- Receita Federal
- business registry
- location intelligence
- proximity search
- radius search
- open government data
- agent-native
- MCP
- x402 micropayments
website: https://pontofato.com/
---
