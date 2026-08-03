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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-08-03'
api_count: 12
apis:
- description: The Call Notes API from Proton.ai — 4 operation(s) for call notes.
  name: Proton.ai Call Notes API
  slug: protonai-call-notes-api
- description: The Contacts API from Proton.ai — 3 operation(s) for contacts.
  name: Proton.ai Contacts API
  slug: protonai-contacts-api
- description: The Custom Fields API from Proton.ai — 5 operation(s) for custom fields.
  name: Proton.ai Custom Fields API
  slug: protonai-custom-fields-api
- description: The Customers API from Proton.ai — 4 operation(s) for customers.
  name: Proton.ai Customers API
  slug: protonai-customers-api
- description: The Leads API from Proton.ai — 3 operation(s) for leads.
  name: Proton.ai Leads API
  slug: protonai-leads-api
- description: The Opportunities API from Proton.ai — 8 operation(s) for opportunities.
  name: Proton.ai Opportunities API
  slug: protonai-opportunities-api
- description: The Product Initiatives API from Proton.ai — 1 operation(s) for product initiatives.
  name: Proton.ai Product Initiatives API
  slug: protonai-product-initiatives-api
- description: The Quotes API from Proton.ai — 3 operation(s) for quotes.
  name: Proton.ai Quotes API
  slug: protonai-quotes-api
- description: The Recommendations API from Proton.ai — 7 operation(s) for recommendations.
  name: Proton.ai Recommendations API
  slug: protonai-recommendations-api
- description: The Search API from Proton.ai — 1 operation(s) for search.
  name: Proton.ai Search API
  slug: protonai-search-api
- description: The Tasks API from Proton.ai — 2 operation(s) for tasks.
  name: Proton.ai Tasks API
  slug: protonai-tasks-api
- description: The Tracking API from Proton.ai — 2 operation(s) for tracking.
  name: Proton.ai Tracking API
  slug: protonai-tracking-api
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/protonai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/protonai-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/protonai-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.proton.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://api.proton.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://api.proton.ai/
- group: build
  title: ''
  type: Postman
  url: https://api.proton.ai/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.proton.ai/
- group: operate
  title: ''
  type: Support
  url: https://help.proton.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.proton.ai/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.proton.ai/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.proton.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.proton.ai/privacy-policy
created: '2026-07-17'
description: Proton.ai is an AI industry cloud platform built for B2B distributors, combining an AI-guided CRM, product information management, e-commerce recommendation engine, and order-capture automation on top of a distributor's existing ERP and e-commerce systems. Proton exposes a public REST API (documented via Postman at api.proton.ai) offering an AI-powered suite of endpoints for product recommendations (cart, reorder, similar items, bought-also-bought, recently viewed), behavioral tracking, and CRM operations across customers, contacts, opportunities and pipelines, quotes, leads, call notes, tasks, and tenant-defined custom fields. Authentication is a static API key supplied at onboarding and sent in the X-Api-Key header, with an X-Company tenant header scoping every request. Proton is backed by Battery Ventures and headquartered around a distribution-industry focus.
image: https://content.pstmn.io/9e57cb73-9d7b-4c3a-8915-f860c9e82380/bG9nby0yMDIzLnBuZw==
layout: provider
modified: '2026-07-20'
name: Proton.ai
nav: Providers
network: true
overview: 'Proton.ai publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Call Notes API, Contacts API, Custom Fields API, and 9 more. Tagged areas include Company, CRM, Sales, Distribution, and Artificial Intelligence.


  Proton.ai''s developer surface includes authentication, documentation, API reference, support, engineering blog, signup flow, and 7 more developer resources.'
random_paper: 21
score:
  band: developing
  composite: 42.7
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 60.8
    developer_ergonomics: 37.0
    discoverability: 92.6
    governance: 3.1
    operational_transparency: 15.8
  previous_composite: 42.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Protonai Authentication
  slug: protonai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Protonai Domain Security
  slug: protonai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Protonai Trust Center
  slug: protonai-trust-center
  summary_line: trust center published
slug: protonai
tags:
- Company
- CRM
- Sales
- Distribution
- Artificial Intelligence
- Recommendations
- B2B
- Wholesale Distribution
website: https://www.proton.ai/
---
