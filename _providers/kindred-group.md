---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
  score: 6.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Developer portal providing API documentation for sportsbook, racing, casino, and poker feeds.
  name: Kindred Group API
  slug: kindred-group-api
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/kindred-group/well-known/kindred-group-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kindred-group-www-security.txt
- group: agent
  href: https://artifacts.apis.io/kindred-group/well-known/kindred-group-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kindred-group-well-known.yml
- group: agent
  href: https://artifacts.apis.io/kindred-group/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/kindred-group/hosts/kindred-group-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kindred-group-hosts.yml
- group: build
  href: https://artifacts.apis.io/kindred-group/packages/kindred-group-packages.yml
  title: ''
  type: SDKs
  url: packages/kindred-group-packages.yml
- group: build
  href: https://artifacts.apis.io/kindred-group/packages/kindred-group-packages.yml
  title: ''
  type: Packages
  url: packages/kindred-group-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fdjunited.com/legal-notice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fdjunited.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.fdjunited.com/news/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.kindredgroup.com/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kindredgroup.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kindredgroup
- group: auth
  href: https://artifacts.apis.io/kindred-group/security/kindred-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kindred-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kindredgroup.com/
coverage:
  checked: '2026-10-15'
  detail: Developer portal provides documentation but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://developer.kindredgroup.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Kindred Group, operating under the brand FDJ United, is a leading European gaming company offering a broad portfolio of iconic brands and advanced technological solutions. The company focuses on responsible gaming, social responsibility, and innovation, with a strong presence across multiple markets and a commitment to stakeholder engagement and sustainable growth.
image: https://www.fdjunited.com/wp-content/uploads/2025/02/GettyImages-1058526628.jpg
layout: provider
modified: '2026-10-15'
name: Kindred Group
nav: Providers
network: true
overview: 'Kindred Group is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Technology, Responsible Gaming, and Europe.


  Kindred Group''s developer surface includes getting-started guide, documentation, and 12 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.0
    discoverability: 58.9
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 19.0
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kindred Group Domain Security
  slug: kindred-group-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: kindred-group
tags:
- Company
- Gaming
- Technology
- Responsible Gaming
- Europe
website: https://kindredgroup.com/
---
