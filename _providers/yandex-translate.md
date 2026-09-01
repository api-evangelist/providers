---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Yandex Translate Agentic Access
  operation_count: 3
  slug: yandex-translate-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- description: REST API for translating text between 100+ languages, detecting the source language of text, and listing supported languages. Built on Yandex neural machine translation technology with support for glo
  name: Yandex Translate API
  slug: yandex-translate-api
- description: Operations for detecting the language of text
  name: Yandex Translate API Language Detection API
  slug: yandex-translate-language-detection-api
- description: Operations for listing supported languages
  name: Yandex Translate API Languages API
  slug: yandex-translate-languages-api
- description: Operations for translating text between languages
  name: Yandex Translate API Translation API
  slug: yandex-translate-translation-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Yandex Translate Language Detection API
  slug: open-yandex-translate-language-detection-api
- collection_type: open
  name: Yandex Translate Language Detection Languages API
  slug: open-yandex-translate-languages-api
- collection_type: open
  name: Yandex Translate Language Detection Translation API
  slug: open-yandex-translate-translation-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yandex-translate-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/yandex-translate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yandex-translate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yandex-translate-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://yandex.cloud/en/services/translate
- group: docs
  title: ''
  type: Documentation
  url: https://yandex.cloud/en/docs/translate/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/yandex-cloud
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yandex-cloud
- group: company
  title: ''
  type: Blog
  url: https://yandex.cloud/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://yandex.cloud/en/docs/translate/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.yandex.cloud/
- group: other
  title: ''
  type: X
  url: https://twitter.com/yandexcloud
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/yandex-translate/refs/heads/main/plans/yandex-translate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/yandex-translate/refs/heads/main/rate-limits/yandex-translate-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/yandex-translate/refs/heads/main/finops/yandex-translate-finops.yml
created: '2026-06-13'
description: Yandex Translate is a machine translation REST API from Yandex that supports 100+ languages. It provides text translation between any supported language pair, automatic source language detection, and a translation dictionary with synonyms, translations, and examples. The API is part of the Yandex Cloud platform and uses neural machine translation to deliver high-quality translations for developers integrating multilingual capabilities into applications, websites, and services.
examples:
- key_count: 3
  name: Detect Language Request
  slug: detect-language-request
- key_count: 1
  name: Detect Language Response
  slug: detect-language-response
- key_count: 1
  name: List Languages Request
  slug: list-languages-request
- key_count: 1
  name: List Languages Response
  slug: list-languages-response
- key_count: 3
  name: Translate Text Request
  slug: translate-text-request
- key_count: 1
  name: Translate Text Response
  slug: translate-text-response
- key_count: 5
  name: Translate With Glossary Request
  slug: translate-with-glossary-request
finops:
- name: Yandex Translate Finops
  service_category: API
  slug: yandex-translate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yandex-translate.png
json_schemas:
- name: DetectLanguageRequest
  property_count: 3
  slug: detect-language-request
- name: DetectLanguageResponse
  property_count: 1
  slug: detect-language-response
- name: ListLanguagesResponse
  property_count: 1
  slug: list-languages-response
- name: TranslateRequest
  property_count: 8
  slug: translate-request
- name: TranslateResponse
  property_count: 1
  slug: translate-response
jsonld:
- class_count: 0
  name: Yandex Translate Context
  property_count: 0
  slug: yandex-translate
layout: provider
modified: '2026-06-13'
name: Yandex Translate API
nav: Providers
network: true
overview: 'Yandex Translate API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Language Detection API, Languages API, and Translation API. Tagged areas include Machine Translation, Natural Language Processing, Language Detection, Translation Dictionary, and Multilingual.


  The Yandex Translate API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Yandex Translate API''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Yandex Translate Plans Pricing
  plan_count: 2
  slug: yandex-translate-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 8
  name: Yandex Translate Rate Limits
  slug: yandex-translate-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Yandex Translate API API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: yandex-translate-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 15
    catalog_gap: 46.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 62.6
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yandex-translate/refs/heads/main/screenshots/yandex-translate-2026-06-20T201724.png
security:
- kind: authentication
  name: Yandex Translate Authentication
  slug: yandex-translate-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Yandex Translate Domain Security
  slug: yandex-translate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Yandex Translate Vulnerability Disclosure
  slug: yandex-translate-vulnerability-disclosure
  summary_line: disclosure policy published
slug: yandex-translate
tags:
- Machine Translation
- Natural Language Processing
- Language Detection
- Translation Dictionary
- Multilingual
- Yandex Cloud
- Localization
- Internationalization
website: https://yandex.cloud/en/services/translate
---
