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
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Send transactional email, manage campaigns, contacts, and templates.
  name: MisarMail
  slug: misarmail
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/misar-io/plans/misar-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/misar-io-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://www.misar.io/security
- group: agent
  href: https://artifacts.apis.io/misar-io/llms/misar-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/misar-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/misar-io/well-known/misar-io-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/misar-io-www-security.txt
- group: auth
  href: https://artifacts.apis.io/misar-io/well-known/misar-io-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/misar-io-status-security.txt
- group: auth
  href: https://artifacts.apis.io/misar-io/well-known/misar-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/misar-io-security.txt
- group: auth
  href: https://artifacts.apis.io/misar-io/well-known/misar-io-misarseo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/misar-io-misarseo-security.txt
- group: auth
  href: https://artifacts.apis.io/misar-io/well-known/misar-io-misarreach-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/misar-io-misarreach-security.txt
- group: auth
  href: https://artifacts.apis.io/misar-io/well-known/misar-io-misarpost-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/misar-io-misarpost-security.txt
- group: auth
  href: https://artifacts.apis.io/misar-io/well-known/misar-io-misar-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/misar-io-misar-security.txt
- group: agent
  href: https://artifacts.apis.io/misar-io/well-known/misar-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/misar-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/misar-io/hosts/misar-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/misar-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/misar-io/vendors/misar-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/misar-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.misar.io/terms
- group: operate
  title: ''
  type: Support
  url: https://www.misar.io/help
- group: operate
  title: ''
  type: StatusPage
  url: https://status.misar.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.misar.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.misar.io/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/misar-ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.misar.io/docs/changelog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.misar.io/
- group: auth
  href: https://artifacts.apis.io/misar-io/security/misar-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/misar-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/misar-io/security/misar-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/misar-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://misar.io/
created: '2026-10-29'
description: Misar.io offers an AI suite for founders, providing tools such as Misar.AI co‑founder, email outreach, social media management, content creation, and an app builder. The platform aims to help startups launch, grow, and operate efficiently with AI‑powered automation and integrated SaaS solutions. Free to start, it targets early‑stage founders seeking scalable, privacy‑first tools.
image: https://www.misar.io/og?title=The+AI+suite+for+founders&subtitle=Raise%2C+build%2C+launch+and+grow+%E2%80%94+one+account
layout: provider
modified: '2026-10-29'
name: misar-io
nav: Providers
network: true
overview: 'misar-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Startups, Software-as-a-Service, and Automation.


  misar-io''s developer surface includes support, pricing, changelog, documentation, and 20 more developer resources.'
plans:
- name: Misar Io Plans Pricing
  plan_count: 11
  slug: misar-io-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 73.2
    operational_transparency: 23.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 30.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/misar-io/misar-io-2026-11-03T135707.png
security:
- kind: domain-security
  name: Misar Io Domain Security
  slug: misar-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Misar Io Vulnerability Disclosure
  slug: misar-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: misar-io
tags:
- Company
- Artificial Intelligence
- Startups
- Software-as-a-Service
- Automation
website: https://misar.io/
---
