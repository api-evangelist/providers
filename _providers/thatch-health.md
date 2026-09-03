---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.8
  scored_at: '2026-09-03'
api_count: 1
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/thatch-health-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/thatch-health-platforms-overlay.yaml
- group: auth
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
  title: ''
  type: Lifecycle
  url: lifecycle/thatch-health-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thatch-health-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/thatch-health-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/thatch-health-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/thatch-health-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thatch-health-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/thatch-health-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thatch-health-llms.txt
- group: design
  title: ''
  type: Components
  url: components/thatch-health-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/thatch-health-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/thatch-health-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thatch-health-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Thatch (Thatch Health, Inc.) is a modern health benefits platform that makes it easy for employers to offer personalized healthcare to employees using an ICHRA (Individual Coverage Health Reimbursement Arrangement). Thatch for Platforms is a set of REST APIs and embeddable components that let partner platforms — payroll, HR, and benefits products — bring ICHRA benefits to their customers, covering employer onboarding, employee management, enrollments, members, pay schedules, and payroll deductions.
image: https://docs.thatch.com/img/thatch.svg
layout: provider
mcp_servers:
- description: ''
  name: Thatch Health MCP Server
  slug: thatch-health-mcp-server
modified: '2026-07-21'
name: Thatch Health
nav: Providers
network: true
overview: 'Thatch Health publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Deductions API, Employees API, Employer onboarding sessions API, and 4 more. Tagged areas include Company, Healthcare, Health Benefits, ICHRA, and Insurance.


  Thatch Health''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 51.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 52.3
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 51.7
  provenance:
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
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
- HR
website: https://thatch.com/
---
