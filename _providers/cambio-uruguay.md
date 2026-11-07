---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.1
  scored_at: '2026-11-06'
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
- baseURL: https://mcp.cambio-uruguay.com/mcp
  baseurl_source: declared
  description: The Precios API from Cambio Uruguay — 5 operation(s) for precios.
  name: Cambio Uruguay Precios API
  slug: cambio-uruguay-precios-api
artifact_total: 25
common:
- group: company
  title: ''
  type: Blog
  url: https://cambio-uruguay.com/blog
- group: other
  href: https://artifacts.apis.io/cambio-uruguay/overlays/cambio-uruguay-openapi-overlay.yaml
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
  href: https://artifacts.apis.io/cambio-uruguay/llms/cambio-uruguay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cambio-uruguay-llms.txt
- group: agent
  href: https://artifacts.apis.io/cambio-uruguay/mcp/cambio-uruguay-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cambio-uruguay-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cambio-uruguay/well-known/cambio-uruguay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cambio-uruguay-well-known.yml
- group: auth
  href: https://artifacts.apis.io/cambio-uruguay/well-known/cambio-uruguay-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cambio-uruguay-security.txt
- group: build
  href: https://artifacts.apis.io/cambio-uruguay/packages/cambio-uruguay-packages.yml
  title: ''
  type: Packages
  url: packages/cambio-uruguay-packages.yml
- group: auth
  href: https://artifacts.apis.io/cambio-uruguay/authentication/cambio-uruguay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cambio-uruguay-authentication.yml
- group: design
  href: https://artifacts.apis.io/cambio-uruguay/conventions/cambio-uruguay-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cambio-uruguay-conventions.yml
- group: design
  href: https://artifacts.apis.io/cambio-uruguay/conformance/cambio-uruguay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cambio-uruguay-conformance.yml
- group: design
  href: https://artifacts.apis.io/cambio-uruguay/lifecycle/cambio-uruguay-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cambio-uruguay-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/cambio-uruguay/security/cambio-uruguay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cambio-uruguay-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cambio-uruguay/security/cambio-uruguay-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cambio-uruguay-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cambio-uruguay/security/cambio-uruguay-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cambio-uruguay-vulnerability-disclosure.yml
- group: operate
  href: https://artifacts.apis.io/cambio-uruguay/rate-limits/cambio-uruguay-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cambio-uruguay-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cambio-uruguay/plans/cambio-uruguay-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cambio-uruguay-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/cambio-uruguay/skills/_index.yml
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
  slug: mcp
modified: '2026-10-06'
name: Cambio Uruguay
nav: Providers
network: true
overview: 'Cambio Uruguay publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Aduana API, AI Insights API, Banks API, and 12 more. Tagged areas include Currency, Exchange Rates, Finance, Uruguay, and Latin America.


  The Cambio Uruguay catalog on APIs.io includes 1 Spectral governance ruleset.


  Cambio Uruguay''s developer surface includes engineering blog, documentation, API reference, support, authentication, and 18 more developer resources.'
plans:
- name: Cambio Uruguay Plans Pricing
  plan_count: 1
  slug: cambio-uruguay-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Cambio Uruguay Rate Limits
  slug: cambio-uruguay-rate-limits
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Cambio Uruguay API Rules
  rule_count: 66
  severity_counts:
    error: 57
    hint: 0
    info: 1
    warn: 8
  slug: cambio-uruguay-rules
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 51.0
    developer_ergonomics: 37.5
    discoverability: 75.0
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - uruguay
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 38.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 51.9
      total: 27
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cambio-uruguay/cambio-uruguay-2026-10-11T102657.png
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
skill_count: 3
skills:
- name: cambio-uruguay-best-exchange-rate
  slug: cambio-uruguay-best-exchange-rate
- name: cambio-uruguay-currency-evolution
  slug: cambio-uruguay-currency-evolution
- name: cambio-uruguay-find-exchange-branches
  slug: cambio-uruguay-find-exchange-branches
slug: cambio-uruguay
tags:
- Currency
- Exchange Rates
- Finance
- Uruguay
- Latin America
- MCP
- Agent-Native
- Open Source
website: https://cambio-uruguay.com
---
