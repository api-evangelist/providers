---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Coala Life Agentic Access
  operation_count: 4
  slug: coala-life-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.coalasolutions.com
  baseurl_source: declared
  description: The PatientSessions API from Coala Life — 1 operation(s) for patientsessions.
  name: Coala Life Patient Sessions API
  slug: coala-life-patientsessions-api
- baseURL: https://api.coalasolutions.com
  baseurl_source: declared
  description: The Platform.Api API from Coala Life — 1 operation(s) for platform.api.
  name: Coala Life Platform.Api API
  slug: coala-life-platform-api-api
- baseURL: https://api.coalasolutions.com
  baseurl_source: declared
  description: The Sessions API from Coala Life — 2 operation(s) for sessions.
  name: Coala Life Sessions API
  slug: coala-life-sessions-api
artifact_total: 9
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coala-life/refs/heads/main/vocabulary/coala-life-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coala-life-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coala-life/refs/heads/main/data-model/coala-life-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coala-life-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coala-life/refs/heads/main/agentic-access/coala-life-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coala-life-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coala-life/refs/heads/main/rules/coala-life-rules.yml
  title: ''
  type: Spectral
  url: rules/coala-life-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coala-life/refs/heads/main/errors/coala-life-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/coala-life-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coala-life/refs/heads/main/conformance/coala-life-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coala-life-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coala-life/refs/heads/main/hosts/coala-life-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coala-life-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coala-life/refs/heads/main/authentication/coala-life-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coala-life-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coala-life/refs/heads/main/security/coala-life-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coala-life-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coalalife.com/
- group: docs
  title: ''
  type: Documentation
  url: https://coalasolutions.com/en/clinician/our-solution/coala-care-portal/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://coalasolutions.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://coalasolutions.com/en/clinician/our-solution/coala-care-app/
- group: start
  title: ''
  type: GettingStarted
  url: https://coalasolutions.com/en/clinician/our-solution/coala-care-portal/
- group: operate
  title: ''
  type: Support
  url: https://coalasolutions.com/en/clinician/support/
- group: company
  title: ''
  type: Blog
  url: https://coalasolutions.com/en/news/
- group: commercial
  title: ''
  type: Pricing
  url: https://coalasolutions.com/en/terms/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coalasolutions.com/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coalasolutions.com/en/privacy-statement/
created: '2026-10-12'
description: Coala Life provides remote cardiac monitoring solutions, offering a platform for arrhythmia investigation and long-term ECG monitoring. Their Coala Care Portal and mobile app enable clinicians and patients to access diagnostic-quality ECG data, integrated stethoscope recordings, and algorithm‑enhanced interpretations in real time. The company supports post‑market services for CE‑marked devices and collaborates with healthcare providers to improve cardiac care.
json_schemas:
- name: SessionDtoPagedResult
  property_count: 0
  slug: coala-life-session-dto-paged-result
- name: SessionDto
  property_count: 0
  slug: coala-life-session-dto
layout: provider
modified: '2026-10-12'
name: Coala Life
nav: Providers
network: true
overview: 'Coala Life publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Patient Sessions API, Platform.Api API, and Sessions API. Tagged areas include Company, Healthcare, Cardiology, Remote Monitoring, and Digital Health.


  The Coala Life catalog on APIs.io includes 1 Spectral governance ruleset.


  Coala Life''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 12 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: Coala Life API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 1
  slug: coala-life-rules
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.8
    catalog_earned_first_party: 0.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 35.6
    contract_quality: 43.9
    developer_ergonomics: 57.1
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Coala Life Authentication
  slug: coala-life-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Coala Life Domain Security
  slug: coala-life-domain-security
  summary_line: TLSv1.3 · HSTS
slug: coala-life
tags:
- Company
- Healthcare
- Cardiology
- Remote Monitoring
- Digital Health
website: https://www.coalalife.com/
---
