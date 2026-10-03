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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avantifinance/refs/heads/main/hosts/avantifinance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avantifinance-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avantifinance/refs/heads/main/vendors/avantifinance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avantifinance-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avantifinance.co.nz/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avantifinance.co.nz/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.avantifinance.co.nz/news-insights/news/non-bank-of-the-year-2023/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avantifinance/refs/heads/main/security/avantifinance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avantifinance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avantifinance.co.nz
coverage:
  checked: '2026-09-26'
  detail: The provider's API host https://api.co.nz returns HTML shells for typical OpenAPI URLs, offering no machine‑readable contract.
  evidence:
  - status: 200
    url: https://api.co.nz/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Avantifinance is a financial technology company that aims to provide innovative lending solutions for underserved markets. The company focuses on leveraging data-driven underwriting and digital platforms to streamline loan applications, approvals, and servicing. As a relatively new entrant, Avantifinance is building its API ecosystem to enable partners and developers to integrate financing options into their services, though public API documentation is not yet available. The firm targets small and medium enterprises in emerging economies, offering flexible credit terms and real-time decisioning powered by machine learning models. Its platform includes APIs for loan origination, repayment tracking, and compliance reporting, positioning Avantifinance as a modern fintech bridge between lenders and borrowers.
layout: provider
modified: '2026-09-26'
name: Avantifinance
nav: Providers
network: true
overview: Avantifinance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Lending, and Data-Driven.
random_paper: 3
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 37.5
    operational_transparency: 0.0
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avantifinance Domain Security
  slug: avantifinance-domain-security
  summary_line: TLSv1.3 · DMARC
slug: avantifinance
tags:
- Company
- Fintech
- Lending
- Data-Driven
website: https://www.avantifinance.co.nz
---
