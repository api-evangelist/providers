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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Apptentive Agentic Access
  operation_count: 36
  slug: apptentive-agentic-access
  summary_line: 36 operations · 1 acting
api_count: 4
apis:
- description: experimental data endpoints
  name: Apptentive experimental API
  slug: apptentive-experimental-api
- description: info endpoints
  name: Apptentive info API
  slug: apptentive-info-api
- description: metrics data endpoints
  name: Apptentive metrics API
  slug: apptentive-metrics-api
- description: raw data endpoints
  name: Apptentive raw API
  slug: apptentive-raw-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apptentive-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apptentive-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apptentive-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/apptentive-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/apptentive-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/apptentive-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apptentive-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/apptentive-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/apptentive-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.alchemer.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/apptentive-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apptentive-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.apptentive.com
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://help.alchemer.com/help/alchemer-digital-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apptentive
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alchemer.com/apptentive-master-service-agreement/
- group: operate
  title: ''
  type: Support
  url: https://help.alchemer.com/
- group: company
  title: ''
  type: Blog
  url: https://www.alchemer.com/resources/blog/
- group: company
  title: ''
  type: Website
  url: http://apptentive.com
created: '2026-07-17'
description: Apptentive, now Alchemer Mobile / Alchemer Digital, is a mobile customer engagement and in-app feedback platform used to run surveys, message prompts (Notes), ratings/review prompts, and Fan Signals inside iOS, Android, React Native, and web apps. Its public Data API at data.apptentive.com gives customers read-only export and analytics access to app metrics (active users, retention, Love Percent, Net Fan Score, ratings, reviews), survey and note reporting, and raw people, device, conversation, and message records, plus a GDPR/CCPA data-request endpoint. Authentication is an X-API-KEY header issued and scoped from the Alchemer Digital dashboard; the service is SOC 2 Type 2 and ISO 27001 certified.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apptentive.png
layout: provider
mcp_servers:
- description: ''
  name: apptentive-mcp.yml
  slug: apptentive-mcpyml
modified: '2026-07-18'
name: Apptentive
nav: Providers
network: true
overview: 'Apptentive publishes 4 APIs on the [APIs.io](https://apis.io/) network, including experimental API, info API, metrics API, and 1 more. Tagged areas include Company, Enterprise, Mobile, Customer Feedback, and Surveys.


  Apptentive''s developer surface includes authentication, documentation, support, engineering blog, and 16 more developer resources.'
random_paper: 43
rate_limits:
- limit_count: 1
  name: Apptentive Rate Limits
  slug: apptentive-rate-limits
score:
  band: thin
  composite: 37.8
  delta: 2.7
  facets:
    commercial_clarity: 26.3
    contract_quality: 32.3
    developer_ergonomics: 36.4
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 42.1
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apptentive/refs/heads/main/screenshots/apptentive-2026-07-25T200848.png
security:
- kind: authentication
  name: Apptentive Authentication
  slug: apptentive-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apptentive Domain Security
  slug: apptentive-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Apptentive Trust Center
  slug: apptentive-trust-center
  summary_line: AICPA SOC 2 Type 2, ISO 27001, GDPR, CCPA, HIPAA, FERPA
slug: apptentive
tags:
- Company
- Enterprise
- Mobile
- Customer Feedback
- Surveys
- Analytics
- Customer Engagement
- Voice of Customer
website: http://apptentive.com
---
