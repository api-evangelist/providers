---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: 'Public cloud REST API for SC//Fleet Manager. Read-mostly, role-restricted access to an organization''s fleet: list and retrieve HyperCore clusters, virtual machines, cluster conditions (issues reported'
  name: SC//Fleet Manager API
  slug: scfleet-manager-api
- description: Undocumented v1 control-plane REST API served alongside SC//Fleet Manager on api.scalecomputing.com, whose OpenAPI 3.0 description is published anonymously at /swagger.json. Covers cluster registratio
  name: Scale Computing Platform Core API
  slug: scale-computing-platform-core-api
- description: On-appliance REST API exposed by every SC//HyperCore (HC3) clustered node for automating virtual machines, virtual disks, networks, snapshots, snapshot schedules, replication, node and cluster operati
  name: SC//HyperCore REST API
  slug: schypercore-rest-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scale-computing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.scalecomputing.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.scalecomputing.com/api/v2
- group: docs
  title: ''
  type: APIReference
  url: https://api.scalecomputing.com/api/v2
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/ScaleComputing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ScaleComputing
- group: operate
  title: ''
  type: Support
  url: https://www.scalecomputing.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.scalecomputing.com/
- group: company
  title: ''
  type: Blog
  url: https://www.scalecomputing.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.scalecomputing.com/pricing
- group: start
  title: ''
  type: Login
  url: https://fleet.scalecomputing.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.scalecomputing.com/eula
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.scalecomputing.com/privacy-policy
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/scale-computing-fleet-manager-application-manifest.json
- group: build
  title: ''
  type: Packages
  url: packages/scale-computing-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/scale-computing-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scale-computing-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/scale-computing-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/scale-computing-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/scale-computing-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/scale-computing-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/scale-computing-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/scale-computing-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/scale-computing-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scale-computing-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/scale-computing-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/scale-computing-well-known.yml
created: '2026-08-26'
description: 'Scale Computing builds SC//Platform, an edge-computing and hyperconverged infrastructure stack made up of SC//HyperCore (a self-healing KVM-based virtualization and storage OS that runs on clustered appliance nodes) and SC//Fleet Manager (a cloud console that monitors, updates and orchestrates thousands of distributed HyperCore clusters, VMs and containerized edge applications from one place). The programmable surface is split the same way: SC//HyperCore exposes an on-appliance REST API at /rest/v1 on each clustered node for VM, disk, network, snapshot and replication automation, while SC//Fleet Manager exposes a public, API-key-authenticated cloud REST API at api.scalecomputing.com for fleet-wide clusters, virtual machines, conditions, metrics, organization activity and API-key management. Scale Computing also ships and maintains a first-party Ansible collection and Terraform provider for HyperCore, publishes REST API example scripts on GitHub, and defines a JSON Schema for
  Fleet Manager application manifests used by its edge application lifecycle management feature.'
image: https://www.scalecomputing.com/asset-transforms/_1200x630_letterbox_center-center_82_none/scale-computing-logo.png?mtime=1778613063
json_schemas:
- name: Fleet Manager Application Manifest
  property_count: 4
  slug: scale-computing-fleet-manager-application-manifest
layout: provider
mcp_servers:
- description: ''
  name: Scale Computing MCP Server
  slug: scale-computing-mcp-server
modified: '2026-08-26'
name: Scale Computing
nav: Providers
network: true
overview: 'Scale Computing publishes 2 APIs on the [APIs.io](https://apis.io/) network: SC//Fleet Manager API and Platform Core API. Tagged areas include Edge Computing, Hyperconverged Infrastructure, Virtualization, Infrastructure Management, and Fleet Management.


  Scale Computing''s developer surface includes documentation, API reference, support, engineering blog, pricing, authentication, and 22 more developer resources.'
plans:
- name: Scale Computing Plans Pricing
  plan_count: 0
  slug: scale-computing-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Scale Computing Rate Limits
  slug: scale-computing-rate-limits
score:
  band: developing
  composite: 41.8
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 16.7
    contract_quality: 48.3
    developer_ergonomics: 54.2
    discoverability: 85.2
    governance: 16.7
    operational_transparency: 5.3
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Scale Computing Authentication
  slug: scale-computing-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Scale Computing Domain Security
  slug: scale-computing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Scale Computing Vulnerability Disclosure
  slug: scale-computing-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Scale Computing Trust Center
  slug: scale-computing-trust-center
  summary_line: trust center published
slug: scale-computing
tags:
- Edge Computing
- Hyperconverged Infrastructure
- Virtualization
- Infrastructure Management
- Fleet Management
- Virtual Machines
- Observability
- Infrastructure as Code
- Kubernetes
- Company
website: https://www.scalecomputing.com/
---
