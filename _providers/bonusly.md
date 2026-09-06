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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Bonusly Agentic Access
  operation_count: 31
  slug: bonusly-agentic-access
  summary_line: 31 operations · 12 acting
api_count: 1
apis:
- baseURL: https://bonus.ly/api/v1
  baseurl_source: declared
  description: Snapshots and lists of recognition activity for reporting.
  name: Bonusly Analytics API
  slug: bonusly-analytics-api
- baseURL: https://bonus.ly/api/v1
  baseurl_source: declared
  description: Peer-to-peer recognition posts that carry points.
  name: Bonusly Bonuses API
  slug: bonusly-bonuses-api
- baseURL: https://bonus.ly/api/v1
  baseurl_source: declared
  description: Company-level settings and achievements.
  name: Bonusly Company API
  slug: bonusly-company-api
- baseURL: https://bonus.ly/api/v1
  baseurl_source: declared
  description: Conversions of earned points into rewards.
  name: Bonusly Redemptions API
  slug: bonusly-redemptions-api
- baseURL: https://bonus.ly/api/v1
  baseurl_source: declared
  description: The catalog of gift cards, donations, and custom rewards.
  name: Bonusly Rewards API
  slug: bonusly-rewards-api
- baseURL: https://bonus.ly/api/v1
  baseurl_source: declared
  description: Company members who give and receive recognition.
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
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 58.6
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
