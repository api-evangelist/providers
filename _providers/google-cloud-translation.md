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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Cloud Translation Agentic Access
  operation_count: 5
  slug: google-cloud-translation-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- description: The Projects API from Google Cloud Translation — 4 operation(s) for projects.
  name: Google Cloud Translation Projects API
  slug: google-cloud-translation-projects-api
artifact_total: 12
collections:
- collection_type: postman
  name: Google Cloud Translation Projects API
  slug: postman-google-cloud-translation-projects-api
- collection_type: open
  name: Google Cloud Translation API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-translation/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-translation-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-translation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-translation-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
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
  url: json-ld/context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://docs.cloud.google.com/feeds/translate-release-notes.xml
created: '2026-03-13'
description: Google Cloud Translation API enables dynamic translation of text between thousands of language pairs. It supports both basic translation using pre-trained Neural Machine Translation models and advanced translation with custom models and glossaries for domain-specific terminology.
finops:
- name: Google Cloud Translation Finops
  service_category: API
  slug: google-cloud-translation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-translation.png
json_schemas:
- name: Translation Request
  property_count: 6
  slug: translation
jsonld:
- class_count: 12
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Cloud Translation
nav: Providers
network: true
overview: 'Google Cloud Translation publishes 1 API on the [APIs.io](https://apis.io/) network: Projects API. Tagged areas include Google Cloud, Language, Localization, Machine Learning, and Translation.


  The Google Cloud Translation catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Translation''s developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, engineering blog, and 9 more developer resources.'
plans:
- name: Google Cloud Translation Plans Pricing
  plan_count: 3
  slug: google-cloud-translation-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 5
  name: Google Cloud Translation Rate Limits
  slug: google-cloud-translation-rate-limits
rules:
- name: Google Cloud Translation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-translation-jsonschema-spectral-rules
score:
  band: strong
  composite: 61.0
  delta: -3.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 64.4
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 64.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-translation/refs/heads/main/screenshots/google-cloud-translation-2026-06-20T182148.png
security:
- kind: domain-security
  name: Google Cloud Translation Domain Security
  slug: google-cloud-translation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Translation Vulnerability Disclosure
  slug: google-cloud-translation-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-translation
tags:
- Google Cloud
- Language
- Localization
- Machine Learning
- Translation
website: https://cloud.google.com/translate
---
