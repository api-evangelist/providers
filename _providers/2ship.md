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
  score: 13.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API Sign-Up page provides access to 2Ship shipping software integration for developers.
  name: 2Ship API
  slug: 2ship-api
artifact_total: 2
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.2ship.com/terms-and-conditions/
- group: agent
  href: https://artifacts.apis.io/2ship/llms/2ship-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/2ship-llms.txt
- group: agent
  href: https://artifacts.apis.io/2ship/well-known/2ship-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/2ship-well-known.yml
- group: other
  href: https://artifacts.apis.io/2ship/hosts/2ship-hosts.yml
  title: ''
  type: Hosts
  url: hosts/2ship-hosts.yml
- group: other
  href: https://artifacts.apis.io/2ship/vendors/2ship-vendors.yml
  title: ''
  type: Vendors
  url: vendors/2ship-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://api.2ship.com/Authentication/Login
- group: auth
  href: https://artifacts.apis.io/2ship/security/2ship-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/2ship-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://2ship.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.2ship.com/integration/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.2ship.com/integration/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://www.2ship.com/integration/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.2ship.com/small-business/create-free-account/
- group: operate
  title: ''
  type: Support
  url: https://www.2ship.com/resources/support/
- group: company
  title: ''
  type: Blog
  url: https://www.2ship.com/resources/blogs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.2ship.com/privacy-policy-2/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.2ship.com/small-business/singup-and-pay-as-you-go/
coverage:
  checked: '2026-10-27'
  detail: The developer portal does not expose any OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://www.2ship.com/integration/developers/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: 2Ship provides shipping software solutions for businesses of all sizes, offering a platform that integrates carrier services, logistics management, and advanced shipping features. Their offerings include packages and pricing plans for small businesses, corporate mailrooms, 3PL providers, and freight forwarders, as well as APIs, ODBC, and embed options for developers to integrate shipping capabilities directly into their applications.
image: https://www.2ship.com/wp-content/uploads/2025/02/New_Website_Images_Fleet_Management_App_Asset-1.png
layout: provider
modified: '2026-10-27'
name: 2Ship
nav: Providers
network: true
overview: '2Ship is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Shipping, Logistics, Software, and API.


  2Ship''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 10 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 2Ship Domain Security
  slug: 2ship-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 2ship
tags:
- Company
- Shipping
- Logistics
- Software
- API
website: https://2ship.com/
---
