---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Scribe Handwritten Agentic Access
  operation_count: 23
  slug: scribe-handwritten-agentic-access
  summary_line: 23 operations · 14 acting
api_count: 1
apis:
- description: v0 Endpoints
  name: Scribe Handwritten v0 Endpoints API
  slug: scribe-handwritten-v0-endpoints-api
- description: v1 Endpoints
  name: Scribe Handwritten v1 Endpoints API
  slug: scribe-handwritten-v1-endpoints-api
- description: Wallet
  name: Scribe Handwritten Wallet API
  slug: scribe-handwritten-wallet-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/scribe-handwritten/agentic-access/scribe-handwritten-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/scribe-handwritten-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/scribe-handwritten/rules/scribe-handwritten-rules.yml
  title: ''
  type: Spectral
  url: rules/scribe-handwritten-rules.yml
- group: design
  href: https://artifacts.apis.io/scribe-handwritten/json-ld/scribe-handwritten-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/scribe-handwritten-context.jsonld
- group: design
  href: https://artifacts.apis.io/scribe-handwritten/vocabulary/scribe-handwritten-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/scribe-handwritten-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/scribe-handwritten/data-model/scribe-handwritten-data-model.yml
  title: ''
  type: DataModel
  url: data-model/scribe-handwritten-data-model.yml
- group: design
  href: https://artifacts.apis.io/scribe-handwritten/errors/scribe-handwritten-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/scribe-handwritten-problem-types.yml
- group: design
  href: https://artifacts.apis.io/scribe-handwritten/conformance/scribe-handwritten-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scribe-handwritten-conformance.yml
- group: other
  href: https://artifacts.apis.io/scribe-handwritten/overlays/scribe-handwritten-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/scribe-handwritten-overlay.yaml
- group: other
  href: https://artifacts.apis.io/scribe-handwritten/hosts/scribe-handwritten-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scribe-handwritten-hosts.yml
- group: other
  href: https://artifacts.apis.io/scribe-handwritten/vendors/scribe-handwritten-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scribe-handwritten-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.scribenurture.com/login
- group: start
  title: ''
  type: Login
  url: https://scribenurture.com/login
- group: auth
  href: https://artifacts.apis.io/scribe-handwritten/authentication/scribe-handwritten-authentication.yml
  title: ''
  type: Authentication
  url: authentication/scribe-handwritten-authentication.yml
- group: auth
  href: https://artifacts.apis.io/scribe-handwritten/security/scribe-handwritten-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scribe-handwritten-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scribenurture.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://scribenurture.com/wallet
- group: start
  title: ''
  type: GettingStarted
  url: https://api.leadconnectorhq.com/widget/booking/EcwpVBrEmTXbGVIF1QcG
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://scribenurture.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Scribe Handwritten provides a platform that digitizes handwritten notes, allowing users to capture, organize, and share their handwritten content securely online. The service offers tools for scanning, transcribing, and managing handwritten documents, catering to professionals, students, and creatives who need to preserve the authenticity of their original writing while benefiting from digital accessibility and collaboration features.
image: https://scribenurture.com/img/logo.svg
json_schemas:
- name: Contact
  property_count: 12
  slug: scribe-handwritten-contact
- name: Order
  property_count: 33
  slug: scribe-handwritten-order
- name: Transaction Resource
  property_count: 9
  slug: scribe-handwritten-transaction-resource
jsonld:
- class_count: 3
  name: Scribe Handwritten Context
  property_count: 48
  slug: scribe-handwritten-context
layout: provider
modified: '2026-10-27'
name: Scribe Handwritten
nav: Providers
network: true
overview: 'Scribe Handwritten publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: v0 Endpoints API, v1 Endpoints API, and Wallet API. Tagged areas include Company, Handwriting, Digital, Collaboration, and Productivity.


  The Scribe Handwritten catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Scribe Handwritten''s developer surface includes support, authentication, pricing, getting-started guide, and 13 more developer resources.'
plans:
- name: Scribe Handwritten Plans Pricing
  plan_count: 0
  slug: scribe-handwritten-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Scribe Handwritten Rate Limits
  slug: scribe-handwritten-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Scribe Handwritten API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: scribe-handwritten-rules
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 55.6
    developer_ergonomics: 20.2
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 32.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/scribe-handwritten/scribe-handwritten-2026-11-03T142847.png
security:
- kind: authentication
  name: Scribe Handwritten Authentication
  slug: scribe-handwritten-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Scribe Handwritten Domain Security
  slug: scribe-handwritten-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: create-campaign
  slug: scribe-handwritten-create-campaign
slug: scribe-handwritten
tags:
- Company
- Handwriting
- Digital
- Collaboration
- Productivity
website: https://scribenurture.com/
---
