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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Private platform API powering the Tem RED utility application. Served from an AWS API Gateway at api.tem.energy and gated behind OIDC authentication; no public OpenAPI, SDK, or developer documentation
  name: Tem RED Platform API
  slug: tem-red-platform-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tem-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tem.energy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tem.energy
- group: operate
  title: ''
  type: Support
  url: https://tem.energy/get-in-touch
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tem.energy/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tem.energy/terms-of-use
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tem-energy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tem-energy/
created: '2026-07-17'
description: Tem (Tem-Energy Limited) is a UK-based energy technology company building AI-native transaction infrastructure for a modern energy market. Its RED platform is a modern utility that removes wholesale market markups to cut business electricity costs by up to 30%, provides transparent line-by-line billing from half-hourly meter data, and gives generators fairer earnings with renewable-energy traceability across 6,000+ sites. Backed by a February 2026 GBP 55M Series B led by Lightspeed Venture Partners. The customer-facing platform runs at app.tem.energy behind an OIDC login; the platform API at api.tem.energy is a private AWS API Gateway with no publicly documented developer surface at the time of profiling.
image: https://app.tem.energy/assets/images/tem-symbol-orange.png
layout: provider
modified: '2026-07-21'
name: Tem
nav: Providers
network: true
overview: 'Tem publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Electricity, Utilities, and Sustainability.


  Tem''s developer surface includes support and 7 more developer resources.'
random_paper: 80
score:
  band: emerging
  composite: 15.3
  delta: -1.8
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 17.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Tem Domain Security
  slug: tem-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tem
tags:
- Company
- Energy
- Electricity
- Utilities
- Sustainability
- Renewable Energy
- Fintech
- Infrastructure
- United Kingdom
website: https://tem.energy
---
