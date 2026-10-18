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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-10-17'
api_count: 7
apis:
- description: CloudSEK API provides endpoints for alerts, incidents, events, and related security data as documented in the API reference.
  name: CloudSEK API
  slug: cloudsek-api-2
- description: The Bulk API from Cloudsek — 1 operation(s) for bulk.
  name: Cloudsek Bulk API
  slug: cloudsek-bulk-api
- description: The Comments API from Cloudsek — 1 operation(s) for comments.
  name: Cloudsek Comments API
  slug: cloudsek-comments-api
- description: The Events API from Cloudsek — 2 operation(s) for events.
  name: Cloudsek Events API
  slug: cloudsek-events-api
- description: The Incidents API from Cloudsek — 5 operation(s) for incidents.
  name: Cloudsek Incidents API
  slug: cloudsek-incidents-api
- description: The Jobs API from Cloudsek — 1 operation(s) for jobs.
  name: Cloudsek Jobs API
  slug: cloudsek-jobs-api
- description: The Snapshot API from Cloudsek — 1 operation(s) for snapshot.
  name: Cloudsek Snapshot API
  slug: cloudsek-snapshot-api
artifact_total: 18
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudsek/refs/heads/main/rules/cloudsek-rules.yml
  title: ''
  type: Spectral
  url: rules/cloudsek-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudsek/refs/heads/main/json-ld/cloudsek-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudsek-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudsek/refs/heads/main/vocabulary/cloudsek-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cloudsek-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudsek/refs/heads/main/data-model/cloudsek-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloudsek-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cloudsek/refs/heads/main/cli/cloudsek-cli.yml
  title: ''
  type: CLI
  url: cli/cloudsek-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudsek/refs/heads/main/conventions/cloudsek-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cloudsek-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cloudsek.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudsek/refs/heads/main/authentication/cloudsek-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloudsek-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudsek/refs/heads/main/conformance/cloudsek-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudsek-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudsek/refs/heads/main/well-known/cloudsek-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudsek-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudsek/refs/heads/main/hosts/cloudsek-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudsek-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudsek/refs/heads/main/vendors/cloudsek-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudsek-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.cloudsek.com/s/
- group: auth
  title: ''
  type: Security
  url: https://www.cloudsek.com/tag/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloudsek.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.cloudsek.com/press
- group: company
  title: ''
  type: Blog
  url: https://www.cloudsek.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://api.cloudsek.com/docs/intro
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudsek/refs/heads/main/security/cloudsek-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cloudsek-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudsek/refs/heads/main/security/cloudsek-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudsek-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloudsek.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://api.cloudsek.com/mcp
  - status: 200
    url: https://www.cloudsek.com
  - status: 403
    url: https://equityzen.com/company/cloudsek
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: CloudSEK provides predictive attack path intelligence, helping security teams anticipate and disrupt cyber threats across digital risk, threat intelligence, external attack surface, AI systems, and third‑party ecosystems. The platform offers real‑time risk scoring, breach simulations, and actionable insights to prioritize defenses and reduce attack surface exposure.
image: https://cdn.prod.website-files.com/634fc5026f66af518e897c77/63ecd1a143d018d878470b4b_Blog%20default%20Cover.png
json_schemas:
- name: GetIncidentsAlertsResponse
  property_count: 4
  slug: cloudsek-get-incidents-alerts-response
- name: GetIncidentsHistoricAlertsResponse
  property_count: 4
  slug: cloudsek-get-incidents-historic-alerts-response
- name: GetV2IncidentsAlertsResponse
  property_count: 4
  slug: cloudsek-get-v2-incidents-alerts-response
- name: PatchV2IncidentsIdRequest
  property_count: 5
  slug: cloudsek-patch-v2-incidents-id-request
- name: PatchV2IncidentsIdResponse
  property_count: 7
  slug: cloudsek-patch-v2-incidents-id-response
- name: PostV2V2IdBulkResponse
  property_count: 6
  slug: cloudsek-post-v2-v2-id-bulk-response
jsonld:
- class_count: 8
  name: Cloudsek Context
  property_count: 6
  slug: cloudsek-context
layout: provider
modified: '2026-10-09'
name: Cloudsek
nav: Providers
network: true
overview: 'Cloudsek is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Bulk API, Comments API, Events API, and 4 more. Tagged areas include Security, Threat Intelligence, Attack Path, Predictive Analytics, and Cyber Risk.


  The Cloudsek catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cloudsek''s developer surface includes CLI, authentication, support, engineering blog, getting-started guide, and 16 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Cloudsek API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: cloudsek-rules
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 22.0
    contract_quality: 22.5
    developer_ergonomics: 38.1
    discoverability: 64.3
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Cloudsek Authentication
  slug: cloudsek-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cloudsek Domain Security
  slug: cloudsek-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Cloudsek Trust Center
  slug: cloudsek-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, GDPR
slug: cloudsek
tags:
- Security
- Threat Intelligence
- Attack Path
- Predictive Analytics
- Cyber Risk
website: https://www.cloudsek.com
---
