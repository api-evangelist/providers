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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 58.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Usersnap Agentic Access
  operation_count: 8
  slug: usersnap-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 4
apis:
- description: Feedback related endpoints
  name: Usersnap feedback API
  slug: usersnap-feedback-api
- description: Available options for submission
  name: Usersnap pre_submit API
  slug: usersnap-pre-submit-api
- description: Project related endpoints
  name: Usersnap project API
  slug: usersnap-project-api
- description: Submit feedback
  name: Usersnap submit API
  slug: usersnap-submit-api
artifact_total: 16
asyncapis:
- description: ''
  name: Usersnap Webhooks
  slug: usersnap-webhooks
collections:
- collection_type: postman
  name: Usersnap feedback API
  slug: postman-usersnap-feedback-api
- collection_type: postman
  name: Usersnap feedback pre_submit API
  slug: postman-usersnap-pre-submit-api
- collection_type: postman
  name: Usersnap feedback project API
  slug: postman-usersnap-project-api
- collection_type: postman
  name: Usersnap feedback submit API
  slug: postman-usersnap-submit-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/usersnap/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/usersnap-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/usersnap-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usersnap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usersnap.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.usersnap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.usersnap.com/docs/getting-started-with-usersnap
- group: docs
  title: ''
  type: APIReference
  url: https://help.usersnap.com/reference/rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://help.usersnap.com/docs/getting-started-with-usersnap
- group: operate
  title: ''
  type: Support
  url: https://usersnap.com/contact
- group: company
  title: ''
  type: Blog
  url: https://usersnap.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://usersnap.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.usersnap.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usersnap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usersnap.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usersnap.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://usersnap.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.usersnap.com/
- group: auth
  title: ''
  type: Security
  url: https://usersnap.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/usersnap-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://usersnap.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://portal.usersnap.com/changelog/2bdcb520-7c12-4691-b9fe-94784b8bd8d6
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/usersnap-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/usersnap-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/usersnap-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/usersnap-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/usersnap-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/usersnap-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/usersnap-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/usersnap-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/usersnap-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/usersnap-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/usersnap-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/usersnap-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/usersnap-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/usersnap-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/usersnap-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Usersnap is a user feedback platform from Perg/Linz, Austria that lets product, development, customer success, and marketing teams capture, organize, and act on user feedback with embeddable widgets for screenshots, screen recordings, ratings, and surveys. Beyond the widgets, Usersnap ships a plan-gated platform REST API (JWT bearer auth) for submitting and querying feedback, HMAC-signed webhooks, an official npm browser package, and a hosted MCP server (mcp.usersnap.com) secured with OAuth 2.1 + PKCE so AI assistants can query feedback and create opportunities.
image: https://github.com/usersnap.png
layout: provider
mcp_servers:
- description: ''
  name: usersnap-mcp.yml
  slug: usersnap-mcpyml
modified: '2026-07-21'
name: Usersnap
nav: Providers
network: true
overview: 'Usersnap publishes 4 APIs on the [APIs.io](https://apis.io/) network, including feedback API, pre_submit API, project API, and 1 more. Tagged areas include Company, Feedback, Bug Tracking, Customer Experience, and Product Management.


  The Usersnap catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Usersnap''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
random_paper: 71
scopes:
- name: Usersnap Scopes
  scope_count: 2
  slug: usersnap-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 62.0
  delta: 0.7
  facets:
    commercial_clarity: 60.5
    contract_quality: 69.7
    developer_ergonomics: 73.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 61.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Usersnap Authentication
  slug: usersnap-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Usersnap Domain Security
  slug: usersnap-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Usersnap Vulnerability Disclosure
  slug: usersnap-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Usersnap Trust Center
  slug: usersnap-trust-center
  summary_line: trust center published
slug: usersnap
tags:
- Company
- Feedback
- Bug Tracking
- Customer Experience
- Product Management
- Surveys
- SaaS
website: https://usersnap.com
---
