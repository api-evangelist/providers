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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Apollo Enrich Agentic Access
  operation_count: 14
  slug: apollo-enrich-agentic-access
  summary_line: 14 operations · 13 acting
api_count: 7
apis:
- description: Manage accounts (companies) saved to your Apollo team.
  name: Apollo.io Accounts API
  slug: apollo-enrich-accounts-api
- description: Manage contacts saved in your Apollo account.
  name: Apollo.io Contacts API
  slug: apollo-enrich-contacts-api
- description: Match and enrich company records, single or in bulk.
  name: Apollo.io Organization Enrichment API
  slug: apollo-enrich-organization-enrichment-api
- description: Search Apollo's company database.
  name: Apollo.io Organization Search API
  slug: apollo-enrich-organization-search-api
- description: Match and enrich person records, single or in bulk.
  name: Apollo.io People Enrichment API
  slug: apollo-enrich-people-enrichment-api
- description: Search Apollo's people database for prospects.
  name: Apollo.io People Search API
  slug: apollo-enrich-people-search-api
- description: Manage sequences (emailer campaigns) and outreach emails.
  name: Apollo.io Sequences API
  slug: apollo-enrich-sequences-api
artifact_total: 13
collections:
- collection_type: open
  name: Apollo.io API
  slug: open-apollo-enrich
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apollo-enrich-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apollo-enrich-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apolloio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apolloio
- group: company
  title: ''
  type: Website
  url: https://www.apollo.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apollo.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.apollo.io
- group: commercial
  title: ''
  type: Plans
  url: plans/apollo-enrich-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.apollo.io/pricing
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/apollo-enrich-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/apollo-enrich-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.apollo.io/blog
created: '2026-07-11'
description: Apollo.io is a sales intelligence and engagement platform built on a B2B database of hundreds of millions of contacts and companies. Its REST API exposes People Enrichment (single and bulk match), People Search, Organization Enrichment and Search, Contacts and Accounts management, and Sequences (emailer campaigns) for outreach - covering contact discovery, data enrichment, prospecting, and sales intelligence use cases. The API is authenticated with an x-api-key header and is gated behind Apollo's paid plans (API access begins on the Professional tier; some endpoints require a master API key).
finops:
- name: Apollo Enrich Finops
  service_category: Sales Intelligence and Data Enrichment
  slug: apollo-enrich-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apollo-enrich.png
layout: provider
modified: '2026-07-11'
name: Apollo.io
nav: Providers
network: true
overview: 'Apollo.io publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Contacts API, Organization Enrichment API, and 4 more. Tagged areas include Contact Discovery, Data Enrichment, Sales Intelligence, B2B Data, and Prospecting.


  Apollo.io''s developer surface includes authentication, documentation, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Apollo Enrich Plans Pricing
  plan_count: 5
  slug: apollo-enrich-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 6
  name: Apollo Enrich Rate Limits
  slug: apollo-enrich-rate-limits
score:
  band: developing
  composite: 43.4
  delta: -2.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.4
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apollo-enrich/refs/heads/main/screenshots/apollo-enrich-2026-07-25T200708.png
security:
- kind: authentication
  name: Apollo Enrich Authentication
  slug: apollo-enrich-authentication
  summary_line: apiKey · 1 scheme
slug: apollo-enrich
tags:
- Contact Discovery
- Data Enrichment
- Sales Intelligence
- B2B Data
- Prospecting
- Web Intelligence
- Lead Generation
- People Search
website: https://www.apollo.io
---
