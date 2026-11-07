---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://app.brightsec.com
  baseurl_source: declared
  description: 'brightsec-com API as documented publicly: 13 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: brightsec-com API
  slug: brightsec-com-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/brightsec-com/rules/brightsec-com-rules.yml
  title: ''
  type: Spectral
  url: rules/brightsec-com-rules.yml
- group: design
  href: https://artifacts.apis.io/brightsec-com/json-ld/brightsec-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/brightsec-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/brightsec-com/vocabulary/brightsec-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/brightsec-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/brightsec-com/data-model/brightsec-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/brightsec-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/brightsec-com/conformance/brightsec-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brightsec-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brightsec-com/llms/brightsec-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brightsec-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/brightsec-com/well-known/brightsec-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brightsec-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/brightsec-com/hosts/brightsec-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brightsec-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/brightsec-com/vendors/brightsec-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brightsec-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/brightsec-com/packages/brightsec-com-packages.yml
  title: ''
  type: SDKs
  url: packages/brightsec-com-packages.yml
- group: build
  href: https://artifacts.apis.io/brightsec-com/packages/brightsec-com-packages.yml
  title: ''
  type: Packages
  url: packages/brightsec-com-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.brightsec.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brightsec.com/terms-of-service/
- group: company
  title: ''
  type: Newsroom
  url: https://brightsec.com/news/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.brightsec.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://brightsec.com/blog/best-enterprise-dast-tools/
- group: auth
  href: https://artifacts.apis.io/brightsec-com/security/brightsec-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brightsec-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brightsec.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.brightsec.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.brightsec.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.brightsec.com/docs/quickstart.md
- group: operate
  title: ''
  type: Support
  url: https://docs.brightsec.com/docs/support.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brightsec
- group: start
  title: ''
  type: SignUp
  url: https://app.brightsec.com/login
created: '2026-10-29'
description: Bright Security offers an agentic application security platform that uses AI to automatically discover, test, and remediate vulnerabilities in web applications, APIs, and LLM features. The solution provides dynamic application security testing (DAST) with minimal false positives, supports various authentication methods, integrates with CI/CD pipelines, and offers both SaaS and private‑cloud deployment options for enterprises seeking comprehensive, automated security testing.
image: https://brightsec.com/wp-content/uploads/2026/10/bright-logo.png
json_schemas:
- name: GetApiV1ProjectIssuesProjectissueidResponse
  property_count: 3
  slug: brightsec-com-get-api-v1-project-issues-projectissueid-response
- name: GetApiV2ProjectsProjectidEntryPointsSummaryResponse
  property_count: 1
  slug: brightsec-com-get-api-v2-projects-projectid-entry-points-summary-response
- name: GetApiV2ProjectsProjectidIssuesResponse
  property_count: 6
  slug: brightsec-com-get-api-v2-projects-projectid-issues-response
- name: GetApiV2ProjectsProjectidIssuesSummaryResponse
  property_count: 1
  slug: brightsec-com-get-api-v2-projects-projectid-issues-summary-response
- name: GetApiV2ProjectsResponse
  property_count: 1
  slug: brightsec-com-get-api-v2-projects-response
- name: PostApiV1ScansRequest
  property_count: 1
  slug: brightsec-com-post-api-v1-scans-request
jsonld:
- class_count: 6
  name: Brightsec Com Context
  property_count: 9
  slug: brightsec-com-context
layout: provider
modified: '2026-10-29'
name: brightsec-com
nav: Providers
network: true
overview: 'brightsec-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Application Security, DAST, Artificial Intelligence, and API Testing.


  The brightsec-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  brightsec-com''s developer surface includes changelog, engineering blog, documentation, getting-started guide, support, signup flow, and 18 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: brightsec-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: brightsec-com-rules
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 24.0
    developer_ergonomics: 26.2
    discoverability: 74.1
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 34.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/brightsec-com/brightsec-com-2026-11-03T122630.png
security:
- kind: domain-security
  name: Brightsec Com Domain Security
  slug: brightsec-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: brightsec-com
tags:
- Security
- Application Security
- DAST
- Artificial Intelligence
- API Testing
website: https://brightsec.com/
---
