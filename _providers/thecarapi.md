---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-02'
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
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/thecarapi-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/thecarapi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/thecarapi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/thecarapi-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://thecarapi.com/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://thecarapi.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/thecarapi-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/thecarapi-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://thecarapi.com/pricing
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/thecarapi-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/thecarapi-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/thecarapi-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: https://thecarapi.com/docs/code-examples
- group: build
  title: ''
  type: Examples
  url: examples/thecarapi-examples.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/thecarapi-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/thecarapi-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://thecarapi.com/llms.txt
- group: build
  title: ''
  type: Postman
  url: https://thecarapi.com/thecarapi.postman_collection.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://thecarapi.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://thecarapi.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://thecarapi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://thecarapi.com/docs/thecarapi-api-reference.md
- group: operate
  title: ''
  type: Support
  url: https://thecarapi.com/contact
- group: company
  title: ''
  type: Blog
  url: https://thecarapi.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thecarapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thecarapi.com/privacy
created: '2026-09-01'
description: A multi-source vehicle auction inventory REST/JSON API aggregating live and archived auction listings and European retail classifieds. Provides search, facets, catalog, auction detail & price history, VIN history, market intelligence, and import cost calculators. Fully specified via OpenAPI 3.1 with Postman collection and agent-native documentation (llms.txt).
image: https://thecarapi.com/og-image.png
layout: provider
modified: '2026-09-02'
name: TheCarApi
nav: Providers
network: true
overview: 'TheCarApi publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Automotive, Vehicle Data, Car Auctions, Used Cars, and Vehicle Inventory.


  TheCarApi''s developer surface includes authentication, changelog, pricing, code examples, documentation, getting-started guide, API reference, and 22 more developer resources.'
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
  band: developing
  composite: 52.2
  coverage:
    artifact_dirs: 22
    catalog_gap: 52.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 21.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 8.3
    contract_quality: 40.0
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 8.3
    operational_transparency: 63.2
  previous_composite: 31.2
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
  scored_at: '2026-09-02'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/thecarapi/refs/heads/main/screenshots/thecarapi-2026-09-02T163425.png
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
website: https://thecarapi.com/docs
---
