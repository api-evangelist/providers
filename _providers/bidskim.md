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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: BidSkim offers a read‑only API for accessing public tender data; documentation is at the MCP page.
  name: BidSkim API
  slug: bidskim-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/bidskim/plans/bidskim-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bidskim-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bidskim/llms/bidskim-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bidskim-llms.txt
- group: other
  href: https://artifacts.apis.io/bidskim/hosts/bidskim-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bidskim-hosts.yml
- group: other
  href: https://artifacts.apis.io/bidskim/vendors/bidskim-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bidskim-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://bidskim.com/market/security
- group: docs
  title: ''
  type: Documentation
  url: https://bidskim.com/guides
- group: auth
  href: https://artifacts.apis.io/bidskim/security/bidskim-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bidskim-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bidskim.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bidskim.com/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://bidskim.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bidskim.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bidskim.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://bidskim.com/support
- group: start
  title: ''
  type: SignUp
  url: https://bidskim.com/signup
coverage:
  checked: '2026-10-30'
  detail: BidSkim provides a public MCP page but no OpenAPI, GraphQL, AsyncAPI, or other machine‑readable contract is published.
  evidence:
  - status: 200
    url: https://bidskim.com/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: BidSkim provides AI-powered tender match reports for small suppliers in Britain, delivering daily email alerts of public-sector contracts that fit the supplier's services, region, contract size and certifications. It reads over 600 buyer sites each morning, covering 800,000+ notices, 10,000+ buyers, and helps users win public contracts by surfacing relevant opportunities early, saving time and increasing win rates.
image: https://bidskim.com/source-logos/find-a-tender-logo.png
layout: provider
modified: '2026-10-30'
name: BidSkim
nav: Providers
network: true
overview: 'BidSkim is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include procurement, public-sector, tenders, UK, and construction.


  BidSkim''s developer surface includes documentation, pricing, support, signup flow, and 10 more developer resources.'
plans:
- name: Bidskim Plans Pricing
  plan_count: 3
  slug: bidskim-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Bidskim Rate Limits
  slug: bidskim-rate-limits
scopes:
- name: Bidskim Scopes
  scope_count: 0
  slug: bidskim-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 21.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bidskim Authentication
  slug: bidskim-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bidskim Domain Security
  slug: bidskim-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bidskim
tags:
- procurement
- public-sector
- tenders
- UK
- construction
- AI
website: https://bidskim.com
---
