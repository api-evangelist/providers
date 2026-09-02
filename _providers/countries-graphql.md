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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-01'
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
  composite: 18.7
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 31.9
    developer_ergonomics: 9.5
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 18.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Language
- Continents
website: https://countries.trevorblades.com
---
