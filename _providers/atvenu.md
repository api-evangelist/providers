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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 18.0
  scored_at: '2026-10-03'
api_count: 15
apis:
- baseURL: https://support.zendesk.com
  baseurl_source: declared
  description: The AtVenu API API from atVenu — 2 operation(s) for atvenu api.
  name: atVenu AtVenu API
  slug: atvenu-atvenu-api-api
- baseURL: https://support.zendesk.com
  baseurl_source: declared
  description: The Download API from atVenu — 2 operation(s) for download.
  name: atVenu Download API
  slug: atvenu-download-api
- baseURL: https://support.zendesk.com
  baseurl_source: declared
  description: The Downloads API from atVenu — 1 operation(s) for downloads.
  name: atVenu Downloads API
  slug: atvenu-downloads-api
- baseURL: https://support.zendesk.com
  baseurl_source: declared
  description: The Help Center API from atVenu — 1 operation(s) for help center.
  name: atVenu Help Center API
  slug: atvenu-help-center-api
- baseURL: https://support.zendesk.com
  baseurl_source: declared
  description: The Incidents API from atVenu — 1 operation(s) for incidents.
  name: atVenu Incidents API
  slug: atvenu-incidents-api
- baseURL: https://support.zendesk.com
  baseurl_source: declared
  description: The Incremental API from atVenu — 2 operation(s) for incremental.
  name: atVenu Incremental API
  slug: atvenu-incremental-api
- baseURL: https://support.zendesk.com
  baseurl_source: declared
  description: The Register API from atVenu — 1 operation(s) for register.
  name: atVenu Register API
  slug: atvenu-register-api
- baseURL: https://support.zendesk.com
  baseurl_source: declared
  description: The Services API from atVenu — 11 operation(s) for services.
  name: atVenu Services API
  slug: atvenu-services-api
- baseURL: https://support.zendesk.com
  baseurl_source: declared
  description: The Sunshine API from atVenu — 4 operation(s) for sunshine.
  name: atVenu Sunshine API
  slug: atvenu-sunshine-api
- baseURL: https://support.zendesk.com
  baseurl_source: declared
  description: The Tickets API from atVenu — 1 operation(s) for tickets.
  name: atVenu Tickets API
  slug: atvenu-tickets-api
- baseURL: https://support.zendesk.com
  baseurl_source: declared
  description: The User Profiles API from atVenu — 3 operation(s) for user profiles.
  name: atVenu User Profiles API
  slug: atvenu-user-profiles-api
- baseURL: https://support.zendesk.com
  baseurl_source: declared
  description: The Users API from atVenu — 3 operation(s) for users.
  name: atVenu Users API
  slug: atvenu-users-api
- baseURL: https://support.zendesk.com
  baseurl_source: declared
  description: The Webhooks API from atVenu — 1 operation(s) for webhooks.
  name: atVenu Webhooks API
  slug: atvenu-webhooks-api
- baseURL: https://support.zendesk.com
  baseurl_source: declared
  description: The Webstore API from atVenu — 1 operation(s) for webstore.
  name: atVenu Webstore API
  slug: atvenu-webstore-api
- baseURL: https://support.zendesk.com
  baseurl_source: declared
  description: The Graph QL API from atVenu — 1 operation(s) for graph ql.
  name: atVenu Graph QL API
  slug: atvenu-graph-ql-api
artifact_total: 25
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atvenu/refs/heads/main/rules/atvenu-rules.yml
  title: ''
  type: Spectral
  url: rules/atvenu-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atvenu/refs/heads/main/json-ld/atvenu-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/atvenu-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atvenu/refs/heads/main/vocabulary/atvenu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/atvenu-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atvenu/refs/heads/main/data-model/atvenu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/atvenu-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atvenu/refs/heads/main/conventions/atvenu-conventions.yml
  title: ''
  type: Conventions
  url: conventions/atvenu-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atvenu/refs/heads/main/authentication/atvenu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/atvenu-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atvenu/refs/heads/main/conformance/atvenu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/atvenu-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atvenu/refs/heads/main/hosts/atvenu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atvenu-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atvenu/refs/heads/main/vendors/atvenu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atvenu-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atvenu.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atvenu.com/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://developer.zendesk.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atvenu
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atvenu/refs/heads/main/security/atvenu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atvenu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atvenu.com/
- group: company
  title: ''
  type: Blog
  url: https://www.atvenu.com/blog
- group: operate
  title: ''
  type: Support
  url: https://atvenu.zendesk.com/hc/en-us
- group: start
  title: ''
  type: GettingStarted
  url: https://www.atvenu.com/sign-up
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://api.atvenu.com/mcp
  - status: 401
    url: https://api.zendesk.com/mcp
  - status: 401
    url: https://atvenu.zendesk.com/mcp
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: atVenu provides an all‑in‑one payment and commerce platform for live events, enabling venues, festivals, artists, and pop‑up experiences to sell merchandise, food, beverage, tickets and services through a unified POS system. The solution supports mobile ordering, promotions, inventory management, and integrates with existing ticketing and CRM tools, aiming to streamline revenue streams for transient event operators.
image: https://cdn.prod.website-files.com/6971425127cb32a80d3a8915/6a3016250738cb3116eb4571_f05b49821ad326db4fbd8407918dec35_OpenGraph.png
json_schemas:
- name: GetApiServicesZisRegistryIntegrationBundlesUuidResponse
  property_count: 7
  slug: atvenu-get-api-services-zis-registry-integration-bundles-uuid-response
- name: GetApiSunshineObjectsRecordsResourceidRelationshipsRelations
  property_count: 6
  slug: atvenu-get-api-sunshine-objects-records-resourceid-relationships-relations
- name: GetApiV2IncrementalItemsJsonResponse
  property_count: 8
  slug: atvenu-get-api-v2-incremental-items-json-response
- name: GetApiV2UserProfilesEventsResponse
  property_count: 2
  slug: atvenu-get-api-v2-user-profiles-events-response
- name: PutApiV2UserProfilesRequest
  property_count: 7
  slug: atvenu-put-api-v2-user-profiles-request
- name: PutApiV2UserProfilesResponse
  property_count: 9
  slug: atvenu-put-api-v2-user-profiles-response
jsonld:
- class_count: 47
  name: Atvenu Context
  property_count: 76
  slug: atvenu-context
layout: provider
modified: '2026-09-26'
name: atVenu
nav: Providers
network: true
overview: 'atVenu publishes 15 APIs on the [APIs.io](https://apis.io/) network, including AtVenu API, Download API, Downloads API, and 12 more. Tagged areas include Company, Payments, Live Events, Commerce, and Point-of-Sale.


  The atVenu catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  atVenu''s developer surface includes authentication, documentation, engineering blog, support, getting-started guide, and 13 more developer resources.'
random_paper: 21
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: atVenu API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: atvenu-rules
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 35.6
    contract_quality: 25.8
    developer_ergonomics: 40.5
    discoverability: 71.4
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 16
      marker_coverage: 100.0
      total: 16
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Atvenu Authentication
  slug: atvenu-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Atvenu Domain Security
  slug: atvenu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atvenu
tags:
- Company
- Payments
- Live Events
- Commerce
- Point-of-Sale
website: https://www.atvenu.com/
---
