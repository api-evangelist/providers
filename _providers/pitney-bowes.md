---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Pitney Bowes Agentic Access
  operation_count: 11
  slug: pitney-bowes-agentic-access
  summary_line: 11 operations · 8 acting
api_count: 8
apis:
- description: The Address API from Pitney Bowes — 1 operation(s) for address.
  name: Pitney Bowes Address API
  slug: pitney-bowes-address-api
- description: The Manifests API from Pitney Bowes — 1 operation(s) for manifests.
  name: Pitney Bowes Manifests API
  slug: pitney-bowes-manifests-api
- description: The Oauth API from Pitney Bowes — 1 operation(s) for oauth.
  name: Pitney Bowes Oauth API
  slug: pitney-bowes-oauth-api
- description: The Pickups API from Pitney Bowes — 2 operation(s) for pickups.
  name: Pitney Bowes Pickups API
  slug: pitney-bowes-pickups-api
- description: The Rating API from Pitney Bowes — 1 operation(s) for rating.
  name: Pitney Bowes Rating API
  slug: pitney-bowes-rating-api
- description: The Reports API from Pitney Bowes — 1 operation(s) for reports.
  name: Pitney Bowes Reports API
  slug: pitney-bowes-reports-api
- description: The Shipments API from Pitney Bowes — 2 operation(s) for shipments.
  name: Pitney Bowes Shipments API
  slug: pitney-bowes-shipments-api
- description: The Tracking API from Pitney Bowes — 1 operation(s) for tracking.
  name: Pitney Bowes Tracking API
  slug: pitney-bowes-tracking-api
artifact_total: 16
collections:
- collection_type: open
  name: Pitney Bowes Shipping API
  slug: open-pitney-bowes
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pitney-bowes-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pitney-bowes-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pitney-bowes-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pitney-bowes-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PitneyBowes
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pitney-bowes
- group: company
  title: ''
  type: Blog
  url: https://www.pitneybowes.com/us/blog.html
created: '2025-03-01'
description: Pitney Bowes is a global technology company that specializes in providing innovative shipping and mailing solutions. They offer a range of products and services, including postage meters, shipping software, and mail sorting equipment, to help businesses streamline their shipping and mailing processes. With a focus on efficiency and productivity, Pitney Bowes aims to help companies save time and money on their shipping and mailing operations.
finops:
- name: Pitney Bowes Finops
  service_category: Shipping and Mailing
  slug: pitney-bowes-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pitney-bowes.png
layout: provider
modified: '2026-05-19'
name: Pitney Bowes
nav: Providers
network: true
overview: 'Pitney Bowes publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Address API, Manifests API, Oauth API, and 5 more. Tagged areas include Mailing, Shipping, and Fortune 1000.


  Pitney Bowes'' developer surface includes authentication, engineering blog, and 5 more developer resources.'
plans:
- name: Pitney Bowes Plans Pricing
  plan_count: 1
  slug: pitney-bowes-plans-pricing
press:
- date: '2026-05-25'
  title: In the News
  url: https://www.pitneybowes.com/us/newsroom/in-the-news.html
- date: '2026-05-25'
  title: Pitney Bowes Partners with Kyndryl to Harness Cloud and ...
  url: https://www.kyndryl.com/us/en/about-us/news/2021/11/2021-11-04-Pitney-Bowes-Partners-with-Kyndryl-to-Harness-Cloud-and-AI-for-Business-Transformation
- date: '2026-05-25'
  title: Pitney Bowes Delivering New Value through Partnership ...
  url: https://www.investorrelations.pitneybowes.com/news-releases/news-release-details/pitney-bowes-delivering-new-value-through-partnership-ecosystem
- date: '2026-05-25'
  title: Pitney Bowes Forms a New Data Practice to Drive Digital ...
  url: https://www.investorrelations.pitneybowes.com/news-releases/news-release-details/pitney-bowes-forms-new-data-practice-drive-digital
- date: '2026-05-25'
  title: Pitney Bowes to Deploy Ambi Robotics AI-Powered ...
  url: https://www.ambirobotics.com/media/pitney-bowes-deploys-ambisort/
random_paper: 94
rate_limits:
- limit_count: 1
  name: Pitney Bowes Rate Limits
  slug: pitney-bowes-rate-limits
scopes:
- name: Pitney Bowes Scopes
  scope_count: 0
  slug: pitney-bowes-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 53.9
    developer_ergonomics: 13.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 31.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pitney-bowes/refs/heads/main/screenshots/pitney-bowes-2026-06-20T191739.png
security:
- kind: authentication
  name: Pitney Bowes Authentication
  slug: pitney-bowes-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Pitney Bowes Domain Security
  slug: pitney-bowes-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: pitney-bowes
tags:
- Mailing
- Shipping
- Fortune 1000
---
