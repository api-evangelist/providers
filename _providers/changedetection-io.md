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
api_count: 1
apis:
- description: API for changedetection.io providing endpoints to create watches, retrieve history, and manage monitoring of web pages.
  name: ChangeDetection.io API
  slug: changedetection-io-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/changedetection-io/hosts/changedetection-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/changedetection-io-hosts.yml
- group: build
  href: https://artifacts.apis.io/changedetection-io/packages/changedetection-io-packages.yml
  title: ''
  type: SDKs
  url: packages/changedetection-io-packages.yml
- group: build
  href: https://artifacts.apis.io/changedetection-io/packages/changedetection-io-packages.yml
  title: ''
  type: Packages
  url: packages/changedetection-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://changedetection.io/terms-of-service.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://changedetection.io/privacy-statement.html
- group: auth
  href: https://artifacts.apis.io/changedetection-io/security/changedetection-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/changedetection-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://changedetection.io/
- group: docs
  title: ''
  type: Documentation
  url: https://changedetection.io/docs/api_v1/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://changedetection.io/docs/api_v1/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dgtlmoon/changedetection.io
- group: commercial
  title: ''
  type: Pricing
  url: https://changedetection.io/#about
- group: operate
  title: ''
  type: Support
  url: https://changedetection.io/#support
coverage:
  checked: '2026-10-26'
  detail: API documentation is served as a Redoc HTML page without a publicly accessible OpenAPI spec.
  evidence:
  - status: 200
    url: https://changedetection.io/docs/api_v1/index.html
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: changedetection.io provides a simple, open‑source web‑page change detection service that monitors websites for visual or content changes and sends alerts via email, Slack, or other channels. Users can configure monitoring intervals, custom selectors, and receive notifications when a page updates, making it useful for tracking price changes, content updates, or compliance monitoring. The platform offers a web UI and API for integration, supporting multiple sites and flexible alerting options.
layout: provider
modified: '2026-10-26'
name: changedetection.io
nav: Providers
network: true
overview: 'changedetection.io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Monitoring, Webhooks, Alerts, and OpenSource.


  changedetection.io''s developer surface includes documentation, API reference, pricing, support, and 8 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Changedetection Io Domain Security
  slug: changedetection-io-domain-security
  summary_line: TLSv1.2 · HSTS
slug: changedetection-io
tags:
- Company
- Monitoring
- Webhooks
- Alerts
- OpenSource
website: https://changedetection.io/
---
