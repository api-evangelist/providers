---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 51
  human_in_the_loop: 2
  name: Streem Com Agentic Access
  operation_count: 90
  slug: streem-com-agentic-access
  summary_line: 90 operations · 51 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.prod-us.streem.cloud
  baseurl_source: declared
  description: The companies API from Greply — 29 operation(s) for companies.
  name: Greply Companies API
  slug: streem-com-companies-api
- baseURL: https://api.prod-us.streem.cloud
  baseurl_source: declared
  description: The groups API from Greply — 16 operation(s) for groups.
  name: Greply Groups API
  slug: streem-com-groups-api
- baseURL: https://api.prod-us.streem.cloud
  baseurl_source: declared
  description: The images API from Greply — 1 operation(s) for images.
  name: Greply Images API
  slug: streem-com-images-api
- baseURL: https://api.prod-us.streem.cloud
  baseurl_source: declared
  description: The rooms API from Greply — 20 operation(s) for rooms.
  name: Greply Rooms API
  slug: streem-com-rooms-api
- baseURL: https://api.prod-us.streem.cloud
  baseurl_source: declared
  description: The users API from Greply — 6 operation(s) for users.
  name: Greply Users API
  slug: streem-com-users-api
- baseURL: https://api.prod-us.streem.cloud
  baseurl_source: declared
  description: The webhooks API from Greply — 5 operation(s) for webhooks.
  name: Greply Webhooks API
  slug: streem-com-webhooks-api
artifact_total: 22
asyncapis:
- description: ''
  name: Streem Com Webhooks
  slug: streem-com-webhooks
common:
- group: other
  href: https://artifacts.apis.io/streem-com/vendors/streem-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/streem-com-vendors.yml
- group: agent
  href: https://artifacts.apis.io/streem-com/agentic-access/streem-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/streem-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/streem-com/rules/streem-com-rules.yml
  title: ''
  type: Spectral
  url: rules/streem-com-rules.yml
- group: design
  href: https://artifacts.apis.io/streem-com/json-ld/streem-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/streem-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/streem-com/vocabulary/streem-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/streem-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/streem-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/streem-com/asyncapi/streem-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/streem-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/streem-com/data-model/streem-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/streem-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/streem-com/conventions/streem-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/streem-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/streem-com/errors/streem-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/streem-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/streem-com/conformance/streem-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/streem-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/streem-com/llms/streem-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/streem-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/streem-com/well-known/streem-com-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/streem-com-www-security.txt
- group: agent
  href: https://artifacts.apis.io/streem-com/well-known/streem-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/streem-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/streem-com/hosts/streem-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/streem-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/streem-com/packages/streem-com-packages.yml
  title: ''
  type: SDKs
  url: packages/streem-com-packages.yml
- group: build
  href: https://artifacts.apis.io/streem-com/packages/streem-com-packages.yml
  title: ''
  type: Packages
  url: packages/streem-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.frontdoorhome.com/terms-of-use/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.streem.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.streem.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.streem.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/streem
- group: auth
  href: https://artifacts.apis.io/streem-com/authentication/streem-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/streem-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/streem-com/security/streem-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/streem-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://streem.com
created: '2026-10-21'
description: Greply, operating under the Streem brand, provides a platform that aggregates and analyzes streaming data for businesses, delivering real‑time insights and automated decision‑making via a robust API. It integrates multiple data sources, offers customizable dashboards, and focuses on scalability, security, and ease of integration. Backed by 500 Global, Greply aims to simplify complex data workflows for enterprises across various industries.
image: https://2qz9b4rx.media.zesty.site/20-FD-0425_-_RUSH_FTDR_website_open_graph_image_FINAL.jpg?width=1200&height=630&fit=crop
json_schemas:
- name: streem.api.CreateCompanyRoomOutcomeConfigRequest
  property_count: 4
  slug: streem-com-streem-api-create-company-room-outcome-config-request
- name: streem.api.CreateGroupReservationRequest
  property_count: 11
  slug: streem-com-streem-api-create-group-reservation-request
- name: streem.api.CreateWebhookRequest
  property_count: 7
  slug: streem-com-streem-api-create-webhook-request
- name: streem.api.ListGroupAvailabilityRequest
  property_count: 5
  slug: streem-com-streem-api-list-group-availability-request
- name: streem.api.UpdateWebhookRequest
  property_count: 7
  slug: streem-com-streem-api-update-webhook-request
- name: streem.internal.api.SaveGroupAverageCallLengthRequest
  property_count: 4
  slug: streem-com-streem-internal-api-save-group-average-call-length-request
jsonld:
- class_count: 120
  name: Streem Com Context
  property_count: 280
  slug: streem-com-context
layout: provider
modified: '2026-10-21'
name: Greply
nav: Providers
network: true
overview: 'Greply publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Companies API, Groups API, Images API, and 3 more. Tagged areas include Company, Data Analytics, Real-time, API Platform, and Streaming.


  The Greply catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Greply''s developer surface includes API reference, getting-started guide, documentation, authentication, and 21 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Greply API Rules
  rule_count: 13
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 2
  slug: streem-com-rules
score:
  band: developing
  composite: 44.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 35.6
    contract_quality: 70.9
    developer_ergonomics: 49.4
    discoverability: 66.1
    operational_transparency: 23.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Streem Com Authentication
  slug: streem-com-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Streem Com Domain Security
  slug: streem-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: streem-com-create-and-activate-user
  slug: streem-com-create-and-activate-user
- name: streem-com-create-company-and-api-key
  slug: streem-com-create-company-and-api-key
- name: streem-com-create-group-and-add-users
  slug: streem-com-create-group-and-add-users
- name: streem-com-manage-room-share-tokens
  slug: streem-com-manage-room-share-tokens
slug: streem-com
tags:
- Company
- Data Analytics
- Real-time
- API Platform
- Streaming
website: https://streem.com
---
