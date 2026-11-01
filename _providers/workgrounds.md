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
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/workgrounds/plans/workgrounds-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/workgrounds-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://workgrounds.com/trust
- group: agent
  href: https://artifacts.apis.io/workgrounds/llms/workgrounds-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/workgrounds-llms.txt
- group: auth
  href: https://artifacts.apis.io/workgrounds/well-known/workgrounds-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/workgrounds-help-security.txt
- group: agent
  href: https://artifacts.apis.io/workgrounds/well-known/workgrounds-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/workgrounds-well-known.yml
- group: other
  href: https://artifacts.apis.io/workgrounds/hosts/workgrounds-hosts.yml
  title: ''
  type: Hosts
  url: hosts/workgrounds-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.workgrounds.com/en/
- group: start
  title: ''
  type: Login
  url: https://workgrounds.com/login
- group: auth
  href: https://artifacts.apis.io/workgrounds/security/workgrounds-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/workgrounds-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/workgrounds/security/workgrounds-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/workgrounds-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://workgrounds.com
- group: docs
  title: ''
  type: Documentation
  url: https://workgrounds.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://workgrounds.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://workgrounds.com/onboard
- group: commercial
  title: ''
  type: Pricing
  url: https://workgrounds.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://workgrounds.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://workgrounds.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://workgrounds.com/blog
created: '2026-10-24'
description: Workgrounds provides an AI-powered platform that automates hotel room block sourcing, booking, and management for corporate travel. By integrating with Slack, Claude, and ChatGPT, Worky enables teams to request, compare, and secure hotel rooms at negotiated rates, reducing planning time by up to 30% and cutting travel costs. The service supports large group trips, offers real-time bidding from hotels, and streamlines expense tracking, making corporate travel more efficient and cost-effective.
image: https://workgrounds.com/assets/og-preview.png
layout: provider
modified: '2026-10-24'
name: Workgrounds
nav: Providers
network: true
overview: 'Workgrounds is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Travel, Hotel, and Automation.


  Workgrounds'' developer surface includes support, documentation, getting-started guide, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Workgrounds Plans Pricing
  plan_count: 2
  slug: workgrounds-plans-pricing
random_paper: 21
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 81.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Workgrounds Domain Security
  slug: workgrounds-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Workgrounds Trust Center
  slug: workgrounds-trust-center
  summary_line: SOC 2, GDPR
slug: workgrounds
tags:
- Company
- AI
- Travel
- Hotel
- Automation
- Corporate
website: https://workgrounds.com
---
