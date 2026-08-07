---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 56.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 78
  human_in_the_loop: 1
  name: Aptible Agentic Access
  operation_count: 225
  slug: aptible-agentic-access
  summary_line: 225 operations · 78 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: The core Aptible platform API. A HAL+JSON REST API covering accounts (environments), apps, databases, backups and retention policies, certificates, configurations, containers, disks, deployments, endp
  name: Aptible Deploy API
  slug: deploy
- description: The Aptible authentication and identity service at auth.aptible.com. A HAL+JSON API exposing organizations, sessions, tokens, OAuth clients, users, U2F trusted facets and SSH key pre-authorizations, p
  name: Aptible Auth API
  slug: auth
- description: The Aptible Cloud API, published as an OpenAPI 3.0.2 document alongside the generated Go, Python and Ruby client libraries in aptible/cloud-api-clients. Covers organizations, environments, assets, con
  name: Aptible Cloud API
  slug: cloud
- description: A small OpenAPI 3.0.0 contract Aptible publishes for an Aptible tool server — list the tools a server exposes and invoke one by tool_id. Bearer token auth. Two operations; it is the contract behind th
  name: Aptible Tool Server API
  slug: tool-server
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aptible-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aptible-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aptible-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aptible-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.aptible.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.aptible.com/docs/getting-started/home
- group: docs
  title: ''
  type: Documentation
  url: https://www.aptible.com/docs/getting-started/home
- group: docs
  title: ''
  type: APIReference
  url: https://www.aptible.com/docs/reference/aptible-cli/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aptible.com/docs/getting-started/deploy-starter-template/overview
- group: operate
  title: ''
  type: Support
  url: https://app.aptible.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.aptible.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aptible
- group: operate
  title: ''
  type: Roadmap
  url: https://portal.productboard.com/aptible/2-aptible-roadmap-portal/tabs/10-in-progress
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aptible.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.aptible.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.aptible.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aptible.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aptible.com/legal/privacy-statement
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aptible.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.aptible.com/docs/core-concepts/security-compliance/overview
- group: auth
  title: ''
  type: Security
  url: https://www.aptible.com/legal/responsible-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aptible-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.aptible.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aptible-changelog.yml
- group: operate
  title: ''
  type: SLA
  url: https://www.aptible.com/legal/service-level-agreement
- group: build
  title: ''
  type: Packages
  url: packages/aptible-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aptible-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/aptible-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aptible-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/aptible-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aptible-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/aptible-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aptible-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aptible-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aptible-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aptible-data-model.yml
created: '2026-08-06'
description: Aptible is a Platform as a Service (PaaS) built for teams that have to prove security and compliance, not just ship. It deploys web apps, managed databases (PostgreSQL, MySQL, Redis, Elasticsearch, InfluxDB, RabbitMQ, SFTP) and AI workloads onto isolated, dedicated AWS infrastructure with encryption, host hardening, DDoS protection, managed host intrusion detection and vulnerability scanning enforced by default. Aptible ships HIPAA Business Associate Agreements, HITRUST R2 inheritance, SOC 2, PCI DSS and PIPEDA support alongside a Security & Compliance Dashboard, and more recently an LLM Gateway (400+ models behind one compliant API, with audit logging, spend limits and model access policies) and an MCP Gateway that governs how teams and agents reach MCP servers. The platform is driven by a public HAL+JSON REST API at api.aptible.com, an auth service at auth.aptible.com, a Ruby CLI, a Terraform provider, and generated Go/Ruby/Python client libraries.
image: https://framerusercontent.com/assets/sM8ECTApfoCzQMGmPJrKL9qxMFo.jpg
layout: provider
mcp_servers:
- description: ''
  name: aptible-mcp.yml
  slug: aptible-mcpyml
modified: '2026-08-06'
name: Aptible
nav: Providers
network: true
overview: 'Aptible publishes 3 APIs on the [APIs.io](https://apis.io/) network: Deploy API, Cloud API, and Tool Server API. Tagged areas include Company, Platform as a Service, Cloud Infrastructure, Deployment, and Managed Databases.


  Aptible''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 30 more developer resources.'
random_paper: 59
score:
  band: strong
  composite: 59.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 50.6
    developer_ergonomics: 80.4
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 52.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Aptible Authentication
  slug: aptible-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Aptible Domain Security
  slug: aptible-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aptible Vulnerability Disclosure
  slug: aptible-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aptible Trust Center
  slug: aptible-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: aptible
tags:
- Company
- Platform as a Service
- Cloud Infrastructure
- Deployment
- Managed Databases
- Security
- Compliance
- HIPAA
- DevOps
- AI Gateway
- MCP
website: https://www.aptible.com/
---
