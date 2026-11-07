---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 7.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Zepp Health wearable devices and health data, documented at the Zepp developer portal.
  name: Zepp Health API
  slug: zepp-health-api
artifact_total: 2
common:
- group: build
  href: https://artifacts.apis.io/zepp-health/cli/zepp-health-cli.yml
  title: ''
  type: CLI
  url: cli/zepp-health-cli.yml
- group: operate
  href: https://artifacts.apis.io/zepp-health/changelog/zepp-health-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/zepp-health-changelog.yml
- group: agent
  href: https://artifacts.apis.io/zepp-health/llms/zepp-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zepp-health-llms.txt
- group: auth
  href: https://artifacts.apis.io/zepp-health/well-known/zepp-health-src-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zepp-health-src-security.txt
- group: agent
  href: https://artifacts.apis.io/zepp-health/well-known/zepp-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zepp-health-well-known.yml
- group: other
  href: https://artifacts.apis.io/zepp-health/hosts/zepp-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zepp-health-hosts.yml
- group: other
  href: https://artifacts.apis.io/zepp-health/vendors/zepp-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zepp-health-vendors.yml
- group: build
  href: https://artifacts.apis.io/zepp-health/packages/zepp-health-packages.yml
  title: ''
  type: SDKs
  url: packages/zepp-health-packages.yml
- group: build
  href: https://artifacts.apis.io/zepp-health/packages/zepp-health-packages.yml
  title: ''
  type: Packages
  url: packages/zepp-health-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zepp.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zepp.com/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.zepp.com/
- group: company
  title: ''
  type: Blog
  url: https://zepp.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zepp.com/docs/guides/quick-start/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.zepp.com/
- group: auth
  href: https://artifacts.apis.io/zepp-health/security/zepp-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zepp-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zepp.com/
created: '2026-10-28'
description: Zepp Health, operating under the Amazfit brand, develops wearable devices and health-focused applications that empower individuals to monitor and improve their well‑being. Their product lineup includes smartwatches, fitness trackers, and a companion mobile app offering features such as heart‑rate monitoring, sleep analysis, activity tracking, and personalized health insights. Zepp Health emphasizes seamless integration of hardware and software to deliver an engaging user experience that inspires joy and promotes a healthier lifestyle.
image: https://cdn.prod.website-files.com/607dba2ba33a21df7ea89f70/660d04fa11dc2bfeadc93eea_Group%202374%20(1).jpg
layout: provider
modified: '2026-10-28'
name: Amazfit
nav: Providers
network: true
overview: 'Amazfit is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wearables, Health, IoT, and Consumer Tech.


  Amazfit''s developer surface includes CLI, changelog, engineering blog, getting-started guide, documentation, and 12 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 24.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/zepp-health/zepp-health-2026-11-03T150507.png
security:
- kind: domain-security
  name: Zepp Health Domain Security
  slug: zepp-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zepp-health
tags:
- Company
- Wearables
- Health
- IoT
- Consumer Tech
website: https://zepp.com/
---
