---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Workday Benefits Agentic Access
  operation_count: 22
  slug: workday-benefits-agentic-access
  summary_line: 22 operations · 7 acting
api_count: 4
apis:
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: Manage employee benefit enrollments and elections
  name: Workday Benefits Benefit Enrollments API
  slug: workday-benefits-benefit-enrollments-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: Manage benefit qualifying events and open enrollment
  name: Workday Benefits Benefit Events API
  slug: workday-benefits-benefit-events-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: Manage benefit plan definitions and configurations
  name: Workday Benefits Benefit Plans API
  slug: workday-benefits-benefit-plans-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: Manage employee dependents and beneficiaries
  name: Workday Benefits Dependents API
  slug: workday-benefits-dependents-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: Manage individual employee benefit summaries and balances
  name: Workday Benefits Employee Benefits API
  slug: workday-benefits-employee-benefits-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: Manage time off and leave benefit plans
  name: Workday Benefits Time Off Plans API
  slug: workday-benefits-time-off-plans-api
- description: 'The Benefits Administration Web Service contains operations that expose Workday Human Capital Management Business Services benefits-related data: 47 SOAP operations covering benefit plans, elections, '
  name: Workday Benefits Administration Web Service (SOAP)
  slug: workday-benefits-benefits-administration-soap-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: Changes for v2024.24
  name: Workday Benefits 06/15/2024 API
  slug: workday-benefits-06-15-2024-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: Changes for v2026.24
  name: Workday Benefits 06/15/2026 API
  slug: workday-benefits-06-15-2026-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: Changes for v2026.26
  name: Workday Benefits 06/30/2026 API
  slug: workday-benefits-06-30-2026-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: Changes for v2026.33
  name: Workday Benefits 08/17/2026 API
  slug: workday-benefits-08-17-2026-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: Changes for v2023.36
  name: Workday Benefits 09/09/2023 API
  slug: workday-benefits-09-09-2023-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: Processing Worker's Latest Employee Enrollment Event
  name: Workday Benefits Employee Enrollment Event API
  slug: workday-benefits-employeeenrollmentevent-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: Provides the ability to import benefits program cards into Workday.
  name: Workday Benefits Programs API
  slug: workday-benefits-programs-api
artifact_total: 62
collections:
- collection_type: postman
  name: Workday Benefits Benefit Enrollments API
  slug: postman-workday-benefits-benefit-enrollments-api
- collection_type: postman
  name: Workday Benefits Benefit Enrollments Benefit Events API
  slug: postman-workday-benefits-benefit-events-api
- collection_type: postman
  name: Workday Benefits Benefit Enrollments Benefit Plans API
  slug: postman-workday-benefits-benefit-plans-api
- collection_type: postman
  name: Workday Benefits Benefit Enrollments Dependents API
  slug: postman-workday-benefits-dependents-api
- collection_type: postman
  name: Workday Benefits Benefit Enrollments Employee Benefits API
  slug: postman-workday-benefits-employee-benefits-api
- collection_type: postman
  name: Workday Benefits Benefit Enrollments Time Off Plans API
  slug: postman-workday-benefits-time-off-plans-api
- collection_type: open
  name: Workday Benefits Benefit Enrollments API
  slug: open-workday-benefits-benefit-enrollments-api
- collection_type: open
  name: Workday Benefits Benefit Enrollments Benefit Events API
  slug: open-workday-benefits-benefit-events-api
- collection_type: open
  name: Workday Benefits Benefit Enrollments Benefit Plans API
  slug: open-workday-benefits-benefit-plans-api
- collection_type: open
  name: Workday Benefits Benefit Enrollments Dependents API
  slug: open-workday-benefits-dependents-api
- collection_type: open
  name: Workday Benefits Benefit Enrollments Employee Benefits API
  slug: open-workday-benefits-employee-benefits-api
- collection_type: open
  name: Workday Benefits Benefit Enrollments Time Off Plans API
  slug: open-workday-benefits-time-off-plans-api
