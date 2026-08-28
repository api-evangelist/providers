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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Intezer Platform API 2.0 — submit files, URLs, hashes and endpoint scans for autonomous malware analysis and code-reuse detection, poll analysis status, and retrieve verdicts, sub-analyses and IOCs. A
  name: Intezer Platform API
  slug: intezer-platform-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://intezer.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://analyze.intezer.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.intezer.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.intezer.com/docs
- group: company
  title: ''
  type: Blog
  url: https://intezer.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://intezer.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://analyze.intezer.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://intezer.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://intezer.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/intezer
- group: build
  title: ''
  type: Packages
  url: packages/intezer-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/intezer-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/intezer-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/intezer-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/intezer-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/intezer-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/intezer-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/intezer-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://intezer.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/intezer-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intezer-domain-security.yml
created: '2026-07-17'
description: Intezer operates a Forensic AI SOC platform that autonomously triages, investigates and helps respond to every security alert flowing from an organization's EDR, NDR, SIEM, identity, cloud and email-security tooling. Its investigation engine combines Genetic Malware Analysis (code-reuse mapping against a large genome of trusted and malicious software), dynamic and static analysis, memory forensics, sandboxing and agentic AI reasoning to reach a verdict on alerts in under two minutes. The Intezer Platform API 2.0 exposes this analysis surface programmatically — submitting files, URLs, hashes and endpoint scans for analysis, retrieving verdicts and code-reuse results, and querying IOCs — and is offered alongside an official Python SDK, a CLI, and an MCP server that connects AI agents such as Claude, Cursor and Codex to case histories and investigation context.
image: https://intezer.com/wp-content/uploads/2023/05/intezer-logo.svg
layout: provider
mcp_servers:
- description: Official Intezer MCP server for security operations. Sits as a layer between an organization's detection systems (EDR, NDR, SIEM, identity, cloud, email security) and AI agents, giving agents access t
  name: Intezer MCP Server
  slug: intezer-mcp-server
modified: '2026-07-19'
name: Intezer
nav: Providers
network: true
overview: 'Intezer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Security, Malware Analysis, and Threat Intelligence.


  Intezer''s developer surface includes documentation, API reference, engineering blog, pricing, CLI, authentication, and 15 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 29.2
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 29.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/intezer/refs/heads/main/screenshots/intezer-2026-07-25T222717.png
security:
- kind: authentication
  name: Intezer Authentication
  slug: intezer-authentication
  summary_line: apiKey/http-bearer · 2 schemes
- kind: domain-security
  name: Intezer Domain Security
  slug: intezer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Intezer Trust Center
  slug: intezer-trust-center
  summary_line: SOC 2 Type II
slug: intezer
tags:
- Company
- Cybersecurity
- Security
- Malware Analysis
- Threat Intelligence
- SOC
- Incident Response
- Artificial Intelligence
- Automation
website: https://intezer.com
---
