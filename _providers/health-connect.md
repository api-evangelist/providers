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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Provides access to health and fitness data on Android devices via the Health Connect platform.
  name: Health Connect API
  slug: health-connect-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/health-connect/refs/heads/main/hosts/health-connect-hosts.yml
  title: ''
  type: Hosts
  url: hosts/health-connect-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.android.com/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.android.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.android.com/about/versions/17/release-notes
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/health-connect/refs/heads/main/security/health-connect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/health-connect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developer.android.com/health-and-fitness/guides/health-connect
- group: docs
  title: ''
  type: Documentation
  url: https://developer.android.com/health-and-fitness/health-connect
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.android.com/health-and-fitness/health-connect/get-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.android.com/health-and-fitness/health-connect
coverage:
  checked: '2026-10-14'
  detail: Docs are served as JavaScript‑rendered pages without a machine‑readable OpenAPI spec.
  evidence:
  - status: 302
    url: https://developer.android.com/health-and-fitness/health-connect
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Health Connect is a Google-backed platform that enables Android apps to read and write a user's health and fitness data in a privacy-preserving way. It provides a unified API for accessing data such as steps, heart rate, sleep, nutrition, and more, allowing developers to build health-focused experiences while giving users granular control over data sharing. The service integrates with Google Fit and other health providers, offering standardized data models and secure permissions management.
image: https://developer.android.com/static/images/social/android-developers.png
layout: provider
modified: '2026-10-13'
name: Health Connect
nav: Providers
network: true
overview: 'Health Connect is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Android, and Data.


  Health Connect''s developer surface includes changelog, documentation, getting-started guide, API reference, and 5 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Health Connect Domain Security
  slug: health-connect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: health-connect
tags:
- Company
- Health
- Android
- Data
website: https://developer.android.com/health-and-fitness/guides/health-connect
---
