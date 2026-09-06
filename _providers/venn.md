---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.7
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Venn's tenant-facing GraphQL API, served through an Apollo Federation gateway on AWS API Gateway. Anonymous introspection returns the full contract — 1,983 types, 320 query fields, 357 mutation fields
  name: Venn Tenant GraphQL API
  slug: venn-tenant-graphql-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/venn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://venn.city/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://venn.city/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://venn.city/privacy
- group: start
  title: ''
  type: Login
  url: https://dashboard.venn.city/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/venn-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.venn.city/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/venn-city
- group: build
  title: ''
  type: Packages
  url: packages/venn-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/venn-packages.yml
- group: design
  title: ''
  type: Components
  url: components/venn-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/venn-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/venn-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/venn-data-model.yml
- group: other
  title: ''
  type: Listing
  url: https://forgeglobal.com/venn_stock/
created: '2026-09-02'
description: Venn is a multifamily resident-experience operating system for owner-operators of rental housing. Founded in 2016 and co-headquartered in New York and Tel Aviv, it merges a resident-facing mobile app, an operator dashboard and a single data layer over the resident lifecycle — leasing, onboarding, living, renewals, maintenance, payments, community programming and an AI concierge — synced with the property management system of record (Yardi, RealPage, Entrata, AppFolio). Venn runs an unversioned Apollo Federation GraphQL API at api.venn.city with anonymous introspection enabled, 320 query fields and 357 mutation fields across 468 object types, authenticated with AWS Cognito bearer tokens. It publishes no developer portal, API reference, OpenAPI or pricing; the contract is discoverable but the data and the docs are not public.
image: https://cdn.prod.website-files.com/6914773f376e5aaadf703caa/6914773f376e5aaadf703de2_logo.svg
layout: provider
modified: '2026-09-02'
name: Venn
nav: Providers
network: true
overview: 'Venn publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Property Management, Multifamily, Resident Experience, and Proptech.


  Venn''s developer surface includes changelog, release notes, and 14 more developer resources.'
plans:
- name: Venn Plans Pricing
  plan_count: 0
  slug: venn-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Venn Rate Limits
  slug: venn-rate-limits
scopes:
- name: Venn Scopes
  scope_count: 0
  slug: venn-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 37.2
    developer_ergonomics: 20.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 33.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Venn Authentication
  slug: venn-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Venn Domain Security
  slug: venn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: venn
tags:
- Real Estate
- Property Management
- Multifamily
- Resident Experience
- Proptech
- Leasing
- Community
- Payments
- GraphQL
- Mobile Apps
website: https://venn.city/
---
