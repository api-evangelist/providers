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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: 'The Clerk.io API provides REST endpoints for managing products, categories, orders, customers, recommendations, and search. The API uses a dual-key authentication model: a public key identifies the st'
  name: Clerk.io API
  slug: clerk-io-api
- description: Clerk.js is the browser-side JavaScript library for embedding Clerk.io recommendation slots, search, and email opens on a storefront, with Liquid templating support and event tracking.
  name: Clerk.js Client Library
  slug: clerkjs
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/clerk-io-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clerk-io-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clerkio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clerk-io
- group: company
  title: ''
  type: Website
  url: https://www.clerk.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.clerk.io/
- group: other
  title: ''
  type: Knowledgebase
  url: https://help.clerk.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clerk.io/
- group: company
  title: ''
  type: Blog
  url: https://www.clerk.io/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clerk.io/pricing
- group: company
  title: ''
  type: Partners
  url: https://www.clerk.io/partners
- group: auth
  title: ''
  type: Trust Center
  url: https://trust.clerk.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clerk.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clerk.io/privacy
- group: design
  title: ''
  type: JSONLD
  url: json-ld/clerk-io-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/clerk-io-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.clerk.io/llms.txt
created: '2025-02-08'
description: Clerk.io is an e-commerce personalization platform that uses artificial intelligence and machine learning to deliver tailored product recommendations, on-site search results, audience-segmented email campaigns, and merchandising controls for online retailers. The platform exposes a REST API for product, category, order, and customer data ingestion, plus client-side JavaScript and Liquid templating for recommendation slots and search experiences.
finops:
- name: Clerk Io Finops
  service_category: API
  slug: clerk-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clerk-io.png
jsonld:
- class_count: 0
  name: Clerk Io Context
  property_count: 5
  slug: clerk-io-context
layout: provider
modified: '2026-04-26'
name: Clerk.io
nav: Providers
network: true
overview: 'Clerk.io publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Commerce, E-Commerce, Email Marketing, and Personalization.


  The Clerk.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clerk.io''s developer surface includes documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Clerk Io Plans Pricing
  plan_count: 3
  slug: clerk-io-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 5
  name: Clerk Io Rate Limits
  slug: clerk-io-rate-limits
rules:
- name: Clerk.io API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: clerk-io-rules
score:
  band: developing
  composite: 45.3
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 48.4
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 20.8
    operational_transparency: 52.6
  previous_composite: 45.3
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clerk-io/refs/heads/main/screenshots/clerk-io-2026-06-20T174507.png
security:
- kind: domain-security
  name: Clerk Io Domain Security
  slug: clerk-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Clerk Io Trust Center
  slug: clerk-io-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: clerk-io
tags:
- AI
- Commerce
- E-Commerce
- Email Marketing
- Personalization
- Recommendations
- Search
website: https://www.clerk.io/
---
