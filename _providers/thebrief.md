---
access_model:
  confidence: high
  label: Self-service with free trial
  onboarding: unknown
  pricing: paid
  public: true
  source:
  - https://www.thebrief.ai/pricing/
  - https://docs.thebrief.ai/public-api
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: The Brief's versioned REST API for creative automation — list and search designs, templates and brand templates, read a template's editable elements and size variants, submit exports with element chan
  name: The Brief Public REST API
  slug: the-brief-public-rest-api
- description: A single POST GraphQL endpoint exposing the same data core as the REST API with arbitrary field selection — 48 queries and 49 mutations across designs, templates, brand kits, projects, folders, export
  name: The Brief Public GraphQL API
  slug: the-brief-public-graphql-api
artifact_total: 8
asyncapis:
- description: ''
  name: Thebrief Webhooks
  slug: thebrief-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/thebrief-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.thebrief.ai/security/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thebrief-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.thebrief.ai
- group: company
  title: ''
  type: Blog
  url: https://www.thebrief.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.thebrief.ai/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/thebrief-plans-pricing.yml
- group: operate
  title: ''
  type: Support
  url: https://help.thebrief.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.thebrief.ai/learning-hub/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thebrief.ai/legal-information/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thebrief.ai/legal-information/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thebrief-ai
- group: start
  title: ''
  type: Login
  url: https://app.thebrief.ai/
- group: start
  title: ''
  type: SignUp
  url: https://app.thebrief.ai/auth/create-account
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thebrief-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thebrief-docs-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.thebrief.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thebrief.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.thebrief.ai/public-api
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/thebrieftechnical/the-brief-api/collection/1lfct1g/graphql-api
- group: docs
  title: ''
  type: GraphQL
  url: graphql/thebrief-public.graphql
- group: auth
  title: ''
  type: Authentication
  url: authentication/thebrief-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/thebrief-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/thebrief-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/thebrief-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/thebrief-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/thebrief-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/thebrief-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/thebrief-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/thebrief-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/thebrief-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: The Brief (formerly Creatopy) is an AI-powered advertising creation platform that helps brands and agencies discover, create, launch, and optimize ads at scale. Its Ad Studio, AI agents (Discover, Create, Optimize), and native ad server generate on-brand creatives, resize a single design into 50+ ad formats, publish directly to networks like Meta, Google Ads, CM360, DV360 and Veeva, and optimize campaign performance with data-backed recommendations. Founded in 2021 and based in Romania, The Brief is a portfolio company of Point Nine. It ships a documented Public API on two co-equal surfaces — a REST API at https://api.thebrief.ai/v1 and a single GraphQL endpoint at https://graphql.thebrief.ai/public whose 186-type schema is readable by anonymous introspection — covering designs and templates, brand kits, projects and folders, exports and creatives, ad serving and ad-tag reporting, team users and roles, credits, and team webhooks. Authentication is a JWT bearer token minted from
  a clientId/clientSecret pair; the same signed token powers the App Integration flow that embeds the Ad Studio editor inside a customer's own product. No OpenAPI is published.
image: https://cdn.sanity.io/images/8wzdrx7x/production/d9d93597b665708876d106aed92e87d0addafc41-760x175.svg
layout: provider
modified: '2026-08-12'
name: TheBrief
nav: Providers
network: true
overview: 'TheBrief publishes 1 API on the [APIs.io](https://apis.io/) network: The Brief Public GraphQL API. Tagged areas include Company, Advertising, Creative, Design, and Artificial Intelligence.


  The TheBrief catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TheBrief''s developer surface includes engineering blog, pricing, support, getting-started guide, signup flow, documentation, API reference, and 25 more developer resources.'
plans:
- name: Thebrief Plans Pricing
  plan_count: 4
  slug: thebrief-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Thebrief Rate Limits
  slug: thebrief-rate-limits
score:
  band: strong
  composite: 55.7
  coverage:
    artifact_dirs: 18
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 4.5
    contract_quality: 54.3
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 55.7
  provenance:
    conformance: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thebrief/refs/heads/main/screenshots/thebrief-2026-08-17T082340.png
security:
- kind: authentication
  name: Thebrief Authentication
  slug: thebrief-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Thebrief Domain Security
  slug: thebrief-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Thebrief Trust Center
  slug: thebrief-trust-center
  summary_line: ISO 27001, GDPR
slug: thebrief
tags:
- Company
- Advertising
- Creative
- Design
- Artificial Intelligence
- Marketing
- Ad Serving
- Software-as-a-Service
- GraphQL
- Creative Automation
- Digital Asset Management
- Webhook
website: https://www.thebrief.ai
---
