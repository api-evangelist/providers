---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.7
  scored_at: '2026-09-12'
api_count: 1
apis:
- baseURL: https://api.aoxlabs.com
  baseurl_source: declared
  description: The REST API behind AOX, ADRO's aerodynamic optimization platform. A Django REST Framework backend serving a public, machine-readable OpenAPI 3.0.3 document (drf-spectacular) with 231 operations acros
  name: AOX Platform API
  slug: aox-platform-api
- description: ADRO's US direct-to-consumer aero-parts storefront at adro.com is a Shopify store that publishes an agent-facing surface on ADRO's own domain — an llms.txt of agent instructions, a UCP merchant profil
  name: ADRO US Store Agent Commerce (UCP / MCP)
  slug: adro-us-store-agent-commerce-ucp-mcp
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://adro.com/
- group: company
  title: ''
  type: Website
  url: https://aoxlabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aoxlabs.com/product
- group: docs
  title: ''
  type: APIReference
  url: https://api.aoxlabs.com/swagger/
- group: commercial
  title: ''
  type: Pricing
  url: https://aoxlabs.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://aoxlabs.com/login
- group: start
  title: ''
  type: Login
  url: https://aoxlabs.com/login
- group: operate
  title: ''
  type: Support
  url: https://aoxlabs.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aoxlabs.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aoxlabs.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://adro.com/blogs/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://aoxlabs.com/board
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/adro1b33-aox-openapi.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/adro1b33-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adro1b33-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/adro1b33-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adro1b33-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adro1b33-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/adro1b33-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adro1b33-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adro1b33-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/adro1b33-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/adro1b33-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adro1b33-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/adro1b33-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adro1b33-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adro1b33-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/adro1b33-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/adro1b33-aox-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adro1b33-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/adro1b33-scopes.yml
created: '2026-09-07'
description: ADRO, Inc. (에이드로) is a South Korean mobility aerotech company in Yongin-si, Gyeonggi-do that designs and manufactures aerospace-grade carbon-fiber aerodynamic components for global automotive brands, and that has extended into software with AOX (Aerodynamic Optimization eXperience) — a web-based, GPU- and HPC-backed aerodynamic design and optimization platform operated at aoxlabs.com that takes a CAD or STL geometry through meshing, CFD simulation, shape optimization and post-processing without requiring CFD expertise. The AOX platform is backed by a public Django REST Framework contract at api.aoxlabs.com serving a 231-operation OpenAPI 3.0.3 document covering projects, jobs, LES runs, sketch sessions, patches, artifacts, assets, teams, credits, plans, subscriptions and payments. The company's US direct-to-consumer parts storefront at adro.com is a Shopify store that serves an agent-facing llms.txt and a live Universal Commerce Protocol (UCP) MCP endpoint.
image: https://aoxlabs.com/logos/AOX_Main_dark.png
layout: provider
mcp_servers:
- description: ''
  name: ADRO US Store — UCP Commerce MCP
  slug: adro-us-store-ucp-commerce-mcp
modified: '2026-09-07'
name: ADRO
nav: Providers
network: true
overview: 'ADRO publishes 1 API on the [APIs.io](https://apis.io/) network: AOX Platform API. Tagged areas include Aerodynamics, Computational Fluid Dynamics, Simulation, Automotive, and Engineering.


  ADRO''s developer surface includes documentation, API reference, pricing, signup flow, support, engineering blog, changelog, and 25 more developer resources.'
plans:
- name: Adro1B33 Plans Pricing
  plan_count: 5
  slug: adro1b33-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Adro1B33 Rate Limits
  slug: adro1b33-rate-limits
scopes:
- name: Adro1B33 Scopes
  scope_count: 0
  slug: adro1b33-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 37.0
    developer_ergonomics: 23.2
    discoverability: 75.9
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 30.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Adro1B33 Authentication
  slug: adro1b33-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Adro1B33 Domain Security
  slug: adro1b33-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Adro1B33 Trust Center
  slug: adro1b33-trust-center
  summary_line: ISO/IEC 27001:2022, TISAX
slug: adro1b33
tags:
- Aerodynamics
- Computational Fluid Dynamics
- Simulation
- Automotive
- Engineering
- Optimization
- Manufacturing
- Artificial Intelligence
- High Performance Computing
- Ecommerce
- MCP
- South Korea
website: https://adro.com/
---
