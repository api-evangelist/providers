---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Bloomy eSIM plans and activation
  name: Bloomy eSIM API
  slug: bloomy-esim-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/bloomyesim-com/plans/bloomyesim-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bloomyesim-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/bloomyesim-com/changelog/bloomyesim-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bloomyesim-com-changelog.yml
- group: agent
  href: https://artifacts.apis.io/bloomyesim-com/llms/bloomyesim-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bloomyesim-com-llms.txt
- group: other
  href: https://artifacts.apis.io/bloomyesim-com/hosts/bloomyesim-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bloomyesim-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bloomyesim.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bloomyesim.com/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://bloomyesim.com/changelog/
- group: company
  title: ''
  type: Blog
  url: https://bloomyesim.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://bloomyesim.com/setup/
- group: auth
  href: https://artifacts.apis.io/bloomyesim-com/security/bloomyesim-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bloomyesim-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bloomyesim.com/
created: '2026-11-02'
description: Bloomy eSIM provides a comparison platform for overseas eSIMs, offering plans across 202 countries and regions starting from ¥100. It targets students, working holiday travelers, and tourists, delivering transparent pricing, data limits, and speed information. Users can purchase and activate eSIMs with a single tap, manage usage via a personal dashboard, and receive support in Japanese. The service emphasizes clear terms, unlimited options, and easy setup for short or long stays abroad.
image: https://bloomyesim.com/wp-content/themes/swell_child/assets/images/ogp/ogp-ja-top.jpg?v=1780611432
layout: provider
modified: '2026-11-02'
name: Bloomy eSIM
nav: Providers
network: true
overview: 'Bloomy eSIM is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, eSIM, Travel, Telecommunications, and Japan.


  Bloomy eSIM''s developer surface includes changelog, engineering blog, getting-started guide, and 8 more developer resources.'
plans:
- name: Bloomyesim Com Plans Pricing
  plan_count: 19
  slug: bloomyesim-com-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 7.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bloomyesim Com Domain Security
  slug: bloomyesim-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bloomyesim-com
tags:
- Company
- eSIM
- Travel
- Telecommunications
- Japan
- Comparison
website: https://bloomyesim.com/
---
