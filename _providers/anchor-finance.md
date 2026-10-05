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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anchor-finance/refs/heads/main/hosts/anchor-finance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anchor-finance-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anchor-finance/refs/heads/main/vendors/anchor-finance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anchor-finance-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anchor-finance/refs/heads/main/security/anchor-finance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anchor-finance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anchoredfinance.com/
coverage:
  checked: 2026-09-24
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on anchoredfinance.com or api.anchoredfinance.com.
  evidence:
  - status: 200
    url: https://anchoredfinance.com/api-docs
  - status: 200
    url: https://anchoredfinance.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: Anchored Finance is a premier auto finance lender offering quick approvals and funding for used auto loans. With over 50 years of combined experience, the company provides tailored financing solutions to customers, emphasizing speed, reliability, and personalized service across its nationwide network.
image: https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/f8a220ff-552d-40b2-8101-9b3fa358919f/id-preview-4a9faa7c--0619f550-3b13-480e-9fef-8622cdb86010.lovable.app-1774453650516.png
layout: provider
modified: '2026-09-24'
name: Anchor Finance
nav: Providers
network: true
overview: Anchor Finance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Auto Loans, Lending, Financial Services, and Company.
random_paper: 18
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anchor Finance Domain Security
  slug: anchor-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anchor-finance
tags:
- Finance
- Auto Loans
- Lending
- Financial Services
- Company
website: https://anchoredfinance.com/
---
