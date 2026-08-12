---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: 'Enterprise AI Gateway that makes applications agent-ready through governed Model Context Protocol integration. Register a REST API from its OpenAPI spec (or proxy a third-party remote MCP server) and '
  name: Cequence AI Gateway
  slug: cequence-ai-gateway
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.cequence.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aigateway.cequence.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aigateway.cequence.ai/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aigateway.cequence.ai/docs/remote-mcp-servers/cequence-ai-gateway
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aigateway.cequence.ai/docs/getstarted
- group: operate
  title: ''
  type: Support
  url: https://helpdesk.cequence.ai/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.cequence.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cequenceai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cequence.ai/legal/saas-ai-gateway-end-user-license-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cequence.ai/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.cequence.ai/compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: security/cequence-security-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cequence.ai/responsible-disclosure-policy/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cequence-security-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cequence-security-domain-security.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cequence-security-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cequence-security-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/cequence-security-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cequence-security-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cequence-security-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cequence-security-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cequence-security-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cequence-security-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cequence-security-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cequence-security-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cequence-security-llms.txt
created: '2026-08-02'
description: Cequence Security (cequence.ai) is an application, API, and AI protection vendor whose Unified API Protection (UAP) platform discovers documented, undocumented, shadow and third-party APIs, builds a runtime API inventory, scores risk and compliance, tests APIs in CI/CD, and mitigates bot, fraud and business-logic abuse at runtime. Its newer Cequence AI Gateway makes existing enterprise applications agent-ready by turning REST APIs (from an uploaded OpenAPI spec) and third-party remote MCP servers into governed Model Context Protocol endpoints, with SSO/OAuth 2.1 inbound authentication, credential injection outbound, per-tool rate limiting, DLP redaction, agent personas, a skill registry and SIEM audit export. Cequence publishes a first-party hosted MCP server for managing the AI Gateway itself, an npm CLI (@cequenceai/mcp-cli), a Zendesk-hosted product knowledge base with dated release notes, and a trust center carrying SOC 2 Type 2, PCI DSS v4.0.1 and ISO 27001:2022 attestations.
image: https://www.cequence.ai/wp-content/uploads/2022/05/Cequence_logo.svg
layout: provider
mcp_servers:
- description: ''
  name: cequence-security-mcp.yml
  slug: cequence-security-mcpyml
modified: '2026-08-02'
name: Cequence Security
nav: Providers
network: true
overview: 'Cequence Security publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include api-security, ai-gateway, model-context-protocol, agentic-ai, and bot-management.


  Cequence Security''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, CLI, and 20 more developer resources.'
random_paper: 34
rate_limits:
- limit_count: 3
  name: Cequence Security Rate Limits
  slug: cequence-security-rate-limits
score:
  band: thin
  composite: 38.5
  delta: -1.1
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 63.2
  previous_composite: 39.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cequence-security/refs/heads/main/screenshots/cequence-security-2026-08-07T163243.png
security:
- kind: authentication
  name: Cequence Security Authentication
  slug: cequence-security-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cequence Security Domain Security
  slug: cequence-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cequence Security Vulnerability Disclosure
  slug: cequence-security-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Cequence Security Trust Center
  slug: cequence-security-trust-center
  summary_line: SOC 2 Type 2, PCI DSS v4.0.1, ISO/IEC 27001:2022
slug: cequence-security
tags:
- api-security
- ai-gateway
- model-context-protocol
- agentic-ai
- bot-management
- api-discovery
- api-governance
- fraud-detection
- waap
- cybersecurity
- api-testing
- agent-native
website: https://www.cequence.ai/
---
