---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Post and fund tasks, track automatic payments and reject submissions from your own server.
  name: Microworker API
  slug: microworker-api
- baseURL: https://microworker.app/api/v1
  baseurl_source: declared
  description: Post and fund tasks, track automatic payments and reject submissions from your own server.
  name: Microworker API V1 API
  slug: microworker-api-v1-api
artifact_total: 12
asyncapis:
- description: ''
  name: Microworker Webhooks
  slug: microworker-webhooks
common:
- group: design
  href: https://artifacts.apis.io/microworker/rules/microworker-rules.yml
  title: ''
  type: Spectral
  url: rules/microworker-rules.yml
- group: design
  href: https://artifacts.apis.io/microworker/json-ld/microworker-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microworker-context.jsonld
- group: design
  href: https://artifacts.apis.io/microworker/vocabulary/microworker-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microworker-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microworker/asyncapi/microworker-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/microworker-webhooks.yml
- group: design
  href: https://artifacts.apis.io/microworker/data-model/microworker-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microworker-data-model.yml
- group: design
  href: https://artifacts.apis.io/microworker/errors/microworker-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microworker-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microworker/conformance/microworker-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microworker-conformance.yml
- group: other
  href: https://artifacts.apis.io/microworker/hosts/microworker-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microworker-hosts.yml
- group: other
  href: https://artifacts.apis.io/microworker/vendors/microworker-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microworker-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://microworker.app/developers/
- group: auth
  href: https://artifacts.apis.io/microworker/security/microworker-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microworker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://microworker.app
- group: docs
  title: ''
  type: Documentation
  url: https://microworker.app/developers
- group: operate
  title: ''
  type: Support
  url: https://micrower.app/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://microworker.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://microworker.app/privacy
- group: start
  title: ''
  type: SignUp
  url: https://microworker.app/register
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://microworker.app
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: Microworker is a marketplace for small online tasks. Employers post instructions and rewards for research, data entry, testing, surveys, feedback, and social‑media engagement, and workers complete the steps and submit proof for review. The platform allows tasks to be funded upfront, reviewed, and paid to workers through a Microworker account.
image: https://microworker.app/assets/og-image-v3.png
json_schemas:
- name: LiveEditBody
  property_count: 6
  slug: microworker-live-edit-body
- name: ResizeResult
  property_count: 11
  slug: microworker-resize-result
- name: Submission
  property_count: 29
  slug: microworker-submission
- name: TaskCreate
  property_count: 19
  slug: microworker-task-create
- name: Task
  property_count: 35
  slug: microworker-task
- name: TaskUpdate
  property_count: 14
  slug: microworker-task-update
jsonld:
- class_count: 30
  name: Microworker Context
  property_count: 156
  slug: microworker-context
layout: provider
modified: '2026-10-22'
name: Microworker
nav: Providers
network: true
overview: 'Microworker publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API V1 API, and 1 more. Tagged areas include Marketplace, Data Entry, Testing, Surveys, and Social Media Engagement.


  The Microworker catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Microworker''s developer surface includes API reference, documentation, support, signup flow, and 13 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Microworker API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: microworker-rules
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 35.6
    contract_quality: 70.8
    developer_ergonomics: 21.4
    discoverability: 66.1
    operational_transparency: 7.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Microworker Domain Security
  slug: microworker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microworker
tags:
- Marketplace
- Data Entry
- Testing
- Surveys
- Social Media Engagement
website: https://microworker.app
---
