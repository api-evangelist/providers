---
agent_readiness:
  band: agent-ready
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.7
  scored_at: '2026-10-17'
api_count: 8
apis:
- baseURL: https://dash.readme.com
  baseurl_source: declared
  description: The Documents API from Vertex — 1 operation(s) for documents.
  name: Vertex Documents API
  slug: vertex-documents-api
- baseURL: https://dash.readme.com
  baseurl_source: declared
  description: The Problems API from Vertex — 1 operation(s) for problems.
  name: Vertex Problems API
  slug: vertex-problems-api
- baseURL: https://dash.readme.com
  baseurl_source: declared
  description: The Project API from Vertex — 2 operation(s) for project.
  name: Vertex Project API
  slug: vertex-project-api
- baseURL: https://dash.readme.com
  baseurl_source: declared
  description: The Reports API from Vertex — 8 operation(s) for reports.
  name: Vertex Reports API
  slug: vertex-reports-api
- baseURL: https://dash.readme.com
  baseurl_source: declared
  description: The Schedules API from Vertex — 1 operation(s) for schedules.
  name: Vertex Schedules API
  slug: vertex-schedules-api
- baseURL: https://dash.readme.com
  baseurl_source: declared
  description: The Templates API from Vertex — 1 operation(s) for templates.
  name: Vertex Templates API
  slug: vertex-templates-api
- baseURL: https://dash.readme.com
  baseurl_source: declared
  description: The Vertex API API from Vertex — 2 operation(s) for vertex api.
  name: Vertex Vertex API
  slug: vertex-vertex-api-api
- baseURL: https://dash.readme.com
  baseurl_source: declared
  description: The Vertex Ws API from Vertex — 1 operation(s) for vertex ws.
  name: Vertex Vertex Ws API
  slug: vertex-vertex-ws-api
artifact_total: 13
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vertex/refs/heads/main/rules/vertex-rules.yml
  title: ''
  type: Spectral
  url: rules/vertex-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vertex/refs/heads/main/json-ld/vertex-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/vertex-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vertex/refs/heads/main/vocabulary/vertex-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/vertex-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vertex/refs/heads/main/data-model/vertex-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vertex-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.vertexinc.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vertex/refs/heads/main/conformance/vertex-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vertex-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vertex/refs/heads/main/llms/vertex-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vertex-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vertex/refs/heads/main/well-known/vertex-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/vertex-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vertex/refs/heads/main/well-known/vertex-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vertex-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vertex/refs/heads/main/hosts/vertex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vertex-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vertex/refs/heads/main/vendors/vertex-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vertex-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vertexinc.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.vertexinc.com/company/news/latest-news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vertexinc
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vertex/refs/heads/main/security/vertex-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/vertex-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vertex/refs/heads/main/security/vertex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vertex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vertexinc.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.vertexinc.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.vertexinc.com/
- group: operate
  title: ''
  type: Support
  url: https://www.vertexinc.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vertexinc.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vertexinc.com/vertex-privacy-policy
coverage:
  checked: '2026-10-13'
  detail: Developer portal pages are rendered via JavaScript and do not expose a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://developer.vertexinc.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Vertex Inc. provides tax technology software and solutions that help businesses automate global tax compliance, calculate taxes, and manage tax data across multiple jurisdictions. Their platform integrates with ERP, e‑commerce, and financial systems, offering APIs for tax calculation, filing, and reporting, enabling enterprises to streamline tax processes and reduce compliance risk.
image: https://www.vertexinc.com/sites/default/files/styles/1_91_1_ratio_for_social_media_sharing/public/2025-05/marketeture-homepage-hero-lg.png?itok=AUYSkhPk
json_schemas:
- name: GetProblemsProblemidResponse
  property_count: 5
  slug: vertex-get-problems-problemid-response
jsonld:
- class_count: 1
  name: Vertex Context
  property_count: 5
  slug: vertex-context
layout: provider
modified: '2026-10-13'
name: Vertex
nav: Providers
network: true
overview: 'Vertex is listed with 8 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Problems API, Project API, and 5 more. Tagged areas include Company, Tax, Compliance, and Automation.


  The Vertex catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Vertex''s developer surface includes documentation, API reference, support, and 19 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Vertex API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: vertex-rules
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 51.2
    catalog_earned_first_party: 0.0
    catalog_gap: 63.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 17.8
    developer_ergonomics: 21.4
    discoverability: 71.4
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Vertex Domain Security
  slug: vertex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vertex Trust Center
  slug: vertex-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: vertex
tags:
- Company
- Tax
- Compliance
- Automation
website: https://www.vertexinc.com/
---
