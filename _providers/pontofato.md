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
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Pontofato Agentic Access
  operation_count: 18
  slug: pontofato-agentic-access
  summary_line: 18 operations · 3 acting
api_count: 1
apis:
- baseURL: https://pontofato.com
  baseurl_source: declared
  description: The Apis.json API from PontoFato — 1 operation(s) for apis.json.
  name: PontoFato Apis.json API
  slug: pontofato-apis-json-api
- baseURL: https://pontofato.com
  baseurl_source: declared
  description: The Buscar API from PontoFato — 1 operation(s) for buscar.
  name: PontoFato Buscar API
  slug: pontofato-buscar-api
- baseURL: https://pontofato.com
  baseurl_source: declared
  description: The Cep API from PontoFato — 2 operation(s) for cep.
  name: PontoFato Cep API
  slug: pontofato-cep-api
- baseURL: https://pontofato.com
  baseurl_source: declared
  description: The Contact API from PontoFato — 1 operation(s) for contact.
  name: PontoFato Contact API
  slug: pontofato-contact-api
- baseURL: https://pontofato.com
  baseurl_source: declared
  description: The Credito API from PontoFato — 1 operation(s) for credito.
  name: PontoFato Credito API
  slug: pontofato-credito-api
- baseURL: https://pontofato.com
  baseurl_source: declared
  description: The Empresas API from PontoFato — 1 operation(s) for empresas.
  name: PontoFato Empresas API
  slug: pontofato-empresas-api
- baseURL: https://pontofato.com
  baseurl_source: declared
  description: The Health API from PontoFato — 1 operation(s) for health.
  name: PontoFato Health API
  slug: pontofato-health-api
- baseURL: https://pontofato.com
  baseurl_source: declared
  description: The Local API from PontoFato — 1 operation(s) for local.
  name: PontoFato Local API
  slug: pontofato-local-api
- baseURL: https://pontofato.com
  baseurl_source: declared
  description: The Mcp API from PontoFato — 1 operation(s) for mcp.
  name: PontoFato MCP API
  slug: pontofato-mcp-api
- baseURL: https://pontofato.com
  baseurl_source: declared
  description: The Metrics API from PontoFato — 1 operation(s) for metrics.
  name: PontoFato Metrics API
  slug: pontofato-metrics-api
- baseURL: https://pontofato.com
  baseurl_source: declared
  description: The Okf API from PontoFato — 1 operation(s) for okf.
  name: PontoFato Okf API
  slug: pontofato-okf-api
- baseURL: https://pontofato.com
  baseurl_source: declared
  description: The PontoFato API from PontoFato — 1 operation(s) for pontofato.
  name: PontoFato Ponto Fato API
  slug: pontofato-pontofato-api
- baseURL: https://pontofato.com
  baseurl_source: declared
  description: The Proximo API from PontoFato — 1 operation(s) for proximo.
  name: PontoFato Proximo API
  slug: pontofato-proximo-api
- baseURL: https://pontofato.com
  baseurl_source: declared
  description: The Raio API from PontoFato — 1 operation(s) for raio.
  name: PontoFato Raio API
  slug: pontofato-raio-api
- baseURL: https://pontofato.com
  baseurl_source: declared
  description: The Vizinhanca API from PontoFato — 1 operation(s) for vizinhanca.
  name: PontoFato Vizinhanca API
  slug: pontofato-vizinhanca-api
- baseURL: https://pontofato.com
  baseurl_source: declared
  description: The .well Known API from PontoFato — 1 operation(s) for .well known.
  name: PontoFato .well Known API
  slug: pontofato-well-known-api
artifact_total: 24
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://pontofato.com/mcp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pontofato/refs/heads/main/agentic-access/pontofato-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pontofato-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pontofato/refs/heads/main/security/pontofato-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pontofato-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pontofato/refs/heads/main/security/pontofato-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pontofato-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://pontofato.com/.well-known/security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pontofato/refs/heads/main/mcp/pontofato-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pontofato-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pontofato/refs/heads/main/mcp/pontofato-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/pontofato-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pontofato/refs/heads/main/llms/pontofato-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pontofato-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pontofato/refs/heads/main/well-known/pontofato-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pontofato-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pontofato/refs/heads/main/well-known/pontofato-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pontofato-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pontofato/refs/heads/main/overlays/pontofato-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pontofato-openapi-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pontofato/refs/heads/main/conformance/pontofato-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pontofato-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pontofato/refs/heads/main/errors/pontofato-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pontofato-problem-types.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pontofato/refs/heads/main/authentication/pontofato-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pontofato-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pontofato/refs/heads/main/conventions/pontofato-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pontofato-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pontofato/refs/heads/main/data-model/pontofato-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pontofato-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/pontofato/refs/heads/main/plans/pontofato-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pontofato-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pontofato/refs/heads/main/rate-limits/pontofato-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pontofato-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pontofato/refs/heads/main/skills/_index.yml
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
overview: 'PontoFato publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Apis.json API, Buscar API, Cep API, and 13 more. Tagged areas include Brazilian CEP, address geocoding, IBGE CNEFE, Geospatial, and latitude/longitude.


  PontoFato''s developer surface includes authentication, getting-started guide, pricing, support, and 21 more developer resources.'
plans:
- name: Pontofato Plans Pricing
  plan_count: 3
  slug: pontofato-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Pontofato Rate Limits
  slug: pontofato-rate-limits
score:
  band: developing
  composite: 49.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.8
  facets:
    access_clarity: 57.9
    contract_governance: 18.2
    contract_quality: 49.8
    developer_ergonomics: 38.7
    discoverability: 75.9
    operational_transparency: 26.3
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: rising
  upsert:
    applies: true
    score: 0.0
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
- Geospatial
- latitude/longitude
- CNPJ
- Receita Federal
- Business Registry
- Location Intelligence
- proximity search
- radius search
- Open Government Data
- agent-native
- MCP
- x402-micropayments
website: https://pontofato.com/
---
