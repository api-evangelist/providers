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
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-09-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Granular Agentic Access
  operation_count: 7
  slug: granular-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: Granular Insights provides analytics and reporting APIs for farm operations, enabling agronomic analysis, yield benchmarking, and field performance reporting for precision agriculture workflows.
  name: Granular Insights API
  slug: granular-insights-api
- baseURL: https://api.granular.ag
  baseurl_source: declared
  description: Field activities — planting, application, harvest
  name: Granular (Corteva Agriscience) Activities API
  slug: granular-activities-api
- baseURL: https://api.granular.ag
  baseurl_source: declared
  description: Crop plans and variety information
  name: Granular (Corteva Agriscience) Crops API
  slug: granular-crops-api
- baseURL: https://api.granular.ag
  baseurl_source: declared
  description: Farm entity management
  name: Granular (Corteva Agriscience) Farms API
  slug: granular-farms-api
- baseURL: https://api.granular.ag
  baseurl_source: declared
  description: Field boundary and attribute management
  name: Granular (Corteva Agriscience) Fields API
  slug: granular-fields-api
- baseURL: https://api.granular.ag
  baseurl_source: declared
  description: Farm financial records and cost tracking
  name: Granular (Corteva Agriscience) Financials API
  slug: granular-financials-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Granular Farm Management Activities API
  slug: open-granular-activities-api
- collection_type: open
  name: Granular Farm Management Activities Crops API
  slug: open-granular-crops-api
- collection_type: open
  name: Granular Farm Management API
  slug: open-granular-farm-management
- collection_type: open
  name: Granular Farm Management Activities Farms API
  slug: open-granular-farms-api
- collection_type: open
  name: Granular Farm Management Activities Fields API
  slug: open-granular-fields-api
- collection_type: open
  name: Granular Farm Management Activities Financials API
  slug: open-granular-financials-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/granular/refs/heads/main/capabilities/granular-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/granular-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/granular/refs/heads/main/agentic-access/granular-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/granular-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/granular/refs/heads/main/security/granular-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/granular-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/granular/refs/heads/main/authentication/granular-authentication.yml
  title: ''
  type: Authentication
  url: authentication/granular-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/granular/refs/heads/main/scopes/granular-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/granular-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/granular/refs/heads/main/lifecycle/granular-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/granular-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/granular/refs/heads/main/conformance/granular-conformance.yml
  title: ''
  type: Conformance
  url: conformance/granular-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/granular/refs/heads/main/packages/granular-packages.yml
  title: ''
  type: Packages
  url: packages/granular-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/granular/refs/heads/main/plans/granular-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/granular-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/granular/refs/heads/main/rate-limits/granular-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/granular-rate-limits.yml
- group: operate
  title: ''
  type: Support
  url: https://support.insights.granular.ag/hc/en-us
- group: company
  title: ''
  type: Website
  url: https://granular.ag/
- group: start
  title: ''
  type: Portal
  url: https://us.app.granular.ag/
coverage:
  checked: '2026-09-12'
  detail: Granular Insights runs a real Kong API gateway at us.insights.granular.ag whose /api routes answer '{"message":"no Route matched with those values"}' to an unauthenticated caller, but there is no developer portal, no API reference and no spec anywhere public — every Granular surface redirects into a tenant sign-in, and the api.granular.ag host this record has always carried has no DNS record at all.
  evidence:
  - status: 404
    url: https://us.insights.granular.ag/api
  - status: 301
    url: https://granular.ag/
  - status: 0
    url: https://api.granular.ag/
  - status: 403
    url: https://us.app.granular.ag/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-04-28'
description: Granular is a farm management platform now part of Corteva Agriscience, providing APIs for crop planning, field records management, financial analysis, and farm operational tracking. The platform serves commercial agriculture operations with data-driven decision support tools.
finops:
- name: Granular Finops
  service_category: API
  slug: granular-finops
json_schemas:
- name: Granular Farm Field
  property_count: 15
  slug: granular-field
jsonld:
- class_count: 9
  name: Granular Context
  property_count: 16
  slug: granular-context
layout: provider
modified: '2026-09-12'
name: Granular (Corteva Agriscience)
nav: Providers
network: true
overview: 'Granular (Corteva Agriscience) publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Crops API, Farms API, and 2 more. Tagged areas include Agriculture, Farm Management, Financial, Crop Planning, and Agronomy.


  The Granular (Corteva Agriscience) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Granular (Corteva Agriscience)''s developer surface includes authentication, support, developer portal, and 10 more developer resources.'
plans:
- name: Granular Plans Pricing
  plan_count: 0
  slug: granular-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Granular Rate Limits
  slug: granular-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Granular (Corteva Agriscience) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: granular-jsonschema-spectral-rules
scopes:
- name: Granular Scopes
  scope_count: 2
  slug: granular-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.3
    catalog_earned_first_party: 0.0
    catalog_gap: 62.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 28.0
    contract_quality: 59.6
    developer_ergonomics: 26.2
    discoverability: 64.8
    operational_transparency: 0.0
  previous_composite: 31.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/granular/refs/heads/main/screenshots/granular-2026-06-20T182321.png
security:
- kind: authentication
  name: Granular Authentication
  slug: granular-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Granular Domain Security
  slug: granular-domain-security
  summary_line: TLSv1.3 · DMARC
slug: granular
tags:
- Agriculture
- Farm Management
- Financial
- Crop Planning
- Agronomy
website: https://granular.ag/
---
