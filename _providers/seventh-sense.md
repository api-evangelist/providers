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
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 51.0
  scored_at: '2026-07-27'
api_count: 5
apis:
- description: Collections are groups of registered `Persons`. You can use collections to organize your registered persons and to search for persons within a specific collection. You can also use collections to mana
  name: Seventh Sense Collections API
  slug: seventh-sense-collections-api
- description: The `/liveness` endpoint allows you to determine if a face image is of a real person or a spoofed image (eg. a printed image of a face, or an image captured from a tablet's screen). The endpoint retur
  name: Seventh Sense Face Anti-Spoofing / Liveness API
  slug: seventh-sense-face-anti-spoofing-liveness-api
- description: The `/compare` endpoint allows you to compare two sets of face images to determine if they correspond to the same person. A score higher than 0.81 is a good indicator that the two sets of images belon
  name: Seventh Sense Face Verification API
  slug: seventh-sense-face-verification-api
- description: Persons are registered persons that you can later search for using face images. Registering a person allows you to search for them later using the `/search` endpoint. You can also use the `/person` en
  name: Seventh Sense Persons API
  slug: seventh-sense-persons-api
- description: The endpoints below allow you to search for previously registered persons using a face image obtained at a later time. The search is performed using a deep learning model trained on millions of face i
  name: Seventh Sense Search API
  slug: seventh-sense-search-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seventh-sense-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/seventh-sense-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/seventh-sense-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/seventh-sense-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/seventh-sense-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/seventh-sense-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/seventh-sense-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/seventh-sense-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/seventh-sense-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/seventh-sense-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/seventh-sense-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/seventh-sense-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://seventhsense.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.opencv.fr
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opencv.fr
- group: start
  title: ''
  type: SignUp
  url: https://developer.opencv.fr/ui/#/onboard/register?details=true
created: '2026-07-17'
description: Seventh Sense AI is a Singapore-based deep-tech company building privacy-preserving, face-based identity and biometric verification technology. Its OpenCV Face Recognition (OpenCV FR) platform — ranked among the top 10 facial recognition algorithms globally by NIST — provides face detection, matching, liveness detection, search and person/collection management through a multi-region REST API and Python/C++ SDKs. Seventh Sense also develops the SenseCrypt suite (eID, PKI and self-sovereign identity built on distributed ledgers, "0% biometrics, 100% privacy") and SenseVantage multimodal video AI. The company is SOC, ISO 27001 certified and GDPR compliant, serving enterprise and government customers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/seventh-sense.png
layout: provider
mcp_servers:
- description: ''
  name: seventh-sense-mcp.yml
  slug: seventh-sense-mcpyml
modified: '2026-07-21'
name: Seventh Sense
nav: Providers
network: true
overview: 'Seventh Sense publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Face Anti-Spoofing / Liveness API, Face Verification API, and 2 more. Tagged areas include Company, Face Recognition, Biometrics, Identity Verification, and Liveness Detection.


  Seventh Sense''s developer surface includes authentication, documentation, signup flow, and 14 more developer resources.'
random_paper: 60
score:
  band: thin
  composite: 37.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 51.5
    developer_ergonomics: 50.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 37.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Seventh Sense Authentication
  slug: seventh-sense-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Seventh Sense Domain Security
  slug: seventh-sense-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: seventh-sense
tags:
- Company
- Face Recognition
- Biometrics
- Identity Verification
- Liveness Detection
- Artificial Intelligence
- Computer Vision
- Security
website: https://seventhsense.ai
---
