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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.3
  scored_at: '2026-10-17'
api_count: 7
apis:
- baseURL: https://api.carium.com
  baseurl_source: declared
  description: The Caredb API from Carium — 12 operation(s) for caredb.
  name: Carium Caredb API
  slug: carium-caredb-api
- baseURL: https://api.carium.com
  baseurl_source: declared
  description: The Carium API API from Carium — 1 operation(s) for carium api.
  name: Carium Carium API
  slug: carium-carium-api-api
- baseURL: https://api.carium.com
  baseurl_source: declared
  description: The Carium Inc API from Carium — 1 operation(s) for carium inc.
  name: Carium Carium Inc API
  slug: carium-carium-inc-api
- baseURL: https://api.carium.com
  baseurl_source: declared
  description: The Identity API from Carium — 4 operation(s) for identity.
  name: Carium Identity API
  slug: carium-identity-api
- baseURL: https://api.carium.com
  baseurl_source: declared
  description: The Lachesis API from Carium — 1 operation(s) for lachesis.
  name: Carium Lachesis API
  slug: carium-lachesis-api
- baseURL: https://api.carium.com
  baseurl_source: declared
  description: The Overlord API from Carium — 2 operation(s) for overlord.
  name: Carium Overlord API
  slug: carium-overlord-api
- baseURL: https://api.carium.com
  baseurl_source: declared
  description: The Showboat API from Carium — 1 operation(s) for showboat.
  name: Carium Showboat API
  slug: carium-showboat-api
artifact_total: 17
asyncapis:
- description: ''
  name: Carium Webhooks
  slug: carium-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carium/refs/heads/main/rules/carium-rules.yml
  title: ''
  type: Spectral
  url: rules/carium-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carium/refs/heads/main/json-ld/carium-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/carium-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carium/refs/heads/main/vocabulary/carium-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/carium-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carium/refs/heads/main/asyncapi/carium-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/carium-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carium/refs/heads/main/data-model/carium-data-model.yml
  title: ''
  type: DataModel
  url: data-model/carium-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/carium/refs/heads/main/cli/carium-cli.yml
  title: ''
  type: CLI
  url: cli/carium-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carium/refs/heads/main/conformance/carium-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carium-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/carium/refs/heads/main/llms/carium-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carium-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carium/refs/heads/main/well-known/carium-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/carium-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/carium/refs/heads/main/well-known/carium-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carium-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carium/refs/heads/main/hosts/carium-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carium-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carium/refs/heads/main/vendors/carium-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carium-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.go.carium.com/terms-of-use-spanish
- group: operate
  title: ''
  type: StatusPage
  url: https://status.carium.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.go.carium.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.go.carium.com/cariuminsights/categories/news
- group: start
  title: ''
  type: Login
  url: https://app.carium.com/sign-in/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.carium.com/
- group: company
  title: ''
  type: Blog
  url: https://www.go.carium.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carium/refs/heads/main/security/carium-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carium-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carium.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.go.carium.com/
- group: operate
  title: ''
  type: Support
  url: https://www.go.carium.com/support
- group: docs
  title: ''
  type: APIReference
  url: https://www.go.carium.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.go.carium.com/virtual-care-platform
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://www.go.carium.com/mcp
  - status: 403
    url: https://www.carium.com/mcp
  - status: 403
    url: https://app.carium.com/mcp
  - status: 200
    url: https://www.carium.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Carium is a virtual care management platform delivering advanced remote patient monitoring and health engagement solutions. It integrates bi-directional EHR data, provides intelligent automation, and supports care teams with real-time analytics to improve patient outcomes and operational efficiency across health systems and payors.
image: https://static.wixstatic.com/media/f60ac3_0004e714ae5a4f3a8657f03fb0bfaa79~mv2.gif/v1/fill/w_1280,h_720,al_c/f60ac3_0004e714ae5a4f3a8657f03fb0bfaa79~mv2.gif
json_schemas:
- name: GetIdentityV1IndividualGroupsResponse
  property_count: 2
  slug: carium-get-identity-v1-individual-groups-response
- name: GetLachesisV1TimeseriesResponse
  property_count: 5
  slug: carium-get-lachesis-v1-timeseries-response
- name: PostCaredbV1OrgAppointmentsRequest
  property_count: 13
  slug: carium-post-caredb-v1-org-appointments-request
- name: PostCaredbV1OrgDocumentReferencesRequest
  property_count: 7
  slug: carium-post-caredb-v1-org-document-references-request
- name: PostLachesisV1TimeseriesRequest
  property_count: 11
  slug: carium-post-lachesis-v1-timeseries-request
- name: PostShowboatV1PatientsRequest
  property_count: 10
  slug: carium-post-showboat-v1-patients-request
jsonld:
- class_count: 23
  name: Carium Context
  property_count: 48
  slug: carium-context
layout: provider
modified: '2026-10-07'
name: Carium
nav: Providers
network: true
overview: 'Carium is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Caredb API, Carium API, Carium Inc API, and 4 more. Tagged areas include Healthcare, VirtualCare, Remote Monitoring, Patient Engagement, and Health Tech.


  The Carium catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Carium''s developer surface includes CLI, engineering blog, documentation, support, API reference, getting-started guide, and 19 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Carium API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: carium-rules
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 35.3
    developer_ergonomics: 52.4
    discoverability: 80.4
    operational_transparency: 23.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Carium Domain Security
  slug: carium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carium
tags:
- Healthcare
- VirtualCare
- Remote Monitoring
- Patient Engagement
- Health Tech
- Company
website: https://www.carium.com/
---
