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
    mcp_server: documented
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: operate
  href: https://artifacts.apis.io/bugezy-dev/changelog/bugezy-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bugezy-dev-changelog.yml
- group: other
  href: https://artifacts.apis.io/bugezy-dev/hosts/bugezy-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bugezy-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/bugezy-dev/vendors/bugezy-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bugezy-dev-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://bugezy.dev/changelog
- group: auth
  href: https://artifacts.apis.io/bugezy-dev/security/bugezy-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bugezy-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bugezy.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://bugezy.dev/guide
- group: company
  title: ''
  type: Blog
  url: https://bugezy.dev/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bugezy.dev/privacy
coverage:
  checked: '2026-10-30'
  detail: The provider's documentation site offers HTML pages but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec.
  evidence:
  - status: 200
    url: https://bugezy.dev/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: BugEzy is a developer-focused bug reporting platform that leverages AI to automatically capture, transcribe, and fix software bugs. Users can record their screen and voice, generating detailed reports with replay, logs, and actionable fixes. The service offers a free tier with 10 recordings per month and supports multiple languages, aiming to streamline debugging and reduce token costs for AI assistance.
image: https://bugezy.dev/icon-128.png
layout: provider
modified: '2026-10-30'
name: bugezy-dev
nav: Providers
network: true
overview: 'bugezy-dev is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include BugReporting, AI, DeveloperTools, SaaS, and Productivity.


  bugezy-dev''s developer surface includes changelog, documentation, engineering blog, and 6 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bugezy Dev Domain Security
  slug: bugezy-dev-domain-security
  summary_line: TLSv1.3
slug: bugezy-dev
tags:
- BugReporting
- AI
- DeveloperTools
- SaaS
- Productivity
website: https://bugezy.dev/
---
