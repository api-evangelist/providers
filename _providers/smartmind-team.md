---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/smartmind-team/hosts/smartmind-team-hosts.yml
  title: ''
  type: Hosts
  url: hosts/smartmind-team-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.smartmind-ai.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.smartmind-ai.io/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.smartmind-ai.io/insights/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.smartmind.team/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.smartmind-ai.io/qurify/releases
- group: company
  title: ''
  type: Blog
  url: https://www.smartmind-ai.io/insights/blog
- group: auth
  href: https://artifacts.apis.io/smartmind-team/security/smartmind-team-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smartmind-team-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.smartmind-ai.io/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://smartmind.team/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: SmartMind provides AI-driven mental health and wellness solutions, offering personalized cognitive training, mood tracking, and therapeutic content through a cloud-based platform. Their services integrate with mobile and web applications, enabling users to monitor mental well-being, receive guided exercises, and access professional resources. Backed by Techstars and venture capital, SmartMind aims to democratize mental health support with data-driven insights and scalable technology.
layout: provider
modified: '2026-10-24'
name: SmartMind
nav: Providers
network: true
overview: 'SmartMind is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, MentalHealth, Wellness, and Platform.


  SmartMind''s developer surface includes changelog, engineering blog, and 7 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 46.4
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Smartmind Team Domain Security
  slug: smartmind-team-domain-security
  summary_line: TLSv1.3 · HSTS
slug: smartmind-team
tags:
- Company
- AI
- MentalHealth
- Wellness
- Platform
website: https://www.smartmind-ai.io/
---
