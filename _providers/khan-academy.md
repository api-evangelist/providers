---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Legacy REST API previously documented at api-explorer.khanacademy.org (now redirects). Some endpoints under https://www.khanacademy.org/api/v1/ remain accessible for content topic trees and exercise d
  name: Khan Academy API v1 (Legacy / Internal)
  slug: api-v1-legacy
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/khan-academy-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/khan
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/khan-academy
- group: company
  title: ''
  type: Website
  url: https://www.khanacademy.org/
- group: other
  title: ''
  type: Developer
  url: https://www.khanacademy.org/
- group: commercial
  title: ''
  type: Plans
  url: plans/khan-academy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/khan-academy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/khan-academy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.khanacademy.org/feed/
created: '2026-05-08'
description: Khan Academy is a non-profit providing free online educational content. The legacy Khan Academy API (v1) is deprecated/limited and the public api-explorer.khanacademy.org redirects to the main site. Some endpoints under www.khanacademy.org/api/v1/ remain in use for internal apps and historical integrations, but Khan Academy no longer maintains a publicly supported developer program.
finops:
- name: Khan Academy Finops
  service_category: Education & Training
  slug: khan-academy-finops
graphqls:
- description: This is a conceptual GraphQL schema for Khan Academy, the non-profit providing free online educational content. Khan Academy's public-facing API is a legacy REST API (v1) available under `https://www.
  name: Khan Academy GraphQL Schema
  slug: khan-academy-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/khan-academy.png
layout: provider
modified: '2026-05-08'
name: Khan Academy
nav: Providers
network: true
overview: 'Khan Academy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include EdTech, Online Learning, Non-Profit, and K-12.


  Khan Academy''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Khan Academy Plans Pricing
  plan_count: 1
  slug: khan-academy-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Khan Academy Rate Limits
  slug: khan-academy-rate-limits
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 2.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 16.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/khan-academy/refs/heads/main/screenshots/khan-academy-2026-06-20T184025.png
security:
- kind: domain-security
  name: Khan Academy Domain Security
  slug: khan-academy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: khan-academy
tags:
- EdTech
- Online Learning
- Non-Profit
- K-12
website: https://www.khanacademy.org/
---
