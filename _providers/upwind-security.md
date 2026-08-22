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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.4
  scored_at: '2026-08-19'
api_count: 12
apis:
- description: The Access Management resource offers methods for managing groups, members, roles, and scopes.
  name: Upwind Security access-management API
  slug: upwind-security-access-management-api
- description: The API Security resource offers methods for retrieving API catalog endpoints and their security information.
  name: Upwind Security api-security API
  slug: upwind-security-api-security-api
- description: The Cloud Accounts resource offers methods for creating, updating, and deleting cloud accounts for monitoring and security analysis.
  name: Upwind Security cloud-accounts API
  slug: upwind-security-cloud-accounts-api
- description: The Configurations resource offers a range of methods for listing, retrieving, and deleting configuration findings and rules.
  name: Upwind Security configurations API
  slug: upwind-security-configurations-api
- description: The Events resource offers a range of methods for listing, retrieving, and deleting events.
  name: Upwind Security events API
  slug: upwind-security-events-api
- description: The Integrations resource offers methods for managing various integrations with external systems, including integration webhooks.
  name: Upwind Security integrations API
  slug: upwind-security-integrations-api
- description: The Inventory resource offers a range of methods for listing and retrieving inventory assets.
  name: Upwind Security inventory API
  slug: upwind-security-inventory-api
- description: The Packages resource offers methods for retrieving Software Bill of Materials (SBOM) package details.
  name: Upwind Security packages API
  slug: upwind-security-packages-api
- description: The ShiftLeft resource offers methods for retrieving ShiftLeft related information
  name: Upwind Security shiftleft API
  slug: upwind-security-shiftleft-api
- description: The Threats resource offers a range of methods for listing, retrieving, and deleting threat detections.
  name: Upwind Security threats API
  slug: upwind-security-threats-api
- description: The Vulnerabilities resource offers a range of methods for listing, retrieving, and deleting vulnerability findings.
  name: Upwind Security vulnerabilities API
  slug: upwind-security-vulnerabilities-api
- description: The Workflows resource offers a range of methods for listing, retrieving, and deleting workflows.
  name: Upwind Security workflows API
  slug: upwind-security-workflows-api
artifact_total: 31
asyncapis:
- description: ''
  name: Upwind Security Webhooks
  slug: upwind-security-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Introduction access-management API
  slug: open-upwind-security-access-management-api
- collection_type: open
  name: Introduction access-management api-security API
  slug: open-upwind-security-api-security-api
- collection_type: open
  name: Introduction access-management cloud-accounts API
  slug: open-upwind-security-cloud-accounts-api
- collection_type: open
  name: Introduction access-management configurations API
  slug: open-upwind-security-configurations-api
- collection_type: open
  name: Introduction access-management events API
  slug: open-upwind-security-events-api
- collection_type: open
  name: Introduction access-management integrations API
  slug: open-upwind-security-integrations-api
- collection_type: open
  name: Introduction access-management inventory API
  slug: open-upwind-security-inventory-api
- collection_type: open
  name: Introduction access-management packages API
  slug: open-upwind-security-packages-api
- collection_type: open
  name: Introduction access-management shiftleft API
  slug: open-upwind-security-shiftleft-api
- collection_type: open
  name: Introduction access-management threats API
  slug: open-upwind-security-threats-api
- collection_type: open
  name: Introduction access-management vulnerabilities API
  slug: open-upwind-security-vulnerabilities-api
- collection_type: open
  name: Introduction access-management workflows API
  slug: open-upwind-security-workflows-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/upwind-security-management-v1-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upwind-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.upwind.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.upwind.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.upwind.io/restapi/v2/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.upwind.io/getting-started/connect-cloud-account/overview
- group: company
  title: ''
  type: Blog
  url: https://www.upwind.io/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upwindsecurity
- group: start
  title: ''
  type: Login
  url: https://console.upwind.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.upwind.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.upwind.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.upwind.io/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/upwind-security-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/upwind-security-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/upwind-security-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/upwind-security-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/upwind-security-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/upwind-security-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/upwind-security-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/upwind-security-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/upwind-security-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/upwind-security-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/upwind-security-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/upwind-security-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/upwind-security-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/upwind-security-data-model.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/upwind-security-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.upwind.io/
created: '2026-07-17'
description: Upwind is a cloud security (CNAPP) platform that pairs cloud security posture with eBPF-based runtime protection across AWS, Azure, Google Cloud, and Oracle Cloud, spanning vulnerability management, threat detection, configuration and compliance, API security, identity security, and shift-left CI/CD scanning. Its Management REST API (v1 and v2) exposes threats, vulnerabilities, configurations, inventory, SBOM packages, workflows, and access management using OAuth 2.0 client credentials, and the company ships a hosted MCP server plus an official Agent Skill for AI coding assistants.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/upwind-security.png
layout: provider
mcp_servers:
- description: ''
  name: upwind-security-mcp.yml
  slug: upwind-security-mcpyml
modified: '2026-07-21'
name: Upwind Security
nav: Providers
network: true
overview: 'Upwind Security publishes 12 APIs on the [APIs.io](https://apis.io/) network, including access-management API, api-security API, cloud-accounts API, and 9 more. Tagged areas include Company, Cybersecurity, Cloud Security, CNAPP, and Runtime Security.


  The Upwind Security catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Upwind Security''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, authentication, CLI, and 22 more developer resources.'
random_paper: 0
scopes:
- name: Upwind Security Scopes
  scope_count: 26
  slug: upwind-security-scopes
  summary_line: 26 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 48.1
  delta: -7.6
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 30.3
    contract_quality: 61.4
    developer_ergonomics: 28.6
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 42.1
  previous_composite: 55.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/upwind-security/refs/heads/main/screenshots/upwind-security-2026-08-17T082645.png
security:
- kind: authentication
  name: Upwind Security Authentication
  slug: upwind-security-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Upwind Security Domain Security
  slug: upwind-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Upwind Security Trust Center
  slug: upwind-security-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: upwind-security
tags:
- Company
- Cybersecurity
- Cloud Security
- CNAPP
- Runtime Security
- Vulnerability Management
- API Security
- Kubernetes
website: https://www.upwind.io/
---
