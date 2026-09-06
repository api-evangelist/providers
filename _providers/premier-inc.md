---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The Premier Inc API provides access to platform services and data for enterprise integration and automation.
  name: Premier Inc API
  slug: premier-inc-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/premier-inc-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PremierInc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/premierinc
- group: company
  title: ''
  type: Website
  url: https://www.premierinc.com
- group: company
  title: ''
  type: Blog
  url: https://www.premierinc.com/feed.xml
created: '2026-04-19'
description: Premier Inc is a major US corporation and Fortune 1000 company. The Premier Inc API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Premier Inc Finops
  service_category: Healthcare
  slug: premier-inc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/premier-inc.png
layout: provider
modified: '2026-04-19'
name: Premier Inc
nav: Providers
network: true
overview: 'Premier Inc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Group Purchasing, and Analytics.


  Premier Inc''s developer surface includes engineering blog and 4 more developer resources.'
plans:
- name: Premier Inc Plans Pricing
  plan_count: 1
  slug: premier-inc-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Premier Inc Rate Limits
  slug: premier-inc-rate-limits
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 10.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/premier-inc/refs/heads/main/screenshots/premier-inc-2026-06-20T192047.png
security:
- kind: domain-security
  name: Premier Inc Domain Security
  slug: premier-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: premier-inc
tags:
- Healthcare
- Group Purchasing
- Analytics
website: https://www.premierinc.com
---
