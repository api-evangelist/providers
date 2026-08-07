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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.8
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: REST API exposed by the Zerto Virtual Manager / Zerto Cloud Appliance for programmatic disaster-recovery management — VPGs, failover, checkpoints, VRAs, peer sites, alerts, events, tasks, and long-ter
  name: Zerto ZVM REST API
  slug: zerto-zvm-rest-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.zerto.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.zerto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.zerto.com/
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/saackerman/ZertoSwaggerAPI
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/ZertoPublic/zerto-api-quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/zerto-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zerto-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zerto-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zerto-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zerto-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zerto-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zerto-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/zerto-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zerto-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zerto-domain-security.yml
- group: build
  title: ''
  type: Postman
  url: https://github.com/ZertoPublic/PostmanCollections
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ZertoPublic
- group: operate
  title: ''
  type: Support
  url: https://www.zerto.com/support-and-services/support/
- group: operate
  title: ''
  type: Community
  url: https://www.zerto.com/myzerto/forums/
- group: company
  title: ''
  type: Blog
  url: https://www.zerto.com/resources/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zerto.com/try-or-buy/pricing-and-licensing/
- group: start
  title: ''
  type: SignUp
  url: https://www.zerto.com/try-or-buy/try-zerto-free/
created: '2026-07-17'
description: Zerto, a Hewlett Packard Enterprise company, provides continuous data protection (CDP), disaster recovery, ransomware resilience, and multi-cloud data mobility for on-premises and cloud workloads. Its ZVM (Zerto Virtual Manager), ZCA (Zerto Cloud Appliance), and ZIC (Zerto In-Cloud) appliances expose a REST API under /v1, authenticated through an embedded Keycloak OAuth2 identity provider. The API lets teams manage Virtual Protection Groups (VPGs), orchestrate non-disruptive failover tests and live failover/failback, browse recovery checkpoints, run file- and VM-level restores, manage long-term retention repositories, and consume alerts and events — everything the Zerto UI does, driven programmatically. Zerto publishes an official PowerShell SDK, plus Python, Ansible, Terraform, and Postman examples via its ZertoPublic GitHub organization.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zerto.png
layout: provider
mcp_servers:
- description: ''
  name: zerto-mcp.yml
  slug: zerto-mcpyml
modified: '2026-07-21'
name: Zerto
nav: Providers
network: true
overview: 'Zerto publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Disaster Recovery, Data Protection, Backup, and Ransomware Resilience.


  Zerto''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 16 more developer resources.'
random_paper: 112
score:
  band: thin
  composite: 28.8
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 66.8
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 28.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Zerto Authentication
  slug: zerto-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Zerto Domain Security
  slug: zerto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zerto
tags:
- Company
- Disaster Recovery
- Data Protection
- Backup
- Ransomware Resilience
- Business Continuity
- Cloud Migration
- Replication
- Infrastructure
website: https://www.zerto.com/
---
