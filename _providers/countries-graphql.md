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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: A public, free GraphQL endpoint that exposes queryable fields for countries, continents, and languages. Countries can be filtered by code, currency, or continent, and each country record includes fiel
  name: Countries GraphQL API GraphQL API
  slug: graphql-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/countries-graphql-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://countries.trevorblades.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/trevorblades/countries
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/in/trevorblades/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trevorblades
- group: commercial
  title: ''
  type: Pricing
  url: https://github.com/trevorblades/countries#readme
- group: commercial
  title: ''
  type: Plans
  url: plans/countries-graphql-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/countries-graphql-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/countries-graphql-finops.md
created: 2026-06-14
description: Countries GraphQL API is a free, public GraphQL API that provides structured information about countries, continents, and languages around the world. Created by Trevor Blades, it draws from the Countries List dataset and the provinces npm package, returning data such as capital cities, currencies, languages, and AWS region mappings for every country.
graphqls:
- description: A free, public GraphQL API exposing queryable data about countries, continents, and languages worldwide. No authentication is required. The schema centers on three core object types — Country, Contine
  name: Countries GraphQL API GraphQL API
  slug: countries-graphql-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/countries-graphql.png
layout: provider
modified: 2026-06-14
name: Countries GraphQL API
nav: Providers
network: true
overview: 'Countries GraphQL API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, Countries, Geography, Open Data, and Free.


  Countries GraphQL API''s developer surface includes documentation, pricing, and 7 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 19.0
  delta: -0.8
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 33.3
    developer_ergonomics: 9.5
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 19.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/countries-graphql/refs/heads/main/screenshots/countries-graphql-2026-06-20T175102.png
security:
- kind: domain-security
  name: Countries Graphql Domain Security
  slug: countries-graphql-domain-security
  summary_line: TLSv1.3
slug: countries-graphql
tags:
- GraphQL
- Countries
- Geography
- Open Data
- Free
- Languages
- Continents
website: https://countries.trevorblades.com
---
