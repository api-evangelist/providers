---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Hhaexchange Agentic Access
  operation_count: 8
  slug: hhaexchange-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.hhaexchange.com
  baseurl_source: declared
  description: The Configuration API from HHAeXchange — 1 operation(s) for configuration.
  name: HHAeXchange Configuration API
  slug: hhaexchange-configuration-api
- baseURL: https://api.hhaexchange.com
  baseurl_source: declared
  description: The Internal API from HHAeXchange — 3 operation(s) for internal.
  name: HHAeXchange Internal API
  slug: hhaexchange-internal-api
- baseURL: https://api.hhaexchange.com
  baseurl_source: declared
  description: The Onboarding API from HHAeXchange — 3 operation(s) for onboarding.
  name: HHAeXchange Onboarding API
  slug: hhaexchange-onboarding-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HHAeXchange FHIR Configuration API
  slug: open-hhaexchange-configuration-api
- collection_type: open
  name: HHAeXchange FHIR Configuration Internal API
  slug: open-hhaexchange-internal-api
- collection_type: open
  name: HHAeXchange FHIR Configuration Onboarding API
  slug: open-hhaexchange-onboarding-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hhaexchange-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hhaexchange-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hhaexchange-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hhaexchange-scopes.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hhaexchange-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hhaexchange-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hhaexchange-finops.yml
- group: other
  title: ''
  type: KnowledgeBase
  url: https://knowledge.hhaexchange.com/
- group: operate
  title: ''
  type: Status
  url: https://hhaexchange.statuspage.io/
- group: operate
  title: ''
  type: Support
  url: https://www.hhaexchange.com/knowledge-base
- group: company
  title: ''
  type: Blog
  url: https://www.hhaexchange.com/feed/
created: 2026-06-13
description: Homecare management platform with a REST API for scheduling aide visits, verifying care delivery via telephony and mobile, managing authorizations, and processing Medicaid billing. Provides EVV (Electronic Visit Verification) APIs for third-party integration with state Medicaid systems.
examples:
- key_count: 1
  name: Hhaexchange Fhir Examples
  slug: hhaexchange-fhir-examples
finops:
- name: Hhaexchange Finops
  service_category: ''
  slug: hhaexchange-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hhaexchange.png
json_schemas:
- name: HHAeXchange FHIR API Schemas
  property_count: 0
  slug: hhaexchange-fhir
jsonld:
- class_count: 4
  name: Hhaexchange Context
  property_count: 43
  slug: hhaexchange-context
layout: provider
modified: 2026-06-13
name: HHAeXchange
nav: Providers
network: true
overview: 'HHAeXchange publishes 3 APIs on the [APIs.io](https://apis.io/) network: Configuration API, Internal API, and Onboarding API. Tagged areas include Home Care, EVV, Electronic Visit Verification, Medicaid, and Scheduling.


  The HHAeXchange catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  HHAeXchange''s developer surface includes authentication, status page, support, engineering blog, and 7 more developer resources.'
plans:
- name: Hhaexchange Plans Pricing
  plan_count: 2
  slug: hhaexchange-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Hhaexchange Rate Limits
  slug: hhaexchange-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: HHAeXchange API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: hhaexchange-jsonschema-spectral-rules
scopes:
- name: Hhaexchange Scopes
  scope_count: 1
  slug: hhaexchange-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 71.3
    catalog_earned_first_party: 0.0
    catalog_gap: 43.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 62.6
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 31.6
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 42.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hhaexchange/refs/heads/main/screenshots/hhaexchange-2026-06-20T182722.png
security:
- kind: authentication
  name: Hhaexchange Authentication
  slug: hhaexchange-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hhaexchange Domain Security
  slug: hhaexchange-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hhaexchange
tags:
- Home Care
- EVV
- Electronic Visit Verification
- Medicaid
- Scheduling
- Caregiver
- Healthcare
---
