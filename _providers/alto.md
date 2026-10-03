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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alto/refs/heads/main/llms/alto-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alto-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/alto/refs/heads/main/plans/alto-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alto-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alto/refs/heads/main/well-known/alto-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/alto-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alto/refs/heads/main/well-known/alto-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alto-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alto/refs/heads/main/hosts/alto-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alto-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alto/refs/heads/main/vendors/alto-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alto-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.altoira.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.altoira.com/help-center
- group: operate
  title: ''
  type: StatusPage
  url: https://status.altoira.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.altoira.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.altoira.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.altoira.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alto/refs/heads/main/security/alto-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.altoira.com/
created: '2026-09-24'
description: Alto provides a platform that enables private wealth advisors, financial institutions, issuers, and individual investors to access private market investments—such as private equity, venture capital, real estate, and infrastructure—through self‑directed retirement accounts (IRAs). The service includes a curated marketplace, a private deal room for retirement‑capital funded deals, and infrastructure for enterprises to embed retirement‑account investing. Alto operates as a chartered trust company and registered broker‑dealer to facilitate compliance and custody for these alternative allocations.
layout: provider
modified: '2026-09-24'
name: Alto
nav: Providers
network: true
overview: 'Alto is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Private Markets, Retirement Accounts, IRA, Wealth Advisors, and Issuers.


  Alto''s developer surface includes support, pricing, and 12 more developer resources.'
plans:
- name: Alto Plans Pricing
  plan_count: 2
  slug: alto-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 33.0
    catalog_earned_first_party: 8.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 53.6
    operational_transparency: 15.8
  previous_composite: 17.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alto Domain Security
  slug: alto-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alto
tags:
- Private Markets
- Retirement Accounts
- IRA
- Wealth Advisors
- Issuers
- Self-Directed Investing
- Alternative Investments
website: https://www.altoira.com/
---