- collection_type: open
  name: Workday Benefits API
  slug: open-workday-benefits
common:
- group: commercial
  href: https://artifacts.apis.io/workday-benefits/finops/workday-benefits-finops.yml
  title: ''
  type: FinOps
  url: finops/workday-benefits-finops.yml
- group: other
  href: https://artifacts.apis.io/workday-benefits/overlays/workday-benefits-benefit-enrollment-event-offerings-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/workday-benefits-benefit-enrollment-event-offerings-overlay.yaml
- group: other
  href: https://artifacts.apis.io/workday-benefits/overlays/workday-benefits-benefit-partner-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/workday-benefits-benefit-partner-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.workday.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/workday-benefits/overview
- group: agent
  href: https://artifacts.apis.io/workday-benefits/agentic-access/workday-benefits-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/workday-benefits-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/workday-benefits/security/workday-benefits-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/workday-benefits-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/workday-benefits/security/workday-benefits-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/workday-benefits-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/workday-benefits/authentication/workday-benefits-authentication.yml
  title: ''
  type: Authentication
  url: authentication/workday-benefits-authentication.yml
- group: auth
  href: https://artifacts.apis.io/workday-benefits/scopes/workday-benefits-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/workday-benefits-scopes.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.workday.com/doc/GUID-6c547385-848b-4005-ab2c-632f1d6b5688.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.workday.com
- group: auth
  title: ''
  type: Authentication
  url: https://developer.workday.com/doc/GUID-6c598444-ce67-40d5-bd95-267ecfe439b8-enHYPHENus.md
- group: company
  title: ''
  type: Blog
  url: https://blog.workday.com/en-us/technology.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workday.com/en-us/privacy.html
- group: design
  href: https://artifacts.apis.io/workday-benefits/json-ld/workday-benefits-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/workday-benefits-context.jsonld
- group: design
  href: https://artifacts.apis.io/workday-benefits/rules/workday-benefits-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/workday-benefits-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/workday-benefits/vocabulary/workday-benefits-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/workday-benefits-vocabulary.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.workday.com/doc/GUID-86d66a6b-5d1a-40e4-af1b-ba4859f5df5a-enHYPHENus.md
- group: docs
  title: ''
  type: APIReference
  url: https://developer.workday.com/rest-api-explorer
- group: operate
  title: ''
  type: Support
  url: https://community.workday.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Workday
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workday.com/en-us/legal.html
- group: operate
  title: ''
  type: Roadmap
  url: https://developer.workday.com/doc/GUID-7ac8632c-1c99-44cd-b939-44c675ea6198.md
- group: agent
  href: https://artifacts.apis.io/workday-benefits/llms/workday-benefits-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/workday-benefits-llms.txt
- group: other
  href: https://artifacts.apis.io/workday-benefits/wsdl/workday-benefits-benefits-administration-v47.wsdl
  title: ''
  type: WSDL
  url: wsdl/workday-benefits-benefits-administration-v47.wsdl
- group: design
  href: https://artifacts.apis.io/workday-benefits/conventions/workday-benefits-conventions.yml
  title: ''
  type: Conventions
  url: conventions/workday-benefits-conventions.yml
- group: design
  href: https://artifacts.apis.io/workday-benefits/errors/workday-benefits-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/workday-benefits-problem-types.yml
- group: design
  href: https://artifacts.apis.io/workday-benefits/lifecycle/workday-benefits-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/workday-benefits-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.workday.com
- group: operate
  href: https://artifacts.apis.io/workday-benefits/lifecycle/workday-benefits-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/workday-benefits-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/workday-benefits/changelog/workday-benefits-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/workday-benefits-changelog.yml
- group: design
  href: https://artifacts.apis.io/workday-benefits/conformance/workday-benefits-conformance.yml
  title: ''
  type: Conformance
  url: conformance/workday-benefits-conformance.yml
