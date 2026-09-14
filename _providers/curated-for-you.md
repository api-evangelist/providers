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
api_count: 1
apis:
- baseURL: https://api.curatedforyou.io
  baseurl_source: declared
  description: The Chronicle API from Curated for You — 1 operation(s) for chronicle.
  name: Curated for You Chronicle API
  slug: curated-for-you-chronicle-api
- baseURL: https://api.curatedforyou.io
  baseurl_source: declared
  description: The Companies API from Curated for You — 1 operation(s) for companies.
  name: Curated for You Companies API
  slug: curated-for-you-companies-api
- baseURL: https://api.curatedforyou.io
  baseurl_source: declared
  description: The Curations API from Curated for You — 1 operation(s) for curations.
  name: Curated for You Curations API
  slug: curated-for-you-curations-api
- baseURL: https://api.curatedforyou.io
  baseurl_source: declared
  description: The Feedback API from Curated for You — 2 operation(s) for feedback.
  name: Curated for You Feedback API
  slug: curated-for-you-feedback-api
- baseURL: https://api.curatedforyou.io
  baseurl_source: declared
  description: The shopify API from Curated for You — 14 operation(s) for shopify.
  name: Curated for You shopify API
  slug: curated-for-you-shopify-api
- baseURL: https://api.curatedforyou.io
  baseurl_source: declared
  description: The Users API from Curated for You — 1 operation(s) for users.
  name: Curated for You Users API
  slug: curated-for-you-users-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Curated for You Chronicle API
  slug: open-curated-for-you-chronicle-api
- collection_type: open
  name: Curated for You Chronicle Companies API
  slug: open-curated-for-you-companies-api
- collection_type: open
  name: Curated for You Chronicle Curations API
  slug: open-curated-for-you-curations-api
- collection_type: open
  name: Curated for You Chronicle Feedback API
  slug: open-curated-for-you-feedback-api
- collection_type: open
  name: Curated for You Chronicle shopify API
  slug: open-curated-for-you-shopify-api
- collection_type: open
  name: Curated for You Chronicle Users API
  slug: open-curated-for-you-users-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/curated-for-you-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://curatedforyou.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.curatedforyou.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.curatedforyou.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.curatedforyou.io/redoc
- group: company
  title: ''
  type: Blog
  url: https://www.curatedforyou.io/resources
- group: start
  title: ''
  type: SignUp
  url: https://app.curatedforyou.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.curatedforyou.io/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.curatedforyou.io/privacy-policy-1
- group: auth
  title: ''
  type: Authentication
  url: authentication/curated-for-you-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/curated-for-you-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/curated-for-you-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/curated-for-you-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/curated-for-you-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/curated-for-you-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/curated-for-you-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/curated-for-you-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/curated-for-you-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/curated-for-you-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Curated for You is an Austin, Texas lifestyle-commerce platform (Techstars-backed) that matches retail products to shoppers' lifestyles — places, affinities, and trends — using a taxonomy of 1,000+ lifestyle concepts and AI to power product discovery across storefronts, Shopify, web, social, email, and organic search. The company works with retailers such as REVOLVE, Steve Madden, and Saks Off 5th, and has partnered with Microsoft to bring AI-powered curations into Copilot. The Curated for You API (v2, OpenAPI 3.1) lets integrators authenticate, discover the companies they can access, retrieve curations and exported curation snapshots, submit product feedback, and manage Shopify store installs, collections, and analysis/resync jobs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/curated-for-you.png
layout: provider
modified: '2026-07-18'
name: Curated for You
nav: Providers
network: true
overview: 'Curated for You publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Chronicle API, Companies API, Curations API, and 3 more. Tagged areas include Company, E-Commerce, Retail, Product Discovery, and Personalization.


  Curated for You''s developer surface includes documentation, API reference, engineering blog, signup flow, authentication, and 15 more developer resources.'
random_paper: 19
screenshot: https://raw.githubusercontent.com/api-evangelist/curated-for-you/refs/heads/main/screenshots/curated-for-you-2026-07-25T210930.png
security:
- kind: authentication
  name: Curated For You Authentication
  slug: curated-for-you-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Curated For You Domain Security
  slug: curated-for-you-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: curated-for-you
tags:
- Company
- E-Commerce
- Retail
- Product Discovery
- Personalization
- Artificial Intelligence
- Curation
- Shopify
- Lifestyle Commerce
website: https://curatedforyou.io/
---
