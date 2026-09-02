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
  band: human-only
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Product Hunt API provides programmatic access to Product Hunt's platform data via GraphQL. Developers can query and retrieve information about products, posts, topics, collections, users, votes, a
  name: Product Hunt API
  slug: product-hunt-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/product-hunt-domain-security.yml
created: '2026-03-24'
description: Product Hunt is a platform for discovering new tech products, connecting makers with early adopters and enthusiasts. Each day, Product Hunt surfaces the best new products in technology including apps, websites, hardware projects, and developer tools, allowing the community to vote, comment, and discuss. It is widely used by founders to launch products and by developers and tech enthusiasts to stay current with the latest innovations in the startup and tech product ecosystem.
finops:
- name: Product Hunt Finops
  service_category: API
  slug: product-hunt-finops
graphqls:
- description: The Product Hunt API provides programmatic access to Product Hunt's platform data via GraphQL. Developers can query and retrieve information about products, posts, topics, collections, users, votes, a
  name: Product Hunt GraphQL API
  slug: product-hunt-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/product-hunt.png
layout: provider
modified: '2026-04-28'
name: Product Hunt
nav: Providers
network: true
overview: Product Hunt publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Product Discovery, Startups, Tech Products, and Maker Community.
plans:
- name: Product Hunt Plans Pricing
  plan_count: 3
  slug: product-hunt-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Product Hunt Rate Limits
  slug: product-hunt-rate-limits
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Product Hunt Domain Security
  slug: product-hunt-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: product-hunt
tags:
- Product Discovery
- Startups
- Tech Products
- Maker Community
---
