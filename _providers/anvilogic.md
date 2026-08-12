---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: The Anvilogic MCP Server is the platform's Model Context Protocol surface, letting AI agents and MCP clients call Anvilogic platform tools against a customer's security graph, detections, searches, an
  name: Anvilogic MCP Server
  slug: mcp
- description: 'The OAuth 2.1 authorization surface for the Anvilogic platform, advertised at the RFC 8414 /.well-known/oauth-authorization-server document on secure.anvilogic.com. It supports the authorization_code '
  name: Anvilogic Platform Authorization API
  slug: authorization
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.anvilogic.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://public-docs.anvilogic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://public-docs.anvilogic.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://public-docs.anvilogic.com/get-started/onboarding-guide
- group: company
  title: ''
  type: Blog
  url: https://www.anvilogic.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anvilogic-forge
- group: start
  title: ''
  type: SignUp
  url: https://secure.anvilogic.com/login
- group: start
  title: ''
  type: Login
  url: https://secure.anvilogic.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://public-docs.anvilogic.com/get-started/ai-operating-system-pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anvilogic.com/legal/msa
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anvilogic.com/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.anvilogic.com/demo
- group: operate
  title: ''
  type: StatusPage
  url: https://status.anvilogic.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/anvilogic-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.anvilogic.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/anvilogic-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/anvilogic-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anvilogic-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/anvilogic-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/anvilogic-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/anvilogic-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/anvilogic-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/anvilogic-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anvilogic-domain-security.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/anvilogic_stock/
created: '2026-07-31'
description: Anvilogic is an Agentic SecOps platform founded in 2019 by former SOC practitioners. It runs AI automation across the security operations lifecycle — onboarding, federated search, detection engineering, and triage & investigation — on top of the SIEMs, data lakes, and storage services a security team already operates, without requiring data migration. An AI Operating System coordinates task-scoped agents over an enterprise security graph, and Blueprints chains those agents into repeatable, human-approved workflows. The platform integrates with Splunk, Snowflake, Databricks, Microsoft Sentinel, Elastic, CrowdStrike, Amazon S3, and dozens of EDR, SOAR, and workflow tools. Anvilogic exposes an OAuth 2.1 protected Model Context Protocol (MCP) server so agents and customer-configured MCP connectors can call platform tools directly.
image: https://cdn.prod.website-files.com/6a4cfd0a31bb60a376cd1ee9/6a68af2d3deeaa9baf085208_anvilogic-og-1c-1200x630.png
layout: provider
mcp_servers:
- description: ''
  name: anvilogic-mcp.yml
  slug: anvilogic-mcpyml
modified: '2026-07-31'
name: Anvilogic
nav: Providers
network: true
overview: 'Anvilogic publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Security Operations, and Detection Engineering.


  Anvilogic''s developer surface includes documentation, getting-started guide, engineering blog, signup flow, pricing, support, authentication, and 18 more developer resources.'
random_paper: 28
score:
  band: thin
  composite: 34.8
  delta: -1.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 35.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anvilogic/refs/heads/main/screenshots/anvilogic-2026-08-07T161428.png
security:
- kind: authentication
  name: Anvilogic Authentication
  slug: anvilogic-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Anvilogic Domain Security
  slug: anvilogic-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Anvilogic Trust Center
  slug: anvilogic-trust-center
  summary_line: SOC 2, SOC 2 Type 2, ISO 27001, ISO/IEC 27001:2022, Data Privacy Framework, CSA AI Trustworthy Pledge
slug: anvilogic
tags:
- Company
- Security
- Cybersecurity
- Security Operations
- Detection Engineering
- SIEM
- Threat Detection
- Artificial Intelligence
- Agents
- Model Context Protocol
- Data Lake
website: https://www.anvilogic.com/
---
