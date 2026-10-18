---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bruce-markets/refs/heads/main/well-known/bruce-markets-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bruce-markets-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bruce-markets/refs/heads/main/hosts/bruce-markets-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bruce-markets-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bruce-markets/refs/heads/main/vendors/bruce-markets-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bruce-markets-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bruce-markets/refs/heads/main/security/bruce-markets-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bruce-markets-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
- group: start
  title: ''
  type: SignUp
  url: https://fe.secondmarket.com/preplatform/
- group: start
  title: ''
  type: Login
  url: https://fe.login.secondmarket.com/
- group: company
  title: ''
  type: About
  url: https://www.nasdaqprivatemarket.com/about-us/
- group: company
  title: ''
  type: Careers
  url: https://www.nasdaqprivatemarket.com/careers/
coverage:
  checked: '2026-10-06'
  detail: The Bruce Markets website provides no machine‑readable API documentation; attempts to locate OpenAPI or developer pages return 404.
  evidence:
  - status: 404
    url: https://www.brucemarkets.com/developer
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: Bruce Markets operates as a secondary market platform enabling the buying and selling of private company shares. Hosted on the Nasdaq Private Market, it provides liquidity solutions for pre-IPO stock, structured secondary transactions, and capital solutions for private firms and investors. The platform facilitates secure, compliant transactions, offering tools for investors, companies, and advisors to manage equity ownership and liquidity events in the private market ecosystem.
layout: provider
modified: '2026-10-06'
name: Bruce Markets
nav: Providers
network: true
overview: 'Bruce Markets is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Secondary Market, Private Equity, Liquidity, and Fintech.


  Bruce Markets'' developer surface includes signup flow and 8 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bruce Markets Domain Security
  slug: bruce-markets-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bruce-markets
tags:
- Company
- Secondary Market
- Private Equity
- Liquidity
- Fintech
website: https://www.nasdaqprivatemarket.com/
---
