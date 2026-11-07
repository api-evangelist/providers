---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Veracode Agentic Access
  operation_count: 33
  slug: veracode-agentic-access
  summary_line: 33 operations · 14 acting · 1 human-in-the-loop
api_count: 4
apis:
- baseURL: https://api.veracode.com
  baseurl_source: declared
  description: API credential lifecycle management
  name: Veracode API Credentials API
  slug: veracode-api-credentials-api
- baseURL: https://api.veracode.com
  baseurl_source: declared
  description: Application profile management
  name: Veracode Applications API
  slug: veracode-applications-api
- baseURL: https://api.veracode.com
  baseurl_source: declared
  description: Business unit management
  name: Veracode Business Units API
  slug: veracode-business-units-api
- baseURL: https://api.veracode.com
  baseurl_source: declared
  description: Application security findings
  name: Veracode Findings API
  slug: veracode-findings-api
- baseURL: https://api.veracode.com
  baseurl_source: declared
  description: Manual penetration test findings
  name: Veracode Manual Penetration Testing API
  slug: veracode-manual-penetration-testing-api
- baseURL: https://api.veracode.com
  baseurl_source: declared
  description: Application policy compliance evaluations
  name: Veracode Policy Evaluations API
  slug: veracode-policy-evaluations-api
- baseURL: https://api.veracode.com
  baseurl_source: declared
  description: Asynchronous report generation and retrieval
  name: Veracode Reports API
  slug: veracode-reports-api
- baseURL: https://api.veracode.com
  baseurl_source: declared
  description: Role and permission management
  name: Veracode Roles API
  slug: veracode-roles-api
- baseURL: https://api.veracode.com
  baseurl_source: declared
  description: Development sandbox management
  name: Veracode Sandboxes API
  slug: veracode-sandboxes-api
- baseURL: https://api.veracode.com
  baseurl_source: declared
  description: Team management
  name: Veracode Teams API
  slug: veracode-teams-api
- baseURL: https://api.veracode.com
  baseurl_source: declared
  description: User and API service account management
  name: Veracode Users API
  slug: veracode-users-api
- baseURL: https://api.veracode.com
  baseurl_source: declared
  description: API credential lifecycle management
  name: Veracode API Credentials API
  slug: veracode-api-credentials-api
artifact_total: 70
collections:
- collection_type: open
  name: Veracode Applications REST API Credentials API
  slug: open-veracode-api-credentials-api
- collection_type: open
  name: Veracode REST API Credentials Applications API
  slug: open-veracode-applications-api
- collection_type: open
  name: Veracode Applications REST API
  slug: open-veracode-applications
- collection_type: open
  name: Veracode Applications REST API Credentials Business Units API
  slug: open-veracode-business-units-api
- collection_type: open
  name: Veracode Applications REST API Credentials Findings API
  slug: open-veracode-findings-api
- collection_type: open
  name: Veracode Findings REST API
  slug: open-veracode-findings
- collection_type: open
  name: Veracode Identity REST API
  slug: open-veracode-identity
- collection_type: open
  name: Veracode Applications REST API Credentials Manual Penetration Testing API
  slug: open-veracode-manual-penetration-testing-api
- collection_type: open
  name: Veracode Applications REST API Credentials Policy Evaluations API
  slug: open-veracode-policy-evaluations-api
- collection_type: open
  name: Veracode Reporting REST API
  slug: open-veracode-reporting
- collection_type: open
  name: Veracode Applications REST API Credentials Reports API
  slug: open-veracode-reports-api
- collection_type: open
  name: Veracode Applications REST API Credentials Roles API
  slug: open-veracode-roles-api
- collection_type: open
  name: Veracode Applications REST API Credentials Sandboxes API
  slug: open-veracode-sandboxes-api
- collection_type: open
  name: Veracode Applications REST API Credentials Teams API
  slug: open-veracode-teams-api
- collection_type: open
  name: Veracode Applications REST API Credentials Users API
  slug: open-veracode-users-api
common:
- group: commercial
  href: https://artifacts.apis.io/veracode/finops/veracode-finops.yml
  title: ''
  type: FinOps
  url: finops/veracode-finops.yml
- group: operate
  href: https://artifacts.apis.io/veracode/rate-limits/veracode-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/veracode-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/veracode/plans/veracode-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/veracode-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/veracode/rules/veracode-rules.yml
  title: ''
  type: Spectral
  url: rules/veracode-rules.yml
