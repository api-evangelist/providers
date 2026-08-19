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
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: The Behavioral Assessments API from The Predictive Index — 1 operation(s) for behavioral assessments.
  name: The Predictive Index Behavioral Assessments API
  slug: the-predictive-index-behavioral-assessments-api
- description: The Candidates API from The Predictive Index — 3 operation(s) for candidates.
  name: The Predictive Index Candidates API
  slug: the-predictive-index-candidates-api
- description: The Employees API from The Predictive Index — 2 operation(s) for employees.
  name: The Predictive Index Employees API
  slug: the-predictive-index-employees-api
- description: The Jobs API from The Predictive Index — 1 operation(s) for jobs.
  name: The Predictive Index Jobs API
  slug: the-predictive-index-jobs-api
artifact_total: 14
asyncapis:
- description: ''
  name: The Predictive Index Webhooks
  slug: the-predictive-index-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: The Predictive Index Integration Behavioral Assessments API
  slug: open-the-predictive-index-behavioral-assessments-api
- collection_type: open
  name: The Predictive Index Integration Behavioral Assessments Candidates API
  slug: open-the-predictive-index-candidates-api
- collection_type: open
  name: The Predictive Index Integration Behavioral Assessments Employees API
  slug: open-the-predictive-index-employees-api
- collection_type: open
  name: The Predictive Index Integration Behavioral Assessments Jobs API
  slug: open-the-predictive-index-jobs-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/the-predictive-index-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-predictive-index-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.predictiveindex.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.predictiveindex.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.predictiveindex.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.predictiveindex.com/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-predictive-index-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/the-predictive-index-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/the-predictive-index-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.predictiveindex.com
- group: auth
  title: ''
  type: Security
  url: https://www.predictiveindex.com/security/responsible-disclosure/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/the-predictive-index-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/the-predictive-index-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/the-predictive-index-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/the-predictive-index-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/predictiveindex
- group: company
  title: ''
  type: Blog
  url: https://www.predictiveindex.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.predictiveindex.com/company/contact-us/#support-case
- group: commercial
  title: ''
  type: Pricing
  url: https://www.predictiveindex.com/plans/
- group: start
  title: ''
  type: SignUp
  url: https://app.predictiveindex.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.predictiveindex.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.predictiveindex.com/privacy/
created: '2026-07-17'
description: The Predictive Index (PI) is a talent optimization platform that pairs 70+ years of behavioral science with software to help organizations hire, engage, and develop teams — behavioral and cognitive assessments, hiring and candidate screening, leadership development, employee engagement, and performance management. PI publishes a RESTful Integration API (on Azure API Management) that lets external systems such as ATS/HRIS platforms programmatically create candidates, send behavioral and cognitive assessments, retrieve jobs and results, and generate insight and coaching-guide reports — the same data that appears in the PI Portal software. Status-change notification webhooks push assessment completion events to listening systems. Backed by a $50M investment from General Catalyst.
image: https://media.predictiveindex.com/wp-content/uploads/2025/02/25165442/ThePredictiveIndex_Thumbnail-1.jpg
layout: provider
mcp_servers:
- description: ''
  name: the-predictive-index-mcp.yml
  slug: the-predictive-index-mcpyml
modified: '2026-07-21'
name: The Predictive Index
nav: Providers
network: true
overview: 'The Predictive Index publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Behavioral Assessments API, Candidates API, Employees API, and 1 more. Tagged areas include Company, Talent Optimization, HR, Human Resources, and Assessments.


  The The Predictive Index catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  The Predictive Index''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 16 more developer resources.'
random_paper: 81
score:
  band: developing
  composite: 46.0
  delta: -3.4
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 59.8
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 49.4
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-predictive-index/refs/heads/main/screenshots/the-predictive-index-2026-08-17T082339.png
security:
- kind: authentication
  name: The Predictive Index Authentication
  slug: the-predictive-index-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: The Predictive Index Domain Security
  slug: the-predictive-index-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: The Predictive Index Vulnerability Disclosure
  slug: the-predictive-index-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: the-predictive-index
tags:
- Company
- Talent Optimization
- HR
- Human Resources
- Assessments
- Behavioral Science
- Hiring
- Recruiting
- Employee Engagement
- Integration API
website: https://developers.predictiveindex.com/
---
