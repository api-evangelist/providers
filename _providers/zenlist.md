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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/zenlist/vendors/zenlist-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zenlist-vendors.yml
- group: agent
  href: https://artifacts.apis.io/zenlist/llms/zenlist-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zenlist-llms.txt
- group: auth
  href: https://artifacts.apis.io/zenlist/well-known/zenlist-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zenlist-help-security.txt
- group: agent
  href: https://artifacts.apis.io/zenlist/well-known/zenlist-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zenlist-well-known.yml
- group: other
  href: https://artifacts.apis.io/zenlist/hosts/zenlist-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zenlist-hosts.yml
- group: build
  href: https://artifacts.apis.io/zenlist/integrations/zenlist-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/zenlist-integration-edges.yml
- group: docs
  title: ''
  type: Documentation
  url: https://help.zenlist.com/
- group: auth
  href: https://artifacts.apis.io/zenlist/security/zenlist-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zenlist-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zenlist.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zenlist
- group: build
  title: ''
  type: Tools
  url: https://rules.zenlist.dev/
- group: start
  title: ''
  type: Login
  url: https://zenlist.com/app/sign-in
- group: operate
  title: ''
  type: Support
  url: https://help.zenlist.com/en/
- group: company
  title: ''
  type: Blog
  url: https://blog.zenlist.com
- group: company
  title: ''
  type: Newsroom
  url: https://enterprise.zenlist.com/press
- group: company
  title: ''
  type: Partner
  url: https://enterprise.zenlist.com/for-mlss
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zenlist.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zenlist.com/privacy
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://blog.zenlist.com/mcp
  - status: 200
    url: https://zenlist.com/
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Zenlist is a collaborative home-search platform for real estate agents and their clients, with MLS-level search on MLS inventory, in-app chat, listing notes, showing requests and itineraries across Mac, Windows, iOS and Android apps, and enterprise offerings for brokerages, teams and MLSs (for example the SFAR MLS mobile app). It contributes open-source RESO tooling on GitHub, including a Rust implementation of RESO RCP-19 RETS validation expressions with compliance tests, and runs a public Rules Playground (rules.zenlist.dev) for listing validation rules. Zenlist publishes no public API, developer documentation or machine-readable contract.
image: https://21517349.fs1.hubspotusercontent-na1.net/hubfs/21517349/Images%20for%20website/ZenlistBannerBig.jpg
layout: provider
modified: '2026-10-13'
name: Zenlist
nav: Providers
network: true
overview: 'Zenlist is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Home Search, MLS, and RESO.


  Zenlist''s developer surface includes documentation, tooling, support, engineering blog, and 14 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 56.3
    operational_transparency: 13.2
  previous_composite: 17.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/zenlist/zenlist-2026-11-03T150455.png
security:
- kind: domain-security
  name: Zenlist Domain Security
  slug: zenlist-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: zenlist
tags:
- Company
- Real Estate
- Home Search
- MLS
- RESO
- Brokerage Software
website: https://zenlist.com/
---
