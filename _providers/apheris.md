---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-03'
api_count: 8
apis:
- description: API reference for ApherisFold platform
  name: ApherisFold API
  slug: apherisfold-api
- description: The Apheris API API from Apheris — 1 operation(s) for apheris api.
  name: Apheris Apheris API
  slug: apheris-apheris-api-api
- description: The Health API from Apheris — 1 operation(s) for health.
  name: Apheris Health API
  slug: apheris-health-api
- description: The Predict Async API from Apheris — 2 operation(s) for predict async.
  name: Apheris Predict Async API
  slug: apheris-predict-async-api
- description: The Results API from Apheris — 1 operation(s) for results.
  name: Apheris Results API
  slug: apheris-results-api
- description: The Schema API from Apheris — 1 operation(s) for schema.
  name: Apheris Schema API
  slug: apheris-schema-api
- description: The Ticket API from Apheris — 2 operation(s) for ticket.
  name: Apheris Ticket API
  slug: apheris-ticket-api
- description: The Weights API from Apheris — 1 operation(s) for weights.
  name: Apheris Weights API
  slug: apheris-weights-api
artifact_total: 17
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apheris/refs/heads/main/well-known/apheris-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/apheris-clarity-security.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apheris/refs/heads/main/rules/apheris-rules.yml
  title: ''
  type: Spectral
  url: rules/apheris-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apheris/refs/heads/main/json-ld/apheris-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apheris-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apheris/refs/heads/main/vocabulary/apheris-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apheris-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apheris/refs/heads/main/data-model/apheris-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apheris-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apheris/refs/heads/main/changelog/apheris-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/apheris-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apheris/refs/heads/main/authentication/apheris-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apheris-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apheris/refs/heads/main/conformance/apheris-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apheris-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apheris/refs/heads/main/well-known/apheris-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apheris-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apheris/refs/heads/main/hosts/apheris-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apheris-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apheris/refs/heads/main/vendors/apheris-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apheris-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.apheris.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apheris.com/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://www.apheris.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.apheris.com/docs/hub/nim-msa-server-setup.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apheris/refs/heads/main/security/apheris-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/apheris-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apheris/refs/heads/main/security/apheris-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apheris-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.apheris.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  reason: no-developer-program
  state: none
created: '2026-09-25'
description: Apheris provides federated AI platforms for drug discovery, enabling superior models through federated data networks. The company focuses on leveraging distributed datasets to train high‑performing predictive models for pharmaceutical research, offering tools that integrate securely across institutions.
json_schemas:
- name: GetApiV1PredictAsyncJobidIdResponse
  property_count: 4
  slug: apheris-get-api-v1-predict-async-jobid-id-response
- name: GetWeightsResponse
  property_count: 1
  slug: apheris-get-weights-response
- name: PostApiV1PredictAsyncRequest
  property_count: 5
  slug: apheris-post-api-v1-predict-async-request
- name: PostApiV1PredictAsyncResponse
  property_count: 2
  slug: apheris-post-api-v1-predict-async-response
jsonld:
- class_count: 4
  name: Apheris Context
  property_count: 10
  slug: apheris-context
layout: provider
modified: '2026-09-25'
name: Apheris
nav: Providers
network: true
overview: 'Apheris publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Apheris API, Health API, Predict Async API, and 5 more. Tagged areas include Company, Artificial Intelligence, Drug Discovery, Federated Learning, and Biotechnology.


  The Apheris catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apheris'' developer surface includes changelog, authentication, documentation, getting-started guide, and 15 more developer resources.'
random_paper: 0
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Apheris API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 1
  slug: apheris-rules
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 22.0
    contract_quality: 21.0
    developer_ergonomics: 33.3
    discoverability: 58.9
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Apheris Authentication
  slug: apheris-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Apheris Domain Security
  slug: apheris-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Apheris Vulnerability Disclosure
  slug: apheris-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apheris
tags:
- Company
- Artificial Intelligence
- Drug Discovery
- Federated Learning
- Biotechnology
website: https://www.apheris.com/
---
