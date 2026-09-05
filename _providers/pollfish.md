---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Pollfish Agentic Access
  operation_count: 17
  slug: pollfish-agentic-access
  summary_line: 17 operations · 3 acting
api_count: 1
apis:
- baseURL: https://www.pollfish.com/api/public/v2
  baseurl_source: declared
  description: Publisher app / placement management (Dashboard API).
  name: Pollfish Apps API
  slug: pollfish-apps-api
- baseURL: https://www.pollfish.com/api/public/v2
  baseurl_source: declared
  description: Respondent demographic profiles.
  name: Pollfish Demographics API
  slug: pollfish-demographics-api
- baseURL: https://www.pollfish.com/api/public/v2
  baseurl_source: declared
  description: Per-user survey logs and disqualification reasons.
  name: Pollfish Logs API
  slug: pollfish-logs-api
- baseURL: https://www.pollfish.com/api/public/v2
  baseurl_source: declared
  description: Survey-serving performance metrics.
  name: Pollfish Performance API
  slug: pollfish-performance-api
- baseURL: https://www.pollfish.com/api/public/v2
  baseurl_source: declared
  description: Revenue reporting per provider and per country.
  name: Pollfish Revenue API
  slug: pollfish-revenue-api
- baseURL: https://www.pollfish.com/api/public/v2
  baseurl_source: declared
  description: Device register, offerwall, and survey rendering.
  name: Pollfish Survey Distribution API
  slug: pollfish-survey-distribution-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pollfish Apps API
  slug: open-pollfish-apps-api
- collection_type: open
  name: Pollfish Apps Demographics API
  slug: open-pollfish-demographics-api
- collection_type: open
  name: Pollfish Apps Logs API
  slug: open-pollfish-logs-api
- collection_type: open
  name: Pollfish Apps Performance API
  slug: open-pollfish-performance-api
- collection_type: open
  name: Pollfish Apps Revenue API
  slug: open-pollfish-revenue-api
- collection_type: open
  name: Pollfish Apps Survey Distribution API
  slug: open-pollfish-survey-distribution-api
- collection_type: open
  name: Pollfish API
  slug: open-pollfish
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pollfish-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pollfish-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pollfish-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pollfish
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pollfish
- group: company
  title: ''
  type: Website
  url: https://www.pollfish.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.pollfish.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/pollfish-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pollfish-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pollfish-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pollfish.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.pollfish.com/blog/
created: '2026-07-04'
description: Pollfish is a mobile-first survey and market research platform, owned by Prodege LLC. It lets researchers reach real respondents inside mobile apps and websites and lets app publishers monetize their audience by serving Pollfish (and mediated third-party) surveys as rewarded ads or an offerwall. Pollfish exposes a REST Dashboard API on https://www.pollfish.com for managing publisher apps and pulling performance, revenue, demographic, and user-log analytics (HTTP Basic Auth), plus a survey-serving / offerwall API on https://wss.pollfish.com for requesting and rendering surveys, and server-to-server postback callbacks for survey-completion and eligibility events. Survey creation and audience targeting for researchers are done through the Pollfish dashboard and are not exposed as a documented public REST API.
finops:
- name: Pollfish Finops
  service_category: Market Research and Survey Monetization
  slug: pollfish-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pollfish.png
layout: provider
modified: '2026-07-04'
name: Pollfish
nav: Providers
network: true
overview: 'Pollfish publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Demographics API, Logs API, and 3 more. Tagged areas include Surveys, Market Research, Mobile, Monetization, and Offerwall.


  Pollfish''s developer surface includes authentication, documentation, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Pollfish Plans Pricing
  plan_count: 4
  slug: pollfish-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Pollfish Rate Limits
  slug: pollfish-rate-limits
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 59.0
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pollfish/refs/heads/main/screenshots/pollfish-2026-09-02T151652.png
security:
- kind: authentication
  name: Pollfish Authentication
  slug: pollfish-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pollfish Domain Security
  slug: pollfish-domain-security
  summary_line: TLSv1.2 · DMARC
slug: pollfish
tags:
- Surveys
- Market Research
- Mobile
- Monetization
- Offerwall
- Rewarded Ads
- Prodege
website: https://www.pollfish.com
---
