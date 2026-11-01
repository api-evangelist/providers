---
agent_readiness:
  band: human-only
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: The Aible API server (self-reported version 2.0.0) is the control plane behind the Aible platform. Its published route index lists 394 routes under the /v1 prefix across 29 modules — account, project,
  name: Aible API
  slug: aible-api
artifact_total: 5
common:
- group: operate
  href: https://artifacts.apis.io/aible/lifecycle/aible-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/aible-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/aible/hosts/aible-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aible-hosts.yml
- group: build
  href: https://artifacts.apis.io/aible/integrations/aible-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/aible-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/aible/vendors/aible-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aible-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.aible.com/security/
- group: company
  title: ''
  type: Newsroom
  url: https://www.aible.com/news
- group: auth
  href: https://artifacts.apis.io/aible/security/aible-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aible-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aible.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.iamaible.com/
- group: operate
  title: ''
  type: Support
  url: https://www.aible.com/partner_support
- group: start
  title: ''
  type: Login
  url: https://www.iamaible.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/marketplace/pp/prodview-77t5fm3cysegw
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aible.com/aible-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aible.com/privacy-policy
- group: operate
  href: https://artifacts.apis.io/aible/changelog/aible-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aible-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/aible/plans/aible-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aible-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/aible/rate-limits/aible-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aible-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/aible/authentication/aible-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aible-authentication.yml
- group: design
  href: https://artifacts.apis.io/aible/conventions/aible-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aible-conventions.yml
- group: design
  href: https://artifacts.apis.io/aible/data-model/aible-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aible-data-model.yml
- group: design
  href: https://artifacts.apis.io/aible/lifecycle/aible-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aible-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/aible/conformance/aible-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aible-conformance.yml
coverage:
  checked: '2026-10-20'
  detail: api.iamaible.com serves only a plain-text route index (394 routes) with no methods or schemas, and every conventional OpenAPI/Swagger path on it returns 404, so no contract can be read or generated.
  evidence:
  - status: 404
    url: https://api.iamaible.com/openapi.json
  - status: 404
    url: https://api.iamaible.com/swagger.json
  - status: 404
    url: https://www.aible.com/llms.txt
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-14'
description: Aible is an enterprise AI company founded in 2018 and headquartered in Pleasanton, California, that lets business users build and run AI agents, AutoML models and generative-AI analytics against data that stays inside the customer's own AWS, Azure, GCP or on-premise account. The platform is organized around projects, segments, scenarios, training data, jobs, models, deployments and content-generation collections, and is operated through a public REST API served at api.iamaible.com. That API server publishes its own route index — 394 routes across 29 modules at /v1, protected by bearer user, tenant and STS tokens — but Aible ships no OpenAPI, AsyncAPI, MCP server, agent card, SDK or public developer portal. Commercial access is sold as prepaid Flex Credits through the AWS and Google Cloud marketplaces.
image: https://www.aible.com/hubfs/Aible_Corp_Logo_Orange_White.svg
layout: provider
modified: '2026-09-14'
name: Aible
nav: Providers
network: true
overview: 'Aible is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Machine Learning, AutoML, Analytics, and Data Science.


  Aible''s developer surface includes API reference, support, pricing, changelog, authentication, and 17 more developer resources.'
plans:
- name: Aible Plans Pricing
  plan_count: 4
  slug: aible-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Aible Rate Limits
  slug: aible-rate-limits
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 67.9
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 32.5
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aible/aible-2026-10-11T093234.png
security:
- kind: authentication
  name: Aible Authentication
  slug: aible-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aible Domain Security
  slug: aible-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aible
tags:
- Artificial Intelligence
- Machine Learning
- AutoML
- Analytics
- Data Science
- AI Agents
- Generative AI
- Enterprise Software
- Cloud
- Company
website: https://www.aible.com/
---
