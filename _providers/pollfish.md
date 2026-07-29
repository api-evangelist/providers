---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 3
  human_in_the_loop: 0
  name: Pollfish Agentic Access
  operation_count: 17
  slug: pollfish-agentic-access
  summary_line: 17 operations · 3 acting
api_count: 6
apis:
- description: Publisher app / placement management (Dashboard API).
  name: Pollfish Apps API
  slug: pollfish-apps-api
- description: Respondent demographic profiles.
  name: Pollfish Demographics API
  slug: pollfish-demographics-api
- description: Per-user survey logs and disqualification reasons.
  name: Pollfish Logs API
  slug: pollfish-logs-api
- description: Survey-serving performance metrics.
  name: Pollfish Performance API
  slug: pollfish-performance-api
- description: Revenue reporting per provider and per country.
  name: Pollfish Revenue API
  slug: pollfish-revenue-api
- description: Device register, offerwall, and survey rendering.
  name: Pollfish Survey Distribution API
  slug: pollfish-survey-distribution-api
artifact_total: 13
collections:
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
random_paper: 55
rate_limits:
- limit_count: 5
  name: Pollfish Rate Limits
  slug: pollfish-rate-limits
score:
  band: thin
  composite: 41.4
  delta: -2.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 59.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
