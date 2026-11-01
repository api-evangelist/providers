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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/signed-com/llms/signed-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/signed-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/signed-com/well-known/signed-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/signed-com-security.txt
- group: auth
  href: https://artifacts.apis.io/signed-com/well-known/signed-com-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/signed-com-mcp-security.txt
- group: agent
  href: https://artifacts.apis.io/signed-com/well-known/signed-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/signed-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/signed-com/hosts/signed-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/signed-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/signed-com/vendors/signed-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/signed-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/signed-com/security/signed-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/signed-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/signed-com/security/signed-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/signed-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://signed.com/
- group: company
  title: ''
  type: Blog
  url: https://signed.com/blog
- group: start
  title: ''
  type: Login
  url: https://signed.com/sign_in
- group: commercial
  title: ''
  type: Pricing
  url: https://signed.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://signed.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://signed.com/investors/security
- group: start
  title: ''
  type: SignUp
  url: https://signed.com/signup
coverage:
  checked: '2026-10-30'
  detail: No public developer program or API documentation is available on the website.
  evidence:
  - status: 404
    url: https://signed.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-30'
description: Signed is an angel investor portfolio tracking platform that helps startup founders and investors monitor equity holdings, calculate returns, and stay informed about follow‑on opportunities. The service provides AI‑driven diligence, QSBS tax analysis, pro‑rata alerts, and automated portfolio updates, enabling users to track multiple entities such as funds, SPVs, LLCs, and personal holdings in one place. It offers free access to core features and premium tools for deeper financial insights.
image: https://signed.com/og.png
layout: provider
modified: '2026-10-30'
name: signed-com
nav: Providers
network: true
overview: 'signed-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Angel Investing, Portfolio Tracking, Equity Management, and Startup Funding.


  signed-com''s developer surface includes engineering blog, pricing, signup flow, and 12 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: derived
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
- kind: domain-security
  name: Signed Com Domain Security
  slug: signed-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Signed Com Vulnerability Disclosure
  slug: signed-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: signed-com
tags:
- Company
- Angel Investing
- Portfolio Tracking
- Equity Management
- Startup Funding
website: https://signed.com/
---
