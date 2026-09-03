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
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://duplocloud.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.duplocloud.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.duplocloud.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.duplocloud.com/docs/introduction/readme
- group: company
  title: ''
  type: Blog
  url: https://duplocloud.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://duplocloud.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://duplocloud.com/request-a-demo
- group: operate
  title: ''
  type: Support
  url: mailto:support@duplocloud.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://duplocloud.com/legal/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/duplocloud
- group: auth
  title: ''
  type: Authentication
  url: authentication/duplo-cloud-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/duplo-cloud-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/duplo-cloud-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/duplo-cloud-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/duplo-cloud-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/duplo-cloud-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/duplo-cloud-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/duplo-cloud-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://duplocloud.com/solutions/security-and-compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: security/duplo-cloud-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/duplo-cloud-domain-security.yml
created: '2026-07-17'
description: DuploCloud is an AI-native DevOps platform that automates cloud infrastructure provisioning, security, and compliance across AWS, Azure, GCP, and Kubernetes. Its ARMOR agent runtime lets teams build and run AI DevOps agents that create tickets, manage workspaces, environments, and providers, while continuously enforcing SOC 2, HIPAA, PCI-DSS, NIST, ISO, HITRUST, and FedRAMP controls. Developers work with the platform through a web UI, a REST API, the duploctl CLI/Python SDK, Terraform and Pulumi providers, a Claude Code plugin, an official MCP server, and Slack/Teams. Backed by Mayfield.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/duplo-cloud.png
layout: provider
mcp_servers:
- description: The DuploCloud MCP (Model Context Protocol) server exposes your DuploCloud HelpDesk as a set of tools that AI assistants can call directly to create tickets and manage workspaces, agents, skills, envi
  name: Duplo Cloud MCP Server
  slug: duplo-cloud-mcp-server
modified: '2026-07-18'
name: Duplo Cloud
nav: Providers
network: true
overview: 'Duplo Cloud is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DevOps, Cloud Infrastructure, Infrastructure as Code, and Security and Compliance.


  Duplo Cloud''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, support, authentication, and 14 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 33.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/duplo-cloud/refs/heads/main/screenshots/duplo-cloud-2026-07-25T212513.png
security:
- kind: authentication
  name: Duplo Cloud Authentication
  slug: duplo-cloud-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Duplo Cloud Domain Security
  slug: duplo-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Duplo Cloud Trust Center
  slug: duplo-cloud-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA
slug: duplo-cloud
tags:
- Company
- DevOps
- Cloud Infrastructure
- Infrastructure as Code
- Security and Compliance
- AI Agents
- Kubernetes
- Automation
website: https://duplocloud.com
---
