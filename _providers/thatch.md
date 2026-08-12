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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Thatch Agentic Access
  operation_count: 19
  slug: thatch-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 7
apis:
- description: Payroll deductions track the costs of plan premiums to employees.
  name: Thatch Deductions API
  slug: thatch-deductions-api
- description: Employees work for employers, both of which are managed by partners. Employees enrolled in plans are also represented in Thatch as member objects.
  name: Thatch Employees API
  slug: thatch-employees-api
- description: Employers onboard into a platform through employer onboarding sessions. After creating a session, provide the claim_url to the onboarding iframe in your app.
  name: Thatch Employer onboarding sessions API
  slug: thatch-employer-onboarding-sessions-api
- description: Platforms onboard employers into Thatch, and have employees enrolled in plans.
  name: Thatch Employers API
  slug: thatch-employers-api
- description: Enrollments use member objects to track employee coverage status.
  name: Thatch Enrollments API
  slug: thatch-enrollments-api
- description: Members represent employees enrolled in plans.
  name: Thatch Members API
  slug: thatch-members-api
- description: Pay schedules model the cadence of employee paychecks for the purpose of deduction calculations.
  name: Thatch Pay Schedules API
  slug: thatch-pay-schedules-api
artifact_total: 12
common:
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
  type: MCPServer
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
mcp_servers:
- description: ''
  name: thatch-mcp.yml
  slug: thatch-mcpyml
modified: '2026-07-21'
name: Thatch
nav: Providers
network: true
overview: 'Thatch publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Deductions API, Employees API, Employer onboarding sessions API, and 4 more. Tagged areas include Health Insurance, Health Benefits, ICHRA, Employee Benefits, and Payroll.


  Thatch''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, pricing, and 21 more developer resources.'
random_paper: 56
score:
  band: developing
  composite: 46.0
  delta: -1.4
  facets:
    commercial_clarity: 47.4
    contract_quality: 58.8
    developer_ergonomics: 51.6
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 47.4
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
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
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
