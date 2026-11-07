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
api_count: 1
apis:
- description: Toolkit API documentation for Pometry platform.
  name: Pometry Platform Toolkit
  slug: pometry-platform-toolkit
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.pometry.com/security/
- group: agent
  href: https://artifacts.apis.io/pometry/llms/pometry-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pometry-llms.txt
- group: other
  href: https://artifacts.apis.io/pometry/hosts/pometry-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pometry-hosts.yml
- group: other
  href: https://artifacts.apis.io/pometry/vendors/pometry-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pometry-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.pometry.com/platform/register/
- group: auth
  title: ''
  type: Security
  url: https://www.pometry.com/security/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Pometry/Raphtory/releases
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pometry.com/v0.17/docs/reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pometry.com/v0.17/docs/getting-started/quickstart
- group: auth
  href: https://artifacts.apis.io/pometry/security/pometry-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/pometry-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/pometry/security/pometry-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pometry-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pometry.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pometry.com/platform/toolkit/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pometry.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.pometry.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.pometry.com/insights/
created: '2026-10-24'
description: Pometry provides institutional intelligence solutions, offering a library of tools that model organizational data across finance, operations, and transformation initiatives. Their platform includes capabilities such as chat, explorer, toolkit, and memory, enabling enterprises to build live models of how their organization works and derive actionable insights for programme delivery, technology optimisation, financial reporting, and client intelligence.
image: https://www.pometry.com/assets-v5/og-pometry.jpg?v=4
layout: provider
modified: '2026-10-24'
name: Pometry
nav: Providers
network: true
overview: 'Pometry is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Institutional-Intelligence, Analytics, Enterprise Software, and Platform.


  Pometry''s developer surface includes signup flow, changelog, API reference, getting-started guide, documentation, support, engineering blog, and 9 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.1
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 64.3
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pometry/pometry-2026-11-03T141404.png
security:
- kind: domain-security
  name: Pometry Domain Security
  slug: pometry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pometry Trust Center
  slug: pometry-trust-center
  summary_line: ISO 27001, GDPR
slug: pometry
tags:
- Company
- Institutional-Intelligence
- Analytics
- Enterprise Software
- Platform
website: https://www.pometry.com/
---
