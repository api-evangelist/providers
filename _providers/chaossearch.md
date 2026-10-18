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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-17'
api_count: 3
apis:
- baseURL: https://<chaossearch
  baseurl_source: declared
  description: The Bulkexport API from ChaosSearch — 1 operation(s) for bulkexport.
  name: ChaosSearch Bulkexport API
  slug: chaossearch-bulkexport-api
- baseURL: https://<chaossearch
  baseurl_source: declared
  description: The ChaosSearch API API from ChaosSearch — 1 operation(s) for chaossearch api.
  name: ChaosSearch ChaosSearch API
  slug: chaossearch-chaossearch-api-api
- baseURL: https://<chaossearch
  baseurl_source: declared
  description: The User API from ChaosSearch — 2 operation(s) for user.
  name: ChaosSearch User API
  slug: chaossearch-user-api
artifact_total: 15
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/chaossearch/refs/heads/main/plans/chaossearch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chaossearch-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chaossearch/refs/heads/main/rules/chaossearch-rules.yml
  title: ''
  type: Spectral
  url: rules/chaossearch-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chaossearch/refs/heads/main/json-ld/chaossearch-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chaossearch-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chaossearch/refs/heads/main/vocabulary/chaossearch-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chaossearch-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chaossearch/refs/heads/main/data-model/chaossearch-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chaossearch-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.chaossearch.io/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chaossearch/refs/heads/main/authentication/chaossearch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chaossearch-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chaossearch/refs/heads/main/conformance/chaossearch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chaossearch-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chaossearch/refs/heads/main/llms/chaossearch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chaossearch-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chaossearch/refs/heads/main/hosts/chaossearch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chaossearch-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chaossearch/refs/heads/main/vendors/chaossearch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chaossearch-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chaossearch.io/legal/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chaossearch.io/
- group: auth
  title: ''
  type: Security
  url: https://www.chaossearch.io/security
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chaossearch.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.chaossearch.io/blog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.chaossearch.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.chaossearch.io/docs/quick-start-guide
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chaossearch.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chaossearch/refs/heads/main/security/chaossearch-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/chaossearch-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chaossearch/refs/heads/main/security/chaossearch-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chaossearch-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chaossearch/refs/heads/main/security/chaossearch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chaossearch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chaossearch.io/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://docs.chaossearch.io/mcp
  - status: 403
    url: https://www.chaossearch.io/mcp
  - status: 200
    url: https://www.chaossearch.io/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: partner-login
  state: gated
created: '2026-10-08'
description: ChaosSearch provides a live analytics platform that transforms cloud storage into a searchable, SQL‑enabled and generative‑AI‑ready analytical database. It enables customers to ingest streaming data at scale, perform real‑time search, visualizations, and advanced analytics without managing infrastructure. The service supports integrations with AWS, Azure, and GCP, offering fast query performance and flexible data retention for operational and business use cases.
image: https://www.chaossearch.io/hubfs/Homepage%20Header%20Graphic.png
json_schemas:
- name: GetUserGroupsResponse
  property_count: 3
  slug: chaossearch-get-user-groups-response
- name: PostBulkexportStatusRequest
  property_count: 1
  slug: chaossearch-post-bulkexport-status-request
- name: PostRequest
  property_count: 4
  slug: chaossearch-post-request
- name: PostUserLoginRequest
  property_count: 4
  slug: chaossearch-post-user-login-request
- name: PostUserLoginResponse
  property_count: 1
  slug: chaossearch-post-user-login-response
jsonld:
- class_count: 5
  name: Chaossearch Context
  property_count: 8
  slug: chaossearch-context
layout: provider
modified: '2026-10-08'
name: ChaosSearch
nav: Providers
network: true
overview: 'ChaosSearch is listed with 3 APIs on the [APIs.io](https://apis.io/) network: Bulkexport API, ChaosSearch API, and User API. Tagged areas include Analytics, Observability, Security, Data Lake, and Cloud Storage.


  The ChaosSearch catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ChaosSearch''s developer surface includes authentication, pricing, engineering blog, API reference, getting-started guide, documentation, and 17 more developer resources.'
plans:
- name: Chaossearch Plans Pricing
  plan_count: 3
  slug: chaossearch-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: ChaosSearch API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: chaossearch-rules
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 22.0
    contract_quality: 22.6
    developer_ergonomics: 42.9
    discoverability: 78.6
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Chaossearch Authentication
  slug: chaossearch-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Chaossearch Domain Security
  slug: chaossearch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chaossearch Vulnerability Disclosure
  slug: chaossearch-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Chaossearch Trust Center
  slug: chaossearch-trust-center
  summary_line: HIPAA, GDPR
slug: chaossearch
tags:
- Analytics
- Observability
- Security
- Data Lake
- Cloud Storage
- ELK
website: https://www.chaossearch.io/
---
