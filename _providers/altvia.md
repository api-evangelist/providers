---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/altvia/well-known/altvia-apis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/altvia-apis-security.txt
- group: build
  href: https://artifacts.apis.io/altvia/integrations/altvia-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/altvia-integration-edges.yml
- group: agent
  href: https://artifacts.apis.io/altvia/well-known/altvia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/altvia-well-known.yml
- group: other
  title: ''
  type: Leadership
  url: https://altvia.com/leadership/
- group: start
  title: ''
  type: Login
  url: https://apis.io/api/v1/auth/login
- group: start
  title: ''
  type: GettingStarted
  url: https://apis.io/onboarding/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.apis.io/
- group: docs
  title: ''
  type: APIReference
  url: https://apis.io/llms.txt
- group: auth
  title: ''
  type: Compliance
  url: https://trust.altvia.com/
- group: auth
  href: https://artifacts.apis.io/altvia/security/altvia-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/altvia-trust-center.yml
- group: other
  href: https://artifacts.apis.io/altvia/hosts/altvia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/altvia-hosts.yml
- group: other
  href: https://artifacts.apis.io/altvia/vendors/altvia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/altvia-vendors.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://www.marlinequity.com/
- group: company
  title: ''
  type: Website
  url: https://altvia.com/
- group: company
  title: ''
  type: Blog
  url: https://altvia.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://altvia.com/get-support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://altvia.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://altvia.com/newsroom/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.altvia.com/
- group: auth
  href: https://artifacts.apis.io/altvia/security/altvia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/altvia-domain-security.yml
coverage:
  checked: '2026-10-20'
  detail: 'Altvia publishes no developer portal or API contract: altvia.com/developers/ and api.altvia.com do not resolve to any docs, support.altvia.com is a "Coming Soon" page, and the only machine surface is a gated SOC 2 trust center at trust.altvia.com.'
  evidence:
  - status: 200
    url: https://altvia.com/
  - status: 200
    url: https://support.altvia.com/
  - status: 200
    url: https://trust.altvia.com/
  - status: 403
    url: https://altvia.com/developers/
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Altvia is fund management software purpose-built for private capital markets, serving private equity, venture capital, fund of funds, real estate, hedge funds, family offices, and placement agents. Built on the Salesforce platform, Altvia unifies a purpose-built CRM, a virtual data room (VDR) and LP investor portal, analytics and reporting, and an AI assistant (AIMe) into one system that spans the full fund lifecycle — capital raising, investor relations, and deal management. Founded in 2006 and based in Broomfield, Colorado, Altvia was acquired by Marlin Equity Partners in 2022. The company exposes no public developer/API portal; integrations are delivered through the platform and the Salesforce ecosystem.
image: https://altvia.com/wp-content/themes/Altvia/favicon.png?v=2
layout: provider
modified: '2026-10-20'
name: Altvia
nav: Providers
network: true
overview: 'Altvia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CRM, Private Equity, Venture Capital, and Fund Management.


  Altvia''s developer surface includes getting-started guide, documentation, API reference, engineering blog, support, and 15 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 20.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/altvia/altvia-2026-07-25T195848.png
security:
- kind: domain-security
  name: Altvia Domain Security
  slug: altvia-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Altvia Trust Center
  slug: altvia-trust-center
  summary_line: SOC 2
slug: altvia
tags:
- Company
- CRM
- Private Equity
- Venture Capital
- Fund Management
- Investor Relations
- Alternative Investments
- Salesforce
- Software-as-a-Service
website: https://altvia.com/
---
