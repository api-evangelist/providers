---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Token-authenticated REST API (v2) for bulk programmatic access to Enverus' energy datasets — well origins, rigs, permits, producing entities, and production. Authenticate with an API key plus client c
  name: Enverus DirectAccess API
  slug: enverus-directaccess-api
- description: Current version of the Enverus Developer API (formerly Drillinginfo Direct Access). Read-only JSON access to energy datasets — wells, well-origins, wellbores, production, completions, permits, rigs, c
  name: Enverus Developer API (v3)
  slug: enverus-developer-api-v3
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/enverus/llms/enverus-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/enverus-llms.txt
- group: operate
  href: https://artifacts.apis.io/enverus/lifecycle/enverus-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/enverus-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/enverus/hosts/enverus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/enverus-hosts.yml
- group: other
  href: https://artifacts.apis.io/enverus/vendors/enverus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/enverus-vendors.yml
- group: auth
  href: https://artifacts.apis.io/enverus/security/enverus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/enverus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.enverus.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.enverus.com/direct/
- group: docs
  title: ''
  type: Documentation
  url: https://app.enverus.com/direct/#/api/explorer/v2/gettingStarted
- group: start
  title: ''
  type: GettingStarted
  url: https://app.enverus.com/direct/#/api/explorer/v2/gettingStarted
- group: start
  title: ''
  type: Login
  url: https://login.auth.enverus.com/
- group: company
  title: ''
  type: Blog
  url: https://www.enverus.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.enverus.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.enverus.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.enverus.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/enverus
- group: auth
  href: https://artifacts.apis.io/enverus/authentication/enverus-authentication.yml
  title: ''
  type: Authentication
  url: authentication/enverus-authentication.yml
- group: design
  href: https://artifacts.apis.io/enverus/conventions/enverus-conventions.yml
  title: ''
  type: Conventions
  url: conventions/enverus-conventions.yml
- group: design
  href: https://artifacts.apis.io/enverus/lifecycle/enverus-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/enverus-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/enverus/conformance/enverus-conformance.yml
  title: ''
  type: Conformance
  url: conformance/enverus-conformance.yml
- group: agent
  href: https://artifacts.apis.io/enverus/well-known/enverus-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/enverus-well-known.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.drillinginfo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://app.enverus.com/direct/#/api/explorer/v3/gettingStarted
- group: docs
  title: ''
  type: APIReference
  url: https://app.enverus.com/direct/#/api/explorer/v3/gettingStarted
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/enverus-ea
coverage:
  checked: '2026-10-20'
  detail: The DirectAccess API explorer at app.enverus.com/direct/ 302s to an Auth0 login at login.auth.enverus.com, and the API host serves no public OpenAPI (openapi.json/swagger.json return 502).
  evidence:
  - status: 302
    url: https://app.enverus.com/direct/
  - status: 502
    url: https://di-api.drillinginfo.com/v2/direct-access/openapi.json
  - status: 401
    url: https://app.enverus.com/mcp
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: Enverus is an energy-dedicated SaaS company providing analytics, market intelligence, and workflow automation across the global energy value chain — oil and gas, power and renewables, minerals, midstream, trading and risk, and financial services. Its developer surface is the Enverus DirectAccess API (formerly Drillinginfo DirectAccess), a token-authenticated REST API that delivers bulk access to Enverus' energy datasets — well origins, rigs, permits, producing entities, production, and related upstream data — with server-side filter functions, field selection, and cursor-based pagination. Enverus serves 8,000+ companies and 35,000+ energy customers from its Austin, Texas headquarters.
image: https://www.enverus.com/wp-content/uploads/2024/08/enverus-og-logo-1553x1553-1.png
layout: provider
modified: '2026-07-19'
name: Enverus
nav: Providers
network: true
overview: 'Enverus is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Oil and Gas, Energy Data, and Analytics.


  Enverus'' developer surface includes documentation, getting-started guide, engineering blog, support, authentication, API reference, and 18 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 24.2
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/enverus/enverus-2026-07-25T213445.png
security:
- kind: authentication
  name: Enverus Authentication
  slug: enverus-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Enverus Domain Security
  slug: enverus-domain-security
  summary_line: TLSv1.3 · DMARC
slug: enverus
tags:
- Company
- Energy
- Oil and Gas
- Energy Data
- Analytics
- Market Intelligence
- Well Data
- Software-as-a-Service
- Direct Access
- Trading and Risk
- Data
- Geospatial
- Developer API
- Production Data
- Energy Intelligence
website: https://www.enverus.com/
---
