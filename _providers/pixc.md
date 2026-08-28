---
access_model:
  confidence: high
  label: Public
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://pixc.com/api/
  - https://pixc.com/photo-editing/
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Pixc Agentic Access
  operation_count: 16
  slug: pixc-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 1
apis:
- description: 'REST API for automated product-photo optimization. Three resources — templates (the reusable photo standard: background, border, shadow, output file types and aspect sizes), orders (a batch of submitt'
  name: Pixc Public API
  slug: pixc-public-api
artifact_total: 11
asyncapis:
- description: ''
  name: Pixc Webhooks
  slug: pixc-webhooks
collections:
- collection_type: open
  name: Pixc Public API Orders
  slug: open-pixc-orders-api
- collection_type: open
  name: Pixc Public API Templates
  slug: open-pixc-templates-api
- collection_type: open
  name: Pixc Public API Webhooks
  slug: open-pixc-webhooks-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pixc.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://pixc.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://dashboard.pixc.com/docs?url=https://dashboard.pixc.com/v1/schema
- group: start
  title: ''
  type: GettingStarted
  url: https://pixc.com/api/#getting-started
- group: company
  title: ''
  type: Website
  url: https://pixc.com
- group: company
  title: ''
  type: Blog
  url: https://pixc.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.pixc.com/en/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Pixc2
- group: start
  title: ''
  type: SignUp
  url: https://pixc.com/dashboard/signup
- group: start
  title: ''
  type: Login
  url: https://pixc.com/dashboard/login
- group: commercial
  title: ''
  type: Pricing
  url: https://pixc.com/photo-editing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pixc.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pixc.com/legal/
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/pixc
- group: build
  title: ''
  type: Packages
  url: packages/pixc-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pixc-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pixc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pixc-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pixc-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pixc-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pixc-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/pixc-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pixc-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pixc-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pixc-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pixc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pixc-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pixc-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pixc-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pixc-domain-security.yml
created: '2026-07-17'
description: Pixc is an ecommerce enablement company that builds Shopify apps automating the visual busywork of running an online store — product photo resizing and AI framing, background removal and retouching, AI-generated alt text for SEO, AI lifestyle imagery, and automated visual merchandising of collections. Founded in 2014 and backed by 500 Global, Pixc also runs a professional bulk product photo-editing service billed in prepaid image credits, and serves 32,000+ Shopify merchants. Pixc publishes a public REST API — the Pixc Public API at https://dashboard.pixc.com/v1 — that lets a store or marketplace automate the same photo optimization programmatically — define a reusable template encoding the photo standard, submit batches of image URLs as orders, register webhooks for completion, and collect the optimized results as image URLs or packaged downloads.
image: https://pixc.com/images/hero-illustration.png
layout: provider
modified: '2026-08-13'
name: Pixc
nav: Providers
network: true
overview: 'Pixc publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Company, Shopify, E-Commerce, Photo Editing, and Image Optimization.


  The Pixc catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pixc''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, pricing, and 24 more developer resources.'
plans:
- name: Pixc Plans Pricing
  plan_count: 4
  slug: pixc-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Pixc Rate Limits
  slug: pixc-rate-limits
scopes:
- name: Pixc Scopes
  scope_count: 11
  slug: pixc-scopes
  summary_line: 11 scopes · implicit
score:
  band: developing
  composite: 54.1
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 16.7
    contract_quality: 56.0
    developer_ergonomics: 73.2
    discoverability: 68.5
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 54.1
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
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pixc/refs/heads/main/screenshots/pixc-2026-08-17T081244.png
security:
- kind: authentication
  name: Pixc Authentication
  slug: pixc-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Pixc Domain Security
  slug: pixc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pixc
tags:
- Company
- Shopify
- E-Commerce
- Photo Editing
- Image Optimization
- Image Processing
- Product Photography
- Background Removal
- SEO
- Automation
- Artificial Intelligence
- Webhook
- Digital Asset Management
website: https://pixc.com
---
