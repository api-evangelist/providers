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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Ibm Translate Agentic Access
  operation_count: 13
  slug: ibm-translate-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 4
apis:
- description: Operations for translating documents
  name: IBM Language Translator Documents API
  slug: ibm-translate-documents-api
- description: Operations for listing supported and identifiable languages
  name: IBM Language Translator Languages API
  slug: ibm-translate-languages-api
- description: Operations for managing translation models
  name: IBM Language Translator Models API
  slug: ibm-translate-models-api
- description: Operations for translating text
  name: IBM Language Translator Translation API
  slug: ibm-translate-translation-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: IBM Watson Language Translator V3 Documents API
  slug: open-ibm-translate-documents-api
- collection_type: open
  name: IBM Watson Language Translator V3 Documents Languages API
  slug: open-ibm-translate-languages-api
- collection_type: open
  name: IBM Watson Language Translator V3 Documents Models API
  slug: open-ibm-translate-models-api
- collection_type: open
  name: IBM Watson Language Translator V3 Documents Translation API
  slug: open-ibm-translate-translation-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/watson-developer-cloud/python-sdk/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/watson-developer-cloud/python-sdk/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/watson-developer-cloud/python-sdk/blob/master/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/watson-developer-cloud/python-sdk/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/watson-developer-cloud/python-sdk/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ibm-translate-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ibm-translate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ibm-translate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ibm-translate-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.ibm.com/cloud/watson-language-translator
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.ibm.com/apidocs/language-translator
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/watson-developer-cloud
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ibm
- group: company
  title: ''
  type: Blog
  url: https://www.ibm.com/blog/category/watson/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ibm.com/cloud/watson-language-translator/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://cloud.ibm.com/status?component=language-translator&selected=status
- group: other
  title: ''
  type: X
  url: https://x.com/IBMcloud
- group: commercial
  title: ''
  type: Plans
  url: plans/ibm-translate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ibm-translate-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ibm-translate-finops.yml
created: '2026-06-13'
description: IBM Watson Language Translator was a REST API service for translating text between 35+ languages, detecting input language automatically, and creating custom domain-specific translation models using TMX, XLIFF, or CSV training data. The service supported neural machine translation (NMT) and was available through IBM Cloud. IBM deprecated the service in June 2023 and fully withdrew it in December 2024.
examples:
- key_count: 4
  name: Identify Language
  slug: identify-language
- key_count: 4
  name: List Models
  slug: list-models
- key_count: 4
  name: Translate Text
  slug: translate-text
finops:
- name: Ibm Translate Finops
  service_category: AI and Machine Learning
  slug: ibm-translate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ibm-translate.png
json_schemas:
- name: DocumentStatus
  property_count: 12
  slug: document-status
- name: TranslationModel
  property_count: 10
  slug: translation-model
- name: TranslateRequest
  property_count: 4
  slug: translation-request
- name: TranslationResult
  property_count: 5
  slug: translation-result
jsonld:
- class_count: 8
  name: context Context
  property_count: 35
  slug: context
layout: provider
modified: '2026-06-13'
name: IBM Language Translator
nav: Providers
network: true
overview: 'IBM Language Translator publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Languages API, Models API, and 1 more. Tagged areas include Translation, Natural Language Processing, Machine Translation, IBM Watson, and AI.


  The IBM Language Translator catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  IBM Language Translator''s developer surface includes authentication, documentation, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Ibm Translate Plans Pricing
  plan_count: 2
  slug: ibm-translate-plans-pricing
random_paper: 139
rate_limits:
- limit_count: 3
  name: Ibm Translate Rate Limits
  slug: ibm-translate-rate-limits
rules:
- name: IBM Language Translator API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ibm-translate-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ibm-translate/refs/heads/main/screenshots/ibm-translate-2026-06-20T183233.png
security:
- kind: authentication
  name: Ibm Translate Authentication
  slug: ibm-translate-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ibm Translate Domain Security
  slug: ibm-translate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ibm Translate Vulnerability Disclosure
  slug: ibm-translate-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: ibm-translate
tags:
- Translation
- Natural Language Processing
- Machine Translation
- IBM Watson
- AI
- Text Analysis
- Deprecated
website: https://www.ibm.com/cloud/watson-language-translator
---
