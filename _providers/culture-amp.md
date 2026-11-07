---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Culture Amp Agentic Access
  operation_count: 19
  slug: culture-amp-agentic-access
  summary_line: 19 operations
api_count: 1
apis:
- baseURL: https://api.cultureamp.com
  baseurl_source: declared
  description: The Employees API from Culture Amp — 3 operation(s) for employees.
  name: Culture Amp Employees API
  slug: culture-amp-employees-api
- baseURL: https://api.cultureamp.com
  baseurl_source: declared
  description: The Performance API from Culture Amp — 6 operation(s) for performance.
  name: Culture Amp Performance API
  slug: culture-amp-performance-api
- baseURL: https://api.cultureamp.com
  baseurl_source: declared
  description: The Surveys API from Culture Amp — 10 operation(s) for surveys.
  name: Culture Amp Surveys API
  slug: culture-amp-surveys-api
artifact_total: 30
collections:
- collection_type: postman
  name: Culture Amp Public Employees API
  slug: postman-culture-amp-employees-api
- collection_type: postman
  name: Culture Amp Public Employees Performance API
  slug: postman-culture-amp-performance-api
- collection_type: postman
  name: Culture Amp Public Employees Surveys API
  slug: postman-culture-amp-surveys-api
- collection_type: open
  name: Culture Amp Public Employees API
  slug: open-culture-amp-employees-api
- collection_type: open
  name: Culture Amp Public Employees Performance API
  slug: open-culture-amp-performance-api
- collection_type: open
  name: Culture Amp Public Employees Surveys API
  slug: open-culture-amp-surveys-api
common:
- group: design
  href: https://artifacts.apis.io/culture-amp/rules/culture-amp-rules.yml
  title: ''
  type: Spectral
  url: rules/culture-amp-rules.yml
- group: design
  href: https://artifacts.apis.io/culture-amp/rules/culture-amp-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/culture-amp-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/culture-amp/json-ld/culture-amp-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/culture-amp-context.jsonld
- group: agent
  href: https://artifacts.apis.io/culture-amp/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/culture-amp/data-model/culture-amp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/culture-amp-data-model.yml
- group: operate
  href: https://artifacts.apis.io/culture-amp/changelog/culture-amp-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/culture-amp-changelog.yml
- group: design
  href: https://artifacts.apis.io/culture-amp/conventions/culture-amp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/culture-amp-conventions.yml
- group: start
  href: https://artifacts.apis.io/culture-amp/sandbox/culture-amp-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/culture-amp-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.cultureamp.com/
- group: operate
  href: https://artifacts.apis.io/culture-amp/lifecycle/culture-amp-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/culture-amp-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/culture-amp/lifecycle/culture-amp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/culture-amp-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/culture-amp/errors/culture-amp-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/culture-amp-problem-types.yml
- group: design
  href: https://artifacts.apis.io/culture-amp/conformance/culture-amp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/culture-amp-conformance.yml
- group: other
  href: https://artifacts.apis.io/culture-amp/overlays/culture-amp-employees-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/culture-amp-employees-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/culture-amp/llms/culture-amp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/culture-amp-llms.txt
- group: auth
  href: https://artifacts.apis.io/culture-amp/well-known/culture-amp-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/culture-amp-support-security.txt
- group: agent
  href: https://artifacts.apis.io/culture-amp/well-known/culture-amp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/culture-amp-well-known.yml
- group: other
  href: https://artifacts.apis.io/culture-amp/hosts/culture-amp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/culture-amp-hosts.yml
- group: build
  href: https://artifacts.apis.io/culture-amp/integrations/culture-amp-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/culture-amp-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/culture-amp/vendors/culture-amp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/culture-amp-vendors.yml
- group: other
  href: https://artifacts.apis.io/culture-amp/capabilities/culture-amp-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/culture-amp-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/culture-amp/overview
- group: agent
  href: https://artifacts.apis.io/culture-amp/agentic-access/culture-amp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/culture-amp-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/culture-amp/security/culture-amp-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/culture-amp-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/culture-amp/security/culture-amp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/culture-amp-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/culture-amp/authentication/culture-amp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/culture-amp-authentication.yml
- group: auth
  href: https://artifacts.apis.io/culture-amp/scopes/culture-amp-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/culture-amp-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.cultureamp.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.cultureamp.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cultureamp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cultureamp
- group: other
  title: ''
  type: X
  url: https://x.com/CultureAmp
- group: company
  title: ''
  type: Blog
  url: https://www.cultureamp.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cultureamp.com/platform/plans-and-pricing
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.cultureamp.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api.cultureamp.com/docs/resources-getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.api.cultureamp.com/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.api.cultureamp.com/llms.txt
- group: operate
  title: ''
  type: Support
  url: https://support.cultureamp.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.cultureamp.com/company/contact-us
