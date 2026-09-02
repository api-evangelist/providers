---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Google Translate Agentic Access
  operation_count: 3
  slug: google-translate-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- description: Detect language of text
  name: Google Cloud Translation API Detections API
  slug: google-translate-detections-api
- description: List supported languages
  name: Google Cloud Translation API Languages API
  slug: google-translate-languages-api
- description: Translate text between languages
  name: Google Cloud Translation API Translations API
  slug: google-translate-translations-api
artifact_total: 20
collections:
- collection_type: postman
  name: Google Cloud Translation Detections API
  slug: postman-google-translate-detections-api
- collection_type: postman
  name: Google Cloud Translation Detections Languages API
  slug: postman-google-translate-languages-api
- collection_type: postman
  name: Google Cloud Translation Detections Translations API
  slug: postman-google-translate-translations-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Translation Detections API
  slug: open-google-translate-detections-api
- collection_type: open
  name: Google Cloud Translation Detections Languages API
  slug: open-google-translate-languages-api
- collection_type: open
  name: Google Cloud Translation Detections Translations API
  slug: open-google-translate-translations-api
- collection_type: open
  name: Google Cloud Translation API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-translation-api/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-translate-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-translate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-translate-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/google-translate
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/translate
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/translate/docs/setup
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/translate/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/translate/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/translate/docs/support
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/google-translate/refs/heads/main/json-ld/google-translate.jsonld
- group: company
  title: ''
  type: Blog
  url: https://docs.cloud.google.com/feeds/translate-release-notes.xml
created: '2026-03-13'
description: The Google Cloud Translation API provides programmatic access to Google's neural machine translation technology. It enables developers to dynamically translate text between thousands of language pairs, detect the source language of text, and retrieve lists of supported languages. The API supports both basic (v2) and advanced (v3) translation capabilities including batch translation, custom models, glossaries, and adaptive translation.
finops:
- name: Google Translate Finops
  service_category: API
  slug: google-translate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-translate.png
json_schemas:
- name: Google Cloud Translation API Schema
  property_count: 0
  slug: google-translate
jsonld:
- class_count: 2
  name: Google Translate Context
  property_count: 8
  slug: google-translate
layout: provider
modified: '2026-05-19'
name: Google Cloud Translation API
nav: Providers
network: true
overview: 'Google Cloud Translation API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Detections API, Languages API, and Translations API. Tagged areas include Google Cloud, Internationalization, Language Detection, Localization, and Machine Translation.


  The Google Cloud Translation API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Translation API''s developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, engineering blog, and 9 more developer resources.'
plans:
- name: Google Translate Plans Pricing
  plan_count: 3
  slug: google-translate-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Google Translate Rate Limits
  slug: google-translate-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google Cloud Translation API API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-translate-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 13
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 57.1
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-translate/refs/heads/main/screenshots/google-translate-2026-06-20T182243.png
security:
- kind: domain-security
  name: Google Translate Domain Security
  slug: google-translate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Translate Vulnerability Disclosure
  slug: google-translate-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-translate
tags:
- Google Cloud
- Internationalization
- Language Detection
- Localization
- Machine Translation
- Natural Language Processing
- Translation
website: https://cloud.google.com/translate
---
