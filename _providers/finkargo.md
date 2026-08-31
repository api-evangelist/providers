---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finkargo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.finkargo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.finkargo.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://app.finkargo.com.co/auth/signup
- group: start
  title: ''
  type: Login
  url: https://app.finkargo.com.co/auth/login
- group: operate
  title: ''
  type: Support
  url: https://docs.google.com/forms/d/e/1FAIpQLSd3ZIYsNEnMDa7rRWDs1ZfX9egMI9Izx-jFX5lx4JZZzgSMhA/viewform
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.finkargo.com/termsandconditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.finkargo.com/politicas_privacidad/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/finkargo
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/finkargo-llms.txt
created: '2026-07-17'
description: Finkargo is a Latin American foreign-trade commerce platform that helps importers overcome the operational and financial barriers to growing their import businesses. Its product suite spans Paga (alternative supplier financing with revolving USD credit lines and 30-150 day terms), Analiza (market-intelligence dashboards that turn trade data into strategic decisions), Verifica (global supplier verification for product quality and legitimacy), and Protege (warehouse-to-warehouse cargo insurance). Operating across Colombia and Mexico and backed by QED Investors, Finkargo digitizes the full import-operations lifecycle from evaluating suppliers and planning imports to financing, transport, and arrival. Finkargo does not currently publish a public developer API or OpenAPI specification; this profile captures the company's public product, legal, and security surfaces.
image: https://static.finkargo.com/finkargo/favicon.ico
layout: provider
modified: '2026-07-19'
name: Finkargo
nav: Providers
network: true
overview: 'Finkargo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Trade Finance, Supply Chain, and Import Financing.


  Finkargo''s developer surface includes engineering blog, signup flow, support, and 7 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 12.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/finkargo/refs/heads/main/screenshots/finkargo-2026-07-25T214525.png
security:
- kind: domain-security
  name: Finkargo Domain Security
  slug: finkargo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: finkargo
tags:
- Company
- Fintech
- Trade Finance
- Supply Chain
- Import Financing
- Working Capital
- Latin America
- Insurance
website: https://www.finkargo.com/
---
