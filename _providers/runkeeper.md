---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/runkeeper/hosts/runkeeper-hosts.yml
  title: ''
  type: Hosts
  url: hosts/runkeeper-hosts.yml
- group: other
  href: https://artifacts.apis.io/runkeeper/vendors/runkeeper-vendors.yml
  title: ''
  type: Vendors
  url: vendors/runkeeper-vendors.yml
- group: build
  href: https://artifacts.apis.io/runkeeper/packages/runkeeper-packages.yml
  title: ''
  type: SDKs
  url: packages/runkeeper-packages.yml
- group: build
  href: https://artifacts.apis.io/runkeeper/packages/runkeeper-packages.yml
  title: ''
  type: Packages
  url: packages/runkeeper-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://runkeeper.com/cms/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://runkeeper.com/cms/privacy-policies/
- group: company
  title: ''
  type: Blog
  url: https://runkeeper.com/cms/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://help.runkeeper.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Runkeeper
- group: auth
  href: https://artifacts.apis.io/runkeeper/security/runkeeper-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/runkeeper-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://runkeeper.com/
coverage:
  checked: '2026-10-26'
  detail: Documentation pages are HTML rendered without machine‑readable specs.
  evidence:
  - status: 200
    url: https://runkeeper.com/cms/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Runkeeper provides a social fitness platform and mobile app that helps users track runs, set goals, and join a community of runners. The service offers GPS‑based activity logging, training plans, and integration with wearables, enabling users to monitor progress, share achievements, and stay motivated through challenges and social features.
image: https://runkeeper.com/cms/wp-content/uploads/sites/4/2023/01/SS23_Runkeeper_Rebrand_Social_Launch-Comms_FacebookPost_02_1920x1080.jpg
layout: provider
modified: '2026-10-26'
name: Runkeeper
nav: Providers
network: true
overview: 'Runkeeper is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fitness, Social, MobileApp, Tracking, and Community.


  Runkeeper''s developer surface includes engineering blog, documentation, and 9 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Runkeeper Domain Security
  slug: runkeeper-domain-security
  summary_line: TLSv1.3 · DMARC
slug: runkeeper
tags:
- Fitness
- Social
- MobileApp
- Tracking
- Community
- Health
website: https://runkeeper.com/
---
