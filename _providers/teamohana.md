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
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Teamohana Agentic Access
  operation_count: 14
  slug: teamohana-agentic-access
  summary_line: 14 operations · 5 acting
api_count: 4
apis:
- description: The Discovery API from TeamOhana — 3 operation(s) for discovery.
  name: TeamOhana Discovery API
  slug: teamohana-discovery-api
- description: The Headcount API from TeamOhana — 2 operation(s) for headcount.
  name: TeamOhana Headcount API
  slug: teamohana-headcount-api
- description: The Scenario API from TeamOhana — 2 operation(s) for scenario.
  name: TeamOhana Scenario API
  slug: teamohana-scenario-api
- description: The SCIM API from TeamOhana — 3 operation(s) for scim.
  name: TeamOhana SCIM API
  slug: teamohana-scim-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TeamOhana Public Discovery API
  slug: open-teamohana-discovery-api
- collection_type: open
  name: TeamOhana Public Discovery Headcount API
  slug: open-teamohana-headcount-api
- collection_type: open
  name: TeamOhana Public Discovery Scenario API
  slug: open-teamohana-scenario-api
- collection_type: open
  name: TeamOhana Public Discovery SCIM API
  slug: open-teamohana-scim-api
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/teamohana-openapi-original.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/teamohana-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/teamohana-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/teamohana-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/teamohana-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/teamohana-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/teamohana-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/teamohana-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.teamohana.us/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/teamohana-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/teamohana-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/teamohana-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/teamohana-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://api.teamohana.us/faq/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://api.teamohana.us/faq/index.html
- group: auth
  title: ''
  type: TrustCenter
  url: security/teamohana-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.teamohana.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teamohana-domain-security.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.teamohana.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.teamohana.com/blogs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.teamohana.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.teamohana.com/terms-and-conditions
- group: start
  title: ''
  type: SignUp
  url: https://www.teamohana.com/book-demo
- group: operate
  title: ''
  type: Support
  url: https://www.teamohana.com/contact-us
- group: company
  title: ''
  type: Website
  url: https://teamohana.com/
created: '2026-07-17'
description: TeamOhana is an HR-technology company that provides a headcount management and planning platform serving as a single source of truth for a company's people budget. It connects Finance, HR, and Talent Acquisition teams around real-time, approved headcount so organizations can plan, track, and control hiring against budget in one collaborative workflow rather than across disconnected spreadsheets. The platform integrates with HRIS, ATS, and financial planning systems (Workday, SAP SuccessFactors, Bamboo HR, HiBob, UKG, Personio, Namely, Greenhouse-class ATS, and Pigment). Its Public API exposes SCIM 2.0 user provisioning plus Headcount, Discovery, and Scenario endpoints for planning and reporting. TeamOhana is backed by Sierra Ventures and runs a security program that is SOC 2 and ISO 27001 certified (verified via its public trust center).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teamohana.png
layout: provider
mcp_servers:
- description: ''
  name: teamohana-mcp.yml
  slug: teamohana-mcpyml
modified: '2026-07-21'
name: TeamOhana
nav: Providers
network: true
overview: 'TeamOhana publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Headcount API, Scenario API, and 1 more. Tagged areas include Company, Hr Tech, Headcount Management, Headcount Planning, and Workforce Planning.


  TeamOhana''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, signup flow, support, and 19 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 1
  name: Teamohana Rate Limits
  slug: teamohana-rate-limits
score:
  band: developing
  composite: 47.4
  delta: 0.7
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 16.7
    contract_quality: 51.5
    developer_ergonomics: 37.5
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 36.8
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/teamohana/refs/heads/main/screenshots/teamohana-2026-08-17T082257.png
security:
- kind: authentication
  name: Teamohana Authentication
  slug: teamohana-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Teamohana Domain Security
  slug: teamohana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Teamohana Trust Center
  slug: teamohana-trust-center
  summary_line: SOC 2, ISO 27001
slug: teamohana
tags:
- Company
- Hr Tech
- Headcount Management
- Headcount Planning
- Workforce Planning
- Human Resources
- Talent Acquisition
- Finance
- SCIM
- SaaS
website: https://teamohana.com/
---
