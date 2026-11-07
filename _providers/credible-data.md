---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.7
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: 'Credible Data Admin API Reference API as documented publicly: 32 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Credible Data Admin API Reference API
  slug: admin-api-reference-api
- description: 'Credible Data Data API Reference API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Credible Data Data API Reference API
  slug: data-api-reference-api
- description: Credible Data API generated from documentation (combined spec) with 40 operations. Not the provider's own published contract.
  name: Credible Data API
  slug: full-api
artifact_total: 21
common:
- group: commercial
  href: https://artifacts.apis.io/credible-data/plans/credible-data-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/credible-data-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/credible-data/rules/credible-data-rules.yml
  title: ''
  type: Spectral
  url: rules/credible-data-rules.yml
- group: design
  href: https://artifacts.apis.io/credible-data/json-ld/credible-data-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/credible-data-context.jsonld
- group: design
  href: https://artifacts.apis.io/credible-data/vocabulary/credible-data-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/credible-data-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/credible-data/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/credible-data/data-model/credible-data-data-model.yml
  title: ''
  type: DataModel
  url: data-model/credible-data-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.credibledata.com/security
- group: design
  href: https://artifacts.apis.io/credible-data/conformance/credible-data-conformance.yml
  title: ''
  type: Conformance
  url: conformance/credible-data-conformance.yml
- group: other
  href: https://artifacts.apis.io/credible-data/overlays/credible-data-admin-api-reference-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/credible-data-admin-api-reference-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/credible-data/llms/credible-data-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/credible-data-llms.txt
- group: other
  href: https://artifacts.apis.io/credible-data/hosts/credible-data-hosts.yml
  title: ''
  type: Hosts
  url: hosts/credible-data-hosts.yml
- group: other
  href: https://artifacts.apis.io/credible-data/vendors/credible-data-vendors.yml
  title: ''
  type: Vendors
  url: vendors/credible-data-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.credibledata.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.credibledata.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.credibledata.com/news
- group: docs
  title: ''
  type: APIReference
  url: https://www.credibledata.com/docs/reference/auth/entra-id
- group: start
  title: ''
  type: GettingStarted
  url: https://www.credibledata.com/docs/platform-admin/cicd
- group: auth
  href: https://artifacts.apis.io/credible-data/security/credible-data-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/credible-data-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/credible-data/security/credible-data-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/credible-data-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/credible-data/security/credible-data-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/credible-data-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.credibledata.com/
- group: company
  title: ''
  type: Blog
  url: https://www.credibledata.com/blog
- group: other
  title: ''
  type: CaseStudies
  url: https://www.credibledata.com/case-studies
- group: commercial
  title: ''
  type: Pricing
  url: https://www.credibledata.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.credibledata.com/docs/introduction
- group: operate
  title: ''
  type: Support
  url: https://www.credibledata.com/docs/community/support
- group: company
  title: ''
  type: AboutUs
  url: https://www.credibledata.com/about
- group: start
  title: ''
  type: SignUp
  url: https://signup.app.credibledata.com/
- group: start
  title: ''
  type: LogIn
  url: https://login.app.credibledata.com
created: '2026-10-29'
description: Credible Data provides the AI Analytics Engine, turning raw data into trustworthy answers, applications, and agents. Their platform lets users connect databases, spreadsheets, or data warehouses, model data with Malloy, and query via natural language. Backed by Gradient Ventures, the company aims to make data reliable for AI-driven decision making, offering a free starter tier and enterprise options.
image: https://www.credibledata.com/opengraph-image.png?opengraph-image.11hhz5jt.hw60.png
json_schemas:
- name: GetEnvironmentsStringPackagesStringModelsResponse
  property_count: 4
  slug: credible-data-get-environments-string-packages-string-models-response
- name: GetEnvironmentsStringPackagesStringPagesResponse
  property_count: 4
  slug: credible-data-get-environments-string-packages-string-pages-response
- name: GetOrganizationsStringEnvironmentsStringPackagesStringRunsRe
  property_count: 15
  slug: credible-data-get-organizations-string-environments-string-packages-string-runs-re
- name: GetOrganizationsStringEnvironmentsStringPackagesStringRunsSt
  property_count: 15
  slug: credible-data-get-organizations-string-environments-string-packages-string-runs-st
- name: GetOrganizationsStringEnvironmentsStringPackagesStringVersio
  property_count: 20
  slug: credible-data-get-organizations-string-environments-string-packages-string-versio
- name: GetOrganizationsStringEnvironmentsStringPackagesStringVersio2
  property_count: 17
  slug: credible-data-get-organizations-string-environments-string-packages-string-versio2
- name: GetUsersStringResponse
  property_count: 7
  slug: credible-data-get-users-string-response
- name: PatchOrganizationsStringEnvironmentsStringPackagesStringVers
  property_count: 20
  slug: credible-data-patch-organizations-string-environments-string-packages-string-vers
- name: PostEnvironmentsStringConnectionsStringSqlqueryResponse
  property_count: 2
  slug: credible-data-post-environments-string-connections-string-sqlquery-response
- name: PostEnvironmentsStringPackagesStringModelsStringQueryRespons
  property_count: 4
  slug: credible-data-post-environments-string-packages-string-models-string-query-respons
- name: PostWatchModeStartRequest
  property_count: 1
  slug: credible-data-post-watch-mode-start-request
jsonld:
- class_count: 27
  name: Credible Data Context
  property_count: 82
  slug: credible-data-context
layout: provider
modified: '2026-10-29'
name: Credible Data
nav: Providers
network: true
overview: 'Credible Data is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Admin API Reference API, Data API Reference API, and 1 more. Tagged areas include Artificial Intelligence, Data Analytics, Machine Learning, Analytics Engine, and Platform.


  The Credible Data catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Credible Data''s developer surface includes API reference, getting-started guide, engineering blog, pricing, documentation, support, signup flow, and 22 more developer resources.'
plans:
- name: Credible Data Plans Pricing
  plan_count: 2
  slug: credible-data-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Credible Data API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: credible-data-rules
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 68.8
    catalog_earned_first_party: 8.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 50.0
    contract_governance: 22.0
    contract_quality: 24.0
    developer_ergonomics: 24.3
    discoverability: 70.5
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 40.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/credible-data/credible-data-2026-11-03T125545.png
security:
- kind: domain-security
  name: Credible Data Domain Security
  slug: credible-data-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Credible Data Vulnerability Disclosure
  slug: credible-data-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Credible Data Trust Center
  slug: credible-data-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 1
skills:
- name: create-environment
  slug: credible-data-create-environment
slug: credible-data
tags:
- Artificial Intelligence
- Data Analytics
- Machine Learning
- Analytics Engine
- Platform
website: https://www.credibledata.com/
---
