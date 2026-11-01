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
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/rapidratings/well-known/rapidratings-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/rapidratings-help-security.txt
- group: agent
  href: https://artifacts.apis.io/rapidratings/well-known/rapidratings-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rapidratings-well-known.yml
- group: other
  href: https://artifacts.apis.io/rapidratings/hosts/rapidratings-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rapidratings-hosts.yml
- group: other
  href: https://artifacts.apis.io/rapidratings/vendors/rapidratings-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rapidratings-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rapidratings.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://help.rapidratings.com/en/
- group: start
  title: ''
  type: SignUp
  url: https://accounts.rapidratings.com/network/signup?clientCode=rVf9kZ-1926
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rapidratings.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.rapidratings.com/our-insights/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.rapidratings.com/company/leadership
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.rapidratings.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.rapidratings.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RapidRatings
- group: auth
  href: https://artifacts.apis.io/rapidratings/security/rapidratings-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rapidratings-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rapidratings.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://rapidratings.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: RapidRatings provides enterprise‑level risk management solutions that assess supply‑chain, third‑party, and credit risk for businesses. Their platform offers tools such as Financial Health Ratings (FHR), RiskPulse, ActionPath, and MCP integration to help companies evaluate and improve the financial stability of suppliers and partners. RapidRatings also offers professional services, workshops, and a badge program to support risk mitigation and compliance across industries.
image: https://cdn.prod.website-files.com/6344850f6651847c3d7112cb/6448c237de882e63dba203de_RR%20Opengraph_1.png
layout: provider
modified: '2026-10-21'
name: RapidRatings
nav: Providers
network: true
overview: 'RapidRatings is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Risk, SupplyChain, Credit, and ThirdParty.


  RapidRatings'' developer surface includes support, signup flow, documentation, and 12 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 51.8
    operational_transparency: 15.8
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
  name: Rapidratings Domain Security
  slug: rapidratings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rapidratings
tags:
- Company
- Risk
- SupplyChain
- Credit
- ThirdParty
website: https://rapidratings.com/
---