- group: auth
  href: https://artifacts.apis.io/workday-benefits/security/workday-benefits-trust-center.yml
  title: ''
  type: Compliance
  url: security/workday-benefits-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/workday-benefits/security/workday-benefits-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/workday-benefits-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/workday-benefits/security/workday-benefits-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/workday-benefits-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/workday-benefits/data-model/workday-benefits-data-model.yml
  title: ''
  type: DataModel
  url: data-model/workday-benefits-data-model.yml
- group: build
  href: https://artifacts.apis.io/workday-benefits/packages/workday-benefits-packages.yml
  title: ''
  type: Packages
  url: packages/workday-benefits-packages.yml
- group: build
  href: https://artifacts.apis.io/workday-benefits/cli/workday-benefits-cli.yml
  title: ''
  type: CLI
  url: cli/workday-benefits-cli.yml
- group: start
  href: https://artifacts.apis.io/workday-benefits/sandbox/workday-benefits-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/workday-benefits-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/workday-benefits/mcp/workday-benefits-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/workday-benefits-mcp.yml
- group: agent
  href: https://artifacts.apis.io/workday-benefits/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/workday-benefits/rate-limits/workday-benefits-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/workday-benefits-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/workday-benefits/plans/workday-benefits-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/workday-benefits-plans-pricing.yml
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/workday/workspace/workday-rest-api
- group: agent
  href: https://artifacts.apis.io/workday-benefits/well-known/workday-benefits-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/workday-benefits-well-known.yml
- group: auth
  href: https://artifacts.apis.io/workday-benefits/well-known/workday-benefits-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/workday-benefits-security.txt
- group: agent
  href: https://artifacts.apis.io/workday-benefits/skills/workday-benefits-read-enrollment-offerings.md
  title: ''
  type: AgentSkill
  url: skills/workday-benefits-read-enrollment-offerings.md
- group: agent
  href: https://artifacts.apis.io/workday-benefits/skills/workday-benefits-import-benefit-program.md
  title: ''
  type: AgentSkill
  url: skills/workday-benefits-import-benefit-program.md
created: '2024-01-01'
description: 'Workday Benefits covers the benefits administration surface of Workday Human Capital Management: benefit plan definitions, enrollment events and offerings, employee elections, dependents and beneficiaries, retirement savings plans, ACA reporting data, rates and benefit providers. Workday publishes machine-readable contracts for this surface in two shapes - production REST services (benefitEnrollmentEventOfferings v1 and benefitPartner v1, OpenAPI 3.0.1 in the Workday REST API Explorer directory) and the Benefits_Administration Workday Web Service, a 47-operation SOAP contract published as a public WSDL at version v47.0. Access is tenant-scoped and OAuth 2.0 only; there is no public sandbox and no public pricing for the API surface.'
examples:
- key_count: 10
  name: Workday Benefits Benefit Enrollment Example
  slug: workday-benefits-benefit-enrollment-example
- key_count: 5
  name: Workday Benefits Benefit Enrollment Request Example
  slug: workday-benefits-benefit-enrollment-request-example
- key_count: 6
  name: Workday Benefits Benefit Event Example
  slug: workday-benefits-benefit-event-example
- key_count: 11
  name: Workday Benefits Benefit Plan Example
  slug: workday-benefits-benefit-plan-example
- key_count: 7
  name: Workday Benefits Dependent Example
  slug: workday-benefits-dependent-example
- key_count: 5
  name: Workday Benefits Employee Benefits Example
  slug: workday-benefits-employee-benefits-example
- key_count: 7
  name: Workday Benefits Time Off Plan Example
  slug: workday-benefits-time-off-plan-example
finops:
- has_sources: true
  method: derived
  name: Workday Benefits Finops
  primary_unit: ''
  service_category: ''
  slug: workday-benefits-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workday-benefits.png
