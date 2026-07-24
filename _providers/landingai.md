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
  band: agent-native
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
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 61.5
  scored_at: '2026-07-23'
api_count: 13
apis:
- description: The Classes API from Landing.ai — 1 operation(s) for classes.
  name: Landing.ai Classes API
  slug: landingai-classes-api
- description: The Deployment API from Landing.ai — 2 operation(s) for deployment.
  name: Landing.ai Deployment API
  slug: landingai-deployment-api
- description: The Extract API from Landing.ai — 3 operation(s) for extract.
  name: Landing.ai Extract API
  slug: landingai-extract-api
- description: The Image API from Landing.ai — 5 operation(s) for image.
  name: Landing.ai Image API
  slug: landingai-image-api
- description: The Metadata API from Landing.ai — 2 operation(s) for metadata.
  name: Landing.ai Metadata API
  slug: landingai-metadata-api
- description: The Metrics API from Landing.ai — 1 operation(s) for metrics.
  name: Landing.ai Metrics API
  slug: landingai-metrics-api
- description: The Model API from Landing.ai — 3 operation(s) for model.
  name: Landing.ai Model API
  slug: landingai-model-api
- description: The Parse API from Landing.ai — 3 operation(s) for parse.
  name: Landing.ai Parse API
  slug: landingai-parse-api
- description: The Project API from Landing.ai — 3 operation(s) for project.
  name: Landing.ai Project API
  slug: landingai-project-api
- description: The Snapshot API from Landing.ai — 3 operation(s) for snapshot.
  name: Landing.ai Snapshot API
  slug: landingai-snapshot-api
- description: The Tags API from Landing.ai — 2 operation(s) for tags.
  name: Landing.ai Tags API
  slug: landingai-tags-api
- description: The Tools API from Landing.ai — 50 operation(s) for tools.
  name: Landing.ai Tools API
  slug: landingai-tools-api
- description: The Training API from Landing.ai — 6 operation(s) for training.
  name: Landing.ai Training API
  slug: landingai-training-api
artifact_total: 20
common:
- group: company
  title: ''
  type: Website
  url: https://landing.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.landing.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.landing.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.landing.ai/api-reference/parse/ade-parse
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.landing.ai/dpt3/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.landing.ai/support
- group: company
  title: ''
  type: Blog
  url: https://www.landing.ai/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/landing-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.landing.ai/pricing-agentic-apis
- group: start
  title: ''
  type: SignUp
  url: https://ade.landing.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.landing.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.landing.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.landing.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.landing.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.landing.ai/
- group: auth
  title: ''
  type: Security
  url: https://www.landing.ai/security-at-landingai
- group: start
  title: ''
  type: Sandbox
  url: sandbox/landingai-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/landingai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/landingai-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/landingai-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/landingai-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/landingai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/landingai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/landingai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/landingai-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.landing.ai/ade/ade-overview-legacy
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/landingai-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/landingai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/landingai-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/landingai-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/landingai-plans.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/landingai-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/landingai-domain-security.yml
created: '2026-07-17'
description: 'LandingAI, founded by Andrew Ng, builds production AI for visual and document understanding. Its flagship product is Agentic Document Extraction (ADE), which converts real-world documents — PDFs, images, Office files and spreadsheets — into structured, auditable data. ADE exposes a family of REST APIs: Parse (document to reading-order Markdown plus hierarchical blocks with per-block visual grounding), Extract (schema-driven field extraction with character-span grounding back into the source), Build Extract Schema, and the preview Classify, Section and Split APIs, each available synchronously or as asynchronous Jobs for large files. The current generation runs on the DPT-3 document pre-trained transformer. LandingAI also operates LandingLens, a computer-vision platform API for creating projects, uploading images, defining classes, training models and deploying them to LandingAI-hosted cloud endpoints, plus a Vision Tools API surfacing OWLv2, Florence-2, SAM2, CountGD, Depth
  Anything, PaddleOCR and other vision models as HTTP tools. The company ships official Python and TypeScript ADE libraries, a hosted remote MCP server, published Agent Skills, an llms.txt agent surface, US and EU data residency, and SOC 2 Type II, HIPAA and GDPR compliance with a zero data retention option.'
image: https://landing.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: landingai-mcp.yml
  slug: landingai-mcpyml
modified: '2026-07-19'
name: Landing.ai
nav: Providers
network: true
overview: 'Landing.ai publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Classes API, Deployment API, Extract API, and 10 more. Tagged areas include Company, Artificial Intelligence, Machine Learning, Document Extraction, and Document Processing.


  Landing.ai''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Landingai Plans
  plan_count: 3
  slug: landingai-plans
random_paper: 17
rate_limits:
- limit_count: 0
  name: Landingai Rate Limits
  slug: landingai-rate-limits
score:
  band: strong
  composite: 63.9
  delta: 0.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 49.0
    developer_ergonomics: 80.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 55.3
  previous_composite: 63.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Landingai Authentication
  slug: landingai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Landingai Domain Security
  slug: landingai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Landingai Vulnerability Disclosure
  slug: landingai-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Landingai Trust Center
  slug: landingai-trust-center
  summary_line: SOC 2 Type II, HIPAA, GDPR
slug: landingai
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Document Extraction
- Document Processing
- Computer Vision
- OCR
- Data Extraction
- Agents
- Developer Tools
website: https://landing.ai/
---
