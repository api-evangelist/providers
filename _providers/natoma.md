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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://natoma.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.natoma.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.natoma.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.natoma.ai/connect-to-ai/getting-started
- group: company
  title: ''
  type: Blog
  url: https://natoma.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://natoma.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://natoma.ai/book-a-demo
- group: operate
  title: ''
  type: Support
  url: https://docs.natoma.ai/support/contact-us
- group: operate
  title: ''
  type: StatusPage
  url: https://natomalabs.statuspage.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/natoma-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://natoma.ai/trust
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/natoma-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/natoma-domain-security.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://natoma.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://natoma.ai/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/natomalabs
- group: agent
  title: ''
  type: MCPServer
  url: mcp/natoma-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/natoma-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/natoma-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/natoma-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/natoma-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/natoma-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/natoma-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/natoma-well-known.yml
created: '2026-07-17'
description: Natoma is an enterprise Model Context Protocol (MCP) platform that lets organizations securely connect AI agents and assistants (ChatGPT, Claude, Cursor, and internal agents) to company data and business tools. It provides one-click deployment of managed and remote MCP servers, a catalog of 100+ verified MCP server connectors with automatic authentication, centralized identity-aware access controls, role-based tool profiles, shadow-AI discovery, and audit trails with SIEM integration. Natoma is a cybersecurity company backed by Greylock, Index Ventures, and Norwest Venture Partners. It is SOC 2 certified and GDPR/CCPA compliant, with SSO/SCIM provisioning via Microsoft Entra and Okta and on-premises deployment options.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/natoma.png
layout: provider
mcp_servers:
- description: ''
  name: natoma-mcp.yml
  slug: natoma-mcpyml
modified: '2026-07-20'
name: Natoma
nav: Providers
network: true
overview: 'Natoma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Model Context Protocol, MCP, and AI Agents.


  Natoma''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, support, CLI, and 17 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 35.4
  delta: 1.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 33.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Natoma Authentication
  slug: natoma-authentication
  summary_line: oauth2/apiKey/saml2/scim · 4 schemes
- kind: domain-security
  name: Natoma Domain Security
  slug: natoma-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Natoma Trust Center
  slug: natoma-trust-center
  summary_line: SOC 2
slug: natoma
tags:
- Company
- Cybersecurity
- Model Context Protocol
- MCP
- AI Agents
- Identity
- Access Management
- Governance
- Security
website: https://natoma.ai/
---
