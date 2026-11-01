---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
  score: 8.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Public, read‑only REST API for Bill Commons providing legislative search and data across all 50 US states + DC.
  name: Bill Commons API
  slug: bill-commons-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/billcommons-org/plans/billcommons-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/billcommons-org-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/billcommons-org/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/billcommons-org/changelog/billcommons-org-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/billcommons-org-changelog.yml
- group: auth
  href: https://artifacts.apis.io/billcommons-org/authentication/billcommons-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/billcommons-org-authentication.yml
- group: design
  href: https://artifacts.apis.io/billcommons-org/conformance/billcommons-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/billcommons-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/billcommons-org/llms/billcommons-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/billcommons-org-llms.txt
- group: other
  href: https://artifacts.apis.io/billcommons-org/hosts/billcommons-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/billcommons-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/billcommons-org/vendors/billcommons-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/billcommons-org-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://billcommons.org/terms
- group: operate
  title: ''
  type: Support
  url: https://billcommons.org/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://billcommons.org/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://billcommons.org/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://billcommons.org/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://billcommons.org/docs/chatgpt
- group: docs
  title: ''
  type: APIReference
  url: https://api.billcommons.org/docs
- group: auth
  href: https://artifacts.apis.io/billcommons-org/security/billcommons-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/billcommons-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://billcommons.org/
created: '2026-10-30'
description: 'billcommons-org is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-30'
name: billcommons-org
nav: Providers
network: true
overview: 'billcommons-org is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Legislative data, State bills, API, Open source, and Research tools.


  billcommons-org''s developer surface includes changelog, authentication, support, pricing, getting-started guide, API reference, and 11 more developer resources.'
plans:
- name: Billcommons Org Plans Pricing
  plan_count: 5
  slug: billcommons-org-plans-pricing
random_paper: 20
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 16.4
    contract_quality: 0.0
    developer_ergonomics: 42.1
    discoverability: 53.6
    operational_transparency: 15.8
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
- kind: authentication
  name: Billcommons Org Authentication
  slug: billcommons-org-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Billcommons Org Domain Security
  slug: billcommons-org-domain-security
  summary_line: TLSv1.3 · HSTS
slug: billcommons-org
tags:
- Legislative data
- State bills
- API
- Open source
- Research tools
website: https://billcommons.org/
---
