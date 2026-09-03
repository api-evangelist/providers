---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    auth_clarity: false
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
  score: 2.5
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: The LegiScan Pull API is an RPC-style JSON service that allows clients to query the national legislative database on demand. Operations include retrieving session lists, master bill lists, bill detail
  name: LegiScan Pull API
  slug: legiscan-pull-api
- description: The LegiScan Push API is a paid subscription service that delivers real-time legislative updates to a client-hosted endpoint. Changes detected in bill information are pushed every 15 minutes to 4 hour
  name: LegiScan Push API
  slug: legiscan-push-api
- description: 'The LegiScan Bulk Dataset API provides access to weekly snapshot ZIP archives containing all getBill, getRollCall, and getPerson payload records as individual JSON files for each legislative session. '
  name: LegiScan Bulk Dataset API
  slug: legiscan-bulk-dataset-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/legiscan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://legiscan.com
- group: docs
  title: ''
  type: Documentation
  url: https://legiscan.com/legiscan
- group: docs
  title: ''
  type: APIReference
  url: https://legiscan.com/gaits/documentation/legiscan
- group: company
  title: ''
  type: Blog
  url: https://legiscan.com/news-update
- group: commercial
  title: ''
  type: Pricing
  url: https://legiscan.com/pricing/api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/legiscan
- group: other
  title: ''
  type: X
  url: https://x.com/LegiScan
- group: commercial
  title: ''
  type: Plans
  url: plans/legiscan-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/legiscan-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/legiscan-finops.yml
created: '2026-06-13'
description: LegiScan is a national legislative tracking service providing real-time data on bill activity, voting records, and legislative actions across all 50 US states and Congress. The LegiScan API offers a JSON-based RPC-style interface supporting both pull and push data delivery models. Developers and organizations can monitor legislation in near real-time, search full-text bill content, retrieve roll call votes, access sponsor and legislator information, and download bulk session datasets. The free public tier provides 30,000 queries per month, with paid subscription plans offering higher limits and push-based real-time updates pushed every 15 minutes to 4 hours as changes are detected.
finops:
- name: Legiscan Finops
  service_category: Data & Analytics
  slug: legiscan-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/legiscan.png
layout: provider
modified: '2026-06-13'
name: LegiScan
nav: Providers
network: true
overview: 'LegiScan publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Legislative Tracking, Government, Bills, Voting Records, and State Legislation.


  LegiScan''s developer surface includes documentation, API reference, engineering blog, pricing, and 7 more developer resources.'
plans:
- name: Legiscan Plans Pricing
  plan_count: 4
  slug: legiscan-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Legiscan Rate Limits
  slug: legiscan-rate-limits
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 7
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 23.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Legiscan Domain Security
  slug: legiscan-domain-security
  summary_line: TLSv1.3 · DMARC
slug: legiscan
tags:
- Legislative Tracking
- Government
- Bills
- Voting Records
- State Legislation
- Congressional Data
- Civic Tech
website: https://legiscan.com
---
