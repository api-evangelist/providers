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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 24.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Fitness Agentic Access
  operation_count: 9
  slug: google-fitness-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 1
apis:
- description: The Users API from Google Fit REST — 6 operation(s) for users.
  name: Google Fit REST Users API
  slug: google-fitness-users-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Fit REST API
  slug: open-fitness
- collection_type: open
  name: Google Fit REST Users API
  slug: open-google-fitness-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-fitness-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-fitness-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-fitness-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-fitness-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-fitness-scopes.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/fit/rest/v1/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.google.com/fit/terms
- group: design
  title: ''
  type: JSONLD
  url: json-ld/fitness.jsonld
created: '2026-03-13'
description: The Google Fit REST API enables you to store and access health and wellness data in the fitness store from apps on any platform. You can manage data sources, datasets, sessions, and aggregate fitness data for activities like steps, heart rate, sleep, and workouts.
finops:
- name: Google Fitness Finops
  service_category: API
  slug: google-fitness-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-fitness.png
json_schemas:
- name: Google Fit Session
  property_count: 9
  slug: fitness
jsonld:
- class_count: 12
  name: Fitness Context
  property_count: 2
  slug: fitness
layout: provider
modified: '2026-05-19'
name: Google Fit REST
nav: Providers
network: true
overview: 'Google Fit REST publishes 1 API on the [APIs.io](https://apis.io/) network: Users API. Tagged areas include Activity Tracking, Fitness, Google, Health, and Sessions.


  The Google Fit REST catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Fit REST''s developer surface includes authentication, getting-started guide, pricing, and 5 more developer resources.'
plans:
- name: Google Fitness Plans Pricing
  plan_count: 3
  slug: google-fitness-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Google Fitness Rate Limits
  slug: google-fitness-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Fit REST API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-fitness-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Google Fit REST API Rules
  rule_count: 18
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 6
  slug: google-fitness-spectral-rules
scopes:
- name: Google Fitness Scopes
  scope_count: 6
  slug: google-fitness-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 66.0
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 50.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-fitness/refs/heads/main/screenshots/google-fitness-2026-06-20T182201.png
security:
- kind: authentication
  name: Google Fitness Authentication
  slug: google-fitness-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Fitness Domain Security
  slug: google-fitness-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Fitness Vulnerability Disclosure
  slug: google-fitness-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-fitness
tags:
- Activity Tracking
- Fitness
- Google
- Health
- Sessions
- Wearables
- Wellness
---
