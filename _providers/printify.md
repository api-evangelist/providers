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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Printify Agentic Access
  operation_count: 33
  slug: printify-agentic-access
  summary_line: 33 operations · 18 acting
api_count: 6
apis:
- description: Blueprints, print providers, variants, and shipping in the Printify catalog.
  name: Printify Catalog API
  slug: printify-catalog-api
- description: Order submission, shipping calculation, production, and cancellation.
  name: Printify Orders API
  slug: printify-orders-api
- description: Products in a shop and their publishing lifecycle.
  name: Printify Products API
  slug: printify-products-api
- description: Stores connected to a Printify account.
  name: Printify Shops API
  slug: printify-shops-api
- description: Artwork uploads to the merchant Media Library.
  name: Printify Uploads API
  slug: printify-uploads-api
- description: Event notifications delivered to merchant endpoints.
  name: Printify Webhooks API
  slug: printify-webhooks-api
artifact_total: 14
collections:
- collection_type: open
  name: Printify API
  slug: open-printify
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/printify-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/printify-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/printify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/printify-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://printify.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/printify
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/printify
- group: company
  title: ''
  type: Website
  url: https://printify.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.printify.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/printify-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/printify-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/printify-finops.yml
created: '2026-06-25'
description: Printify is a print-on-demand marketplace connecting merchants with a global network of print providers. The Printify REST API lets applications manage a Printify shop on a merchant's behalf - browsing the catalog of blueprints and print providers, creating and publishing products, submitting and tracking orders, uploading artwork, and subscribing to webhooks.
finops:
- name: Printify Finops
  service_category: Ecommerce and Fulfillment
  slug: printify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/printify.png
layout: provider
modified: '2026-06-25'
name: Printify
nav: Providers
network: true
overview: 'Printify publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Orders API, Products API, and 3 more. Tagged areas include Print on Demand, Ecommerce, Marketplace, Fulfillment, and Merchandise.


  Printify''s developer surface includes authentication, engineering blog, documentation, and 9 more developer resources.'
plans:
- name: Printify Plans Pricing
  plan_count: 3
  slug: printify-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 4
  name: Printify Rate Limits
  slug: printify-rate-limits
score:
  band: thin
  composite: 38.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Printify Authentication
  slug: printify-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Printify Domain Security
  slug: printify-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Printify Vulnerability Disclosure
  slug: printify-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: printify
tags:
- Print on Demand
- Ecommerce
- Marketplace
- Fulfillment
- Merchandise
website: https://printify.com/
---