- group: start
  title: ''
  type: Login
  url: https://id.cultureamp.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cultureamp.com/company/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cultureamp.com/company/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.cultureamp.com/company/newsroom
- group: auth
  title: ''
  type: TrustCenterPage
  url: https://www.cultureamp.com/company/trust
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cultureamp.com
- group: commercial
  href: https://artifacts.apis.io/culture-amp/plans/culture-amp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/culture-amp-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/culture-amp/rate-limits/culture-amp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/culture-amp-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/culture-amp/finops/culture-amp-finops.yml
  title: ''
  type: FinOps
  url: finops/culture-amp-finops.yml
- group: design
  href: https://artifacts.apis.io/culture-amp/vocabulary/culture-amp-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/culture-amp-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/culture-amp/json-ld/culture-amp-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/culture-amp-context.jsonld
created: '2026-06-12'
description: Culture Amp is the leading employee experience platform providing tools for employee engagement surveys, performance management, and people analytics. The Culture Amp Public API is a RESTful, read-only interface that enables organizations to programmatically retrieve their people data—including employee records, demographics, performance cycles, manager reviews, and survey results—for use in external systems and custom analytics. The API uses OAuth 2.0 Client Credentials Flow for authentication and is available to all Culture Amp subscribers at no additional cost as part of standard subscription fees. The platform serves thousands of organizations worldwide and integrates with leading HRIS systems, Slack, Microsoft Teams, and compensation tools like Pave.
examples:
- key_count: 1
  name: Culture Amp Employee Example
  slug: culture-amp-employee-example
- key_count: 2
  name: Culture Amp Employees List Example
  slug: culture-amp-employees-list-example
- key_count: 1
  name: Culture Amp Manager Review Example
  slug: culture-amp-manager-review-example
- key_count: 1
  name: Culture Amp Performance Cycle Example
  slug: culture-amp-performance-cycle-example
finops:
- has_sources: false
  method: generated
  name: Culture Amp Finops
  primary_unit: ''
  service_category: ''
  slug: culture-amp-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/culture-amp.png
json_schemas:
- name: Employee
  property_count: 10
  slug: culture-amp-employee
- name: ManagerReview
  property_count: 15
  slug: culture-amp-manager-review
- name: PerformanceCycle
  property_count: 6
  slug: culture-amp-performance-cycle
jsonld:
- class_count: 52
  name: Culture Amp Context
  property_count: 24
  slug: culture-amp-context
layout: provider
modified: '2026-10-20'
name: Culture Amp
nav: Providers
network: true
overview: 'Culture Amp publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Employees API, Performance API, and Surveys API. Tagged areas include Human Resources, Employee Engagement, Performance Management, People Analytics, and Surveys.


  The Culture Amp catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Culture Amp''s developer surface includes changelog, sandbox, authentication, documentation, engineering blog, pricing, API reference, and 44 more developer resources.'
plans:
- name: Culture Amp Plans Pricing
  plan_count: 2
  slug: culture-amp-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Culture Amp Rate Limits
  slug: culture-amp-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Culture Amp — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: culture-amp-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Culture Amp API Rules
  rule_count: 18
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 0
  slug: culture-amp-rules
scopes:
- name: Culture Amp Scopes
  scope_count: 4
  slug: culture-amp-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: strong
  composite: 60.0
  coverage:
    artifact_dirs: 38
    catalog_earned: 82.0
    catalog_earned_first_party: 16.0
    catalog_gap: 33.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 55.3
    contract_governance: 45.5
    contract_quality: 69.0
    developer_ergonomics: 39.9
    discoverability: 74.1
    operational_transparency: 57.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 66.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 40.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/culture-amp/culture-amp-2026-06-20T175332.png
security:
- kind: authentication
  name: Culture Amp Authentication
  slug: culture-amp-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Culture Amp Domain Security
  slug: culture-amp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Culture Amp Trust Center
  slug: culture-amp-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CSA STAR
skill_count: 3
skills:
- name: culture-amp-collect-performance-cycle-reviews
  slug: culture-amp-collect-performance-cycle-reviews
- name: culture-amp-export-survey-results
  slug: culture-amp-export-survey-results
- name: culture-amp-look-up-an-employee
  slug: culture-amp-look-up-an-employee
slug: culture-amp
tags:
- Human Resources
- Employee Engagement
- Performance Management
- People Analytics
- Surveys
- Australia
website: https://www.cultureamp.com
---
