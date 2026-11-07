---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Project management software API for Breeze
  name: Breeze API
  slug: breeze-api
- baseURL: https://api.breeze.pm
  baseurl_source: declared
  description: 'breeze-pm API as documented publicly: 63 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: breeze-pm API
  slug: breeze-pm-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/breeze-pm/plans/breeze-pm-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/breeze-pm-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/breeze-pm/rules/breeze-pm-rules.yml
  title: ''
  type: Spectral
  url: rules/breeze-pm-rules.yml
- group: design
  href: https://artifacts.apis.io/breeze-pm/json-ld/breeze-pm-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/breeze-pm-context.jsonld
- group: design
  href: https://artifacts.apis.io/breeze-pm/vocabulary/breeze-pm-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/breeze-pm-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/breeze-pm/data-model/breeze-pm-data-model.yml
  title: ''
  type: DataModel
  url: data-model/breeze-pm-data-model.yml
- group: operate
  href: https://artifacts.apis.io/breeze-pm/changelog/breeze-pm-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/breeze-pm-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.breeze.pm/security
- group: design
  href: https://artifacts.apis.io/breeze-pm/conformance/breeze-pm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/breeze-pm-conformance.yml
- group: auth
  href: https://artifacts.apis.io/breeze-pm/well-known/breeze-pm-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/breeze-pm-security.txt
- group: auth
  href: https://artifacts.apis.io/breeze-pm/well-known/breeze-pm-breeze-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/breeze-pm-breeze-security.txt
- group: agent
  href: https://artifacts.apis.io/breeze-pm/well-known/breeze-pm-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/breeze-pm-well-known.yml
- group: other
  href: https://artifacts.apis.io/breeze-pm/hosts/breeze-pm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/breeze-pm-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.breeze.pm/terms
- group: operate
  title: ''
  type: Support
  url: https://www.breeze.pm/help
- group: auth
  title: ''
  type: Security
  url: https://www.breeze.pm/security
- group: operate
  title: ''
  type: Roadmap
  url: https://www.breeze.pm/product/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.breeze.pm/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.breeze.pm/pricing
- group: start
  title: ''
  type: Login
  url: https://app.breeze.pm/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/breezepm/
- group: company
  title: ''
  type: Blog
  url: https://www.breeze.pm/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.breeze.pm/getting-started-with-breeze
- group: auth
  href: https://artifacts.apis.io/breeze-pm/security/breeze-pm-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/breeze-pm-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/breeze-pm/security/breeze-pm-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/breeze-pm-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/breeze-pm/security/breeze-pm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/breeze-pm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://breeze.pm/
coverage:
  checked: '2026-11-03'
  detail: API documentation page renders HTML with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.breeze.pm/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Breeze provides simple project management software that helps teams organize tasks, plan projects, and collaborate. The platform includes features such as task boards, kanban visualizations, time tracking, project calendars, reporting, and real‑time chat. It is marketed to a range of teams—including marketing, design, sales, development, and remote work groups—and offers a single pricing plan with unlimited projects and client users.
image: https://d1wdkw032nxkks.cloudfront.net/front/1/projects_and_tasks.jpg
json_schemas:
- name: GetProjectsJsonResponse
  property_count: 13
  slug: breeze-pm-get-projects-json-response
- name: GetProjects1JsonResponse
  property_count: 13
  slug: breeze-pm-get-projects1-json-response
- name: GetRunningTimersJsonResponse
  property_count: 10
  slug: breeze-pm-get-running-timers-json-response
- name: PostProjectsJsonResponse
  property_count: 13
  slug: breeze-pm-post-projects-json-response
- name: PostProjectsProjectidCardsJsonRequest
  property_count: 12
  slug: breeze-pm-post-projects-projectid-cards-json-request
- name: PutProjectsProjectidCardsCardIdJsonRequest
  property_count: 11
  slug: breeze-pm-put-projects-projectid-cards-card-id-json-request
jsonld:
- class_count: 48
  name: Breeze Pm Context
  property_count: 56
  slug: breeze-pm-context
layout: provider
modified: '2026-11-03'
name: breeze-pm
nav: Providers
network: true
overview: 'breeze-pm is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Project Management, Task Management, Time Tracking, Kanban, and Remote Work.


  The breeze-pm catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  breeze-pm''s developer surface includes changelog, support, pricing, engineering blog, getting-started guide, and 21 more developer resources.'
plans:
- name: Breeze Pm Plans Pricing
  plan_count: 2
  slug: breeze-pm-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: breeze-pm API Rules
  rule_count: 38
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 1
  slug: breeze-pm-rules
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 26.3
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
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Breeze Pm Domain Security
  slug: breeze-pm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Breeze Pm Vulnerability Disclosure
  slug: breeze-pm-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Breeze Pm Trust Center
  slug: breeze-pm-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: breeze-pm
tags:
- Project Management
- Task Management
- Time Tracking
- Kanban
- Remote Work
website: https://breeze.pm/
---
