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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Yandex Translate Agentic Access
  operation_count: 3
  slug: yandex-translate-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 4
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
artifact_total: 25
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
random_paper: 44
rate_limits:
- limit_count: 8
  name: Yandex Translate Rate Limits
  slug: yandex-translate-rate-limits
rules:
- name: Yandex Translate API API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: yandex-translate-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 70.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
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
