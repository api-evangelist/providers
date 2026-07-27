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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Detect Language Agentic Access
  operation_count: 3
  slug: detect-language-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 3
apis:
- description: Account status and metadata
  name: Detect Language Account API
  slug: detect-language-account-api
- description: Language detection endpoints
  name: Detect Language Detection API
  slug: detect-language-detection-api
- description: Supported languages
  name: Detect Language Languages API
  slug: detect-language-languages-api
artifact_total: 10
collections:
- collection_type: open
  name: Detect Language API
  slug: open-detect-language
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/detect-language-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/detect-language-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/detect-language-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/detectlanguage
- group: docs
  title: ''
  type: Documentation
  url: https://detectlanguage.com/documentation
- group: auth
  title: ''
  type: Security
  url: https://detectlanguage.com/documentation#security
- group: commercial
  title: ''
  type: Pricing
  url: https://detectlanguage.com/plans
- group: auth
  title: ''
  type: Authentication
  url: https://detectlanguage.com/documentation#auth
- group: operate
  title: ''
  type: FAQ
  url: https://detectlanguage.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://detectlanguage.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://detectlanguage.com/privacy_policy
- group: other
  title: ''
  type: Regions
  url: https://detectlanguage.com/regions
created: '2025-02-08'
description: The Detect Language API is a web service that identifies the language of a given text with high accuracy, whether it's a long passage, short phrase, or single word. It supports detection of 164 languages and offers fast performance with low latency globally. The API also allows for batch processing, maintains strong security and privacy standards, and is available through both free and premium plans.
finops:
- name: Detect Language Finops
  service_category: API
  slug: detect-language-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/detect-language.png
layout: provider
modified: '2026-05-19'
name: Detect Language
nav: Providers
network: true
overview: 'Detect Language publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Detection API, and Languages API. Tagged areas include Detection, Languages, and Translation.


  Detect Language''s developer surface includes authentication, documentation, pricing, FAQ, and 8 more developer resources.'
plans:
- name: Detect Language Plans Pricing
  plan_count: 3
  slug: detect-language-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Detect Language Rate Limits
  slug: detect-language-rate-limits
score:
  band: developing
  composite: 47.4
  delta: 3.3
  facets:
    commercial_clarity: 71.1
    contract_quality: 57.2
    developer_ergonomics: 19.6
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 44.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/detect-language/refs/heads/main/screenshots/detect-language-2026-06-20T175938.png
security:
- kind: authentication
  name: Detect Language Authentication
  slug: detect-language-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Detect Language Domain Security
  slug: detect-language-domain-security
  summary_line: TLSv1.3 · DMARC
slug: detect-language
tags:
- Detection
- Languages
- Translation
---
