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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: KCL constraint-based record and functional programming language for configuration and policy scenarios in cloud-native environments.
  name: KCL
  slug: kcl
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kcl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kcl-lang.io/
- group: docs
  title: ''
  type: Documentation
  url: https://kcl-lang.io/docs/user_docs/getting-started/intro
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kcl-lang
- group: company
  title: ''
  type: Blog
  url: https://kcl-lang.io/blog/rss.xml
created: '2025-01-01'
description: KCL (Kusion Configuration Language) is a constraint-based record and functional programming language designed for configuration and policy scenarios. It provides features like type safety, automation, and validation for cloud-native configurations.
finops:
- name: Kcl Finops
  service_category: API
  slug: kcl-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kcl.png
layout: provider
modified: '2026-03-16'
name: KCL
nav: Providers
network: true
overview: 'KCL publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud-Native, Configuration Language, Infrastructure as Code, and Policy as Code.


  KCL''s developer surface includes documentation, engineering blog, and 3 more developer resources.'
plans:
- name: Kcl Plans Pricing
  plan_count: 3
  slug: kcl-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Kcl Rate Limits
  slug: kcl-rate-limits
score:
  band: emerging
  composite: 11.6
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
    developer_ergonomics: 23.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kcl/refs/heads/main/screenshots/kcl-2026-06-20T183930.png
security:
- kind: domain-security
  name: Kcl Domain Security
  slug: kcl-domain-security
  summary_line: TLSv1.3 · HSTS
slug: kcl
tags:
- Cloud-Native
- Configuration Language
- Infrastructure as Code
- Policy as Code
website: https://kcl-lang.io/
---
