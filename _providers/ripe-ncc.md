---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: RIPE Database RESTful API
  name: RIPE Database REST API
  slug: ripe-database-rest-api
- baseURL: https://rest.db.ripe.net
  baseurl_source: declared
  description: 'RIPE NCC API as documented publicly: 28 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: RIPE NCC API
  slug: ripe-ncc-api
artifact_total: 14
common:
- group: auth
  href: https://artifacts.apis.io/ripe-ncc/well-known/ripe-ncc-trust-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ripe-ncc-trust-security.txt
- group: auth
  href: https://artifacts.apis.io/ripe-ncc/well-known/ripe-ncc-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ripe-ncc-status-security.txt
- group: design
  href: https://artifacts.apis.io/ripe-ncc/rules/ripe-ncc-rules.yml
  title: ''
  type: Spectral
  url: rules/ripe-ncc-rules.yml
- group: design
  href: https://artifacts.apis.io/ripe-ncc/json-ld/ripe-ncc-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ripe-ncc-context.jsonld
- group: design
  href: https://artifacts.apis.io/ripe-ncc/vocabulary/ripe-ncc-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ripe-ncc-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ripe-ncc/data-model/ripe-ncc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ripe-ncc-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://www.ripe.net/about-us/support/contact/responsible-disclosure-policy/
- group: design
  href: https://artifacts.apis.io/ripe-ncc/conformance/ripe-ncc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ripe-ncc-conformance.yml
- group: auth
  href: https://artifacts.apis.io/ripe-ncc/well-known/ripe-ncc-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ripe-ncc-security.txt
- group: auth
  href: https://artifacts.apis.io/ripe-ncc/well-known/ripe-ncc-ripe-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ripe-ncc-ripe-security.txt
- group: auth
  href: https://artifacts.apis.io/ripe-ncc/well-known/ripe-ncc-labs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ripe-ncc-labs-security.txt
- group: auth
  href: https://artifacts.apis.io/ripe-ncc/well-known/ripe-ncc-apps-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ripe-ncc-apps-security.txt
- group: agent
  href: https://artifacts.apis.io/ripe-ncc/well-known/ripe-ncc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ripe-ncc-well-known.yml
- group: other
  href: https://artifacts.apis.io/ripe-ncc/hosts/ripe-ncc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ripe-ncc-hosts.yml
- group: other
  href: https://artifacts.apis.io/ripe-ncc/vendors/ripe-ncc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ripe-ncc-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.ripe.net/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ripe.net/
- group: company
  title: ''
  type: Newsroom
  url: https://www.ripe.net/about-us/news/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.ripe.net/manage-ips-and-asns/db/release-notes/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.db.ripe.net/RIPE-Database-Mirror/Setup-RIPE-Database-Mirror/
- group: auth
  href: https://artifacts.apis.io/ripe-ncc/security/ripe-ncc-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ripe-ncc-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ripe-ncc/security/ripe-ncc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ripe-ncc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ripe.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.ripe.net/publications/documentation/developer-documentation/
- group: operate
  title: ''
  type: Support
  url: https://www.ripe.net/about-us/support/
- group: company
  title: ''
  type: Blog
  url: https://labs.ripe.net/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RIPE-NCC
- group: start
  title: ''
  type: SignUp
  url: https://www.ripe.net/membership/member-support/become-a-member/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ripe.net/about-us/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ripe.net/about-us/legal/ripe-ncc-privacy-statement/
coverage:
  checked: '2026-10-29'
  detail: Documentation page lists the RIPE Database RESTful API but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec is provided.
  evidence:
  - status: 200
    url: https://apps.db.ripe.net/docs/Update-Methods/RESTful-API/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: RIPE NCC is the Regional Internet Registry for Europe, the Middle East and parts of Central Asia. It is a not‑for‑profit membership association that allocates IP address space, manages the DNS root for the .ripe region, and provides a range of services to support the RIPE community, including RIPE Atlas measurements, training, and policy development.
image: https://www.ripe.net/static/images/ripe-ncc-logo-2025.svg
json_schemas:
- name: GetSourceObjecttypeKeyVersionsResponse
  property_count: 1
  slug: ripe-ncc-get-source-objecttype-key-versions-response
- name: GetSourceObjecttypeKeyVersionsVersionnumberResponse
  property_count: 1
  slug: ripe-ncc-get-source-objecttype-key-versions-versionnumber-response
- name: PostSourceObjecttypeRequest
  property_count: 1
  slug: ripe-ncc-post-source-objecttype-request
- name: PostSourceObjecttypeResponse
  property_count: 1
  slug: ripe-ncc-post-source-objecttype-response
- name: PutSourceObjecttypeKeyRequest
  property_count: 1
  slug: ripe-ncc-put-source-objecttype-key-request
- name: PutSourceObjecttypeKeyResponse
  property_count: 1
  slug: ripe-ncc-put-source-objecttype-key-response
jsonld:
- class_count: 22
  name: Ripe Ncc Context
  property_count: 3
  slug: ripe-ncc-context
layout: provider
modified: '2026-10-28'
name: RIPE NCC
nav: Providers
network: true
overview: 'RIPE NCC is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Internet, Regional Internet Registry, Not-for-profit, and IP Allocation.


  The RIPE NCC catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RIPE NCC''s developer surface includes changelog, getting-started guide, support, engineering blog, signup flow, and 25 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: RIPE NCC API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: ripe-ncc-rules
scopes:
- name: Ripe Ncc Scopes
  scope_count: 0
  slug: ripe-ncc-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 54.0
    catalog_earned_first_party: 0.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 19.7
    contract_quality: 24.0
    developer_ergonomics: 28.6
    discoverability: 58.9
    operational_transparency: 47.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ripe Ncc Authentication
  slug: ripe-ncc-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ripe Ncc Domain Security
  slug: ripe-ncc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ripe Ncc Vulnerability Disclosure
  slug: ripe-ncc-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ripe-ncc
tags:
- Company
- Internet
- Regional Internet Registry
- Not-for-profit
- IP Allocation
website: https://ripe.net/
---
