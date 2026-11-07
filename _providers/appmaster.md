---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/appmaster/plans/appmaster-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appmaster-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/appmaster/changelog/appmaster-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/appmaster-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://appmaster.io/security
- group: auth
  href: https://artifacts.apis.io/appmaster/authentication/appmaster-authentication.yml
  title: ''
  type: Authentication
  url: authentication/appmaster-authentication.yml
- group: design
  href: https://artifacts.apis.io/appmaster/conformance/appmaster-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appmaster-conformance.yml
- group: agent
  href: https://artifacts.apis.io/appmaster/llms/appmaster-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appmaster-llms.txt
- group: auth
  href: https://artifacts.apis.io/appmaster/well-known/appmaster-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/appmaster-security.txt
- group: agent
  href: https://artifacts.apis.io/appmaster/well-known/appmaster-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appmaster-well-known.yml
- group: other
  href: https://artifacts.apis.io/appmaster/hosts/appmaster-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appmaster-hosts.yml
- group: other
  href: https://artifacts.apis.io/appmaster/vendors/appmaster-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appmaster-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://appmaster.io/security
- group: company
  title: ''
  type: Newsroom
  url: https://appmaster.io/news
- group: other
  title: ''
  type: Leadership
  url: https://appmaster.io/integrations/library/management
- group: operate
  title: ''
  type: ChangeLog
  url: https://appmaster.io/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://appmaster.io/docs/getting-started/what-is-appmaster-io
- group: auth
  href: https://artifacts.apis.io/appmaster/security/appmaster-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/appmaster-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/appmaster/security/appmaster-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/appmaster-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/appmaster/security/appmaster-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appmaster-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appmaster.io/
- group: docs
  title: ''
  type: Documentation
  url: https://appmaster.io/docs
- group: company
  title: ''
  type: Blog
  url: https://appmaster.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://appmaster.io/pricing
- group: operate
  title: ''
  type: Roadmap
  url: https://appmaster.io/roadmap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appmaster.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appmaster.io/legal/privacy
created: '2026-10-20'
description: AppMaster.io provides a no‑code development platform that enables users to build web and mobile applications through a visual drag‑and‑drop interface. It offers data modeling, business process automation, integrations with popular services, and deployment options for both cloud and on‑premises environments. The platform targets enterprises and developers seeking rapid application delivery without writing code, supporting a range of industries with customizable templates and extensive documentation.
image: https://appmaster.io/images/appmaster.png
layout: provider
modified: '2026-10-20'
name: AppMaster.io
nav: Providers
network: true
overview: 'AppMaster.io is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, No-Code, Platform, Automation, and Integration.


  AppMaster.io''s developer surface includes changelog, authentication, getting-started guide, documentation, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Appmaster Plans Pricing
  plan_count: 4
  slug: appmaster-plans-pricing
random_paper: 13
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 59.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 38.1
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/appmaster/appmaster-2026-11-03T121032.png
security:
- kind: authentication
  name: Appmaster Authentication
  slug: appmaster-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Appmaster Domain Security
  slug: appmaster-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Appmaster Vulnerability Disclosure
  slug: appmaster-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Appmaster Trust Center
  slug: appmaster-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: appmaster
tags:
- Company
- No-Code
- Platform
- Automation
- Integration
website: https://appmaster.io/
---
