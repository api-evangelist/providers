---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: The Defakto control-plane API. A gRPC service surface of sixteen versioned services covering trust domains, clusters, realms, workloads, access policy, service accounts and sessions, agent and provide
  name: Defakto Management API
  slug: defakto-security-management-api
- description: The pre-rebrand SPIRL control-plane endpoint, still documented and still serving the legacy app.spirl.com console and the spirlctl CLI alongside the current api.defakto.security host. Same gRPC servic
  name: SPIRL Management API (legacy)
  slug: defakto-security-legacy-management-api
artifact_total: 8
asyncapis:
- description: ''
  name: Defakto Security Audit Events
  slug: defakto-security-audit-events
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/defakto-security-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/defakto-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.defakto.security/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://d.defakto.security/
- group: docs
  title: ''
  type: Documentation
  url: https://d.defakto.security/
- group: docs
  title: ''
  type: APIReference
  url: https://d.defakto.security/cli/spirlctl/overview.md
- group: start
  title: ''
  type: GettingStarted
  url: https://d.defakto.security/mint/quick-start.md
- group: company
  title: ''
  type: Blog
  url: https://www.defakto.security/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/defakto-security
- group: operate
  title: ''
  type: Support
  url: https://www.defakto.security/contact/
- group: start
  title: ''
  type: SignUp
  url: https://www.defakto.security/demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.defakto.security/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.defakto.security/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://www.defakto.security/security/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/defakto-security-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/defakto-security-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/defakto-security-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/defakto-security-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/defakto-security-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/defakto-security-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/defakto-security-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/defakto-security-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/defakto-security-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/defakto-security-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/defakto-security-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/defakto-security-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/defakto-security-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/defakto-security-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/defakto-security-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-12'
description: 'Defakto (formerly SPIRL) is a non-human identity (NHI) security company that issues short-lived, cryptographically attested identities to workloads, services, CI/CD pipelines and AI agents in place of static secrets, API keys and long-lived service accounts. The platform is built on SPIFFE and ships two products: Mint, which runs Trust Domain Servers and Agents that mint X.509-SVIDs, JWT-SVIDs and proof-of-possession WIT-SVIDs for Kubernetes, Linux, Docker and serverless workloads under a dozen attestation methods; and Ledger, which discovers, risk-scores and eradicates static secrets across AWS, Azure, GCP, Kubernetes, Anthropic, OpenAI, Bedrock AgentCore and Gemini. The control plane is driven by a gRPC management API and the spirlctl CLI, with a Go SDK, an OpenTofu/Terraform provider, workload identity federation into AWS/Azure/GCP, and OCSF 1.8.0 audit logging.'
image: https://www.defakto.security/wp-content/uploads/2025/09/defakto-logo.svg
layout: provider
modified: '2026-08-12'
name: Defakto Security
nav: Providers
network: true
overview: 'Defakto Security publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Identity, Non-Human Identity, Workload Identity, and SPIFFE.


  The Defakto Security catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Defakto Security''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, CLI, and 23 more developer resources.'
plans:
- name: Defakto Security Plans Pricing
  plan_count: 0
  slug: defakto-security-plans-pricing
random_paper: 107
rate_limits:
- limit_count: 0
  name: Defakto Security Rate Limits
  slug: defakto-security-rate-limits
score:
  band: developing
  composite: 49.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 78.3
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 39.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: authentication
  name: Defakto Security Authentication
  slug: defakto-security-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Defakto Security Domain Security
  slug: defakto-security-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Defakto Security Vulnerability Disclosure
  slug: defakto-security-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: defakto-security
tags:
- Security
- Identity
- Non-Human Identity
- Workload Identity
- SPIFFE
- Authentication
- Zero Trust
- Secrets Management
- Kubernetes
- CI/CD
- Cloud Security
- gRPC
- Machine Identity
- Agentic AI
website: https://www.defakto.security/
---
