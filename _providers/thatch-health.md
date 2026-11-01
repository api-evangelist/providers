---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Thatch Health Agentic Access
  operation_count: 19
  slug: thatch-health-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 2
apis:
- baseURL: https://partners.thatchcloud.com/api/partners/v1
  baseurl_source: declared
  description: Payroll deductions track the costs of plan premiums to employees.
  name: Thatch Health Deductions API
  slug: thatch-health-deductions-api
- baseURL: https://partners.thatchcloud.com/api/partners/v1
  baseurl_source: declared
  description: Employees work for employers, both of which are managed by partners. Employees enrolled in plans are also represented in Thatch as member objects.
  name: Thatch Health Employees API
  slug: thatch-health-employees-api
- baseURL: https://partners.thatchcloud.com/api/partners/v1
  baseurl_source: declared
  description: Employers onboard into a platform through employer onboarding sessions. After creating a session, provide the `claim_url` to the onboarding iframe in your app.
  name: Thatch Health Employer onboarding sessions API
  slug: thatch-health-employer-onboarding-sessions-api
- baseURL: https://partners.thatchcloud.com/api/partners/v1
  baseurl_source: declared
  description: Platforms onboard employers into Thatch, and have employees enrolled in plans.
  name: Thatch Health Employers API
  slug: thatch-health-employers-api
- baseURL: https://partners.thatchcloud.com/api/partners/v1
  baseurl_source: declared
  description: Enrollments use member objects to track employee coverage status.
  name: Thatch Health Enrollments API
  slug: thatch-health-enrollments-api
