---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'The Ximilar REST API at https://api.ximilar.com. One account token in an ''Authorization: Token'' header unlocks every service the active plan includes: fashion, home-decor and photo tagging, collectibl'
  name: Ximilar API
  slug: ximilar
artifact_total: 9
asyncapis:
- description: ''
  name: Ximilar Webhooks
  slug: ximilar-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.ximilar.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.ximilar.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ximilar.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ximilar.com/services
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ximilar.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.ximilar.com/faq/
- group: operate
  title: ''
  type: Contact
  url: https://www.ximilar.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.ximilar.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.ximilar.com/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ximilar-com
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.com/ximilar-public/ximilar-client
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ximilar
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ximilar.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.ximilar.com/register
- group: start
  title: ''
  type: Login
  url: https://app.ximilar.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ximilar.com/terms-of-use-privacy/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ximilar.com/terms-of-use-privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.ximilar.com/how-we-handle-data/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ximilar.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.ximilar.com/llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/ximilar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ximilar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ximilar-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/ximilar-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ximilar-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ximilar-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ximilar-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ximilar-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/ximilar-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ximilar-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ximilar-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ximilar-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ximilar-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ximilar-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ximilar-domain-security.yml
created: '2025-03-01'
description: Ximilar is a Czech visual-AI company that sells computer vision as a REST API and a no-code platform. Its api.ximilar.com surface covers image recognition and tagging (fashion, home decor, stock photo), collectibles AI (trading-card, sports-card and comic identification, AI card grading and TCG price search), visual search and similarity (reverse image search, product matching, multimodal text-to-image), OCR, background removal and image upscaling, plus a Computer Vision Platform for training custom classification, regression, detection and vision-language models and chaining them with Flows. Everything is billed in API credits against a monthly plan allowance, authenticated with a single account token, and callable synchronously or through an asynchronous request API with webhook callbacks. Ximilar also publishes a first-party Python SDK and a local MCP server exposing eleven of its services to LLM clients.
finops:
- name: Ximilar Finops
  service_category: API
  slug: ximilar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ximilar.png
layout: provider
mcp_servers:
- description: 'Ximilar publishes a first-party MCP server for its Computer Vision Platform. It is a Python FastMCP server distributed inside the official ximilar-client repository (ximilar/server/server.py) and run '
  name: Ximilar MCP Server
  slug: ximilar-mcp-server
- description: ''
  name: Ximilar MCP Server
  slug: ximilar-mcp-server-2
modified: '2026-08-28'
name: Ximilar
nav: Providers
network: true
overview: 'Ximilar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Computer-Vision, Image Recognition, Visual Search, Image Tagging, and Machine-Learning.


  The Ximilar catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ximilar''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Ximilar Plans Pricing
  plan_count: 16
  slug: ximilar-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 9
  name: Ximilar Rate Limits
  slug: ximilar-rate-limits
score:
  band: strong
  composite: 58.8
  coverage:
    artifact_dirs: 17
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 48.1
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 58.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ximilar/refs/heads/main/screenshots/ximilar-2026-06-20T201703.png
security:
- kind: authentication
  name: Ximilar Authentication
  slug: ximilar-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ximilar Domain Security
  slug: ximilar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ximilar
tags:
- Computer-Vision
- Image Recognition
- Visual Search
- Image Tagging
- Machine-Learning
- Artificial Intelligence
- OCR
- Collectibles
- Fashion
- E-Commerce
- MCP
- Image Processing
website: https://www.ximilar.com/
---