- group: design
  href: https://artifacts.apis.io/veracode/rules/veracode-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/veracode-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/veracode/json-ld/veracode-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/veracode-context.jsonld
- group: design
  href: https://artifacts.apis.io/veracode/vocabulary/veracode-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/veracode-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/veracode/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/veracode/data-model/veracode-data-model.yml
  title: ''
  type: DataModel
  url: data-model/veracode-data-model.yml
- group: design
  href: https://artifacts.apis.io/veracode/conventions/veracode-conventions.yml
  title: ''
  type: Conventions
  url: conventions/veracode-conventions.yml
- group: start
  href: https://artifacts.apis.io/veracode/sandbox/veracode-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/veracode-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.veracode.com/
- group: design
  href: https://artifacts.apis.io/veracode/errors/veracode-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/veracode-problem-types.yml
- group: design
  href: https://artifacts.apis.io/veracode/conformance/veracode-conformance.yml
  title: ''
  type: Conformance
  url: conformance/veracode-conformance.yml
- group: agent
  href: https://artifacts.apis.io/veracode/llms/veracode-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/veracode-llms.txt
- group: auth
  href: https://artifacts.apis.io/veracode/well-known/veracode-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/veracode-status-security.txt
- group: agent
  href: https://artifacts.apis.io/veracode/well-known/veracode-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/veracode-well-known.yml
- group: other
  href: https://artifacts.apis.io/veracode/hosts/veracode-hosts.yml
  title: ''
  type: Hosts
  url: hosts/veracode-hosts.yml
- group: other
  href: https://artifacts.apis.io/veracode/vendors/veracode-vendors.yml
  title: ''
  type: Vendors
  url: vendors/veracode-vendors.yml
- group: build
  href: https://artifacts.apis.io/veracode/packages/veracode-packages.yml
  title: ''
  type: SDKs
  url: packages/veracode-packages.yml
- group: build
  href: https://artifacts.apis.io/veracode/packages/veracode-packages.yml
  title: ''
  type: Packages
  url: packages/veracode-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.veracode.com/terms-of-use/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.veracode.com/
- group: auth
  title: ''
  type: Security
  url: https://www.veracode.com/security/
- group: company
  title: ''
  type: Newsroom
  url: https://www.veracode.com/newsroom/
- group: start
  title: ''
  type: Login
  url: https://web.analysiscenter.veracode.com/login
- group: other
  title: ''
  type: Leadership
  url: https://www.veracode.com/about/leadership/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.veracode.com/solutions/developers/
- group: agent
  href: https://artifacts.apis.io/veracode/agentic-access/veracode-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/veracode-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/veracode/security/veracode-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/veracode-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/veracode/security/veracode-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/veracode-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/veracode/security/veracode-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/veracode-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/veracode/authentication/veracode-authentication.yml
  title: ''
  type: Authentication
  url: authentication/veracode-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/veracode
- group: company
  title: ''
  type: Website
  url: https://www.veracode.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.veracode.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.veracode.com/r/REST_APIs_Quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://docs.veracode.com/r/c_enabling_hmac
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/veracode
- group: other
  title: ''
  type: OpenSourceSite
  url: https://veracode.github.io/
- group: company
  title: ''
  type: Blog
  url: https://www.veracode.com/blog
- group: operate
  title: ''
  type: Support
  url: https://community.veracode.com/
- group: other
  href: https://artifacts.apis.io/veracode/capabilities/veracode-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/veracode-capability-edges.yml
coverage:
  checked: '2026-10-03'
  detail: OpenAPI specifications require authentication, returning 401 Unauthorized.
  evidence:
  - status: 401
    url: https://api.veracode.com/openapi.json
  reason: sales-gate
  state: gated
created: '2025-01-08'
description: Veracode is an application security testing (AST) platform offering static analysis (SAST), dynamic analysis (DAST), software composition analysis (SCA), manual penetration testing, and developer security training. The Veracode Platform provides a comprehensive suite of REST APIs enabling organizations to automate security testing, access findings, manage policies, generate reports, and administer users and teams. All REST APIs use HMAC authentication with API ID/key credentials and return JSON responses following OpenAPI standards.
examples:
- key_count: 2
  name: Veracode Generate Report Example
  slug: veracode-generate-report-example
- key_count: 2
  name: Veracode List Applications Example
  slug: veracode-list-applications-example