- baseURL: https://partners.thatchcloud.com/api/partners/v1
  baseurl_source: declared
  description: Members represent employees enrolled in plans. Thatch creates member objects automatically, but you can retrieve them (for example, to aid in supporting an enrolled employee.
  name: Thatch Health Members API
  slug: thatch-health-members-api
- baseURL: https://partners.thatchcloud.com/api/partners/v1
  baseurl_source: declared
  description: Pay schedules model the cadence of employee paychecks for the purpose of deduction calculations.
  name: Thatch Health Pay Schedules API
  slug: thatch-health-pay-schedules-api
artifact_total: 24
collections:
- collection_type: open
  name: Thatch for Platforms Deductions API
  slug: open-thatch-health-deductions-api
- collection_type: open
  name: Thatch for Platforms Deductions Employees API
  slug: open-thatch-health-employees-api
- collection_type: open
  name: Thatch for Platforms Deductions Employer onboarding sessions API
  slug: open-thatch-health-employer-onboarding-sessions-api
- collection_type: open
  name: Thatch for Platforms Deductions Employers API
  slug: open-thatch-health-employers-api
- collection_type: open
  name: Thatch for Platforms Deductions Enrollments API
  slug: open-thatch-health-enrollments-api
- collection_type: open
  name: Thatch for Platforms Deductions Members API
  slug: open-thatch-health-members-api
- collection_type: open
  name: Thatch for Platforms Deductions Pay Schedules API
  slug: open-thatch-health-pay-schedules-api
common:
- group: commercial
  href: https://artifacts.apis.io/thatch-health/plans/thatch-health-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/thatch-health-plans-pricing.yml
- group: docs
  href: https://artifacts.apis.io/thatch-health/openapi/_original/thatch-health-partners-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/thatch-health-partners-openapi.yml
- group: design
  href: https://artifacts.apis.io/thatch-health/errors/thatch-health-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/thatch-health-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/thatch-health/agentic-access/thatch-health-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/thatch-health-agentic-access.yml
- group: other
  href: https://artifacts.apis.io/thatch-health/capabilities/thatch-health-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/thatch-health-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/thatch-health/overlays/thatch-health-platforms-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thatch-health-platforms-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/thatch-health/security/thatch-health-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/thatch-health-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://thatch.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.thatch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thatch.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.thatch.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.thatch.com/
- group: operate
  title: ''
  type: Support
  url: https://support.thatch.com/
- group: company
  title: ''
  type: Blog
  url: https://thatch.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://thatch.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.thatch.com/employers/onboarding/welcome/get-started
- group: start
  title: ''
  type: Login
  url: https://app.thatch.com/magic_link/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thatch.com/legal/platform-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thatch.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thatch-health
- group: operate
  title: ''
  type: StatusPage
  url: https://status.thatch.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.thatch.com/
- group: design
  href: https://artifacts.apis.io/thatch-health/lifecycle/thatch-health-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/thatch-health-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/thatch-health/authentication/thatch-health-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thatch-health-authentication.yml
- group: design
  href: https://artifacts.apis.io/thatch-health/conventions/thatch-health-conventions.yml
  title: ''
  type: Conventions
  url: conventions/thatch-health-conventions.yml
- group: design
  href: https://artifacts.apis.io/thatch-health/conformance/thatch-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thatch-health-conformance.yml
- group: build
  href: https://artifacts.apis.io/thatch-health/packages/thatch-health-packages.yml
  title: ''
  type: Packages
  url: packages/thatch-health-packages.yml
- group: agent
  href: https://artifacts.apis.io/thatch-health/well-known/thatch-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/thatch-health-well-known.yml
- group: agent
  href: https://artifacts.apis.io/thatch-health/mcp/thatch-health-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/thatch-health-mcp.yml
- group: agent
  href: https://artifacts.apis.io/thatch-health/llms/thatch-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thatch-health-llms.txt
- group: design
  href: https://artifacts.apis.io/thatch-health/components/thatch-health-components.yml
  title: ''
  type: Components
  url: components/thatch-health-components.yml
- group: start
  href: https://artifacts.apis.io/thatch-health/sandbox/thatch-health-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/thatch-health-sandbox.yml
- group: design
  href: https://artifacts.apis.io/thatch-health/data-model/thatch-health-data-model.yml
  title: ''
  type: DataModel
  url: data-model/thatch-health-data-model.yml
- group: auth
  href: https://artifacts.apis.io/thatch-health/security/thatch-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thatch-health-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/thatch-health/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Thatch (Thatch Health, Inc.) is a modern health benefits platform that makes it easy for employers to offer personalized healthcare to employees using an ICHRA (Individual Coverage Health Reimbursement Arrangement). Thatch for Platforms is a set of REST APIs and embeddable components that let partner platforms — payroll, HR, and benefits products — bring ICHRA benefits to their customers, covering employer onboarding, employee management, enrollments, members, pay schedules, and payroll deductions.
finops:
- has_sources: true
  method: derived
  name: Thatch Health Finops
  primary_unit: 'company (example: $45 × 4 employees + $50 compliance fee)'
  service_category: ''
  slug: thatch-health-finops
  template: false
image: https://docs.thatch.com/img/thatch.svg
layout: provider
modified: '2026-07-21'
name: Thatch Health
nav: Providers
network: true
overview: 'Thatch Health publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Deductions API, Employees API, Employer onboarding sessions API, and 4 more. Tagged areas include Company, Healthcare, Health Benefits, ICHRA, and Insurance.


  Thatch Health''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Thatch Health Plans Pricing
  plan_count: 2
  slug: thatch-health-plans-pricing
- name: Thatch Health Price Estimates
  plan_count: 0
  slug: thatch-health-price-estimates
random_paper: 15
score:
  band: strong
  composite: 55.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.8
  facets:
    access_clarity: 89.5
    contract_governance: 4.5
    contract_quality: 51.2
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/thatch-health/thatch-health-2026-08-17T082333.png
security:
- kind: authentication
  name: Thatch Health Authentication
  slug: thatch-health-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Thatch Health Domain Security
  slug: thatch-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Thatch Health Trust Center
  slug: thatch-health-trust-center
  summary_line: SOC 2
skill_count: 3
skills:
- name: Manage employees and dependents
  slug: thatch-health-manage-employees
- name: Onboard an employer into ICHRA benefits
  slug: thatch-health-onboard-employer
- name: Sync payroll deductions and pay schedules
  slug: thatch-health-payroll-deductions
slug: thatch-health
tags:
- Company
- Healthcare
- Health Benefits
- ICHRA
- Insurance
- Payroll
- Embedded Benefits
- Human Resources
website: https://thatch.com/
---
