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
- acting_count: 1
  human_in_the_loop: 0
  name: Microsoft Cognitive Services Agentic Access
  operation_count: 1
  slug: microsoft-cognitive-services-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
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
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure AI Vision - Image Analysis REST ImageAnalysis API
  slug: open-microsoft-cognitive-services-imageanalysis-api
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
overview: 'Microsoft Cognitive Services publishes 1 API on the [APIs.io](https://apis.io/) network: ImageAnalysis API. Tagged areas include Azure AI, Computer-Vision, Speech, NLP, and OpenAI.


  Microsoft Cognitive Services'' developer surface includes authentication, developer portal, pricing, support, engineering blog, and 7 more developer resources.'
plans:
- name: Microsoft Cognitive Services Plans Pricing
  plan_count: 3
  slug: microsoft-cognitive-services-plans-pricing
random_paper: 10
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
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 11
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 52.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Computer-Vision
- Speech
- NLP
- OpenAI
- Machine-Learning
website: https://portal.azure.com/
---
