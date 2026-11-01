---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 10
  human_in_the_loop: 10
  name: Hacktron Agentic Access
  operation_count: 38
  slug: hacktron-agentic-access
  summary_line: 38 operations · 10 acting · 10 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.hacktron.ai/v1
  baseurl_source: declared
  description: The REST API - Cost Estimations API from Hacktron — 2 operation(s) for rest api - cost estimations.
  name: Hacktron REST API - Cost Estimations API
  slug: hacktron-rest-api-cost-estimations-api
- baseURL: https://api.hacktron.ai/v1
  baseurl_source: declared
  description: The REST API - Findings API from Hacktron — 4 operation(s) for rest api - findings.
  name: Hacktron REST API - Findings API
  slug: hacktron-rest-api-findings-api
- baseURL: https://api.hacktron.ai/v1
  baseurl_source: declared
  description: The REST API - HFW API from Hacktron — 4 operation(s) for rest api - hfw.
  name: Hacktron REST API - HFW API
  slug: hacktron-rest-api-hfw-api
- baseURL: https://api.hacktron.ai/v1
  baseurl_source: declared
  description: The REST API - Repos API from Hacktron — 1 operation(s) for rest api - repos.
  name: Hacktron REST API - Repos API
  slug: hacktron-rest-api-repos-api
- baseURL: https://api.hacktron.ai/v1
  baseurl_source: declared
  description: The REST API - Scans API from Hacktron — 5 operation(s) for rest api - scans.
  name: Hacktron REST API - Scans API
  slug: hacktron-rest-api-scans-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/hacktron/agentic-access/hacktron-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hacktron-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/hacktron/rate-limits/hacktron-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hacktron-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/hacktron/rules/hacktron-rules.yml
  title: ''
  type: Spectral
  url: rules/hacktron-rules.yml
- group: design
  href: https://artifacts.apis.io/hacktron/json-ld/hacktron-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hacktron-context.jsonld
- group: design
  href: https://artifacts.apis.io/hacktron/vocabulary/hacktron-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hacktron-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/hacktron/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/hacktron/data-model/hacktron-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hacktron-data-model.yml
- group: operate
  href: https://artifacts.apis.io/hacktron/changelog/hacktron-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hacktron-changelog.yml
- group: design
  href: https://artifacts.apis.io/hacktron/conventions/hacktron-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hacktron-conventions.yml
- group: auth
  href: https://artifacts.apis.io/hacktron/authentication/hacktron-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hacktron-authentication.yml
- group: design
  href: https://artifacts.apis.io/hacktron/errors/hacktron-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hacktron-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hacktron/conformance/hacktron-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hacktron-conformance.yml
- group: agent
  href: https://artifacts.apis.io/hacktron/llms/hacktron-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hacktron-llms.txt
- group: other
  href: https://artifacts.apis.io/hacktron/a2a/hacktron-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hacktron-a2a.yml
- group: auth
  href: https://artifacts.apis.io/hacktron/well-known/hacktron-trust-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hacktron-trust-security.txt
- group: auth
  href: https://artifacts.apis.io/hacktron/well-known/hacktron-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hacktron-status-security.txt
- group: auth
  href: https://artifacts.apis.io/hacktron/well-known/hacktron-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hacktron-security.txt
- group: auth
  href: https://artifacts.apis.io/hacktron/well-known/hacktron-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hacktron-docs-security.txt
- group: auth
  href: https://artifacts.apis.io/hacktron/well-known/hacktron-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hacktron-api-security.txt
- group: agent
  href: https://artifacts.apis.io/hacktron/well-known/hacktron-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hacktron-well-known.yml
- group: other
  href: https://artifacts.apis.io/hacktron/hosts/hacktron-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hacktron-hosts.yml
- group: other
  href: https://artifacts.apis.io/hacktron/vendors/hacktron-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hacktron-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.hacktron.ai/tags/security
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hacktron.ai/code-review/setup
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hacktron.ai/llms.txt
- group: auth
  href: https://artifacts.apis.io/hacktron/security/hacktron-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hacktron-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hacktron/security/hacktron-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hacktron-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hacktron.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hacktron.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.hacktron.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.hacktron.ai/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hacktronai
- group: other
  title: ''
  type: Leadership
  url: https://www.hacktron.ai/team
- group: company
  title: ''
  type: Newsroom
  url: https://www.hacktron.ai/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.hacktron.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hacktron.ai/terms-of-service
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.hacktron.ai
created: '2026-10-29'
description: Hacktron is an AI-powered automation platform that enables enterprises to integrate, orchestrate, and monitor their digital workflows across cloud services and on‑premises systems. The company provides a unified dashboard, extensive developer documentation, and a robust API suite covering data ingestion, device management, and analytics. Backed by crane-venture-partners, Hacktron serves customers in manufacturing, logistics, and IoT sectors, offering scalable solutions with strong security and compliance features.
image: https://www.hacktron.ai/static/og/home.png
json_schemas:
- name: CostEstimationResponseDto
  property_count: 14
  slug: hacktron-cost-estimation-response-dto
- name: CreateCostEstimationDto
  property_count: 2
  slug: hacktron-create-cost-estimation-dto
- name: RestCreateScanDto
  property_count: 6
  slug: hacktron-rest-create-scan-dto
- name: RestFindingDetailResponseDto
  property_count: 21
  slug: hacktron-rest-finding-detail-response-dto
- name: RestScanResponseDto
  property_count: 12
  slug: hacktron-rest-scan-response-dto
- name: RestUpdateFindingDto
  property_count: 6
  slug: hacktron-rest-update-finding-dto
jsonld:
- class_count: 33
  name: Hacktron Context
  property_count: 112
  slug: hacktron-context
layout: provider
modified: '2026-10-29'
name: Hacktron
nav: Providers
network: true
overview: 'Hacktron publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including REST API - Cost Estimations API, REST API - Findings API, REST API - HFW API, and 2 more. Tagged areas include AI, Automation, Integration, IoT, and Enterprise.


  The Hacktron catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Hacktron''s developer surface includes changelog, authentication, getting-started guide, API reference, documentation, engineering blog, and 31 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 1
  name: Hacktron Rate Limits
  slug: hacktron-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Hacktron API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: hacktron-rules
score:
  band: developing
  composite: 49.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 35.6
    contract_quality: 56.7
    developer_ergonomics: 44.6
    discoverability: 69.6
    operational_transparency: 52.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hacktron Authentication
  slug: hacktron-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hacktron Domain Security
  slug: hacktron-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hacktron Vulnerability Disclosure
  slug: hacktron-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: hacktron-create-list-get-cost-estimation
  slug: hacktron-create-list-get-cost-estimation
- name: hacktron-list-and-export-findings
  slug: hacktron-list-and-export-findings
- name: hacktron-run-scan-and-fetch-findings
  slug: hacktron-run-scan-and-fetch-findings
slug: hacktron
tags:
- AI
- Automation
- Integration
- IoT
- Enterprise
website: https://www.hacktron.ai/
---
