---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Kairos Ar Agentic Access
  operation_count: 13
  slug: kairos-ar-agentic-access
  summary_line: 13 operations · 11 acting
api_count: 3
apis:
- description: Analyze emotion, demographics and attention in images and video.
  name: Kairos AR Emotion Analysis API
  slug: kairos-ar-emotion-analysis-api
- description: Detect, enroll, verify and recognize faces in photos against galleries.
  name: Kairos AR Face Recognition API
  slug: kairos-ar-face-recognition-api
- description: Manage galleries and the subjects/face templates enrolled in them.
  name: Kairos AR Galleries API
  slug: kairos-ar-galleries-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kairos Face Recognition & Emotion Analysis API
  slug: open-kairos-ar-emotion-analysis-api
- collection_type: open
  name: Kairos & Emotion Analysis Face Recognition API
  slug: open-kairos-ar-face-recognition-api
- collection_type: open
  name: Kairos Face Recognition & Emotion Analysis Galleries API
  slug: open-kairos-ar-galleries-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/kairos-ar-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://kairos.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.kairos.com
- group: docs
  title: ''
  type: Documentation
  url: https://face.kairos.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://face.kairos.com/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://face.kairos.com/docs/getting-started-with-kairos-face-recognition
- group: operate
  title: ''
  type: Support
  url: https://www.kairos.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.kairos.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kairosinc
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kairos.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://developer.kairos.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kairos.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kairos.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kairos.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://face.kairos.com/docs/api/changelog
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/566316/SVYnSMHo
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kairos-ar-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kairos-ar-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/kairos-ar-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kairos-ar-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kairos-ar-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kairos-ar-sandbox.yml
- group: operate
  title: ''
  type: Changelog
  url: changelog/kairos-ar-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kairos-ar-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Kairos AR, Inc. is a Miami-based human-analytics company providing face recognition, facial detection, and emotion analysis as a REST API. The platform lets developers enroll, verify, and recognize faces against galleries they create, detect faces and facial features (age, gender, ethnicity, glasses, landmarks) in photos, and analyze emotion, demographics and attention across images and video. Requests and responses are JSON and every call is authenticated with an app_id + app_key header pair. Kairos ships official SDKs for JavaScript, PHP, Android, and .NET, publishes an Apiary-hosted API reference with a live sandbox console, and offers a free tier plus usage-based pricing and an on-premise biometric offering. The company was surfaced as a 500 Global portfolio company and is enriched here into the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kairos-ar.png
layout: provider
mcp_servers:
- description: ''
  name: kairos-ar-mcp.yml
  slug: kairos-ar-mcpyml
modified: '2026-07-19'
name: Kairos AR
nav: Providers
network: true
overview: 'Kairos AR publishes 3 APIs on the [APIs.io](https://apis.io/) network: Emotion Analysis API, Face Recognition API, and Galleries API. Tagged areas include Company, Face Recognition, Facial Recognition, Biometrics, and Emotion Analysis.


  Kairos AR''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 18 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 50.3
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 58.2
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kairos-ar/refs/heads/main/screenshots/kairos-ar-2026-07-25T223414.png
security:
- kind: authentication
  name: Kairos Ar Authentication
  slug: kairos-ar-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Kairos Ar Domain Security
  slug: kairos-ar-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kairos-ar
tags:
- Company
- Face Recognition
- Facial Recognition
- Biometrics
- Emotion Analysis
- Computer Vision
- Identity
- Artificial Intelligence
- Machine Learning
- Image Analysis
website: https://kairos.com
---
