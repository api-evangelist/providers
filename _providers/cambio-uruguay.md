---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.4
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: First-party MCP server for AI agents, shipped both as a hosted anonymous Streamable HTTP endpoint and as the npx-runnable npm package cambio-uruguay-mcp. Seven read-only tools — rates, best house, con
  name: Cambio Uruguay MCP Server
  slug: cambio-uruguay-mcp-server
- baseURL: https://api.cambio-uruguay.com
  baseurl_source: declared
  description: 'Guía de problemas con la aduana uruguaya: hechos legales citados, procedimientos y testimonios de r/uruguay'
  name: Cambio Uruguay Aduana API
  slug: cambio-uruguay-aduana-api
- baseURL: https://api.cambio-uruguay.com
  baseurl_source: declared
  description: Endpoints de inteligencia artificial para análisis de mercado y generación de insights
  name: Cambio Uruguay AI Insights API
  slug: cambio-uruguay-ai-insights-api
- baseURL: https://api.cambio-uruguay.com
  baseurl_source: declared
  description: The Banks API from Cambio Uruguay — 1 operation(s) for banks.
  name: Cambio Uruguay Banks API
  slug: cambio-uruguay-banks-api
- baseURL: https://api.cambio-uruguay.com
  baseurl_source: declared
  description: Endpoints para datos del Banco Central del Uruguay
  name: Cambio Uruguay BCU API
  slug: cambio-uruguay-bcu-api
- baseURL: https://api.cambio-uruguay.com
  baseurl_source: declared
  description: Endpoints de depuración para monitorear el estado interno del servicio
  name: Cambio Uruguay Debug API
  slug: cambio-uruguay-debug-api
- baseURL: https://api.cambio-uruguay.com
  baseurl_source: declared
  description: Endpoints para datos históricos y evolución de monedas
  name: Cambio Uruguay Evolution API
  slug: cambio-uruguay-evolution-api
- baseURL: https://api.cambio-uruguay.com
  baseurl_source: declared
  description: Endpoints para obtener datos de tipos de cambio
  name: Cambio Uruguay Exchange Data API
  slug: cambio-uruguay-exchange-data-api
- baseURL: https://api.cambio-uruguay.com
  baseurl_source: declared
  description: Endpoints para servicios de geocodificación
  name: Cambio Uruguay Geocoding API
  slug: cambio-uruguay-geocoding-api
- baseURL: https://api.cambio-uruguay.com
  baseurl_source: declared
  description: Endpoints para verificar el estado del servicio
  name: Cambio Uruguay Health API
  slug: cambio-uruguay-health-api
- baseURL: https://api.cambio-uruguay.com
  baseurl_source: declared
  description: The Indicators API from Cambio Uruguay — 7 operation(s) for indicators.
  name: Cambio Uruguay Indicators API
  slug: cambio-uruguay-indicators-api
- baseURL: https://api.cambio-uruguay.com
  baseurl_source: declared
  description: Endpoints para obtener información de ubicaciones
  name: Cambio Uruguay Locations API
  slug: cambio-uruguay-locations-api
- baseURL: https://api.cambio-uruguay.com
  baseurl_source: declared
  description: Endpoints para obtener parámetros válidos del sistema
  name: Cambio Uruguay Parameters API
  slug: cambio-uruguay-parameters-api
- baseURL: https://api.cambio-uruguay.com
  baseurl_source: declared
  description: 'Cotizaciones de la región: el dólar y los cruces en Argentina, Brasil, Paraguay, Chile, Bolivia y Uruguay, con series diarias y comparación de rutas'
  name: Cambio Uruguay Regional API
  slug: cambio-uruguay-regional-api
artifact_total: 21
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-uruguay/refs/heads/main/overlays/cambio-uruguay-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cambio-uruguay-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://cambio-uruguay.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.cambio-uruguay.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.cambio-uruguay.com/api-docs
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/eduair94/cambio-uruguay
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cambio-uruguay.com/terminos
- group: operate
  title: ''
  type: Support
  url: https://cambio-uruguay.com/preguntas-frecuentes
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cambio-uruguay/refs/heads/main/llms/cambio-uruguay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cambio-uruguay-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cambio-uruguay/refs/heads/main/mcp/cambio-uruguay-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cambio-uruguay-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cambio-uruguay/refs/heads/main/well-known/cambio-uruguay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cambio-uruguay-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cambio-uruguay/refs/heads/main/well-known/cambio-uruguay-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cambio-uruguay-security.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cambio-uruguay/refs/heads/main/packages/cambio-uruguay-packages.yml
  title: ''
  type: Packages
  url: packages/cambio-uruguay-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cambio-uruguay/refs/heads/main/authentication/cambio-uruguay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cambio-uruguay-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cambio-uruguay/refs/heads/main/conventions/cambio-uruguay-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cambio-uruguay-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cambio-uruguay/refs/heads/main/conformance/cambio-uruguay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cambio-uruguay-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cambio-uruguay/refs/heads/main/lifecycle/cambio-uruguay-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cambio-uruguay-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cambio-uruguay/refs/heads/main/security/cambio-uruguay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cambio-uruguay-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cambio-uruguay/refs/heads/main/security/cambio-uruguay-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cambio-uruguay-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cambio-uruguay/refs/heads/main/security/cambio-uruguay-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cambio-uruguay-vulnerability-disclosure.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cambio-uruguay/refs/heads/main/rate-limits/cambio-uruguay-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cambio-uruguay-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cambio-uruguay/refs/heads/main/plans/cambio-uruguay-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cambio-uruguay-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cambio-uruguay/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-07'
description: Uruguayan currency exchange-rate comparison API covering 40+ casas de cambio and banks, refreshed roughly every 10 minutes from Banco Central del Uruguay-registered sources. Public keyless JSON — no registration, no API key — with current buy/sell quotes, best-house comparison, six-month historical series, branch locations with geocoding, BCU reference rates, and economic indicators, plus a hosted anonymous Streamable HTTP MCP server and an npx-runnable stdio package for AI agents. Open source (MIT) by Eduardo Airaudo.
image: https://cambio-uruguay.com/__og-image__/image/og.png
layout: provider
mcp_servers:
- description: ''
  name: Cambio Uruguay MCP Server
  slug: cambio-uruguay-mcp-server
- description: ''
  name: Cambio Uruguay MCP Server
  slug: cambio-uruguay-mcp-server-2
modified: '2026-09-07'
name: Cambio Uruguay
nav: Providers
network: true
overview: 'Cambio Uruguay publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Aduana API, AI Insights API, Banks API, and 10 more. Tagged areas include Currency, Exchange Rates, Finance, Uruguay, and Latin America.


  Cambio Uruguay''s developer surface includes documentation, API reference, support, authentication, and 18 more developer resources.'
plans:
- name: Cambio Uruguay Plans Pricing
  plan_count: 1
  slug: cambio-uruguay-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Cambio Uruguay Rate Limits
  slug: cambio-uruguay-rate-limits
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.6
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 49.0
    developer_ergonomics: 35.1
    discoverability: 75.9
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 29.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Cambio Uruguay Authentication
  slug: cambio-uruguay-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cambio Uruguay Domain Security
  slug: cambio-uruguay-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Cambio Uruguay Vulnerability Disclosure
  slug: cambio-uruguay-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: cambio-uruguay
tags:
- Currency
- Exchange Rates
- Finance
- Uruguay
- Latin America
- MCP
- agent-native
- Open-Source
website: https://cambio-uruguay.com
---
