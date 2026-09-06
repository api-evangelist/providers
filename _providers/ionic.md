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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Ionic provides a platform and APIs for building and deploying modern mobile applications and micro frontend experiences with cross-platform support.
  name: Ionic API
  slug: ionic-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ionic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ionic-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://ionic.io/blog/feed
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/drifty-co-
- group: company
  title: ''
  type: Website
  url: https://ionic.io/
- group: docs
  title: ''
  type: Documentation
  url: https://ionic.io/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ionic-team
- group: operate
  title: ''
  type: Support
  url: https://ionic.io/support
created: '2025-02-08'
description: Ionic is a platform for building and deploying modern mobile applications and micro frontend experiences. Ionic provides tools, guides, and APIs to help developers build and ship incredible apps faster, including cross-platform mobile development capabilities.
finops:
- name: Ionic Finops
  service_category: API
  slug: ionic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ionic.png
layout: provider
modified: '2026-04-28'
name: Ionic
nav: Providers
network: true
overview: 'Ionic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Application, Cross-Platform, Frontend, and Mobile Development.


  Ionic''s developer surface includes engineering blog, documentation, support, and 5 more developer resources.'
plans:
- name: Ionic Plans Pricing
  plan_count: 3
  slug: ionic-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Ionic Rate Limits
  slug: ionic-rate-limits
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 15.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ionic/refs/heads/main/screenshots/ionic-2026-06-20T183530.png
security:
- kind: domain-security
  name: Ionic Domain Security
  slug: ionic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ionic Vulnerability Disclosure
  slug: ionic-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ionic
tags:
- Application
- Cross-Platform
- Frontend
- Mobile Development
website: https://ionic.io/
---
