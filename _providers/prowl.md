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
- group: other
  href: https://artifacts.apis.io/prowl/hosts/prowl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/prowl-hosts.yml
- group: build
  href: https://artifacts.apis.io/prowl/packages/prowl-packages.yml
  title: ''
  type: SDKs
  url: packages/prowl-packages.yml
- group: build
  href: https://artifacts.apis.io/prowl/packages/prowl-packages.yml
  title: ''
  type: Packages
  url: packages/prowl-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.prowlapp.com/register.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.prowlapp.com/privacy.php
- group: auth
  href: https://artifacts.apis.io/prowl/security/prowl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prowl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.prowlapp.com/
coverage:
  checked: '2026-10-27'
  detail: The API documentation page returns only HTML with login/register links and no machine‑readable OpenAPI, GraphQL, or other contract.
  evidence:
  - status: 200
    url: https://www.prowlapp.com/api.php
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Prowl is a push notification service for iOS devices, allowing developers to send real‑time alerts to iPhones, iPads, and iPod touches. The platform supports integration from macOS, Windows, and various apps, offering a simple HTTP API to trigger notifications. It aims to help apps keep users engaged through timely alerts.
layout: provider
modified: '2026-10-26'
name: Prowl
nav: Providers
network: true
overview: 'Prowl is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, PushNotifications, iOS, API, and Mobile.


  Prowl''s developer surface includes signup flow and 6 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Prowl Domain Security
  slug: prowl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: prowl
tags:
- Company
- PushNotifications
- iOS
- API
- Mobile
website: https://www.prowlapp.com/
---
