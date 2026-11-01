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
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/tablesready/plans/tablesready-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tablesready-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.tablesready.com/security/
- group: agent
  href: https://artifacts.apis.io/tablesready/llms/tablesready-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tablesready-llms.txt
- group: auth
  href: https://artifacts.apis.io/tablesready/well-known/tablesready-tablesready-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tablesready-tablesready-security.txt
- group: auth
  href: https://artifacts.apis.io/tablesready/well-known/tablesready-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tablesready-status-security.txt
- group: auth
  href: https://artifacts.apis.io/tablesready/well-known/tablesready-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tablesready-security.txt
- group: agent
  href: https://artifacts.apis.io/tablesready/well-known/tablesready-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tablesready-well-known.yml
- group: other
  href: https://artifacts.apis.io/tablesready/hosts/tablesready-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tablesready-hosts.yml
- group: other
  href: https://artifacts.apis.io/tablesready/vendors/tablesready-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tablesready-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tablesready.com/
- group: auth
  title: ''
  type: Security
  url: https://www.tablesready.com/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tablesready
- group: auth
  href: https://artifacts.apis.io/tablesready/security/tablesready-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tablesready-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/tablesready/security/tablesready-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tablesready-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tablesready/security/tablesready-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tablesready-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tablesready.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.tablesready.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tablesready.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tablesready.com/self-guided-demo
- group: operate
  title: ''
  type: Support
  url: https://support.tablesready.com/
- group: company
  title: ''
  type: Blog
  url: https://www.tablesready.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tablesready.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tablesready.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tablesready.com/privacy
coverage:
  checked: '2026-10-27'
  detail: The API reference page https://www.tablesready.com/api returns a 404 page, providing no machine‑readable specification.
  evidence:
  - status: 404
    url: https://www.tablesready.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: TablesReady provides smart waitlist management and scheduling software for restaurants, retail, hospitality, and other service businesses. Their platform lets customers join virtual queues, receive real‑time updates via SMS or app notifications, and helps staff optimize seating and appointment flow. Features include table management, guest messaging, appointment reservations, queue analytics, and integrations with POS systems like Square. The solution aims to reduce wait times, improve customer experience, and increase operational efficiency across multiple industries.
layout: provider
modified: '2026-10-27'
name: TablesReady
nav: Providers
network: true
overview: 'TablesReady is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Waitlist, Scheduling, Restaurant, and SaaS.


  TablesReady''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Tablesready Plans Pricing
  plan_count: 3
  slug: tablesready-plans-pricing
random_paper: 16
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 44.6
    operational_transparency: 31.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tablesready Domain Security
  slug: tablesready-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tablesready Vulnerability Disclosure
  slug: tablesready-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Tablesready Trust Center
  slug: tablesready-trust-center
  summary_line: SOC 2, ISO 27001
slug: tablesready
tags:
- Company
- Waitlist
- Scheduling
- Restaurant
- SaaS
website: https://tablesready.com/
---
