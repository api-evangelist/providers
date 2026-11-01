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
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/glory-global-solutions/llms/glory-global-solutions-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/glory-global-solutions-llms.txt
- group: other
  href: https://artifacts.apis.io/glory-global-solutions/hosts/glory-global-solutions-hosts.yml
  title: ''
  type: Hosts
  url: hosts/glory-global-solutions-hosts.yml
- group: other
  href: https://artifacts.apis.io/glory-global-solutions/vendors/glory-global-solutions-vendors.yml
  title: ''
  type: Vendors
  url: vendors/glory-global-solutions-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.glory-global.com/en-us/terms
- group: auth
  title: ''
  type: Security
  url: https://www.glory-global.com/en-us/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.glory-global.com/en-us/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.glory-global.com/en-us/news
- group: auth
  href: https://artifacts.apis.io/glory-global-solutions/security/glory-global-solutions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/glory-global-solutions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://glory-global.com/
coverage:
  checked: '2026-10-27'
  detail: No public developer portal or API documentation was found; attempts to locate API specs returned 404/307.
  evidence:
  - status: 307
    url: https://www.glory-global.com/en-us/api
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: Glory Global Solutions provides cash handling automation and transaction processing technologies for retail, banking, gaming, and hospitality sectors. Their platform integrates cash‑in‑transit services, vending solutions, and digital payment workflows to streamline cash operations across multiple industries worldwide.
image: https://www.glory-global.com/media/gloryglobal/generic-imagery-1140x810/homepage-image-1440x810-.jpg?h=810&iar=0&w=1440
layout: provider
modified: '2026-10-27'
name: Glory
nav: Providers
network: true
overview: Glory is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CashAutomation, RetailTech, FinancialServices, and Gaming.
random_paper: 0
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Glory Global Solutions Domain Security
  slug: glory-global-solutions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: glory-global-solutions
tags:
- Company
- CashAutomation
- RetailTech
- FinancialServices
- Gaming
website: https://glory-global.com/
---