json_schemas:
- name: Benefit Enrollment Request
  property_count: 6
  slug: workday-benefits-benefit-enrollment-request
- name: Benefit Enrollment
  property_count: 10
  slug: workday-benefits-benefit-enrollment
- name: Benefit Event
  property_count: 7
  slug: workday-benefits-benefit-event
- name: Benefit Plan
  property_count: 11
  slug: workday-benefits-benefit-plan
- name: Dependent
  property_count: 7
  slug: workday-benefits-dependent
- name: Employee Benefits
  property_count: 5
  slug: workday-benefits-employee-benefits
- name: Time Off Plan
  property_count: 7
  slug: workday-benefits-time-off-plan
json_structures:
- name: Workday Benefits Benefit Enrollment Request Structure
  property_count: 6
  slug: workday-benefits-benefit-enrollment-request-structure
- name: Workday Benefits Benefit Enrollment Structure
  property_count: 10
  slug: workday-benefits-benefit-enrollment-structure
- name: Workday Benefits Benefit Event Structure
  property_count: 7
  slug: workday-benefits-benefit-event-structure
- name: Workday Benefits Benefit Plan Structure
  property_count: 11
  slug: workday-benefits-benefit-plan-structure
- name: Workday Benefits Dependent Structure
  property_count: 7
  slug: workday-benefits-dependent-structure
- name: Workday Benefits Employee Benefits Structure
  property_count: 5
  slug: workday-benefits-employee-benefits-structure
- name: Workday Benefits Time Off Plan Structure
  property_count: 7
  slug: workday-benefits-time-off-plan-structure
jsonld:
- class_count: 25
  name: Workday Benefits Context
  property_count: 14
  slug: workday-benefits-context
layout: provider
modified: '2026-09-17'
name: Workday Benefits
nav: Providers
network: true
overview: 'Workday Benefits publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Benefit Enrollments API, Benefit Events API, Benefit Plans API, and 11 more. Tagged areas include Benefits, Human Resources, HCM, Enterprise, and Payroll.


  The Workday Benefits catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Workday Benefits'' developer surface includes authentication, getting-started guide, engineering blog, documentation, API reference, support, changelog, and 42 more developer resources.'
plans:
- name: Workday Benefits Plans Pricing
  plan_count: 0
  slug: workday-benefits-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Workday Benefits Rate Limits
  slug: workday-benefits-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Workday Benefits — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: workday-benefits-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Workday Benefits API Rules
  rule_count: 44
  severity_counts:
    error: 7
    hint: 0
    info: 12
    warn: 25
  slug: workday-benefits-spectral-rules
scopes:
- name: Workday Benefits Scopes
  scope_count: 1
  slug: workday-benefits-scopes
  summary_line: 1 scope · implicit/clientCredentials
score:
  band: developing
  composite: 51.0
  coverage:
    artifact_dirs: 34
    catalog_earned: 69.0
    catalog_earned_first_party: 0.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    contract_governance: 31.8
    contract_quality: 42.5
    developer_ergonomics: 54.2
    discoverability: 78.6
    operational_transparency: 47.4
  previous_composite: 51.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 7
      marker_coverage: 50.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/workday-benefits/workday-benefits-2026-06-20T201559.png
security:
- kind: authentication
  name: Workday Benefits Authentication
  slug: workday-benefits-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Workday Benefits Domain Security
  slug: workday-benefits-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Workday Benefits Vulnerability Disclosure
  slug: workday-benefits-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Workday Benefits Trust Center
  slug: workday-benefits-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
skill_count: 2
skills:
- name: workday-benefits-import-benefit-program
  slug: workday-benefits-import-benefit-program
- name: workday-benefits-read-enrollment-offerings
  slug: workday-benefits-read-enrollment-offerings
slug: workday-benefits
tags:
- Benefits
- Human Resources
- HCM
- Enterprise
- Payroll
- Employee Benefits
- SOAP
- OpenAPI
website: https://www.workday.com/
---
