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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Microsoft Cognitive Services Agentic Access
  operation_count: 1
  slug: microsoft-cognitive-services-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 5
apis:
- description: Image analysis, OCR, spatial analysis, and face detection capabilities.
  name: Azure AI Vision API
  slug: vision
- description: Speech-to-text, text-to-speech, speech translation, and speaker recognition.
  name: Azure AI Speech API
  slug: speech
- description: Natural language processing including sentiment analysis, entity recognition, and summarization.
  name: Azure AI Language API
  slug: language
- description: REST API access to OpenAI models including GPT-4, DALL-E, and Whisper with enterprise security.
  name: Azure OpenAI Service API
  slug: openai
- description: Analyze images for visual features
  name: Microsoft Cognitive Services ImageAnalysis API
  slug: microsoft-cognitive-services-imageanalysis-api
artifact_total: 13
collections:
- collection_type: open
  name: Azure AI Vision - Image Analysis REST API
  slug: open-microsoft-cognitive-services
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-cognitive-services-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-cognitive-services-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-cognitive-services-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-cognitive-services-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/cognitive-services/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/azure/ai-services/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/feed/
created: '2026-03-13'
description: Microsoft Cognitive Services (Azure AI Services) provides AI APIs for vision, speech, language, and OpenAI model access.
finops:
- name: Microsoft Cognitive Services Finops
  service_category: API
  slug: microsoft-cognitive-services-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-cognitive-services.png
layout: provider
modified: '2026-04-28'
name: Microsoft Cognitive Services
nav: Providers
network: true
overview: 'Microsoft Cognitive Services publishes 1 API on the [APIs.io](https://apis.io/) network: ImageAnalysis API. Tagged areas include Azure AI, Computer Vision, Speech, NLP, and OpenAI.


  Microsoft Cognitive Services'' developer surface includes authentication, developer portal, pricing, support, engineering blog, and 7 more developer resources.'
plans:
- name: Microsoft Cognitive Services Plans Pricing
  plan_count: 3
  slug: microsoft-cognitive-services-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 5
  name: Microsoft Cognitive Services Rate Limits
  slug: microsoft-cognitive-services-rate-limits
scopes:
- name: Microsoft Cognitive Services Scopes
  scope_count: 1
  slug: microsoft-cognitive-services-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 37.1
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 51.5
    developer_ergonomics: 32.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-cognitive-services/refs/heads/main/screenshots/microsoft-cognitive-services-2026-06-20T185447.png
security:
- kind: authentication
  name: Microsoft Cognitive Services Authentication
  slug: microsoft-cognitive-services-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Microsoft Cognitive Services Domain Security
  slug: microsoft-cognitive-services-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-cognitive-services
tags:
- Azure AI
- Computer Vision
- Speech
- NLP
- OpenAI
- Machine Learning
website: https://portal.azure.com/
---
