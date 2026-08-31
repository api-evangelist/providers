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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Octopus Deploy Agentic Access
  operation_count: 6
  slug: octopus-deploy-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: REST API exposing projects, environments, releases, deployments, runbooks, accounts, certificates, tenants, variables, packages, and tasks managed by an Octopus Deploy server or Octopus Cloud instance
  name: Octopus Deploy REST API
  slug: rest-api
- description: The Accounts API from Octopus Deploy — 1 operation(s) for accounts.
  name: Octopus Deploy Accounts API
  slug: octopus-deploy-accounts-api
- description: The Environments API from Octopus Deploy — 1 operation(s) for environments.
  name: Octopus Deploy Environments API
  slug: octopus-deploy-environments-api
- description: The Feeds API from Octopus Deploy — 1 operation(s) for feeds.
  name: Octopus Deploy Feeds API
  slug: octopus-deploy-feeds-api
- description: The Machines API from Octopus Deploy — 1 operation(s) for machines.
  name: Octopus Deploy Machines API
  slug: octopus-deploy-machines-api
- description: The Projects API from Octopus Deploy — 1 operation(s) for projects.
  name: Octopus Deploy Projects API
  slug: octopus-deploy-projects-api
- description: The Root API from Octopus Deploy — 1 operation(s) for root.
  name: Octopus Deploy Root API
  slug: octopus-deploy-root-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Octopus Deploy REST Accounts API
  slug: open-octopus-deploy-accounts-api
- collection_type: open
  name: Octopus Deploy REST Accounts Environments API
  slug: open-octopus-deploy-environments-api
- collection_type: open
  name: Octopus Deploy REST Accounts Feeds API
  slug: open-octopus-deploy-feeds-api
- collection_type: open
  name: Octopus Deploy REST Accounts Machines API
  slug: open-octopus-deploy-machines-api
- collection_type: open
  name: Octopus Deploy REST Accounts Projects API
  slug: open-octopus-deploy-projects-api
- collection_type: open
  name: Octopus Deploy REST Accounts Root API
  slug: open-octopus-deploy-root-api
- collection_type: open
  name: Octopus Deploy REST API
  slug: open-octopus-deploy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/octopus-deploy-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/octopus-deploy-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/octopus-deploy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/octopus-deploy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/octopus-deploy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/octopus-deploy-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/octopus-deploy
- group: company
  title: ''
  type: Website
  url: https://octopus.com
- group: docs
  title: ''
  type: Documentation
  url: https://octopus.com/docs
- group: docs
  title: ''
  type: API Documentation
  url: https://octopus.com/docs/octopus-rest-api
- group: commercial
  title: ''
  type: Pricing
  url: https://octopus.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://octopus.com/start
- group: start
  title: ''
  type: Login
  url: https://octopus.com/login
- group: operate
  title: ''
  type: Support
  url: https://octopus.com/support
- group: company
  title: ''
  type: Blog
  url: https://octopus.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OctopusDeploy
- group: build
  title: ''
  type: CLI
  url: https://github.com/OctopusDeploy/cli
- group: build
  title: ''
  type: SDKs
  url: https://github.com/OctopusDeploy/OctopusClients
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/OctopusDeploy/mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://octopus.com/llms.txt
created: '2026-05-11'
description: Octopus Deploy is a continuous delivery and release orchestration platform for managing deployments across development, test, and production environments to virtual machines, containers, Kubernetes, and cloud services. The platform handles environments, tenants, runbooks, release promotion, and approvals for both regulated and high-velocity teams. The Octopus REST API provides programmatic access to projects, environments, releases, deployments, runbooks, variables, accounts, and tasks via API-key authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/octopus-deploy.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Octopus Deploy
nav: Providers
network: true
overview: 'Octopus Deploy publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Environments API, Feeds API, and 3 more. Tagged areas include DevOps, Continuous Delivery, Deployment Automation, Release Management, and Runbooks.


  Octopus Deploy''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, CLI, and 13 more developer resources.'
random_paper: 9
scopes:
- name: Octopus Deploy Scopes
  scope_count: 0
  slug: octopus-deploy-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 0.0
    contract_quality: 42.2
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 34.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/octopus-deploy/refs/heads/main/screenshots/octopus-deploy-2026-06-20T190613.png
security:
- kind: authentication
  name: Octopus Deploy Authentication
  slug: octopus-deploy-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Octopus Deploy Domain Security
  slug: octopus-deploy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Octopus Deploy Vulnerability Disclosure
  slug: octopus-deploy-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Octopus Deploy Trust Center
  slug: octopus-deploy-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: octopus-deploy
tags:
- DevOps
- Continuous Delivery
- Deployment Automation
- Release Management
- Runbooks
- CI/CD
website: https://octopus.com
---
