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
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 57.0
  scored_at: '2026-08-06'
api_count: 5
apis:
- description: AI Colleague run metrics.
  name: Leena AI Analytics API
  slug: leena-ai-analytics-api
- description: Agent Operating Procedure execution and status.
  name: Leena AI AOP API
  slug: leena-ai-aop-api
- description: Retrieve audit log records for the authenticated bot.
  name: Leena AI Audit Logs API
  slug: leena-ai-audit-logs-api
- description: Obtain a bearer token.
  name: Leena AI Authentication API
  slug: leena-ai-authentication-api
- description: Stage attachments and sync articles into the Leena Knowledge Base.
  name: Leena AI Knowledge Articles API
  slug: leena-ai-knowledge-articles-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://leena.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.leena.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.leena.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.leena.ai/docs/external-aop-api-authentication-usage-guide
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.leena.ai/docs/getting-started
- group: start
  title: ''
  type: Quickstart
  url: https://docs.leena.ai/docs/quick-start-guide
- group: operate
  title: ''
  type: Support
  url: https://leena.ai/contact-us
- group: other
  title: ''
  type: Resources
  url: https://leena.ai/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leena-ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://leena.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://leena.ai/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.leena.ai/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/leena-ai-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/leena-ai-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/leena-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/leena-ai-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leena-ai-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leena-ai-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/leena-ai-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leena-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/leena-ai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/leena-ai-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/leena-ai-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/leena-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/leena-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leena-ai-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/leena-ai-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/leena-ai-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/leena-ai-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leena-ai-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/leena-ai-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Leena AI is an enterprise Agentic AI platform that deploys "AI Colleagues" — domain-specific, role-based autonomous agents — to automate back-office work across IT, HR, Finance, Procurement and Operations. Built on its proprietary WorkLM large language model, the platform pairs a no-code AI Colleagues Studio and Workflows Studio with Agent Operating Procedures (AOPs), guardrails, evals and approval paths. Its external developer surface is small but real: an OAuth 2.0 protected External AOP API for triggering and polling agent runs, an Audit Logs External API for compliance-grade activity export, a Knowledge Management REST connector for pushing knowledge base articles, and a first-party hosted MCP server plus an A2A endpoint that let third-party agents from Microsoft Copilot Studio, IBM watsonx Orchestrate, Salesforce Agentforce and ServiceNow call into Leena AI''s agents. The platform is region-partitioned across eight named regions and carries SOC 2 Type 2, ISO/IEC 27001/27017/27018/27701,
  HIPAA and CSA STAR certifications.'
image: https://assets.leena.ai/images/og/homepage_OG_image.webp
layout: provider
mcp_servers:
- description: ''
  name: leena-ai-mcp.yml
  slug: leena-ai-mcpyml
modified: '2026-07-19'
name: Leena AI
nav: Providers
network: true
overview: 'Leena AI publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, AOP API, Audit Logs API, and 2 more. Tagged areas include Company, Ai Ml, Agentic AI, Artificial Intelligence, and Enterprise Software.


  Leena AI''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, changelog, authentication, and 25 more developer resources.'
random_paper: 86
rate_limits:
- limit_count: 1
  name: Leena Ai Rate Limits
  slug: leena-ai-rate-limits
scopes:
- name: Leena Ai Scopes
  scope_count: 0
  slug: leena-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.5
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 58.1
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 52.6
  previous_composite: 52.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leena-ai/refs/heads/main/screenshots/leena-ai-2026-07-25T224821.png
security:
- kind: authentication
  name: Leena Ai Authentication
  slug: leena-ai-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Leena Ai Domain Security
  slug: leena-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Leena Ai Vulnerability Disclosure
  slug: leena-ai-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Leena Ai Trust Center
  slug: leena-ai-trust-center
  summary_line: SOC 2 Type 2, SOC 1, ISO/IEC 27001, ISO/IEC 27017:2015, ISO/IEC 27018:2019, ISO/IEC 27701, CSA STAR, HIPAA, FedRAMP Certified Class C
slug: leena-ai
tags:
- Company
- Ai Ml
- Agentic AI
- Artificial Intelligence
- Enterprise Software
- Human Resources
- IT Service Management
- Employee Experience
- Workflow Automation
- Conversational AI
- Model Context Protocol
- Knowledge Management
website: https://leena.ai
---
