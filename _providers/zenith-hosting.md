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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for managing hosted applications, deployments and billing.
  name: Zenith Hosting API
  slug: zenith-hosting-api
artifact_total: 4
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://zenith.hosting/pricing.md
- group: commercial
  href: https://artifacts.apis.io/zenith-hosting/plans/zenith-hosting-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zenith-hosting-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://zenith.hosting/security
- group: agent
  href: https://artifacts.apis.io/zenith-hosting/llms/zenith-hosting-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zenith-hosting-llms.txt
- group: other
  href: https://artifacts.apis.io/zenith-hosting/a2a/zenith-hosting-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/zenith-hosting-a2a.yml
- group: auth
  href: https://artifacts.apis.io/zenith-hosting/well-known/zenith-hosting-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zenith-hosting-security.txt
- group: auth
  href: https://artifacts.apis.io/zenith-hosting/well-known/zenith-hosting-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zenith-hosting-app-security.txt
- group: agent
  href: https://artifacts.apis.io/zenith-hosting/well-known/zenith-hosting-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zenith-hosting-well-known.yml
- group: other
  href: https://artifacts.apis.io/zenith-hosting/hosts/zenith-hosting-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zenith-hosting-hosts.yml
- group: other
  href: https://artifacts.apis.io/zenith-hosting/vendors/zenith-hosting-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zenith-hosting-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.zenith.hosting/login
- group: auth
  href: https://artifacts.apis.io/zenith-hosting/security/zenith-hosting-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/zenith-hosting-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/zenith-hosting/security/zenith-hosting-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zenith-hosting-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zenith.hosting/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://zenith.hosting/developers
- group: docs
  title: ''
  type: Documentation
  url: https://zenith.hosting/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://zenith.hosting/developers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zenith.hosting/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zenith.hosting/privacy
- group: operate
  title: ''
  type: Support
  url: https://zenith.hosting/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zenith-hosting
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/zenith-hosting/workspace
coverage:
  checked: '2026-10-26'
  detail: Developers page provides HTML documentation but no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://zenith.hosting/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Zenith Hosting provides a one‑click managed app hosting platform that lets users deploy a wide range of open‑source and commercial applications with minimal configuration. The service offers a catalog of apps, automated provisioning, SSL, DNS, and persistent storage, targeting both individual users and enterprises. Pricing is tiered per deployment, and the platform includes developer tools for publishing and managing apps. Zenith Hosting emphasizes simplicity, reliability, and integration with Stripe for billing, aiming for 99.9% uptime.
image: https://zenith.hosting/og-banner.png
layout: provider
modified: '2026-10-26'
name: Zenith Hosting
nav: Providers
network: true
overview: 'Zenith Hosting is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hosting, Cloud, Software-as-a-Service, and Application.


  Zenith Hosting''s developer surface includes pricing, documentation, getting-started guide, support, and 18 more developer resources.'
plans:
- name: Zenith Hosting Plans Pricing
  plan_count: 4
  slug: zenith-hosting-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.1
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 64.3
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 33.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/zenith-hosting/zenith-hosting-2026-11-03T150453.png
security:
- kind: domain-security
  name: Zenith Hosting Domain Security
  slug: zenith-hosting-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Zenith Hosting Vulnerability Disclosure
  slug: zenith-hosting-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zenith-hosting
tags:
- Company
- Hosting
- Cloud
- Software-as-a-Service
- Application
website: https://zenith.hosting/
---
