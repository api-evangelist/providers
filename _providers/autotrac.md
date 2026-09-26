---
access_model:
  confidence: high
  label: Contact Sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.autotrac.com.br/produtos-para-voce/embarcadores/
  - https://www.autotrac.com.br/solucoes/solucao-mercado-segurador/
  - https://www.autotrac.com.br/fale-com-a-gente/
  - https://www.autotrac.com.br/sitemap_index.xml
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-25'
api_count: 4
apis:
- description: 'The AutoTrac Supervisor Web platform provides fleet management capabilities for monitoring vehicle locations, managing fleet operations, generating reports, and coordinating driver assignments across '
  name: AutoTrac Supervisor Web API
  slug: supervisor-web-api
- description: The AutoTrac Telemetria platform provides real-time vehicle telemetry data including speed, fuel consumption, engine diagnostics, tire pressure, temperature sensors (for refrigerated cargo), and drive
  name: AutoTrac Telemetria API
  slug: telemetria-api
- description: The AutoTrac Jornada platform manages driver journey logs and compliance with Brazilian driving hour regulations, tracking driving time, rest periods, and journey records for long-distance transport c
  name: AutoTrac Jornada Driver Journey API
  slug: jornada-api
- description: The "Serviço API de integração" is the one product AutoTrac markets as an API. For shippers (embarcadores) it feeds a control tower with real-time information on the carriers serving the company — log
  name: AutoTrac Serviço API de Integração
  slug: integration-api
artifact_total: 21
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autotrac/refs/heads/main/security/autotrac-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autotrac-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.autotrac.com.br
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/autotrac/refs/heads/main/plans/autotrac-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/autotrac-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/autotrac/refs/heads/main/rate-limits/autotrac-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/autotrac-rate-limits.yml
- group: operate
  title: ''
  type: Support
  url: https://www.autotrac.com.br/fale-com-a-gente/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.autotrac.com.br/fale-com-a-gente/perguntas-frequentes/
- group: company
  title: ''
  type: Blog
  url: https://www.autotrac.com.br/noticias/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.autotrac.com.br/politica-de-privacidade/
- group: start
  title: ''
  type: Login
  url: https://www.autotrac-online.com.br/supervisor/Pages/login.aspx
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/meuautotrac
- group: company
  title: ''
  type: About
  url: https://www.autotrac.com.br/por-que-autotrac/conheca-a-autotrac/
coverage:
  checked: '2026-09-18'
  detail: AutoTrac markets a "Serviço API de integração" on its shipper and insurer product pages but publishes no developer page, reference, spec or pricing anywhere in its 745-URL sitemap — every developer path on www.autotrac.com.br 404s, the application host www.autotrac-online.com.br redirects every path to the Supervisor customer login, and third-party integrators describe credentials and IP allow-listing issued by AutoTrac per contract.
  evidence:
  - status: 200
    url: https://www.autotrac.com.br/produtos-para-voce/embarcadores/
  - status: 404
    url: https://www.autotrac.com.br/developers
  - status: 404
    url: https://www.autotrac.com.br/api
  - status: 302
    url: https://www.autotrac-online.com.br/api
  - status: 404
    url: https://www.autotrac.com.br/openapi.json
  - status: 404
    url: https://www.autotrac.com.br/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2024-01-01'
description: AutoTrac is a Brazilian fleet management and vehicle tracking technology company with over 30 years of experience. As the national market leader, AutoTrac provides satellite and cellular fleet tracking solutions, real-time telemetry, driver journey management, and management intelligence platforms for logistics, agriculture, maritime, and insurance sectors. The company operates its own terrestrial satellite communication station and data center for nationwide coverage.
features:
- description: AutoTrac operates its own terrestrial satellite communication station and integrated data center, providing coverage in areas with limited cellular connectivity across Brazil.
  name: Proprietary Satellite Communication
- description: Real-time monitoring of vehicle parameters including location, speed, fuel consumption, engine diagnostics, and cargo temperature for refrigerated transport.
  name: Real-Time Vehicle Telemetry
- description: Jornada platform for tracking driver hours, rest periods, and journey compliance with Brazilian transportation regulations.
  name: Driver Journey Management
- description: Informacoes Gerenciais business intelligence dashboards for fleet performance analytics, cost analysis, and operational reporting.
  name: Fleet Intelligence Reporting
- description: Specialized tracking solutions for agricultural machinery including harvesters, tractors, and implements with field operation monitoring.
  name: Agricultural Equipment Tracking
finops:
- name: Autotrac Finops
  service_category: API
  slug: autotrac-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/autotrac.png
integrations:
- description: Integration with transportation management systems for freight dispatch, route optimization, and delivery confirmation workflows.
  name: TMS Systems
- description: Connect AutoTrac fleet data with ERP systems (SAP, TOTVS) for fleet cost accounting, maintenance scheduling, and asset management.
  name: ERP Systems
- description: API integration with insurance carriers for vehicle recovery, claims verification, and telematics-based premium calculation.
  name: Insurance Platforms
layout: provider
modified: '2026-09-18'
name: AutoTrac
nav: Providers
network: true
overview: 'AutoTrac publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fleet Management, GPS Tracking, Telematics, Vehicle Tracking, and Logistics.


  AutoTrac''s developer surface includes support, engineering blog, and 9 more developer resources.'
plans:
- name: Autotrac Plans Pricing
  plan_count: 0
  slug: autotrac-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Autotrac Rate Limits
  slug: autotrac-rate-limits
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 25.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 62.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 11.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 8.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/autotrac/refs/heads/main/screenshots/autotrac-2026-06-20T172710.png
security:
- kind: domain-security
  name: Autotrac Domain Security
  slug: autotrac-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: autotrac
tags:
- Fleet Management
- GPS Tracking
- Telematics
- Vehicle Tracking
- Logistics
- Brazil
- Satellite Communication
- Insurance Telematics
- Supply Chain Visibility
use_cases:
- description: Track trucks and cargo across Brazil using satellite and cellular communication for nationwide visibility of logistics operations.
  name: Long-Distance Logistics Tracking
- description: Monitor temperature-controlled cargo transport with real-time telemetry alerts for temperature deviations in refrigerated vehicles.
  name: Refrigerated Cargo Monitoring
- description: Ensure compliance with Brazilian driver hour regulations by tracking journey logs and rest periods automatically via Jornada.
  name: Driver Compliance Management
- description: Track agricultural equipment, monitor field operations, and manage harvest logistics for agribusiness operations.
  name: Agricultural Fleet Management
- description: Provide vehicle behavior and location data to insurance companies for usage-based insurance and stolen vehicle recovery programs.
  name: Insurance Telematics
website: https://www.autotrac.com.br
---
