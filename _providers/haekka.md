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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Haekka Agentic Access
  operation_count: 8
  slug: haekka-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 1
apis:
- description: Per-employee training assignments and completion state.
  name: Haekka Employee Trainings API
  slug: haekka-employee-trainings-api
- description: Company employees enrolled in Haekka.
  name: Haekka Employees API
  slug: haekka-employees-api
- description: Training courses configured for the company.
  name: Haekka Trainings API
  slug: haekka-trainings-api
arazzos:
- description: List trainings and active employees, then assign a training and confirm the assignment.
  name: Assign a Haekka training to employees
  slug: haekka-assign-training
- description: Read an employee-training record and update its completion state, then confirm.
  name: Sync a Haekka employee-training completion
  slug: haekka-sync-completion
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Haekka Public Employee Trainings API
  slug: open-haekka-employee-trainings-api
- collection_type: open
  name: Haekka Public Employee Trainings Employees API
  slug: open-haekka-employees-api
- collection_type: open
  name: Haekka Public Employee Trainings API
  slug: open-haekka-trainings-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/haekka-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/haekka-public-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://haekka.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.haekka.com/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://www.haekka.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://www.haekka.com/documentation/haekka-public-api-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://www.haekka.com/documentation/installing-and-using-haekka
- group: operate
  title: ''
  type: Support
  url: https://www.haekka.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.haekka.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.haekka.com/pricing
- group: start
  title: ''
  type: Login
  url: https://dashboard.haekka.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.haekka.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.haekka.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/haekka
- group: operate
  title: ''
  type: StatusPage
  url: https://status.haekka.com/
- group: auth
  title: ''
  type: Security
  url: https://www.haekka.com/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/haekka-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/haekka-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/haekka-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/haekka-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/haekka-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/haekka-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/haekka-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/haekka-assign-training.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/haekka-sync-completion.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/haekka-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/haekka-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/haekka-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/haekka-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/haekka-trust-center.yml
created: '2026-07-17'
description: Haekka is a Slack-native microlearning and security-awareness training platform that delivers short, timely training inside Slack to improve knowledge, compliance, and team performance. Core products include Training, Streams (auto-drip microlearning), Workflows (event-triggered training assignment), Pulse Engagements (surveys, quizzes, announcements), and a Phishing simulator with a Gmail Chrome extension. Haekka's catalog maps to SOC 2, HIPAA, GDPR, and PCI training requirements and integrates with Slack, Google Workspace, and HRIS/LMS/IAM systems. Its Public REST API exposes employees, trainings, and employee-training completion records plus training assignment, secured with a bearer API key generated in account settings.
image: https://cdn.prod.website-files.com/63614de03f02a69460a3de25/63614e1362ff9e6729e56195_HKA--logo-color-white.svg
layout: provider
mcp_servers:
- description: ''
  name: Haekka MCP Server
  slug: haekka-mcp-server
modified: '2026-07-19'
name: Haekka
nav: Providers
network: true
overview: 'Haekka publishes 3 APIs on the [APIs.io](https://apis.io/) network: Employee Trainings API, Employees API, and Trainings API. Tagged areas include Company, Security Awareness Training, Compliance Training, Microlearning, and Slack.


  Haekka''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 24 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 4.5
    contract_quality: 14.3
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/haekka/refs/heads/main/screenshots/haekka-2026-07-25T220528.png
security:
- kind: authentication
  name: Haekka Authentication
  slug: haekka-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Haekka Domain Security
  slug: haekka-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Haekka Vulnerability Disclosure
  slug: haekka-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Haekka Trust Center
  slug: haekka-trust-center
  summary_line: trust center published
slug: haekka
tags:
- Company
- Security Awareness Training
- Compliance Training
- Microlearning
- Slack
- Phishing Simulation
- Employee Training
- HIPAA
- SOC 2
website: https://haekka.com/
---
