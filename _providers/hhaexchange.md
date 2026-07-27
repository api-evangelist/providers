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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Hhaexchange Agentic Access
  operation_count: 8
  slug: hhaexchange-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 3
apis:
- description: The Configuration API from HHAeXchange — 1 operation(s) for configuration.
  name: HHAeXchange Configuration API
  slug: hhaexchange-configuration-api
- description: The Internal API from HHAeXchange — 3 operation(s) for internal.
  name: HHAeXchange Internal API
  slug: hhaexchange-internal-api
- description: The Onboarding API from HHAeXchange — 3 operation(s) for onboarding.
  name: HHAeXchange Onboarding API
  slug: hhaexchange-onboarding-api
artifact_total: 14
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
overview: 'HHAeXchange publishes 3 APIs on the [APIs.io](https://apis.io/) network: Configuration API, Internal API, and Onboarding API. Tagged areas include Homecare, EVV, Electronic Visit Verification, Medicaid, and Scheduling.


  The HHAeXchange catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  HHAeXchange''s developer surface includes authentication, status page, support, engineering blog, and 7 more developer resources.'
plans:
- name: Hhaexchange Plans Pricing
  plan_count: 2
  slug: hhaexchange-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 0
  name: Hhaexchange Rate Limits
  slug: hhaexchange-rate-limits
rules:
- name: HHAeXchange API Rules
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
  composite: 46.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 64.9
    developer_ergonomics: 17.4
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 0.0
  previous_composite: 46.5
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 58.7
  schema_version: 0.5
  scored_at: '2026-07-27'
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
- Homecare
- EVV
- Electronic Visit Verification
- Medicaid
- Scheduling
- Caregiver
- Healthcare
---
