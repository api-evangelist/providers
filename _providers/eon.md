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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 80
  human_in_the_loop: 6
  name: Eon Agentic Access
  operation_count: 99
  slug: eon-agentic-access
  summary_line: 99 operations · 80 acting · 6 human-in-the-loop
api_count: 13
apis:
- description: Manage connected cloud accounts onboarded to Eon.
  name: Eon accounts API
  slug: eon-accounts-api
- description: The actionApprovals API from Eon — 3 operation(s) for actionapprovals.
  name: Eon actionApprovals API
  slug: eon-actionapprovals-api
- description: Authentication and access token management.
  name: Eon auth API
  slug: eon-auth-api
- description: Define and manage backup policies and schedules.
  name: Eon backupPolicies API
  slug: eon-backuppolicies-api
- description: The backups API from Eon — 1 operation(s) for backups.
  name: Eon backups API
  slug: eon-backups-api
- description: Access billing and usage metering information.
  name: Eon billing API
  slug: eon-billing-api
- description: The dashboard API from Eon — 1 operation(s) for dashboard.
  name: Eon dashboard API
  slug: eon-dashboard-api
- description: Manage database snapshots and their recovery points.
  name: Eon databaseSnapshots API
  slug: eon-databasesnapshots-api
- description: The iam API from Eon — 8 operation(s) for iam.
  name: Eon iam API
  slug: eon-iam-api
- description: Track backup, restore, and other asynchronous jobs.
  name: Eon jobs API
  slug: eon-jobs-api
- description: Discover and manage protected cloud resources.
  name: Eon resources API
  slug: eon-resources-api
- description: Manage resource snapshots and point-in-time recovery points.
  name: Eon snapshots API
  slug: eon-snapshots-api
- description: Manage backup vaults that store snapshots.
  name: Eon vaults API
  slug: eon-vaults-api
artifact_total: 18
common:
- group: company
  title: ''
  type: Website
  url: https://www.eon.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.eon.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.eon.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.eon.io
- group: start
  title: ''
  type: GettingStarted
  url: https://console.eon.io/global-management/api-credentials
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eon-io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.eon.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.eon.io/get-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eon.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eon.io/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.eon.io/resources
- group: auth
  title: ''
  type: Compliance
  url: https://trust.eon.io
- group: auth
  title: ''
  type: TrustCenter
  url: security/eon-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eon-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eon-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/eon-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/eon-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/eon-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eon-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/eon-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eon-problem-types.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eon-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eon-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eon-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eon-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/eon-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/eon-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Eon is a next-generation cloud backup and data-protection platform that turns cloud backups into live, searchable, strategic assets across AWS, Google Cloud, and Azure. It provides agentless backup, cloud backup posture management, ransomware protection, global search over backups, live and granular file/resource restore, and a zero-ETL data-lake storage tier that makes old snapshots useful for analytics and AI. Eon exposes a REST API (OpenAPI 3.0, 99 operations) covering source/restore accounts, resources, vaults, snapshots, backup policies, restores, jobs, IAM, billing, and multi-party action approvals, with an official Go SDK and Terraform provider. Backed by BOND Capital and Lightspeed Venture Partners.
image: https://cdn.prod.website-files.com/6728a53e42fda9e629eb3ed6/672a2f7a6d97e6ab9f07f37e_og.webp
layout: provider
mcp_servers:
- description: ''
  name: eon-mcp.yml
  slug: eon-mcpyml
modified: '2026-07-19'
name: Eon
nav: Providers
network: true
overview: 'Eon publishes 13 APIs on the [APIs.io](https://apis.io/) network, including accounts API, actionApprovals API, auth API, and 10 more. Tagged areas include Company, Cloud Backup, Data Protection, Disaster Recovery, and Ransomware Protection.


  Eon''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, authentication, and 22 more developer resources.'
random_paper: 37
score:
  band: developing
  composite: 49.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 59.1
    developer_ergonomics: 58.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eon/refs/heads/main/screenshots/eon-2026-07-25T213500.png
security:
- kind: authentication
  name: Eon Authentication
  slug: eon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Eon Domain Security
  slug: eon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Eon Trust Center
  slug: eon-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, GDPR
slug: eon
tags:
- Company
- Cloud Backup
- Data Protection
- Disaster Recovery
- Ransomware Protection
- Backup
- Cloud Storage
- Data Lake
- Multi-Cloud
- Azure
- Google Cloud
website: https://www.eon.io
---
