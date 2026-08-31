---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: 'The core API gateway behind the Redaptive ONE platform, serving the account, portfolio and building-insights surfaces of the ONE web application. Access is OAuth 2.0 protected: every path returns 401 '
  name: Redaptive ONE Core API
  slug: redaptive-one-core-api
- description: The Denali service behind the Redaptive ONE platform, serving the metering, consumption and sustainability-reporting surfaces of the ONE web application. OAuth 2.0 protected; anonymous requests to eve
  name: Redaptive ONE Denali API
  slug: redaptive-one-denali-api
- description: 'The API Redaptive licenses to Data Solutions customers, alongside an optional SDK, for programmatic access to metered energy, gas and water usage data. Its existence, its API-key credential model and '
  name: Redaptive Data Solutions API
  slug: redaptive-data-solutions-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redaptive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://redaptive.com/
- group: company
  title: ''
  type: Blog
  url: https://redaptive.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://redaptive.my.site.com/Redaptivecustomersupport/s/cs
- group: start
  title: ''
  type: Login
  url: https://one.redaptive.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://redaptive.com/platform-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://redaptive.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/redaptiveinc
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/redaptive-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/redaptive-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/redaptive-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/redaptive-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/redaptive-lifecycle.yml
coverage:
  checked: '2026-08-05'
  detail: Redaptive's own Data Solutions Terms and Conditions define an API, an SDK and developer documentation that Redaptive "may make available from time to time" to contracted customers, and all three production backends behind the Redaptive ONE app (core, denali, data-browser) answer anonymous requests with a bare 401 or 404 — the only document reachable without a Redaptive-issued API key is the OAuth authorization-server metadata at the core gateway.
  evidence:
  - status: 401
    url: https://core.api.prod.redaptivegroup.com/api/core/v1
  - status: 401
    url: https://denali-api.redaptive.com/api/denali
  - status: 200
    url: https://core.api.prod.redaptivegroup.com/.well-known/oauth-authorization-server
  - status: 200
    url: https://redaptive.com/data-solutions-terms-and-conditions/
  reason: customer-only-docs
  state: gated
created: '2026-08-05'
description: Redaptive is an energy infrastructure modernization company that funds, installs, and measures energy-saving and energy-generating equipment across large multi-site commercial, industrial, healthcare and real-estate portfolios under an Efficiency-as-a-Service and Energy-as-a-Service model, so customers modernize lighting, HVAC, refrigeration, solar and EV infrastructure without capital expenditure. Its Redaptive ONE platform meters electricity, gas and water at the asset level and turns that telemetry into portfolio consumption, sustainability benchmarking and ESG reporting. Redaptive contracts an API and an SDK to Data Solutions customers under published terms, but the reference and specification are not public.
image: https://redaptive.com/wp-content/uploads/2025/09/LI-Corp-Header-and-profile-2.png
layout: provider
modified: '2026-08-05'
name: Redaptive
nav: Providers
network: true
overview: 'Redaptive publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Energy Efficiency, Energy as a Service, and Sustainability.


  Redaptive''s developer surface includes engineering blog, support, authentication, and 10 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 20.5
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Redaptive Authentication
  slug: redaptive-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Redaptive Domain Security
  slug: redaptive-domain-security
  summary_line: TLSv1.3 · DMARC
slug: redaptive
tags:
- Company
- Energy
- Energy Efficiency
- Energy as a Service
- Sustainability
- ESG Reporting
- Metering
- Buildings
- Real-Estate
- Industrial
- Climate Tech
website: https://redaptive.com/
---
