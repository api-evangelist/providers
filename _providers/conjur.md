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
- description: REST API for authenticating machine and human identities, retrieving and rotating secrets, loading policy-as-code, and inspecting RBAC roles and resources. Compatible with Conjur OSS and CyberArk Secr
  name: Conjur / CyberArk Secrets Manager API
  slug: conjur-cyberark-secrets-manager-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://conjur.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cyberark.github.io/conjur/
- group: docs
  title: ''
  type: Documentation
  url: https://cyberark.github.io/conjur/
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/cyberark/conjur-openapi-spec
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cyberark
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/cyberark/conjur
- group: auth
  title: ''
  type: Authentication
  url: authentication/conjur-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/conjur-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/conjur-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/conjur-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/conjur-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/conjur-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/conjur-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/conjur-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/conjur-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/conjur-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/conjur-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/conjur-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conjur-domain-security.yml
created: '2026-07-17'
description: Conjur is CyberArk's open-source secrets management platform. It automatically secures secrets used by privileged users and machine identities across CI/CD, cloud, and Kubernetes environments. Conjur uses a role-based access control (RBAC) model, policy-as-code, and pluggable cloud-native authenticators (AWS IAM, Azure, GCP, Kubernetes, JWT, OIDC, LDAP) to issue short-lived access tokens and broker secret retrieval, rotation, and auditing. Originally Conjur Inc. (backed by Amplify Partners), it was acquired by CyberArk and is now part of Palo Alto Networks. The Conjur / CyberArk Secrets Manager REST API is published as an OpenAPI 3.1 definition with official Ruby, Python, Go, Java, and .NET client libraries, a CLI, and an official MCP server.
image: https://avatars.githubusercontent.com/u/30869256?v=4
layout: provider
mcp_servers:
- description: ''
  name: conjur-mcp.yml
  slug: conjur-mcpyml
modified: '2026-07-18'
name: Conjur
nav: Providers
network: true
overview: 'Conjur publishes 1 API on the [APIs.io](https://apis.io/) network: / CyberArk Secrets Manager API. Tagged areas include Company, Cybersecurity, Secrets Management, Identity and Access Management, and DevSecOps.


  Conjur''s developer surface includes documentation, API reference, authentication, CLI, changelog, and 15 more developer resources.'
random_paper: 45
score:
  band: thin
  composite: 34.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 37.7
    developer_ergonomics: 63.0
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 34.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Conjur Authentication
  slug: conjur-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Conjur Domain Security
  slug: conjur-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: conjur
tags:
- Company
- Cybersecurity
- Secrets Management
- Identity and Access Management
- DevSecOps
- Kubernetes
- Machine Identity
- Open Source
website: https://conjur.org
---
