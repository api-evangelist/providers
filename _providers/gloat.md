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
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.5
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Tenant-scoped REST API to sync users, jobs, candidacies, projects, learning items, and the Skills Foundation job architecture into Gloat, plus RBAC authorization and company settings.
  name: Gloat Customer API
  slug: gloat-customer-api
artifact_total: 6
asyncapis:
- description: ''
  name: Gloat Webhooks
  slug: gloat-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.gloat.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.gloat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.gloat.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.gloat.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.gloat.com/docs/using-gloat-apis
- group: auth
  title: ''
  type: Authentication
  url: authentication/gloat-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gloat-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://gloat.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gloat.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gloat.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gloat.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://compliance.gloat.com/
- group: auth
  title: ''
  type: Compliance
  url: https://gloat.com/security-and-compliance/
- group: design
  title: ''
  type: Conformance
  url: conformance/gloat-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gloat-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gloat-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gloat-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/gloat-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gloat-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/gloat-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gloat-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gloat-domain-security.yml
created: '2026-07-17'
description: 'Gloat is an AI-native workforce orchestration and talent-marketplace platform. Its developer APIs let enterprises connect HR, learning, and skills data to Gloat: syncing users, jobs, projects, candidacies, and learning items, and maintaining a skills-and-job-architecture ontology (the Skills Foundation) of job families, job codes, and position titles. The platform also exposes RBAC authorization (roles, groups, permissions, access rules), certifications, applications, analytics embeds, and outbound sync webhooks. Customer APIs authenticate with a client-credentials JWT; Talent Marketplace APIs use an X-Gloat-API-Key header. All hosts are per-tenant at https://{company_slug}.gloat.com/api.'
image: https://www.gloat.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: gloat-mcp.yml
  slug: gloat-mcpyml
modified: '2026-07-19'
name: Gloat
nav: Providers
network: true
overview: 'Gloat publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai, Human Resources, Talent Marketplace, and Skills.


  The Gloat catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gloat''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, sandbox, and 17 more developer resources.'
random_paper: 55
score:
  band: developing
  composite: 44.1
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 51.6
    developer_ergonomics: 58.2
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 23.7
  previous_composite: 44.1
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/screenshots/gloat-2026-07-25T215912.png
security:
- kind: authentication
  name: Gloat Authentication
  slug: gloat-authentication
  summary_line: oauth2/apiKey/http · 2 schemes
- kind: domain-security
  name: Gloat Domain Security
  slug: gloat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Gloat Trust Center
  slug: gloat-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, GDPR, CSA / Cloud Controls Matrix (CCM)
slug: gloat
tags:
- Company
- Ai
- Human Resources
- Talent Marketplace
- Skills
- Workforce
- Internal Mobility
- HR Tech
website: https://www.gloat.com/
---
