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
  scored_at: '2026-10-17'
api_count: 7
apis:
- baseURL: https://status.zendesk.com
  baseurl_source: declared
  description: The Comunix API API from Comunix — 1 operation(s) for comunix api.
  name: Comunix Comunix API
  slug: comunix-comunix-api-api
- baseURL: https://status.zendesk.com
  baseurl_source: declared
  description: The Incidents API from Comunix — 2 operation(s) for incidents.
  name: Comunix Incidents API
  slug: comunix-incidents-api
- baseURL: https://status.zendesk.com
  baseurl_source: declared
  description: The Register API from Comunix — 1 operation(s) for register.
  name: Comunix Register API
  slug: comunix-register-api
- baseURL: https://status.zendesk.com
  baseurl_source: declared
  description: The Sunshine API from Comunix — 4 operation(s) for sunshine.
  name: Comunix Sunshine API
  slug: comunix-sunshine-api
- baseURL: https://status.zendesk.com
  baseurl_source: declared
  description: The Tickets API from Comunix — 1 operation(s) for tickets.
  name: Comunix Tickets API
  slug: comunix-tickets-api
- baseURL: https://status.zendesk.com
  baseurl_source: declared
  description: The User Profiles API from Comunix — 3 operation(s) for user profiles.
  name: Comunix User Profiles API
  slug: comunix-user-profiles-api
- baseURL: https://status.zendesk.com
  baseurl_source: declared
  description: The Users API from Comunix — 1 operation(s) for users.
  name: Comunix Users API
  slug: comunix-users-api
artifact_total: 17
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/comunix/refs/heads/main/rules/comunix-rules.yml
  title: ''
  type: Spectral
  url: rules/comunix-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/comunix/refs/heads/main/json-ld/comunix-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/comunix-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/comunix/refs/heads/main/vocabulary/comunix-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/comunix-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/comunix/refs/heads/main/data-model/comunix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/comunix-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/comunix/refs/heads/main/authentication/comunix-authentication.yml
  title: ''
  type: Authentication
  url: authentication/comunix-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/comunix/refs/heads/main/conformance/comunix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/comunix-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/comunix/refs/heads/main/llms/comunix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/comunix-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/comunix/refs/heads/main/hosts/comunix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/comunix-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/comunix/refs/heads/main/vendors/comunix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/comunix-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.getcomunix.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.zendesk.com/documentation/developer-tools/getting-started/getting-a-trial-or-sponsored-account-for-development/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.zendesk.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/comunix/refs/heads/main/security/comunix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/comunix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getcomunix.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getcomunix.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getcomunix.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://getcomunixhelp.zendesk.com/hc/en-us
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://api.zendesk.com/mcp
  - status: 403
    url: https://www.getcomunix.com/mcp
  - status: 401
    url: https://getcomunixhelp.zendesk.com/mcp
  - status: 200
    url: https://www.getcomunix.com
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: Comunix is a social gaming company that creates interactive live gaming experiences centered on human connection. Their flagship product, Pokerface, combines group video chat with Texas Hold’em poker, allowing players worldwide to meet, play, and socialize in real time. Founded by seasoned technology and gaming professionals, Comunix aims to reinvent online gaming by integrating innovative communication methods and fostering community.
image: https://static.wixstatic.com/media/58c529_457d7e831dcd4171af0a2b8da7947365~mv2.jpg/v1/fill/w_1200,h_630,al_c/58c529_457d7e831dcd4171af0a2b8da7947365~mv2.jpg
json_schemas:
- name: GetApiV2UserProfilesResponse
  property_count: 1
  slug: comunix-get-api-v2-user-profiles-response
- name: PostApiSunshineObjectsObjectidRequest
  property_count: 6
  slug: comunix-post-api-sunshine-objects-objectid-request
- name: PostApiSunshineSunshineidTypesRequest
  property_count: 10
  slug: comunix-post-api-sunshine-sunshineid-types-request
- name: PostApiV2UserProfilesEventsRequest
  property_count: 12
  slug: comunix-post-api-v2-user-profiles-events-request
- name: PutApiV2UserProfilesRequest
  property_count: 7
  slug: comunix-put-api-v2-user-profiles-request
- name: PutApiV2UserProfilesResponse
  property_count: 9
  slug: comunix-put-api-v2-user-profiles-response
jsonld:
- class_count: 19
  name: Comunix Context
  property_count: 53
  slug: comunix-context
layout: provider
modified: '2026-10-10'
name: Comunix
nav: Providers
network: true
overview: 'Comunix is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Comunix API, Incidents API, Register API, and 4 more. Tagged areas include Gaming, Social, Live, VideoChat, and Poker.


  The Comunix catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Comunix''s developer surface includes authentication, engineering blog, getting-started guide, documentation, support, and 12 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Comunix API Rules
  rule_count: 12
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 2
  slug: comunix-rules
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 24.6
    developer_ergonomics: 40.5
    discoverability: 78.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: unknown
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
    score: 22.2
security:
- kind: authentication
  name: Comunix Authentication
  slug: comunix-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Comunix Domain Security
  slug: comunix-domain-security
  summary_line: TLSv1.3 · HSTS
slug: comunix
tags:
- Gaming
- Social
- Live
- VideoChat
- Poker
website: https://www.getcomunix.com
---
