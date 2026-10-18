---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-17'
api_count: 4
apis:
- description: The Activities API from Platform24 — 1 operation(s) for activities.
  name: Platform24 Activities API
  slug: platform24-activities-api
- description: The Data Collect API from Platform24 — 2 operation(s) for data collect.
  name: Platform24 Data Collect API
  slug: platform24-data-collect-api
- description: The Front Door Connect API from Platform24 — 2 operation(s) for front door connect.
  name: Platform24 Front Door Connect API
  slug: platform24-front-door-connect-api
- description: The Sso Url API from Platform24 — 1 operation(s) for sso url.
  name: Platform24 Sso Url API
  slug: platform24-sso-url-api
artifact_total: 12
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/platform24/refs/heads/main/rules/platform24-rules.yml
  title: ''
  type: Spectral
  url: rules/platform24-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/platform24/refs/heads/main/json-ld/platform24-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/platform24-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/platform24/refs/heads/main/vocabulary/platform24-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/platform24-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/platform24/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/platform24/refs/heads/main/data-model/platform24-data-model.yml
  title: ''
  type: DataModel
  url: data-model/platform24-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/platform24/refs/heads/main/changelog/platform24-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/platform24-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://platform24.com/products/compliance/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/platform24/refs/heads/main/authentication/platform24-authentication.yml
  title: ''
  type: Authentication
  url: authentication/platform24-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/platform24/refs/heads/main/conformance/platform24-conformance.yml
  title: ''
  type: Conformance
  url: conformance/platform24-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/platform24/refs/heads/main/llms/platform24-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/platform24-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/platform24/refs/heads/main/hosts/platform24-hosts.yml
  title: ''
  type: Hosts
  url: hosts/platform24-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/platform24/refs/heads/main/vendors/platform24-vendors.yml
  title: ''
  type: Vendors
  url: vendors/platform24-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.platform24.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/platform24/refs/heads/main/security/platform24-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/platform24-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/platform24/refs/heads/main/security/platform24-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/platform24-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://platform24.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://platform24.com/about-us/
- group: operate
  title: ''
  type: Support
  url: https://platform24.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://platform24.com/privacy-policy/
created: '2026-10-12'
description: Platform24 provides an intelligent care platform that connects patients, providers, and health systems through digital intake, triage, virtual clinics, care plans, and analytics. The solution enables seamless access, continuity, and sustainable delivery of healthcare services across primary, specialist, and hospital settings, supporting multilingual experiences and integration with insurance and health data ecosystems.
json_schemas:
- name: GetClientidActivitiesV1Response
  property_count: 9
  slug: platform24-get-clientid-activities-v1-response
- name: PostClientidSsoUrlV1V1IdRequest
  property_count: 2
  slug: platform24-post-clientid-sso-url-v1-v1-id-request
- name: PostClientidSsoUrlV1V1IdResponse
  property_count: 2
  slug: platform24-post-clientid-sso-url-v1-v1-id-response
jsonld:
- class_count: 3
  name: Platform24 Context
  property_count: 4
  slug: platform24-context
layout: provider
modified: '2026-10-12'
name: Platform24
nav: Providers
network: true
overview: 'Platform24 is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Data Collect API, Front Door Connect API, and 1 more. Tagged areas include Healthcare, Digital Health, Platform, Patient Engagement, and Company.


  The Platform24 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Platform24''s developer surface includes changelog, authentication, documentation, getting-started guide, support, and 14 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Platform24 API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: platform24-rules
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 44.5
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 83.3
      total: 6
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 20.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Platform24 Authentication
  slug: platform24-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Platform24 Domain Security
  slug: platform24-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Platform24 Trust Center
  slug: platform24-trust-center
  summary_line: ISO 27001, GDPR
slug: platform24
tags:
- Healthcare
- Digital Health
- Platform
- Patient Engagement
- Company
website: https://platform24.com/
---
