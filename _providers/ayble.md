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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Ayble Health API (no machine-readable contract discovered)
  name: Ayble API
  slug: ayble-api-2
- baseURL: https://api.ashbyhq.com
  baseurl_source: declared
  description: 'Ayble API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Ayble API
  slug: ayble-api
artifact_total: 13
asyncapis:
- description: ''
  name: Ayble Webhooks
  slug: ayble-webhooks
common:
- group: design
  href: https://artifacts.apis.io/ayble/rules/ayble-rules.yml
  title: ''
  type: Spectral
  url: rules/ayble-rules.yml
- group: design
  href: https://artifacts.apis.io/ayble/json-ld/ayble-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ayble-context.jsonld
- group: design
  href: https://artifacts.apis.io/ayble/vocabulary/ayble-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ayble-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ayble/asyncapi/ayble-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/ayble-webhooks.yml
- group: design
  href: https://artifacts.apis.io/ayble/data-model/ayble-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ayble-data-model.yml
- group: design
  href: https://artifacts.apis.io/ayble/conventions/ayble-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ayble-conventions.yml
- group: auth
  href: https://artifacts.apis.io/ayble/authentication/ayble-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ayble-authentication.yml
- group: operate
  href: https://artifacts.apis.io/ayble/lifecycle/ayble-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/ayble-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ayble/lifecycle/ayble-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ayble-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ayble/conformance/ayble-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ayble-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ayble/well-known/ayble-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ayble-well-known.yml
- group: other
  href: https://artifacts.apis.io/ayble/hosts/ayble-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ayble-hosts.yml
- group: other
  href: https://artifacts.apis.io/ayble/vendors/ayble-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ayble-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.ashbyhq.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.ashbyhq.com/
- group: auth
  href: https://artifacts.apis.io/ayble/security/ayble-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ayble-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ayblehealth.com/
- group: company
  title: ''
  type: About
  url: https://www.ayblehealth.com/our-story
- group: company
  title: ''
  type: Blog
  url: https://www.ayblehealth.com/newsroom
- group: company
  title: ''
  type: Careers
  url: https://jobs.ashbyhq.com/ayblehealth
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ayblehealth.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ayblehealth.com/terms-of-service
coverage:
  checked: '2026-10-29'
  detail: Ayble health site serves HTML shells for OpenAPI endpoints, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://app.ayblehealth.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Ayble Health operates a virtual digestive health clinic offering online gastrointestinal care. It provides telemedicine services for individuals and organizations, enabling patients to receive expert diagnosis, treatment plans, and ongoing support for a range of digestive conditions. The platform emphasizes in‑network access, personalized care, and data‑driven outcomes, aiming to improve quality of life while reducing healthcare costs. Ayble’s services include symptom assessment, video consultations with dietitians and physicians, and integration with employer health benefits.
image: https://cdn.prod.website-files.com/6a4e018d4ab07aac52455d2e/6a674be55e0d15e835c56298_ayble-health-opengraph-image.jpg
json_schemas:
- name: PostCandidateCreatenoteRequest
  property_count: 2
  slug: ayble-post-candidate-createnote-request
- name: PostJobInfoResponse
  property_count: 8
  slug: ayble-post-job-info-response
- name: PostReportGenerateRequest
  property_count: 1
  slug: ayble-post-report-generate-request
- name: PostReportGenerateResponse
  property_count: 2
  slug: ayble-post-report-generate-response
- name: PostReportSynchronousRequest
  property_count: 1
  slug: ayble-post-report-synchronous-request
- name: PostReportSynchronousResponse
  property_count: 2
  slug: ayble-post-report-synchronous-response
jsonld:
- class_count: 6
  name: Ayble Context
  property_count: 15
  slug: ayble-context
layout: provider
modified: '2026-10-29'
name: Ayble
nav: Providers
network: true
overview: 'Ayble is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Telehealth, Digestive Health, VirtualClinic, and Employer Benefits.


  The Ayble catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Ayble''s developer surface includes authentication, getting-started guide, documentation, engineering blog, and 18 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Ayble API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: ayble-rules
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 10.5
    contract_governance: 35.6
    contract_quality: 33.8
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 32.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ayble/ayble-2026-11-03T121449.png
security:
- kind: authentication
  name: Ayble Authentication
  slug: ayble-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ayble Domain Security
  slug: ayble-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ayble
tags:
- Health
- Telehealth
- Digestive Health
- VirtualClinic
- Employer Benefits
- Healthcare
website: https://www.ayblehealth.com/
---
