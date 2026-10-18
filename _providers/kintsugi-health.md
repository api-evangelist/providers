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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-17'
api_count: 6
apis:
- description: Provides endpoints to initiate a session, submit audio, retrieve results, and submit feedback for voice biomarker analysis.
  name: Kintsugi Voice API
  slug: kintsugi-voice-api
- baseURL: https://api.kintsugihealth.com
  baseurl_source: declared
  description: The Feedback API from Kintsugi Health — 6 operation(s) for feedback.
  name: Kintsugi Health Feedback API
  slug: kintsugi-health-feedback-api
- baseURL: https://api.kintsugihealth.com
  baseurl_source: declared
  description: The Initiate API from Kintsugi Health — 2 operation(s) for initiate.
  name: Kintsugi Health Initiate API
  slug: kintsugi-health-initiate-api
- baseURL: https://api.kintsugihealth.com
  baseurl_source: declared
  description: The Kintsugi Health API API from Kintsugi Health — 1 operation(s) for kintsugi health api.
  name: Kintsugi Health Kintsugi Health API
  slug: kintsugi-health-kintsugi-health-api-api
- baseURL: https://api.kintsugihealth.com
  baseurl_source: declared
  description: The Predict API from Kintsugi Health — 5 operation(s) for predict.
  name: Kintsugi Health Predict API
  slug: kintsugi-health-predict-api
- baseURL: https://api.kintsugihealth.com
  baseurl_source: declared
  description: The Prediction API from Kintsugi Health — 1 operation(s) for prediction.
  name: Kintsugi Health Prediction API
  slug: kintsugi-health-prediction-api
artifact_total: 16
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kintsugi-health/refs/heads/main/rules/kintsugi-health-rules.yml
  title: ''
  type: Spectral
  url: rules/kintsugi-health-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kintsugi-health/refs/heads/main/json-ld/kintsugi-health-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kintsugi-health-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kintsugi-health/refs/heads/main/vocabulary/kintsugi-health-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kintsugi-health-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kintsugi-health/refs/heads/main/data-model/kintsugi-health-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kintsugi-health-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kintsugi-health/refs/heads/main/authentication/kintsugi-health-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kintsugi-health-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kintsugi-health/refs/heads/main/conformance/kintsugi-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kintsugi-health-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kintsugi-health/refs/heads/main/hosts/kintsugi-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kintsugi-health-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kintsugi-health/refs/heads/main/vendors/kintsugi-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kintsugi-health-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.kintsugihealth.com/
- group: auth
  title: ''
  type: Security
  url: https://www.kintsugihealth.com/blog-categories/security
- group: build
  title: ''
  type: SDKs
  url: https://www.kintsugihealth.com/api/sdks
- group: company
  title: ''
  type: Newsroom
  url: https://www.kintsugihealth.com/press
- group: other
  title: ''
  type: Leadership
  url: https://www.kintsugihealth.com/blog-categories/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kintsugi-health/refs/heads/main/security/kintsugi-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kintsugi-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kintsugihealth.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.kintsugihealth.com/api/intro-to-kintsugi-voice-api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.kintsugihealth.com/api/intro-to-kintsugi-voice-api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.kintsugihealth.com/request-demo
- group: operate
  title: ''
  type: Support
  url: https://www.kintsugihealth.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.kintsugihealth.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kintsugihealth.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kintsugihealth.com/privacy
coverage:
  checked: '2026-10-14'
  detail: API documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found.
  evidence:
  - status: 307
    url: https://api.kintsugihealth.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Kintsugi Health provides AI-driven voice analysis solutions to detect mental health challenges and other clinical indicators from speech. Their Kintsugi Voice API enables developers to integrate real-time voice biomarker detection into healthcare applications, supporting use cases from depression screening to deep‑fake detection. The company emphasizes privacy, regulatory compliance, and evidence‑based technology, aiming to improve patient outcomes through innovative digital health tools.
image: https://cdn.prod.website-files.com/62bdd1459016066e353bd6b0/62ff59f1af0efcfec060df13_open-graph-image.jpeg
json_schemas:
- name: GetV2PredictSessionsSessionidResponse
  property_count: 7
  slug: kintsugi-health-get-v2-predict-sessions-sessionid-response
- name: PatchV2FeedbackDepressionBinaryResponse
  property_count: 7
  slug: kintsugi-health-patch-v2-feedback-depression-binary-response
- name: PatchV2FeedbackGad7Response
  property_count: 7
  slug: kintsugi-health-patch-v2-feedback-gad7-response
- name: PatchV2FeedbackPhqPhqidResponse
  property_count: 7
  slug: kintsugi-health-patch-v2-feedback-phq-phqid-response
- name: PostV2PredictionResponse
  property_count: 8
  slug: kintsugi-health-post-v2-prediction-response
- name: PostV2V2IdRequest
  property_count: 9
  slug: kintsugi-health-post-v2-v2-id-request
jsonld:
- class_count: 19
  name: Kintsugi Health Context
  property_count: 24
  slug: kintsugi-health-context
layout: provider
modified: '2026-10-14'
name: Kintsugi Health
nav: Providers
network: true
overview: 'Kintsugi Health is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including Feedback API, Initiate API, Kintsugi Health API, and 3 more. Tagged areas include Health Tech, Artificial Intelligence, VoiceAnalytics, Mental Health, and Digital Health.


  The Kintsugi Health catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Kintsugi Health''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, and 17 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Kintsugi Health API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: kintsugi-health-rules
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 35.6
    contract_quality: 25.7
    developer_ergonomics: 57.1
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 27.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Kintsugi Health Authentication
  slug: kintsugi-health-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Kintsugi Health Domain Security
  slug: kintsugi-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kintsugi-health
tags:
- Health Tech
- Artificial Intelligence
- VoiceAnalytics
- Mental Health
- Digital Health
website: https://www.kintsugihealth.com
---
