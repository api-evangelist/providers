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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.5
  scored_at: '2026-09-24'
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
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/thatch-health/refs/heads/main/openapi/_original/thatch-health-partners-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/thatch-health-partners-openapi.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thatch-health/refs/heads/main/errors/thatch-health-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/thatch-health-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thatch-health/refs/heads/main/agentic-access/thatch-health-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/thatch-health-agentic-access.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thatch-health/refs/heads/main/capabilities/thatch-health-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/thatch-health-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thatch-health/refs/heads/main/overlays/thatch-health-platforms-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thatch-health-platforms-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thatch-health/refs/heads/main/security/thatch-health-trust-center.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/thatch-health/refs/heads/main/lifecycle/thatch-health-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/thatch-health-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thatch-health/refs/heads/main/authentication/thatch-health-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thatch-health-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thatch-health/refs/heads/main/conventions/thatch-health-conventions.yml
  title: ''
  type: Conventions
  url: conventions/thatch-health-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thatch-health/refs/heads/main/conformance/thatch-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thatch-health-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/thatch-health/refs/heads/main/packages/thatch-health-packages.yml
  title: ''
  type: Packages
  url: packages/thatch-health-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thatch-health/refs/heads/main/well-known/thatch-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/thatch-health-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thatch-health/refs/heads/main/mcp/thatch-health-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/thatch-health-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thatch-health/refs/heads/main/llms/thatch-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thatch-health-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thatch-health/refs/heads/main/components/thatch-health-components.yml
  title: ''
  type: Components
  url: components/thatch-health-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/thatch-health/refs/heads/main/sandbox/thatch-health-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/thatch-health-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thatch-health/refs/heads/main/data-model/thatch-health-data-model.yml
  title: ''
  type: DataModel
  url: data-model/thatch-health-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thatch-health/refs/heads/main/security/thatch-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thatch-health-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thatch-health/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Thatch (Thatch Health, Inc.) is a modern health benefits platform that makes it easy for employers to offer personalized healthcare to employees using an ICHRA (Individual Coverage Health Reimbursement Arrangement). Thatch for Platforms is a set of REST APIs and embeddable components that let partner platforms — payroll, HR, and benefits products — bring ICHRA benefits to their customers, covering employer onboarding, employee management, enrollments, members, pay schedules, and payroll deductions.
image: https://docs.thatch.com/img/thatch.svg
layout: provider
modified: '2026-07-21'
name: Thatch Health
nav: Providers
network: true
overview: 'Thatch Health publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Deductions API, Employees API, Employer onboarding sessions API, and 4 more. Tagged areas include Company, Healthcare, Health Benefits, ICHRA, and Insurance.


  Thatch Health''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
random_paper: 13
score:
  band: developing
  composite: 52.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 56.9
    developer_ergonomics: 66.1
    discoverability: 75.9
    operational_transparency: 18.4
  previous_composite: 52.2
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
    score: 37.5
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/thatch-health/refs/heads/main/screenshots/thatch-health-2026-08-17T082333.png
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
