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
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Thatch Agentic Access
  operation_count: 19
  slug: thatch-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 1
apis:
- baseURL: https://partners.thatchcloud.com/api/partners/v1
  baseurl_source: declared
  description: Payroll deductions track the costs of plan premiums to employees.
  name: Thatch Deductions API
  slug: thatch-deductions-api
- baseURL: https://partners.thatchcloud.com/api/partners/v1
  baseurl_source: declared
  description: Employees work for employers, both of which are managed by partners. Employees enrolled in plans are also represented in Thatch as member objects.
  name: Thatch Employees API
  slug: thatch-employees-api
- baseURL: https://partners.thatchcloud.com/api/partners/v1
  baseurl_source: declared
  description: Employers onboard into a platform through employer onboarding sessions. After creating a session, provide the claim_url to the onboarding iframe in your app.
  name: Thatch Employer onboarding sessions API
  slug: thatch-employer-onboarding-sessions-api
- baseURL: https://partners.thatchcloud.com/api/partners/v1
  baseurl_source: declared
  description: Platforms onboard employers into Thatch, and have employees enrolled in plans.
  name: Thatch Employers API
  slug: thatch-employers-api
- baseURL: https://partners.thatchcloud.com/api/partners/v1
  baseurl_source: declared
  description: Enrollments use member objects to track employee coverage status.
  name: Thatch Enrollments API
  slug: thatch-enrollments-api
- baseURL: https://partners.thatchcloud.com/api/partners/v1
  baseurl_source: declared
  description: Members represent employees enrolled in plans.
  name: Thatch Members API
  slug: thatch-members-api
- baseURL: https://partners.thatchcloud.com/api/partners/v1
  baseurl_source: declared
  description: Pay schedules model the cadence of employee paychecks for the purpose of deduction calculations.
  name: Thatch Pay Schedules API
  slug: thatch-pay-schedules-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Thatch for Platforms Deductions API
  slug: open-thatch-deductions-api
- collection_type: open
  name: Thatch for Platforms Deductions Employees API
  slug: open-thatch-employees-api
- collection_type: open
  name: Thatch for Platforms Deductions Employer onboarding sessions API
  slug: open-thatch-employer-onboarding-sessions-api
- collection_type: open
  name: Thatch for Platforms Deductions Employers API
  slug: open-thatch-employers-api
- collection_type: open
  name: Thatch for Platforms Deductions Enrollments API
  slug: open-thatch-enrollments-api
- collection_type: open
  name: Thatch for Platforms Deductions Members API
  slug: open-thatch-members-api
- collection_type: open
  name: Thatch for Platforms Deductions Pay Schedules API
  slug: open-thatch-pay-schedules-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/thatch-capability-edges.yml
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
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/thatch-partners-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/thatch-partners-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thatch-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/thatch-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/thatch-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/thatch-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/thatch-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.thatch.com
- group: design
  title: ''
  type: Conformance
  url: conformance/thatch-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.thatch.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/thatch-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thatch-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thatch-agentic-access.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/thatch-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/thatch-onboard-employer.md
- group: design
  title: ''
  type: Components
  url: components/thatch-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thatch-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thatch-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://thatch.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://thatch.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thatch.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thatch.com/privacy
- group: company
  title: ''
  type: Website
  url: https://thatch.com
created: '2026-07-17'
description: 'Thatch is a health benefits company that helps businesses offer personalized health insurance through an ICHRA (Individual Coverage Health Reimbursement Arrangement) plus a Thatch Visa spend card. Its developer product, Thatch for Platforms, is a set of REST APIs and embeddable JavaScript components that let partners (payroll, HR, and SMB platforms) bring ICHRA benefits into their own applications: create employers, manage employees, run a hosted employer onboarding flow, track enrollments and members, model pay schedules, and pull monthly payroll deductions. The API is partner-gated, authenticates with a Bearer API key, and is documented at docs.thatch.com. Thatch is backed by a16z, General Catalyst, GV, Index Ventures, and Lux Capital.'
image: https://thatch.com/opengraph/thatch-main.png
layout: provider
modified: '2026-07-21'
name: Thatch
nav: Providers
network: true
overview: 'Thatch publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Deductions API, Employees API, Employer onboarding sessions API, and 4 more. Tagged areas include Health Insurance, Health Benefits, ICHRA, Employee Benefits, and Payroll.


  Thatch''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, pricing, and 22 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 46.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 54.8
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 46.9
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
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thatch/refs/heads/main/screenshots/thatch-2026-08-17T082332.png
security:
- kind: authentication
  name: Thatch Authentication
  slug: thatch-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Thatch Domain Security
  slug: thatch-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Thatch Trust Center
  slug: thatch-trust-center
  summary_line: SOC 2
slug: thatch
tags:
- Health Insurance
- Health Benefits
- ICHRA
- Employee Benefits
- Payroll
- Insurance
- Fintech
- Embedded Finance
- Company
website: https://thatch.com
---
