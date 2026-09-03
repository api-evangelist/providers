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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Reference page describing the third-party API integrations GammaStack provides for sports betting platforms, including betting odds, live market data, and sport fixtures.
  name: GammaStack Sports Betting API Integrations
  slug: integrations
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gammastack-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gammastack
- group: company
  title: ''
  type: Website
  url: https://www.gammastack.com/
- group: company
  title: ''
  type: Blog
  url: https://www.gammastack.com/feed/
created: '2025-02-08'
description: GammaStack is a sports betting and iGaming software provider that integrates third-party APIs (betting odds, fixtures, payments, KYC) into customer-facing sportsbook platforms. GammaStack does not publish its own public API; this repository tracks the company and the categories of APIs it integrates.
finops:
- name: Gammastack Finops
  service_category: API
  slug: gammastack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gammastack.png
layout: provider
modified: '2026-07-25'
name: Gammastack
nav: Providers
network: true
overview: 'Gammastack publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Odds, Sports Betting, iGaming, and Sportsbook.


  Gammastack''s developer surface includes engineering blog and 3 more developer resources.'
plans:
- name: Gammastack Plans Pricing
  plan_count: 3
  slug: gammastack-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Gammastack Rate Limits
  slug: gammastack-rate-limits
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 11.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gammastack/refs/heads/main/screenshots/gammastack-2026-06-20T181641.png
security:
- kind: domain-security
  name: Gammastack Domain Security
  slug: gammastack-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gammastack
tags:
- Odds
- Sports Betting
- iGaming
- Sportsbook
website: https://www.gammastack.com/
---
