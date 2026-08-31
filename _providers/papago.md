---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Papago Agentic Access
  operation_count: 3
  slug: papago-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- description: Automatically detects the language of input text, supporting 15 languages including Korean, English, Japanese, Chinese, Vietnamese, Thai, Indonesian, French, Spanish, Russian, German, Italian, Portugu
  name: Papago Language Detection API
  slug: papago-language-detection
- description: 'Translates documents while preserving their original layout, supporting MS Office formats (DOCX, PPTX, XLSX), PDF, and Korean Hangul (HWP v5.0+) files up to 100 MB and 300,000 characters per document '
  name: Papago Document Translation API
  slug: papago-document-translation
- description: Detects and translates HTML documents and web elements using proprietary tag restoration technology for improved translation accuracy across websites and web applications, supporting 15 language pairs
  name: Papago Website Translation API
  slug: papago-website-translation
- description: Manages custom terminology dictionaries for contextually appropriate translations. Allows registration and retrieval of glossaries with up to 20 terms per request, applied across all Papago translatio
  name: Papago Glossary API
  slug: papago-glossary
- description: Naver Machine Learning Translation APIs
  name: Papago Papago API
  slug: papago-papago-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Translation Papago API
  slug: open-papago-papago-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/papago-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/papago-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/papago-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.ncloud.com/v2/product/aiService/papagoTranslation
- group: docs
  title: ''
  type: Documentation
  url: https://guide.ncloud-docs.com/docs/en/papagotranslation-overview
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/NaverCloudPlatform
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/navercloud
- group: company
  title: ''
  type: Blog
  url: https://medium.com/naver-cloud
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ncloud.com/charge/calc
- group: operate
  title: ''
  type: StatusPage
  url: https://www.ncloud.com/v2/serviceStatus
- group: other
  title: ''
  type: X
  url: https://x.com/NaverCloudPlatf
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/papago/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/papago/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/papago/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: Naver Papago translation REST API for translating text between Korean, English, Japanese, Chinese, and other Asian and European languages using Neural Machine Translation (NMT) algorithms. The service offers text translation, document translation, website translation, language detection, and glossary management, supporting 29 language pairs with high accuracy and no data retention for user privacy.
examples:
- key_count: 4
  name: Nmt Translation Request
  slug: nmt-translation-request
- key_count: 1
  name: Nmt Translation Response
  slug: nmt-translation-response
- key_count: 1
  name: Romanization Request
  slug: romanization-request
- key_count: 1
  name: Romanization Response
  slug: romanization-response
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/papago.png
json_schemas:
- name: RomanizationResponse
  property_count: 1
  slug: romanization-response
- name: TranslationRequest
  property_count: 5
  slug: translation-request
- name: TranslationResponse
  property_count: 1
  slug: translation-response
jsonld:
- class_count: 3
  name: context Context
  property_count: 17
  slug: context
layout: provider
modified: '2026-06-13'
name: Papago
nav: Providers
network: true
overview: 'Papago publishes 1 API on the [APIs.io](https://apis.io/) network: Papago API. Tagged areas include Translation, Natural Language Processing, Machine Translation, Neural Machine Translation, and Korean.


  The Papago catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Papago''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 2
rate_limits:
- limit_count: 5
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Papago API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: papago-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 14
    catalog_gap: 39.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 61.2
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/papago/refs/heads/main/screenshots/papago-2026-06-20T191349.png
security:
- kind: authentication
  name: Papago Authentication
  slug: papago-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Papago Domain Security
  slug: papago-domain-security
  summary_line: TLSv1.3 · HSTS
slug: papago
tags:
- Translation
- Natural Language Processing
- Machine Translation
- Neural Machine Translation
- Korean
- Asian Languages
- Localization
- Language Detection
website: https://www.ncloud.com/v2/product/aiService/papagoTranslation
---
