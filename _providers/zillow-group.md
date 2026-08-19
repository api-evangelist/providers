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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Zillow Group is a leading real estate technology company that operates a suite of online platforms and services designed to make the process of buying, selling, renting, and financing homes easier and
  name: Zillow Group
  slug: zillow-group
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zillow-group-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zillow
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zillow-group
- group: company
  title: ''
  type: Blog
  url: https://www.zillowgroup.com/feed/
created: '2025-03-01'
description: Zillow Group is a leading real estate and rental marketplace that aims to make the process of buying, selling, and renting homes more streamlined and efficient. The company offers a wide range of services, including an online platform where users can search for properties, view listings, and connect with real estate agents. Zillow Group also provides tools and resources for homeowners, such as Zestimate, an automated valuation model that estimates the market value of a property.
finops:
- name: Zillow Group Finops
  service_category: API
  slug: zillow-group-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zillow-group.png
layout: provider
modified: '2026-03-16'
name: Zillow Group
nav: Providers
network: true
overview: 'Zillow Group publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate.


  Zillow Group''s developer surface includes engineering blog and 3 more developer resources.'
plans:
- name: Zillow Group Plans Pricing
  plan_count: 3
  slug: zillow-group-plans-pricing
random_paper: 83
rate_limits:
- limit_count: 5
  name: Zillow Group Rate Limits
  slug: zillow-group-rate-limits
score:
  band: minimal
  composite: 10.0
  delta: -0.3
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 10.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zillow-group/refs/heads/main/screenshots/zillow-group-2026-06-20T201913.png
security:
- kind: domain-security
  name: Zillow Group Domain Security
  slug: zillow-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zillow-group
tags:
- Real Estate
---
