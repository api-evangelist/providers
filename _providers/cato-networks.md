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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'Public GraphQL API for the Cato Management Application (CMA): site and account provisioning, policy configuration, network/security analytics, entity lookup, and event streaming. Single GraphQL endpoi'
  name: Cato GraphQL API
  slug: cato-graphql-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.catonetworks.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.catonetworks.com/documentation/
- group: docs
  title: ''
  type: Documentation
  url: https://api.catonetworks.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://api.catonetworks.com/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.catonetworks.com/documentation/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/catonetworks
- group: company
  title: ''
  type: Blog
  url: https://www.catonetworks.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.catonetworks.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.catonetworks.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.catonetworks.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.catonetworks.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/cato-networks-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/cato-networks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cato-networks-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cato-networks-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cato-networks-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cato-networks-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cato-networks-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cato-networks-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cato-networks-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/cato-networks-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cato-networks-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.catonetworks.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/cato-networks-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cato-networks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.catonetworks.com/responsible-disclosure/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cato-networks-domain-security.yml
created: '2026-07-17'
description: Cato Networks is the SASE (Secure Access Service Edge) pioneer, delivering networking and security as a single global cloud platform that converges SD-WAN, a global private backbone, and a full cloud security stack — FWaaS, Secure Web Gateway, CASB, DLP, ZTNA/SDP, IPS, anti-malware, Remote Browser Isolation, and XDR. Cato exposes a public GraphQL API (api/v1/graphql2) for programmatic management, analytics, and event streaming of the Cato Management Application (CMA), authenticated with an API key sent in the x-api-key header. The official developer surface includes a Python CLI (catocli), a Go SDK (cato-go-sdk), a Terraform provider (catonetworks/cato), a local Model Context Protocol server (cato-mcp-server), and a web-based API explorer.
image: https://avatars.githubusercontent.com/u/182921385
layout: provider
mcp_servers:
- description: Local Model Context Protocol (MCP) server for Cato Networks' public GraphQL API (Cato Management Application / CMA).
  name: Cato Networks MCP Server
  slug: cato-networks-mcp-server
modified: '2026-07-18'
name: Cato Networks
nav: Providers
network: true
overview: 'Cato Networks publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, SASE, SSE, and Networking.


  Cato Networks'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, CLI, and 20 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 26.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cato-networks/refs/heads/main/screenshots/cato-networks-2026-07-25T204914.png
security:
- kind: authentication
  name: Cato Networks Authentication
  slug: cato-networks-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cato Networks Domain Security
  slug: cato-networks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cato Networks Vulnerability Disclosure
  slug: cato-networks-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Cato Networks Trust Center
  slug: cato-networks-trust-center
  summary_line: SOC 2 Type II, ISO 27001, PCI DSS, HIPAA, GDPR, CSA STAR
slug: cato-networks
tags:
- Company
- Cybersecurity
- SASE
- SSE
- Networking
- Security
- SD-WAN
- Zero Trust
- GraphQL
website: https://www.catonetworks.com
---
