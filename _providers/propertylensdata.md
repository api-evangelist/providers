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
api_count: 1
apis:
- description: PropertyLens provides property data APIs for insurers, MGAs, and inspectors, delivering detailed risk assessments and over 3,200 data points for U.S. properties.
  name: PropertyLens API
  slug: propertylens-api
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/propertylensdata/well-known/propertylensdata-propertylens-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/propertylensdata-propertylens-security.txt
- group: agent
  href: https://artifacts.apis.io/propertylensdata/well-known/propertylensdata-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/propertylensdata-well-known.yml
- group: other
  href: https://artifacts.apis.io/propertylensdata/hosts/propertylensdata-hosts.yml
  title: ''
  type: Hosts
  url: hosts/propertylensdata-hosts.yml
- group: other
  href: https://artifacts.apis.io/propertylensdata/vendors/propertylensdata-vendors.yml
  title: ''
  type: Vendors
  url: vendors/propertylensdata-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://propertylens.statuspage.io
- group: start
  title: ''
  type: SignUp
  url: https://my.propertylensdata.com/create-account
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://propertylensdata.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://propertylensdata.com/press
- group: docs
  title: ''
  type: APIReference
  url: https://propertylensdata.com/api-reference
- group: auth
  href: https://artifacts.apis.io/propertylensdata/security/propertylensdata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/propertylensdata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://propertylensdata.com/
coverage:
  checked: '2026-10-18'
  detail: The API reference pages provide data endpoints but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications are available.
  evidence:
  - status: 200
    url: https://propertylensdata.com/api-reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: PropertyLens provides property data APIs for insurers, MGAs, and inspectors, delivering detailed risk assessments, roof condition analysis, replacement cost estimates, permit information, valuations, and over 3,200 data points for any U.S. property. The platform enables real-time access to comprehensive property intelligence to support underwriting, claims, and risk management workflows.
image: https://www.propertylensdata.com/images/og-image.png
layout: provider
modified: '2026-10-18'
name: PropertyLens MCP Server
nav: Providers
network: true
overview: 'PropertyLens MCP Server is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Property Data, Insurance, Real Estate, Risk Assessment, and Inspection.


  PropertyLens MCP Server''s developer surface includes signup flow, API reference, and 9 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 58.0
    operational_transparency: 18.4
  previous_composite: 14.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 7.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/propertylensdata/propertylensdata-2026-11-03T141628.png
security:
- kind: domain-security
  name: Propertylensdata Domain Security
  slug: propertylensdata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: propertylensdata
tags:
- Property Data
- Insurance
- Real Estate
- Risk Assessment
- Inspection
- Replacement Cost
- Scores
website: https://propertylensdata.com/
---
