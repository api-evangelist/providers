---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''http://www.homeaway.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.vrbo.com/?vgdc=HAUS&preferlocale=true — a different registrable domain (homeaway.com -> vrbo.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/expedia-group/
- group: company
  title: ''
  type: Website
  url: http://www.homeaway.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/homeaway
- group: auth
  title: ''
  type: Authentication
  url: authentication/homeaway-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/homeaway-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/homeaway-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/homeaway-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/homeaway-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/homeaway-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/homeaway-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/homeaway-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.expediagroup.com/about/privacy-data-handling-requirements/
created: '2026-07-17'
description: 'HomeAway was an Austin, Texas vacation-rental marketplace that connected travelers with owners and property managers of holiday homes, cabins, condos, and beach houses worldwide. It published a first-party HomeAway API (OAuth 2.0) for listing management, availability and booking synchronization, pricing, and guest communication, along with a Ruby SDK and the hacurl command-line tool from its GitHub organization. HomeAway was acquired by Expedia Group in 2015 and the brand was retired into Vrbo: homeaway.com now redirects to Vrbo and the developer platform is no longer maintained. This profile captures the genuine historical first-party API surface (SDK, CLI, OAuth auth model) that remains publicly available.'
image: https://avatars.githubusercontent.com/u/349558?v=4
layout: provider
modified: '2026-07-19'
name: HomeAway *
nav: Providers
network: true
overview: 'HomeAway * is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Vacation Rentals, Travel, and Hospitality.


  HomeAway *''s developer surface includes authentication, CLI, and 10 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: authentication
  name: Homeaway Authentication
  slug: homeaway-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Homeaway Domain Security
  slug: homeaway-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Homeaway Vulnerability Disclosure
  slug: homeaway-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: homeaway
tags:
- Company
- Consumer
- Vacation Rentals
- Travel
- Hospitality
- Marketplace
- Bookings
- Property Management
website: http://www.homeaway.com/
---
