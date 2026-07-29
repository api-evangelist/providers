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
- acting_count: 8
  human_in_the_loop: 0
  name: Eden Ai Agentic Access
  operation_count: 9
  slug: eden-ai-agentic-access
  summary_line: 9 operations · 8 acting
api_count: 6
apis:
- description: Eden AI API is a versatile tool that leverages artificial intelligence to enhance and streamline various business processes. By providing access to advanced machine learning and natural language proce
  name: Eden AI API
  slug: eden-ai
- description: The Audio API from Eden AI — 2 operation(s) for audio.
  name: Eden AI Audio API
  slug: eden-ai-audio-api
- description: The Image API from Eden AI — 1 operation(s) for image.
  name: Eden AI Image API
  slug: eden-ai-image-api
- description: The OCR API from Eden AI — 1 operation(s) for ocr.
  name: Eden AI OCR API
  slug: eden-ai-ocr-api
- description: The Text API from Eden AI — 4 operation(s) for text.
  name: Eden AI Text API
  slug: eden-ai-text-api
- description: The Translation API from Eden AI — 1 operation(s) for translation.
  name: Eden AI Translation API
  slug: eden-ai-translation-api
artifact_total: 14
collections:
- collection_type: open
  name: Eden AI API
  slug: open-eden-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eden-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/eden-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eden-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eden-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/edenai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/edenai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.edenai.co/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://docs.edenai.co/docs/quickstart-ai-apis
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.edenai.co/docs/rate-limiting
- group: company
  title: ''
  type: Blog
  url: https://www.edenai.co/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.edenai.co/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.edenai.co/privacy-policy
created: '2025-02-09'
description: Eden AI is an innovative artificial intelligence platform that specializes in providing advanced solutions for businesses looking to optimize their operations and improve efficiency. Using cutting-edge machine learning algorithms and data analytics tools, Eden AI helps companies automate tedious tasks, streamline processes, and extract valuable insights from their data.
finops:
- name: Eden Ai Finops
  service_category: API
  slug: eden-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eden-ai.png
layout: provider
modified: '2026-04-28'
name: Eden AI
nav: Providers
network: true
overview: 'Eden AI publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Image API, OCR API, and 2 more. Tagged areas include Artificial Intelligence, Emotion, and Emotion Detection.


  Eden AI''s developer surface includes authentication, pricing, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Eden Ai Plans Pricing
  plan_count: 3
  slug: eden-ai-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Eden Ai Rate Limits
  slug: eden-ai-rate-limits
score:
  band: developing
  composite: 44.1
  delta: -1.4
  facets:
    commercial_clarity: 78.9
    contract_quality: 54.4
    developer_ergonomics: 21.7
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eden-ai/refs/heads/main/screenshots/eden-ai-2026-06-20T180450.png
security:
- kind: authentication
  name: Eden Ai Authentication
  slug: eden-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Eden Ai Domain Security
  slug: eden-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Eden Ai Trust Center
  slug: eden-ai-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: eden-ai
tags:
- Artificial Intelligence
- Emotion
- Emotion Detection
---
