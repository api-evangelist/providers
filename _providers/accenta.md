---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The HTTP API behind Accenta's effiPilot building-energy platform. It is an RPC-style JSON surface — requests take the form /api/method/<methodName> — served per customer tenant from the wildcard accen
  name: effiPilot Platform API
  slug: effipilot-platform-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.accenta.ai/
- group: company
  title: ''
  type: WebsiteFrench
  url: https://www.accenta.ai/
- group: start
  title: ''
  type: Login
  url: https://app.accenta.ai/login/
- group: operate
  title: ''
  type: Support
  url: https://www.accenta.ai/en/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.accenta.ai/articles/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.accenta.ai/feed/
- group: company
  title: ''
  type: Press
  url: https://www.accenta.ai/en/press/
- group: other
  title: ''
  type: CaseStudies
  url: https://www.accenta.ai/en/projects/
- group: company
  title: ''
  type: About
  url: https://www.accenta.ai/en/about/
- group: company
  title: ''
  type: Careers
  url: https://www.accenta.ai/jobs/
- group: commercial
  title: ''
  type: LegalNotice
  url: https://www.accenta.ai/mentions-legales/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.accenta.ai/politique-de-confidentialite/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://storage.sbg.cloud.ovh.net/v1/AUTH_3d9cbc20c59c4c77a70475ce27cd4ecb/Images%20publiques%20effiPilot/Contrat_Licence_Utilisateur_Final_v200_20260602.pdf
- group: auth
  title: ''
  type: Compliance
  url: https://storage.sbg.cloud.ovh.net/v1/AUTH_3d9cbc20c59c4c77a70475ce27cd4ecb/Images%20publiques%20effiPilot/RGPD_Collecte_et_utilisation_donnees_personnelles_v200_20260602.pdf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/accenta-ai
- group: auth
  title: ''
  type: Authentication
  url: authentication/accenta-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/accenta-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/accenta-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/accenta-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/accenta-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/accenta-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/accenta-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/accenta-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accenta-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accenta-llms.txt
coverage:
  checked: '2026-08-17'
  detail: Accenta's effiPilot API reference is real and is Accenta's own — the login application at app.accenta.ai explicitly offers redirectTo=api%2Fdoc and search engines still index the page title "documentation API effiPilot 2.16.3" — but the /api/doc route is only served to an authenticated tenant session, so an anonymous GET returns {"message":"Route not found"} and no machine-readable contract of any kind (OpenAPI, GraphQL, MCP, AsyncAPI, agent card, or any /.well-known/ document) is reachable on www.accenta.ai, app.accenta.ai or demo.accenta.ai.
  evidence:
  - status: 404
    url: https://app.accenta.ai/api/doc
  - status: 200
    url: https://app.accenta.ai/api/method/brandConf
  - status: 301
    url: https://app.effipilot.com/api/doc/
  - status: 404
    url: https://app.accenta.ai/api/v3/api-docs
  - status: 404
    url: https://www.accenta.ai/.well-known/agent-card.json
  - status: 403
    url: https://app.accenta.ai/.well-known/security.txt
  reason: customer-only-docs
  state: gated
created: '2026-08-17'
description: Accenta is a French energy and carbon performance company for real estate portfolios, founded in 2016 and headquartered in Boulogne-Billancourt. It combines AI-driven building control (an intelligent building management system plus an Accenta Communication Box for sites with no BMS) with low-carbon heat and cold production built on shallow geothermal energy, inter-seasonal geostorage, heat pumps and solar, and it wraps the whole package in audit, design, build, operate, financing and performance-contract services. Accenta says it manages roughly 10 million square metres of real estate for owners such as Airbus, Prologis, Icade, Redevco and Decathlon, targeting energy reductions up to 80% and CO2 reductions up to 95%. Its software platform is effiPilot, acquired in 2020, delivered as a per-customer tenant on accenta.ai with a web application, an Android app and an HTTP API whose reference documentation sits behind the customer login.
image: https://www.accenta.ai/app/uploads/2020/09/og_fb.jpg
layout: provider
modified: '2026-08-17'
name: Accenta
nav: Providers
network: true
overview: 'Accenta publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Data, Energy, Buildings, and Smart Buildings.


  Accenta''s developer surface includes support, engineering blog, authentication, and 22 more developer resources.'
plans:
- name: Accenta Plans Pricing
  plan_count: 0
  slug: accenta-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Accenta Rate Limits
  slug: accenta-rate-limits
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 23.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 40.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Accenta Authentication
  slug: accenta-authentication
  summary_line: cookie-session · 1 scheme
- kind: domain-security
  name: Accenta Domain Security
  slug: accenta-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: accenta
tags:
- Company
- Ai Data
- Energy
- Buildings
- Smart Buildings
- Building Management
- Geothermal
- Decarbonization
- Sustainability
- Energy Management
- Artificial Intelligence
- Real-Estate
- IoT
- France
website: https://www.accenta.ai/
---
