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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Nayya Agentic Access
  operation_count: 35
  slug: nayya-agentic-access
  summary_line: 35 operations · 21 acting
api_count: 11
apis:
- description: The Benefits API from Nayya — 4 operation(s) for benefits.
  name: Nayya Benefits API
  slug: nayya-benefits-api
- description: The Carriers API from Nayya — 1 operation(s) for carriers.
  name: Nayya Carriers API
  slug: nayya-carriers-api
- description: The Connections API from Nayya — 2 operation(s) for connections.
  name: Nayya Connections API
  slug: nayya-connections-api
- description: The Dependents API from Nayya — 2 operation(s) for dependents.
  name: Nayya Dependents API
  slug: nayya-dependents-api
- description: The Employees API from Nayya — 2 operation(s) for employees.
  name: Nayya Employees API
  slug: nayya-employees-api
- description: The Employers API from Nayya — 3 operation(s) for employers.
  name: Nayya Employers API
  slug: nayya-employers-api
- description: The Enrollments API from Nayya — 2 operation(s) for enrollments.
  name: Nayya Enrollments API
  slug: nayya-enrollments-api
- description: The Recommendations API from Nayya — 1 operation(s) for recommendations.
  name: Nayya Recommendations API
  slug: nayya-recommendations-api
- description: The Rule Templates API from Nayya — 1 operation(s) for rule templates.
  name: Nayya Rule Templates API
  slug: nayya-rule-templates-api
- description: The Snapshots API from Nayya — 1 operation(s) for snapshots.
  name: Nayya Snapshots API
  slug: nayya-snapshots-api
- description: The Token API from Nayya — 1 operation(s) for token.
  name: Nayya Token API
  slug: nayya-token-api
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://nayya.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nayya.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nayya.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nayya.com/reference/create-employer
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nayya.com/docs/getting-started-with-choose
- group: operate
  title: ''
  type: Support
  url: https://support.nayya.com/
- group: company
  title: ''
  type: Blog
  url: https://www.nayya.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nayya.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.nayya.com/end-user-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nayya.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://trust.nayya.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/nayya-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nayya-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nayya-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.nayya.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/nayya-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nayya-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nayya-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nayya-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nayya-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nayya-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nayya-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/nayya-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nayya-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nayya-llms.txt
created: '2026-07-17'
description: Nayya is an AI-powered health and wealth benefits decision-support platform used by employers, brokers, carriers, and benefits-administration partners to help employees choose and use their benefits. Its "Choose" experience delivers personalized plan recommendations, and its agentic adviser can answer benefits questions and file supplemental-health claims on an employee's behalf. Nayya exposes a partner-facing REST API — Nayya Integrate — with three surfaces (Accounts, Benefits, and Choose) that let integrators map employers, employees, and dependents, configure benefits, snapshot an employee's context, retrieve recommendations, and record enrollments, plus an embedded UI that partners drop into their own enrollment flow via SSO.
image: https://logo.clearbit.com/nayya.com
layout: provider
mcp_servers:
- description: ''
  name: nayya-mcp.yml
  slug: nayya-mcpyml
modified: '2026-07-20'
name: Nayya
nav: Providers
network: true
overview: 'Nayya publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Benefits API, Carriers API, Connections API, and 8 more. Tagged areas include Company, Employee Benefits, Insurance, Insurtech, and Health.


  Nayya''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 20 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 47.8
  delta: -4.3
  facets:
    commercial_clarity: 36.8
    contract_quality: 51.5
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 26.3
  previous_composite: 52.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 54.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Nayya Authentication
  slug: nayya-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nayya Domain Security
  slug: nayya-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nayya Vulnerability Disclosure
  slug: nayya-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Nayya Trust Center
  slug: nayya-trust-center
  summary_line: SOC 2, HIPAA
slug: nayya
tags:
- Company
- Employee Benefits
- Insurance
- Insurtech
- Health
- Decision Support
- HR Tech
- Enrollment
- Recommendations
- Artificial Intelligence
website: https://nayya.com
---
