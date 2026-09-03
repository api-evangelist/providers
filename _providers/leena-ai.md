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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-03'
api_count: 5
apis:
- baseURL: https://us-east-1-aic.leena.ai
  baseurl_source: declared
  description: AI Colleague run metrics.
  name: Leena AI Analytics API
  slug: leena-ai-analytics-api
- baseURL: https://us-east-1-aic.leena.ai
  baseurl_source: declared
  description: Agent Operating Procedure execution and status.
  name: Leena AI AOP API
  slug: leena-ai-aop-api
- baseURL: https://us-east-1-aic.leena.ai
  baseurl_source: declared
  description: Retrieve audit log records for the authenticated bot.
  name: Leena AI Audit Logs API
  slug: leena-ai-audit-logs-api
- baseURL: https://us-east-1-aic.leena.ai
  baseurl_source: declared
  description: Obtain a bearer token.
  name: Leena AI Authentication API
  slug: leena-ai-authentication-api
- baseURL: https://us-east-1-aic.leena.ai
  baseurl_source: declared
  description: Stage attachments and sync articles into the Leena Knowledge Base.
  name: Leena AI Knowledge Articles API
  slug: leena-ai-knowledge-articles-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Leena AI External AOP Analytics API
  slug: open-leena-ai-analytics-api
- collection_type: open
  name: Leena AI External Analytics AOP API
  slug: open-leena-ai-aop-api
- collection_type: open
  name: Leena AI External AOP Analytics Audit Logs API
  slug: open-leena-ai-audit-logs-api
- collection_type: open
  name: Leena AI External AOP Analytics Authentication API
  slug: open-leena-ai-authentication-api
- collection_type: open
  name: Leena AI External AOP Analytics Knowledge Articles API
  slug: open-leena-ai-knowledge-articles-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/leena-ai-aop-overlay.yaml
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
  name: Leena AI MCP Server
  slug: leena-ai-mcp-server
modified: '2026-07-19'
name: Leena AI
nav: Providers
network: true
overview: 'Leena AI publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, AOP API, Audit Logs API, and 2 more. Tagged areas include Company, Ai Ml, Agentic AI, Artificial Intelligence, and Enterprise Software.


  Leena AI''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, changelog, authentication, and 26 more developer resources.'
random_paper: 8
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
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 19
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 13.0
    developer_ergonomics: 37.5
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 33.9
  provenance:
    conformance: first-party
    contracts:
      callable: 87.5
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- ITSM
- Employee Experience
- Workflow-Automation
- Conversational AI
- MCP
- Knowledge-Management
website: https://leena.ai
---
