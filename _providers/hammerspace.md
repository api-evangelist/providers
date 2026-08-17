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
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The management REST API served by the Hammerspace Anvil metadata server at the base path /mgmt/v1.2/rest. It is the programmatic control plane behind the Hammerspace GUI and admin CLI, covering shares
  name: Hammerspace Anvil Management API
  slug: anvil-management-api
artifact_total: 5
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/hammer-space/csi-plugin/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/hammer-space/csi-plugin/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/hammer-space/csi-plugin/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hammerspace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hammerspace.com/
- group: company
  title: ''
  type: About
  url: https://hammerspace.com/about-us/
- group: docs
  title: ''
  type: Documentation
  url: https://hammerspace.com/resources/
- group: other
  title: ''
  type: Resources
  url: https://hammerspace.com/resources/
- group: operate
  title: ''
  type: Support
  url: https://hammerspace.com/support/
- group: start
  title: ''
  type: Login
  url: https://supportportal.hammerspace.com/
- group: company
  title: ''
  type: Blog
  url: https://hammerspace.com/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://hammerspace.com/news-room/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hammer-space
- group: other
  title: ''
  type: Marketplace
  url: https://aws.amazon.com/marketplace/seller-profile?id=bf2492c2-776f-4390-a1cc-bf489509ce7b
- group: company
  title: ''
  type: Partners
  url: https://hammerspace.com/hs-partners_category/technology-partners/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hammerspace.com/eula/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hammerspace.com/privacy-statement-us/
- group: auth
  title: ''
  type: Authentication
  url: authentication/hammerspace-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hammerspace-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hammerspace-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hammerspace-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hammerspace-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hammerspace-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://hammerspace.com/hammerspace-announces-fips-140-3-validation-plans-to-integrate-certified-cryptography-into-data-platform/
- group: build
  title: ''
  type: Packages
  url: packages/hammerspace-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hammerspace-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/hammerspace-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hammerspace-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hammerspace-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hammerspace-llms.txt
created: '2026-08-04'
description: Hammerspace, Inc. is a Redwood City, California software company behind the Hammerspace Global Data Platform (formerly the Global Data Environment), a parallel file system and software-defined data platform that unifies unstructured data across on-premises storage, edge sites, and AWS, Azure and Google Cloud into a single global namespace. Data is reached through standard protocols — NFS, pNFS v4.2 with Flex Files, SMB, S3, and CSI for Kubernetes — while placement, replication, tiering, snapshots and retention are driven by declarative objectives rather than by manual data movement. The platform is administered through a GUI, an admin CLI, the open source hstk Python toolkit, Ansible and Terraform automation, and the Anvil metadata server REST API at /mgmt/v1.2/rest. The 2026 AI Data Platform release adds Tier-0 NVMe pooling on GPU servers, Milvus vector search, and a Model Context Protocol (MCP) server that exposes enterprise data to AI agents and RAG pipelines.
image: https://avatars.githubusercontent.com/u/47825731?v=4
layout: provider
mcp_servers:
- description: ''
  name: hammerspace-mcp.yml
  slug: hammerspace-mcpyml
modified: '2026-08-04'
name: Hammerspace
nav: Providers
network: true
overview: 'Hammerspace publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Storage, Data Management, File Systems, and Data Orchestration.


  Hammerspace''s developer surface includes documentation, support, engineering blog, authentication, changelog, CLI, and 24 more developer resources.'
random_paper: 115
scopes:
- name: Hammerspace Scopes
  scope_count: 36
  slug: hammerspace-scopes
  summary_line: 36 scopes · authorizationCode/implicit
score:
  band: thin
  composite: 30.9
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 30.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hammerspace/refs/heads/main/screenshots/hammerspace-2026-08-07T165941.png
security:
- kind: authentication
  name: Hammerspace Authentication
  slug: hammerspace-authentication
  summary_line: http/session-cookie/openIdConnect · 2 schemes
- kind: domain-security
  name: Hammerspace Domain Security
  slug: hammerspace-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hammerspace
tags:
- Company
- Storage
- Data Management
- File Systems
- Data Orchestration
- Hybrid Cloud
- Kubernetes
- Artificial Intelligence
- Unstructured Data
- Infrastructure
website: https://hammerspace.com/
---
