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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Bonusly Agentic Access
  operation_count: 31
  slug: bonusly-agentic-access
  summary_line: 31 operations · 12 acting
api_count: 6
apis:
- description: Snapshots and lists of recognition activity for reporting.
  name: Bonusly Analytics API
  slug: bonusly-analytics-api
- description: Peer-to-peer recognition posts that carry points.
  name: Bonusly Bonuses API
  slug: bonusly-bonuses-api
- description: Company-level settings and achievements.
  name: Bonusly Company API
  slug: bonusly-company-api
- description: Conversions of earned points into rewards.
  name: Bonusly Redemptions API
  slug: bonusly-redemptions-api
- description: The catalog of gift cards, donations, and custom rewards.
  name: Bonusly Rewards API
  slug: bonusly-rewards-api
- description: Company members who give and receive recognition.
  name: Bonusly Users API
  slug: bonusly-users-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bonusly Analytics API
  slug: open-bonusly-analytics-api
- collection_type: open
  name: Bonusly Analytics Bonuses API
  slug: open-bonusly-bonuses-api
- collection_type: open
  name: Bonusly Analytics Company API
  slug: open-bonusly-company-api
- collection_type: open
  name: Bonusly Analytics Redemptions API
  slug: open-bonusly-redemptions-api
- collection_type: open
  name: Bonusly Analytics Rewards API
  slug: open-bonusly-rewards-api
- collection_type: open
  name: Bonusly Analytics Users API
  slug: open-bonusly-users-api
- collection_type: open
  name: Bonusly API
  slug: open-bonusly
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bonusly-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bonusly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bonusly-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bonusly
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bonusly
- group: company
  title: ''
  type: Website
  url: https://bonusly.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bonus.ly/
- group: commercial
  title: ''
  type: Plans
  url: plans/bonusly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bonusly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bonusly-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://bonusly.com/blog
created: '2026-07-10'
description: Bonusly is an employee recognition and rewards platform that lets coworkers give each other small, frequent, public bonuses tied to company values, which recipients redeem for gift cards, custom rewards, donations, and more. The Bonusly REST API (base https://bonus.ly/api/v1) exposes the same surface the product is built on - bonuses, users, the reward catalog, redemptions, awards, company settings, and analytics - authenticated with a Bearer personal access token. API access is available on paid plans; tokens are minted by admins with fine-grained read / write / administer scopes.
finops:
- name: Bonusly Finops
  service_category: HR and Employee Engagement
  slug: bonusly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bonusly.png
layout: provider
modified: '2026-07-10'
name: Bonusly
nav: Providers
network: true
overview: 'Bonusly publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Bonuses API, Company API, and 3 more. Tagged areas include Employee Recognition, Rewards, Employee Engagement, HR, and Company Culture.


  Bonusly''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Bonusly Plans Pricing
  plan_count: 4
  slug: bonusly-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Bonusly Rate Limits
  slug: bonusly-rate-limits
score:
  band: developing
  composite: 39.9
  delta: 1.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 58.6
    developer_ergonomics: 27.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bonusly/refs/heads/main/screenshots/bonusly-2026-07-25T203601.png
security:
- kind: authentication
  name: Bonusly Authentication
  slug: bonusly-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bonusly Domain Security
  slug: bonusly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bonusly
tags:
- Employee Recognition
- Rewards
- Employee Engagement
- HR
- Company Culture
- Bonuses
website: https://bonusly.com
---
