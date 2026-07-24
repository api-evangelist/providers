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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 51.0
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: 'The Theta Lake API (v1) provides programmatic access to the DCGA platform: ingest AI, audio, chat, document, email, and video content; manage records, comments, labels, and dispositions; run unified s'
  name: Theta Lake API
  slug: theta-lake-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/theta-lake-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thetalake.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.thetalake.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.thetalake.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.thetalake.ai/
- group: start
  title: ''
  type: SignUp
  url: https://developer.thetalake.ai/
- group: company
  title: ''
  type: Blog
  url: https://thetalake.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://developer.thetalake.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thetalake.com/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thetalake.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://thetalake.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/theta-lake-trust-center.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/theta-lake-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/theta-lake-authentication.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.thetalake.ai/
- group: design
  title: ''
  type: Conventions
  url: conventions/theta-lake-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/theta-lake-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/theta-lake-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/theta-lake-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/theta-lake-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/theta-lake-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/theta-lake-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Theta Lake is a cloud- and AI-native Digital Communications Governance and Archiving (DCGA) platform for compliance and security across unified communications. It captures, archives, supervises, and monitors electronic (eComms), audio (aComms), video (vComms), and AI (aiComms) interactions across 100+ certified integrations including Zoom, Microsoft Teams, Webex, RingCentral, Slack, Microsoft Copilot, and Anthropic. The Theta Lake API (v1) exposes data ingestion, records, unified search, supervision spaces, legal hold and legal matters, retention libraries, workflows, identities, exports, and audit logs, secured with OAuth2 client-credentials and JWT bearer tokens carrying fine-grained permission scopes.
image: https://thetalake.com/wp-content/uploads/2018/05/TL_logo_transparent.png
layout: provider
mcp_servers:
- description: ''
  name: theta-lake-mcp.yml
  slug: theta-lake-mcpyml
modified: '2026-07-21'
name: Theta Lake
nav: Providers
network: true
overview: 'Theta Lake publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Communications Governance, Compliance, Archiving, Security, and Supervision.


  Theta Lake''s developer surface includes documentation, API reference, signup flow, engineering blog, support, authentication, getting-started guide, and 16 more developer resources.'
random_paper: 23
scopes:
- name: Theta Lake Scopes
  scope_count: 70
  slug: theta-lake-scopes
  summary_line: 70 scopes · clientCredentials
score:
  band: thin
  composite: 42.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 37.7
    developer_ergonomics: 67.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 42.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Theta Lake Authentication
  slug: theta-lake-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Theta Lake Domain Security
  slug: theta-lake-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Theta Lake Trust Center
  slug: theta-lake-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001, ISO/IEC 42001, PCI DSS, HIPAA, CSA STAR for AI (Level 2), GDPR
slug: theta-lake
tags:
- Communications Governance
- Compliance
- Archiving
- Security
- Supervision
- eDiscovery
- Legal Hold
- Records Management
- Unified Communications
- AI Governance
- Regulatory Compliance
website: https://thetalake.com/
---
