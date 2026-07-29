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
- acting_count: 29
  human_in_the_loop: 1
  name: Codeproject Agentic Access
  operation_count: 42
  slug: codeproject-agentic-access
  summary_line: 42 operations · 29 acting · 1 human-in-the-loop
api_count: 13
apis:
- description: Articles, technical blogs, and tips and tricks (rating >= 3.0).
  name: CodeProject Articles API
  slug: codeproject-articles-api
- description: Sound classification.
  name: CodeProject Audio API
  slug: codeproject-audio-api
- description: Latest messages for a forum or message thread.
  name: CodeProject ForumMessages API
  slug: codeproject-forummessages-api
- description: Background removal, cartoonise, portrait filter, super-resolution.
  name: CodeProject Image-Processing API
  slug: codeproject-image-processing-api
- description: Authenticated user resources (answers, articles, blogs, bookmarks, notifications, profile, reputation, tips).
  name: CodeProject My API
  slug: codeproject-my-api
- description: Q&A questions (new, active, unanswered).
  name: CodeProject Questions API
  slug: codeproject-questions-api
- description: Server status, version, logs, and update checks.
  name: CodeProject Status API
  slug: codeproject-status-api
- description: Sentiment analysis and summarization.
  name: CodeProject Text API
  slug: codeproject-text-api
- description: Custom YOLO dataset and model training lifecycle.
  name: CodeProject Training API
  slug: codeproject-training-api
- description: Automatic license-plate recognition.
  name: CodeProject Vision-ALPR API
  slug: codeproject-vision-alpr-api
- description: Object detection across general and custom YOLO models.
  name: CodeProject Vision-Detection API
  slug: codeproject-vision-detection-api
- description: Face detection, comparison, registration, and recognition.
  name: CodeProject Vision-Face API
  slug: codeproject-vision-face-api
- description: Scene classification.
  name: CodeProject Vision-Scene API
  slug: codeproject-vision-scene-api
artifact_total: 24
collections:
- collection_type: open
  name: CodeProject.AI Server API
  slug: open-codeproject-ai-server
- collection_type: open
  name: CodeProject REST API
  slug: open-codeproject-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/codeproject-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codeproject-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/codeproject-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/codeproject-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-code-project
- group: company
  title: ''
  type: Website
  url: https://www.codeproject.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.codeproject.com/Help
- group: build
  title: ''
  type: Samples
  url: https://api.codeproject.com/Samples
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.codeproject.com/Terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.codeproject.com/privacy
- group: operate
  title: ''
  type: Forums
  url: https://www.codeproject.com/Lounge.aspx
- group: learn
  title: ''
  type: Tutorials
  url: https://www.codeproject.com/KB/
- group: operate
  title: ''
  type: Support
  url: https://www.codeproject.com/Questions/
- group: company
  title: ''
  type: Newsletter
  url: https://www.codeproject.com/newsletters
- group: start
  title: ''
  type: Portal
  url: https://codeproject.ai/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/codeproject
- group: design
  title: ''
  type: JSONLD
  url: json-ld/codeproject-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/codeproject-rules.yml
created: '2025-01-01'
description: CodeProject is a long-running online community for software developers founded in 1999, hosting hundreds of thousands of developer-contributed articles, tutorials, code samples, tips, and a Q&A forum across a broad range of programming topics. It exposes a public REST API at api.codeproject.com (V1 Beta) for read access to articles, forum messages, questions, and authenticated user data, secured by OAuth 2.0 Bearer Tokens. CodeProject also operates CodeProject.AI Server, a free, open-source, self-hosted AI service that exposes object detection, face recognition, license-plate reading (ALPR), scene classification, image processing, audio classification, text analytics, and YOLOv5 training through a local HTTP REST API. CodeProject.AI is widely integrated with home-automation and surveillance platforms (Blue Iris, Home Assistant, Agent DVR).
finops:
- name: Codeproject Finops
  service_category: API
  slug: codeproject-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/codeproject.png
jsonld:
- class_count: 0
  name: Codeproject Context
  property_count: 7
  slug: codeproject-context
layout: provider
modified: '2026-05-19'
name: CodeProject
nav: Providers
network: true
overview: 'CodeProject publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Articles API, Audio API, ForumMessages API, and 10 more. Tagged areas include AI, Articles, Community, Computer Vision, and Developer Community.


  The CodeProject catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CodeProject''s developer surface includes authentication, documentation, support, developer portal, GitHub presence, and 13 more developer resources.'
plans:
- name: Codeproject Plans Pricing
  plan_count: 3
  slug: codeproject-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 5
  name: Codeproject Rate Limits
  slug: codeproject-rate-limits
rules:
- name: CodeProject API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 3
  slug: codeproject-rules
scopes:
- name: Codeproject Scopes
  scope_count: 1
  slug: codeproject-scopes
  summary_line: 1 scope · clientCredentials/authorizationCode/implicit
score:
  band: developing
  composite: 46.3
  delta: -4.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 49.0
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 27.1
    operational_transparency: 36.8
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codeproject/refs/heads/main/screenshots/codeproject-2026-06-20T174804.png
security:
- kind: authentication
  name: Codeproject Authentication
  slug: codeproject-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Codeproject Domain Security
  slug: codeproject-domain-security
  summary_line: TLSv1.3 · DMARC
slug: codeproject
tags:
- AI
- Articles
- Community
- Computer Vision
- Developer Community
- Face Recognition
- Forum
- Knowledge Base
- License Plate Recognition
- Object Detection
- Q&A
- Software Development
- Tutorials
website: https://www.codeproject.com/
---
