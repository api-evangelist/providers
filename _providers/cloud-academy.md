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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 36
  human_in_the_loop: 4
  name: Cloud Academy Agentic Access
  operation_count: 52
  slug: cloud-academy-agentic-access
  summary_line: 52 operations · 36 acting · 4 human-in-the-loop
api_count: 3
apis:
- description: The Learning Management System API from Cloud Academy — 9 operation(s) for learning management system.
  name: Cloud Academy Learning Management System API
  slug: cloud-academy-learning-management-system-api
- description: The Organizations API from Cloud Academy — 5 operation(s) for organizations.
  name: Cloud Academy Organizations API
  slug: cloud-academy-organizations-api
- description: The Reports API from Cloud Academy — 32 operation(s) for reports.
  name: Cloud Academy Reports API
  slug: cloud-academy-reports-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://cloudacademy.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.qa.com/restapi/docs/swagger/
- group: docs
  title: ''
  type: Documentation
  url: https://support.platform.qa.com/hc/en-us/articles/360040446031-Cloud-Academy-API
- group: docs
  title: ''
  type: APIReference
  url: https://platform.qa.com/restapi/docs/swagger/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.platform.qa.com/hc/en-us/articles/360040446031-Cloud-Academy-API
- group: operate
  title: ''
  type: Support
  url: https://support.platform.qa.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.qa.com/resources/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudacademy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.platform.qa.com
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/cloud-academy-lifecycle.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://platform.qa.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://platform.qa.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qa.com/legal-privacy/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qa.com/legal-privacy/privacy-notice/
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloud-academy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cloud-academy-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cloud-academy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cloud-academy-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloud-academy-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cloud-academy-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cloud-academy-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cloud-academy-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cloud-academy-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cloud-academy-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloud-academy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloud-academy-domain-security.yml
created: '2026-07-17'
description: Cloud Academy is a hands-on technology skills training platform, now operating as the QA Learning Platform (cloudacademy.com redirects to platform.qa.com). It combines self-paced course content with hands-on labs, learning paths, quizzes, and exams across cloud, security, and software disciplines. Its public REST API lets enterprise administrators integrate the platform with internal business systems — browsing the content catalog, managing organization teams and members, and generating asynchronous reports on learner activity, progress, and skills. Authentication is OAuth2 client-credentials and the public API is rate-limited to 100 requests per minute. Cloud Academy was surfaced as a 500 Global portfolio company and enriched into the API Evangelist network from its live Swagger definition.
image: https://assets.platform.qa.com/hanami/static/favicon-platform/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: cloud-academy-mcp.yml
  slug: cloud-academy-mcpyml
modified: '2026-07-18'
name: Cloud Academy
nav: Providers
network: true
overview: 'Cloud Academy publishes 3 APIs on the [APIs.io](https://apis.io/) network: Learning Management System API, Organizations API, and Reports API. Tagged areas include Company, Training, Education, Learning Management, and Cloud Computing.


  Cloud Academy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 40
rate_limits:
- limit_count: 0
  name: Cloud Academy Rate Limits
  slug: cloud-academy-rate-limits
scopes:
- name: Cloud Academy Scopes
  scope_count: 0
  slug: cloud-academy-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.6
  delta: -3.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 32.3
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloud-academy/refs/heads/main/screenshots/cloud-academy-2026-07-25T205650.png
security:
- kind: authentication
  name: Cloud Academy Authentication
  slug: cloud-academy-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cloud Academy Domain Security
  slug: cloud-academy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cloud-academy
tags:
- Company
- Training
- Education
- Learning Management
- Cloud Computing
- Skills
- Reporting
- eLearning
website: https://cloudacademy.com
---
