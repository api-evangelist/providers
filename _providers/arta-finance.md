---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 16.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/arta-finance/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/arta-finance/well-known/arta-finance-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arta-finance-well-known.yml
- group: other
  href: https://artifacts.apis.io/arta-finance/hosts/arta-finance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arta-finance-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.arta.finance/
- group: auth
  href: https://artifacts.apis.io/arta-finance/security/arta-finance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arta-finance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arta.finance
coverage:
  checked: '2026-10-29'
  detail: The provider's website https://arta.finance returns a JavaScript shell with no machine-readable documentation.
  evidence:
  - status: 200
    url: https://arta.finance
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Arta is a global wealth platform that enables individuals and institutions to manage, invest, and grow their financial assets through a unified digital experience. The company provides tools for portfolio tracking, investment insights, and seamless integration with banking and brokerage services. Backed by Ribbit Capital, Arta focuses on delivering secure, scalable, and user‑friendly solutions for wealth management across multiple markets.
image: https://app.artafinance.com/share_thumb.png
layout: provider
modified: '2026-10-28'
name: Arta
nav: Providers
network: true
overview: 'Arta is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include FinTech, WealthManagement, Investment, API, and Finance.


  Arta''s developer surface includes documentation and 5 more developer resources.'
random_paper: 17
scopes:
- name: Arta Finance Scopes
  scope_count: 0
  slug: arta-finance-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arta Finance Authentication
  slug: arta-finance-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Arta Finance Domain Security
  slug: arta-finance-domain-security
  summary_line: TLSv1.3
slug: arta-finance
tags:
- FinTech
- WealthManagement
- Investment
- API
- Finance
- Company
website: https://arta.finance
---
