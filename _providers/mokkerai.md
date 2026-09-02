---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Early-access v2 REST API that replaces product-photo backgrounds with AI-generated scenes and upscales images — the same functionality as the Mokker web app. Documented with a POST /v2/replace-backgro
  name: Mokker API
  slug: mokker-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mokkerai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mokker.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mokker.ai/api
- group: commercial
  title: ''
  type: Pricing
  url: https://mokker.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://mokker.ai/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.mokker.ai/login
- group: operate
  title: ''
  type: Support
  url: https://support.soona.co/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mokker.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mokker.ai/privacy
created: '2026-07-17'
description: Mokker AI is an AI product-photography tool that replaces the background of a product photo with a realistic, AI-generated scene and upscales images, turning a plain product shot into studio-quality marketing imagery without Photoshop. It serves e-commerce sellers and marketers across categories like cosmetics, electronics, furniture, and jewellery. Mokker is now part of soona (soona.co/mokker) and exposes a v2 REST API in early access that offers the same background-replacement and upscale capabilities as its web app, with free API credits for developers building integrations. Mokker is backed by Point Nine and was added to the API Evangelist network as a portfolio lead.
image: https://framerusercontent.com/assets/xdLOSfokuQlszbASX5TOpMKlZw.jpg
layout: provider
mcp_servers:
- description: ''
  name: Mokker.ai MCP Server
  slug: mokkerai-mcp-server
modified: '2026-07-20'
name: Mokker.ai
nav: Providers
network: true
overview: 'Mokker.ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Image Processing, Product Photography, and E-Commerce.


  Mokker.ai''s developer surface includes pricing, engineering blog, signup flow, support, and 5 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 5
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.9
  provenance:
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mokkerai/refs/heads/main/screenshots/mokkerai-2026-08-07T184055.png
security:
- kind: domain-security
  name: Mokkerai Domain Security
  slug: mokkerai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: mokkerai
tags:
- Company
- Artificial Intelligence
- Image Processing
- Product Photography
- E-Commerce
- Background Removal
- Computer-Vision
- Generative AI
website: https://mokker.ai
---
