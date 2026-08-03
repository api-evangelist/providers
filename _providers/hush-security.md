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
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.1
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: REST API for the Hush Security platform, secured with OAuth 2.0 client-credentials (API Key ID + Secret exchanged at POST /v1/oauth/token for a Bearer access token). Region-scoped host (US). Errors fo
  name: Hush Security API
  slug: hush-security-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hush-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hush.security/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.hush.security/knowledgebase/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hush.security/knowledgebase/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hush.security/knowledgebase/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hush.security/knowledgebase/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.hush.security/blog
- group: operate
  title: ''
  type: Support
  url: https://www.hush.security/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hushsecurity
- group: start
  title: ''
  type: SignUp
  url: https://www.hush.security/free-forever/
- group: start
  title: ''
  type: Login
  url: https://login.hush.security/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hush.security/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hush.security/privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.hush.security/trust-center/
- group: auth
  title: ''
  type: Compliance
  url: https://www.hush.security/trust-center/
- group: auth
  title: ''
  type: Authentication
  url: authentication/hush-security-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hush-security-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hush-security-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hush-security-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hush-security-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/hush-security-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hush-security-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/hush-security-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hush-security-llms.txt
created: '2026-07-17'
description: Hush Security delivers identity-first access management for AI agents, workloads, and non-human identities (NHIs), replacing static secrets and long-lived API keys with dynamic, identity-based access at runtime. The platform provides runtime discovery and inventory of non-human identities, secrets detection and remediation, risk and posture management, and identity-based access for workloads and agentic AI through an "identity as code" model. Hush exposes a REST API (api.us.hush-security.com/v1) secured with OAuth 2.0 client-credentials, a Terraform provider, Helm charts, a Kubernetes Universal Access Management (UAM) operator with AccessCredential / AccessPrivilege / AccessPolicy CRDs, and first-party Claude Code agent skills. The company is SOC 2 and ISO 27001 certified.
image: https://avatars.githubusercontent.com/u/170552960?v=4
layout: provider
modified: '2026-07-19'
name: Hush Security
nav: Providers
network: true
overview: 'Hush Security publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Non-Human Identity, Identity and Access Management, and Secrets Management.


  Hush Security''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 18 more developer resources.'
random_paper: 43
score:
  band: thin
  composite: 35.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 71.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 35.2
  provenance:
    conformance: first-party
    skills: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hush-security/refs/heads/main/screenshots/hush-security-2026-07-25T221747.png
security:
- kind: authentication
  name: Hush Security Authentication
  slug: hush-security-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hush Security Domain Security
  slug: hush-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Hush Security Trust Center
  slug: hush-security-trust-center
  summary_line: SOC 2, ISO 27001
slug: hush-security
tags:
- Company
- Security
- Non-Human Identity
- Identity and Access Management
- Secrets Management
- AI Agents
- Agentic AI
- Kubernetes
- Cloud Security
- Workload Identity
website: https://www.hush.security/
---
