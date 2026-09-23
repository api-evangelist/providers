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
  score: 12.9
  scored_at: '2026-09-23'
api_count: 2
apis:
- description: UniCourt provides litigation data APIs as described in their documentation.
  name: UniCourt API
  slug: unicourt-api
- baseURL: https://enterpriseapi.unicourt.com
  baseurl_source: declared
  description: 'UniCourt API as documented publicly: 47 operations. Contract generated from the documentation by API Evangelist (2026-09-22); not the provider''s own document.'
  name: UniCourt API
  slug: unicourt-api
artifact_total: 11
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unicourt/refs/heads/main/rules/unicourt-rules.yml
  title: ''
  type: Spectral
  url: rules/unicourt-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unicourt/refs/heads/main/json-ld/unicourt-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/unicourt-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unicourt/refs/heads/main/vocabulary/unicourt-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/unicourt-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unicourt/refs/heads/main/data-model/unicourt-data-model.yml
  title: ''
  type: DataModel
  url: data-model/unicourt-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unicourt/refs/heads/main/conformance/unicourt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/unicourt-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unicourt/refs/heads/main/conventions/unicourt-conventions.yml
  title: ''
  type: Conventions
  url: conventions/unicourt-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/unicourt/refs/heads/main/security/unicourt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unicourt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unicourt.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.unicourt.com/login/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unicourt.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.unicourt.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.unicourt.com/getting-started/welcome-to-unicourt-API
- group: operate
  title: ''
  type: Support
  url: https://unicourt.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://unicourt.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://unicourt.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://unicourt.com/signup?p=s00006&li=pc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unicourt.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unicourt.com/privacy-policy
coverage:
  checked: 2026-09-21
  detail: Documentation is public but no OpenAPI or other machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://docs.unicourt.com/authentication-and-authorization
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-21'
description: UniCourt provides a single platform for accessing litigation data, analytics, and insights. It offers APIs, widgets, and data share solutions that give real-time access to over 2 billion dockets and documents from 4,000+ state and federal courts. Customers can integrate structured litigation data into applications, data warehouses, and experience management systems for better decision‑making and risk assessment.
image: https://cdn.prod.website-files.com/68e96a346d8a3699dd3316b1/698113f630e1434ec18db8f1_og-img-logo.jpg
json_schemas:
- name: GetCaseCaseak44001593745AResponse
  property_count: 26
  slug: unicourt-get-case-caseak44001593745-aresponse
- name: GetCasecountanalyticsbycasetypeResponse
  property_count: 19
  slug: unicourt-get-casecountanalyticsbycasetype-response
- name: GetCasecountanalyticsbynormattorneyResponse
  property_count: 11
  slug: unicourt-get-casecountanalyticsbynormattorney-response
- name: GetNormattorneyNatyppnmw8Ayt8QvjtResponse
  property_count: 10
  slug: unicourt-get-normattorney-natyppnmw8-ayt8-qvjt-response
- name: GetNormattorneyNatyst9Ko4FsnjbjthCasecountanalyticsbyopposin
  property_count: 11
  slug: unicourt-get-normattorney-natyst9-ko4-fsnjbjth-casecountanalyticsbyopposin
- name: PutNormattorneytrackRequest
  property_count: 7
  slug: unicourt-put-normattorneytrack-request
jsonld:
- class_count: 52
  name: Unicourt Context
  property_count: 121
  slug: unicourt-context
layout: provider
modified: '2026-09-21'
name: UniCourt
nav: Providers
network: true
overview: 'UniCourt publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Legal Tech, Data Analytics, Litigation, and Platform.


  The UniCourt catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  UniCourt''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 11 more developer resources.'
random_paper: 9
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: UniCourt API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: unicourt-rules
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 21.3
    developer_ergonomics: 45.2
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 30.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Unicourt Domain Security
  slug: unicourt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: unicourt
tags:
- Legal Tech
- Data Analytics
- Litigation
- Platform
website: https://unicourt.com/
---
