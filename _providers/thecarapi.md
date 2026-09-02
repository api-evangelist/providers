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
  score: 18.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST/JSON API for multi-source vehicle auction inventory, search, facets, auction detail and price history, VIN history, market intel, classifieds, and import cost calculation. API key required for li
  name: TheCarApi REST API
  slug: thecarapi-rest-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thecarapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thecarapi-authentication.yml
created: '2026-09-01'
description: A multi-source vehicle auction inventory REST/JSON API aggregating live and archived auction listings and European retail classifieds. Provides search, facets, catalog, auction detail & price history, VIN history, market intelligence, and import cost calculators. Fully specified via OpenAPI 3.1 with Postman collection and agent-native documentation (llms.txt).
layout: provider
modified: '2026-09-01'
name: TheCarApi
nav: Providers
network: true
overview: 'TheCarApi publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Automotive, Vehicle Data, Car Auctions, Used Cars, and Vehicle Inventory.


  TheCarApi''s developer surface includes authentication and 1 more developer resources.'
plans:
- name: Thecarapi Plans Pricing
  plan_count: 3
  slug: thecarapi-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Thecarapi Rate Limits
  slug: thecarapi-rate-limits
scopes:
- name: Thecarapi Scopes
  scope_count: 0
  slug: thecarapi-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 21
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 33.3
    developer_ergonomics: 26.2
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
security:
- kind: authentication
  name: Thecarapi Authentication
  slug: thecarapi-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Thecarapi Domain Security
  slug: thecarapi-domain-security
  summary_line: TLSv1.3
slug: thecarapi
tags:
- Automotive
- Vehicle Data
- Car Auctions
- Used Cars
- Vehicle Inventory
- Classifieds
- Market Intelligence
- Pricing
- VIN
- Image CDN
- Europe
- Korea
- Japan Auctions
---
