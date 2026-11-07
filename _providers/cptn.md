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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/cptn/hosts/cptn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cptn-hosts.yml
- group: other
  href: https://artifacts.apis.io/cptn/vendors/cptn-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cptn-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cptn/security/cptn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cptn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cptn.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cptn.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cptn.io/
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/ZGFyzhDjZ2
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cptn-io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cptn.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cptn.io/privacy
- group: other
  title: ''
  type: CookiePolicy
  url: https://cptn.io/cookie_policy
coverage:
  checked: '2026-10-20'
  detail: Documentation pages are rendered via Docusaurus JavaScript and provide no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.cptn.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: DevRaven provides an open‑source integration and data platform that enables users to build, deploy, and manage data processing pipelines quickly. The platform offers a visual editor, supports JavaScript transformations, and includes a library of ready‑to‑use apps for connecting to cloud services, data warehouses, and messaging systems. It features built‑in security key rotation, CORS configuration, and optional single‑sign‑on. DevRaven is MIT‑licensed, community‑driven, and aims to simplify complex integrations without requiring separate message queues or serverless functions.
image: https://www.cptn.io/images/og-image.png?v=3
layout: provider
modified: '2026-10-19'
name: DevRaven
nav: Providers
network: true
overview: 'DevRaven is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, Open Source, Data Pipeline, and Automation.


  DevRaven''s developer surface includes documentation, support, and 9 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 14.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cptn/cptn-2026-11-03T125502.png
security:
- kind: domain-security
  name: Cptn Domain Security
  slug: cptn-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cptn
tags:
- Company
- Integration
- Open Source
- Data Pipeline
- Automation
website: https://cptn.io/
---
