---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Tenyks Agentic Access
  operation_count: 8
  slug: tenyks-agentic-access
  summary_line: 8 operations · 7 acting
api_count: 1
apis:
- baseURL: https://dashboard.tenyks.ai
  baseurl_source: declared
  description: Obtain a Bearer access token from an API key and secret.
  name: Tenyks Auth API
  slug: tenyks-auth-api
- baseURL: https://dashboard.tenyks.ai
  baseurl_source: declared
  description: Upload and ingest annotations, models and predictions from cloud storage.
  name: Tenyks Data Upload API
  slug: tenyks-data-upload-api
- baseURL: https://dashboard.tenyks.ai
  baseurl_source: declared
  description: Create and retrieve datasets.
  name: Tenyks Datasets API
  slug: tenyks-datasets-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tenyks Auth API
  slug: open-tenyks-auth-api
- collection_type: open
  name: Tenyks Auth Data Upload API
  slug: open-tenyks-data-upload-api
- collection_type: open
  name: Tenyks Auth Datasets API
  slug: open-tenyks-datasets-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.tenyks.ai/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tenyks-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tenyks-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tenyks.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tenyks.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tenyks.ai/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tenyks.ai/docs/the-foundations
- group: company
  title: ''
  type: Blog
  url: https://www.tenyks.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tenyks.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://sandbox.tenyks.ai
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/tenyks
- group: auth
  title: ''
  type: Authentication
  url: authentication/tenyks-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tenyks-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tenyks-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/tenyks-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/tenyks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tenyks-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tenyks-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tenyks-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tenyks-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tenyks-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tenyks-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tenyks-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tenyks-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.tenyks.ai
- group: auth
  title: ''
  type: TrustCenter
  url: security/tenyks-trust-center.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tenyks-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Tenyks is a University of Cambridge spin-out (Y Combinator; backed by Speedinvest) building a visual-intelligence platform for computer vision. Its original product is an MLOps monitoring and validation platform that helps ML engineers working with computer-vision data find and fix what is wrong with their models — data-quality analysis, model performance comparison, text-to-image / image-to-image / object-level similarity search, embeddings, tagging and custom metadata across image and video datasets. Tenyks has since extended into a Vision AI / Video AI Agents platform that turns everyday camera feeds into privacy-first operational analytics for brick-and-mortar businesses. The Tenyks API (currently alpha, for Premium/Dashboard users, with a freemium Sandbox) lets teams authenticate with an API key + secret to obtain a Bearer token, then create datasets and models, and upload and ingest annotations and predictions directly from AWS S3, GCS or Azure. A Python SDK and CLI wrap
  the same surface.
image: https://cdn.prod.website-files.com/63a0220866f41638081f4fce/63d07b4812f0f901e939d964_tenyks_logo-color.png
layout: provider
modified: '2026-07-21'
name: Tenyks
nav: Providers
network: true
overview: 'Tenyks publishes 3 APIs on the [APIs.io](https://apis.io/) network: Auth API, Data Upload API, and Datasets API. Tagged areas include Company, Computer-Vision, Machine-Learning, MLOps, and Data Quality.


  Tenyks'' developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 21 more developer resources.'
random_paper: 19
screenshot: https://raw.githubusercontent.com/api-evangelist/tenyks/refs/heads/main/screenshots/tenyks-2026-08-17T082314.png
security:
- kind: authentication
  name: Tenyks Authentication
  slug: tenyks-authentication
  summary_line: http/apiKey-exchange · 1 scheme
- kind: domain-security
  name: Tenyks Domain Security
  slug: tenyks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tenyks Trust Center
  slug: tenyks-trust-center
  summary_line: SOC 2 Type II, GDPR, CCPA
slug: tenyks
tags:
- Company
- Computer-Vision
- Machine-Learning
- MLOps
- Data Quality
- Model Validation
- Visual Intelligence
- Video Analytics
- Artificial Intelligence
- Developer Tools
website: https://www.tenyks.ai/
---
