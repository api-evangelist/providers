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
api_count: 1
apis:
- description: API integration options for agents and brokers, though no machine‑readable contract was found.
  name: Coterie Insurance API
  slug: coterie-insurance-api
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coteriee1d3/refs/heads/main/well-known/coteriee1d3-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coteriee1d3-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coteriee1d3/refs/heads/main/well-known/coteriee1d3-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coteriee1d3-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coteriee1d3/refs/heads/main/hosts/coteriee1d3-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coteriee1d3-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coteriee1d3/refs/heads/main/vendors/coteriee1d3-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coteriee1d3-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coterieinsurance.com/
- group: company
  title: ''
  type: Newsroom
  url: https://coterieinsurance.com/newsroom/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coteriee1d3/refs/heads/main/security/coteriee1d3-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coteriee1d3-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coterieinsurance.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://coterieinsurance.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://coterieinsurance.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://coterieinsurance.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://coterieinsurance.com/agents-brokers/
- group: operate
  title: ''
  type: Support
  url: https://coterieinsurance.com/support/
- group: company
  title: ''
  type: Blog
  url: https://coterieinsurance.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://coterieinsurance.com/insurance/
- group: start
  title: ''
  type: SignUp
  url: https://coterieinsurance.com/agents-brokers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coterieinsurance.com/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coterieinsurance.com/legal/privacy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/coterieinsurance/workspace
coverage:
  checked: '2026-10-11'
  detail: Developer portal redirects to homepage with JS‑rendered content, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://coterieinsurance.com/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-11'
description: Coterie Insurance provides small business insurance solutions that streamline coverage and underwriting for agents, brokers, and owners. The platform offers digital, real-time underwriting, instant binding, and a range of policies including General Liability, Business Owners Policy, Professional Liability, Cyber Insurance, and Workplace Violence coverage. It serves agents and small business owners through an online portal with API integration options, aiming to simplify the insurance process and accelerate quote-to-bind times.
image: https://coterieinsurance.com/wp-content/uploads/2022/08/icon-agents-brokers.svg
layout: provider
modified: '2026-10-11'
name: Coteriee1d3
nav: Providers
network: true
overview: 'Coteriee1d3 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Small Business, Fintech, Software-as-a-Service, and Company.


  Coteriee1d3''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 12 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 58.9
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 17.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coteriee1D3 Domain Security
  slug: coteriee1d3-domain-security
  summary_line: TLSv1.3 · DMARC
slug: coteriee1d3
tags:
- Insurance
- Small Business
- Fintech
- Software-as-a-Service
- Company
website: https://coterieinsurance.com
---