- key_count: 2
  name: Veracode List Findings Example
  slug: veracode-list-findings-example
finops:
- has_sources: true
  method: generated
  name: Veracode Finops
  primary_unit: ''
  service_category: Application Security
  slug: veracode-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/veracode.png
json_schemas:
- name: ApplicationProfile
  property_count: 1
  slug: veracode-application-profile
- name: Application
  property_count: 6
  slug: veracode-application
- name: ApplicationsPage
  property_count: 2
  slug: veracode-applications-page
- name: BusinessUnitProfile
  property_count: 1
  slug: veracode-business-unit-profile
- name: BusinessUnit
  property_count: 3
  slug: veracode-business-unit
- name: BusinessUnitsPage
  property_count: 2
  slug: veracode-business-units-page
- name: DynamicFlawInfo
  property_count: 3
  slug: veracode-dynamic-flaw-info
- name: Veracode Security Finding
  property_count: 8
  slug: veracode-finding
- name: FindingsPage
  property_count: 2
  slug: veracode-findings-page
- name: MptScansPage
  property_count: 2
  slug: veracode-mpt-scans-page
- name: PolicyCompliance
  property_count: 5
  slug: veracode-policy-compliance
- name: ReportInitiated
  property_count: 3
  slug: veracode-report-initiated
- name: ReportRequest
  property_count: 9
  slug: veracode-report-request
- name: ReportResults
  property_count: 4
  slug: veracode-report-results
- name: RolesPage
  property_count: 2
  slug: veracode-roles-page
- name: SandboxProfile
  property_count: 3
  slug: veracode-sandbox-profile
- name: Sandbox
  property_count: 6
  slug: veracode-sandbox
- name: SandboxesPage
  property_count: 2
  slug: veracode-sandboxes-page
- name: StaticFlawInfo
  property_count: 1
  slug: veracode-static-flaw-info
- name: TeamProfile
  property_count: 2
  slug: veracode-team-profile
- name: Team
  property_count: 5
  slug: veracode-team
- name: TeamsPage
  property_count: 2
  slug: veracode-teams-page
- name: UserProfile
  property_count: 6
  slug: veracode-user-profile
- name: User
  property_count: 11
  slug: veracode-user
- name: UsersPage
  property_count: 2
  slug: veracode-users-page
json_structures:
- name: Veracode Finding Structure
  property_count: 0
  slug: veracode-finding-structure
jsonld:
- class_count: 28
  name: Veracode Context
  property_count: 4
  slug: veracode-context
layout: provider
modified: '2026-05-19'
name: Veracode
nav: Providers
network: true
overview: 'Veracode publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Credentials API, Applications API, Business Units API, and 9 more. Tagged areas include Application Security, SAST, DAST, Software Composition Analysis, and Security Testing.


  The Veracode catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Veracode''s developer surface includes sandbox, authentication, documentation, getting-started guide, engineering blog, support, and 37 more developer resources.'
plans:
- name: Veracode Plans Pricing
  plan_count: 1
  slug: veracode-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Veracode Rate Limits
  slug: veracode-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Veracode — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: veracode-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Veracode API Rules
  rule_count: 11
  severity_counts:
    error: 5
    hint: 1
    info: 0
    warn: 5
  slug: veracode-rules
score:
  band: developing
  composite: 50.6
  coverage:
    artifact_dirs: 34
    catalog_earned: 70.0
    catalog_earned_first_party: 0.0
    catalog_gap: 45.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 28.9
    contract_governance: 31.8
    contract_quality: 67.7
    developer_ergonomics: 61.3
    discoverability: 80.4
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 57.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/veracode/veracode-2026-06-20T200920.png
security:
- kind: authentication
  name: Veracode Authentication
  slug: veracode-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Veracode Domain Security
  slug: veracode-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Veracode Vulnerability Disclosure
  slug: veracode-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Veracode Trust Center
  slug: veracode-trust-center
  summary_line: SOC 2, FedRAMP, GDPR
skill_count: 3
skills:
- name: veracode-list-and-create-business-units
  slug: veracode-list-and-create-business-units
- name: veracode-manage-team
  slug: veracode-manage-team
- name: veracode-reports-generate-and-fetch
  slug: veracode-reports-generate-and-fetch
slug: veracode
tags:
- Application Security
- SAST
- DAST
- Software Composition Analysis
- Security Testing
- DevSecOps
website: https://www.veracode.com/
---
