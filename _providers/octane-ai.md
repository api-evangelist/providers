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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 22.3
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 5
asyncapis:
- description: ''
  name: Octane Ai Webhooks
  slug: octane-ai-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://octaneai.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.octaneai.com/en/collections/9496268-developer-docs
- group: docs
  title: ''
  type: Documentation
  url: https://help.octaneai.com
- group: start
  title: ''
  type: GettingStarted
  url: https://help.octaneai.com/en/articles/4346619-getting-started-with-quizzes
- group: operate
  title: ''
  type: Support
  url: https://help.octaneai.com
- group: company
  title: ''
  type: Blog
  url: https://octaneai.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://octaneai.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.octaneai.com/dashboard/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.octaneai.com/dashboard/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://octaneai.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://octaneai.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/octaneai
- group: auth
  title: ''
  type: Authentication
  url: authentication/octane-ai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/octane-ai-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/octane-ai-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/octane-ai-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/octane-ai-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/octane-ai-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/octane-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/octane-ai-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/octane-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/octane-ai-conformance.yml
created: '2026-07-17'
description: 'Octane AI is an AI-powered quiz and product-recommendation platform for Shopify merchants, turning storefront browsers into buyers with no-code personalized quizzes, zero-party data capture, and its CORE-1 recommendation engine. It integrates with 50+ marketing, CRM, and automation tools (Klaviyo, Attentive, Postscript, Recharge, Gorgias, Zapier, Alloy) and syncs shopper data in real time. Its developer surface is client-side rather than a public REST API: an embeddable quiz widget that dispatches a documented set of browser JavaScript events (octane.quiz.*), custom CSS/JS injection hooks, a headless-store integration path, and a per-account API key plus webhook secret used for integrations and outbound webhook verification. Backed by Bullpen Capital and General Catalyst.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/octane-ai.png
layout: provider
modified: '2026-08-13'
name: Octane AI
nav: Providers
network: true
overview: 'Octane AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Shopify, E-Commerce, Product Recommendations, and Quizzes.


  The Octane AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Octane AI''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, authentication, and 15 more developer resources.'
plans:
- name: Octane Ai Plans Pricing
  plan_count: 4
  slug: octane-ai-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Octane Ai Rate Limits
  slug: octane-ai-rate-limits
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 14
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 50.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 43.9
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/octane-ai/refs/heads/main/screenshots/octane-ai-2026-08-07T185929.png
security:
- kind: authentication
  name: Octane Ai Authentication
  slug: octane-ai-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Octane Ai Domain Security
  slug: octane-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: octane-ai
tags:
- Company
- Shopify
- E-Commerce
- Product Recommendations
- Quizzes
- Personalization
- Zero-Party Data
- Marketing
- Conversion Optimization
- Artificial Intelligence
website: https://octaneai.com
---
