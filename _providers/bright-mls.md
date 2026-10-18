---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Bright Mls Agentic Access
  operation_count: 7
  slug: bright-mls-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 3
apis:
- description: 'OData-based RESO Web API giving licensed vendors access to Bright MLS listing data described by the RESO Data Dictionary; the $metadata document and the service root require a bearer token (anonymous '
  name: Bright MLS RESO Web API
  slug: bright-mls-reso-web-api
- description: ShowingHub is an MLS-provided service for interoperability between showing-scheduling systems, covering registrations and transfers, appointments and event notifications through subscriptions; per-env
  name: Bright MLS ShowingHub API
  slug: bright-mls-showinghub-api
- baseURL: https://bright-reso.brightmls.com/RESO/OData/bright
  baseurl_source: declared
  description: The Auth API from Bright MLS — 1 operation(s) for auth.
  name: Bright MLS Auth API
  slug: bright-mls-auth-api
- baseURL: https://bright-reso.brightmls.com/RESO/OData/bright
  baseurl_source: declared
  description: The Listing API from Bright MLS — 2 operation(s) for listing.
  name: Bright MLS Listing API
  slug: bright-mls-listing-api
- baseURL: https://bright-reso.brightmls.com/RESO/OData/bright
  baseurl_source: declared
  description: Operations available to Manifests
  name: Bright MLS Manifests API
  slug: bright-mls-manifests-api
- baseURL: https://bright-reso.brightmls.com/RESO/OData/bright
  baseurl_source: declared
  description: The User API from Bright MLS — 1 operation(s) for user.
  name: Bright MLS User API
  slug: bright-mls-user-api
- baseURL: https://bright-reso.brightmls.com/RESO/OData/bright
  baseurl_source: declared
  description: The Data Hub API from Bright MLS — 1 operation(s) for data hub.
  name: Bright MLS Data Hub API
  slug: bright-mls-data-hub-api
artifact_total: 20
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bright-mls/refs/heads/main/agentic-access/bright-mls-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bright-mls-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bright-mls/refs/heads/main/rules/bright-mls-rules.yml
  title: ''
  type: Spectral
  url: rules/bright-mls-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bright-mls/refs/heads/main/json-ld/bright-mls-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bright-mls-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bright-mls/refs/heads/main/vocabulary/bright-mls-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bright-mls-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bright-mls/refs/heads/main/data-model/bright-mls-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bright-mls-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bright-mls/refs/heads/main/errors/bright-mls-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bright-mls-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bright-mls/refs/heads/main/conformance/bright-mls-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bright-mls-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bright-mls/refs/heads/main/llms/bright-mls-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bright-mls-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bright-mls/refs/heads/main/hosts/bright-mls-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bright-mls-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bright-mls/refs/heads/main/vendors/bright-mls-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bright-mls-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bright-mls/refs/heads/main/authentication/bright-mls-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bright-mls-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bright-mls/refs/heads/main/security/bright-mls-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bright-mls-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brightmls.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.brightmls.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.brightmls.com/benefits/developers
- group: operate
  title: ''
  type: Support
  url: https://support.brightmls.com/s/
- group: start
  title: ''
  type: Login
  url: https://login.brightmls.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.brightmls.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brightmls.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brightmls.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.brightmls.com/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BrightMLS
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brightmls.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.brightmls.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Bright MLS is one of the largest multiple listing services in the United States, serving real estate professionals across the Mid-Atlantic. Its developer portal (developer.brightmls.com, a SwaggerHub Portal) documents the RESO Web API (OData, RESO Data Dictionary 1.6 Platinum certified) for licensed listing data and the ShowingHub showing-scheduling interoperability API, and its public SwaggerHub registry publishes OpenAPI contracts for the Data Hub ingestion and DataLake distribution services and the Manifest Services API for media vendors.
image: https://images.ctfassets.net/1g8q1frp41ix/19Q1y6e6KSRESmQY8117MC/28b12fb1278bf35568ad05efd3c7b577/social-share-default-image.jpg
json_schemas:
- name: authTokenBody
  property_count: 2
  slug: bright-mls-auth-token-body
- name: authTokenResponse
  property_count: 4
  slug: bright-mls-auth-token-response
- name: GetPackageResponse
  property_count: 4
  slug: bright-mls-get-package-response
- name: IngestionApiBody
  property_count: 3
  slug: bright-mls-ingestion-api-body
- name: Manifest
  property_count: 6
  slug: bright-mls-manifest
- name: userApiBody
  property_count: 4
  slug: bright-mls-user-api-body
- name: userApiResponse
  property_count: 4
  slug: bright-mls-user-api-response
- name: UuidResponse
  property_count: 1
  slug: bright-mls-uuid-response
jsonld:
- class_count: 19
  name: Bright Mls Context
  property_count: 35
  slug: bright-mls-context
layout: provider
modified: '2026-10-14'
name: Bright MLS
nav: Providers
network: true
overview: 'Bright MLS publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Listing API, Manifests API, and 4 more. Tagged areas include Company, Real Estate, MLS, RESO, and OData.


  The Bright MLS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bright MLS''s developer surface includes authentication, documentation, support, pricing, engineering blog, and 18 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Bright MLS API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 1
  slug: bright-mls-rules
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 35.6
    contract_quality: 61.7
    developer_ergonomics: 38.1
    discoverability: 69.6
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Bright Mls Authentication
  slug: bright-mls-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Bright Mls Domain Security
  slug: bright-mls-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bright-mls
tags:
- Company
- Real Estate
- MLS
- RESO
- OData
- Listings
- Property Data
website: https://www.brightmls.com
---
