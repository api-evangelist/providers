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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 51
  human_in_the_loop: 3
  name: Simplivity Agentic Access
  operation_count: 87
  slug: simplivity-agentic-access
  summary_line: 87 operations · 51 acting · 3 human-in-the-loop
api_count: 10
apis:
- description: A backup is a complete, standalone image of a specific virtual machine, taken at a specific point in time.
  name: SimpliVity backups API
  slug: simplivity-backups-api
- description: A set of omnistack_clusters that are able to perform backup and restore operations between each other
  name: SimpliVity cluster_groups API
  slug: simplivity-cluster-groups-api
- description: A datastore is a data repository of files that constitute virtual machines.
  name: SimpliVity datastores API
  slug: simplivity-datastores-api
- description: An external (non HPE SimpliVity) destination for storing backups, such as an HPE StoreOnce Catalyst store
  name: SimpliVity external_stores API
  slug: simplivity-external-stores-api
- description: A host is a virtual object that uses HPE OmniStack software in a federation.
  name: SimpliVity hosts API
  slug: simplivity-hosts-api
- description: An omnistack_cluster is a logical grouping of systems that run the HPE OmniStack software. The user defines an omnistack_cluster to efficiently share resources across the systems.
  name: SimpliVity omnistack_clusters API
  slug: simplivity-omnistack-clusters-api
- description: A policy contains backup rules that can be applied to an individual datastore or virtual_machine.
  name: SimpliVity policies API
  slug: simplivity-policies-api
- description: Includes the REST APIs that support security operations for HPE SimpliVity objects
  name: SimpliVity security API
  slug: simplivity-security-api
- description: A task is created by the system to enable a client to track state changes where a managed object moves when it is created or modified.
  name: SimpliVity tasks API
  slug: simplivity-tasks-api
- description: A virtual_machine represents a single virtual machine created within an HPE SimpliVity datastore.
  name: SimpliVity virtual_machines API
  slug: simplivity-virtual-machines-api
artifact_total: 15
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/HewlettPackard/simplivity-python/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simplivity-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/simplivity-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.hpe.com/us/en/hpe-simplivity.html
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/HewlettPackard/simplivity-python/blob/master/README.md
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/HewlettPackard/hpe-simplivity-swagger
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HewlettPackard
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/HewlettPackard/simplivity-python
- group: build
  title: ''
  type: Packages
  url: packages/simplivity-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/simplivity-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/simplivity-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/simplivity-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/simplivity-omnistack-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/simplivity-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/simplivity-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/simplivity-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/simplivity-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/simplivity-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/simplivity-lifecycle.yml
created: '2026-07-17'
description: SimpliVity is the hyperconverged infrastructure (HCI) pioneer acquired by Hewlett Packard Enterprise in 2017 and now shipped as HPE SimpliVity. Its data virtualization platform runs on the OmniStack software stack, delivering built-in deduplication, compression, backup, replication, and disaster recovery across VMware and Hyper-V clusters. The programmatic surface is the HPE OmniStack REST API (v1.25), which manages the key components of a SimpliVity configuration — virtual machines, backups, backup policies, datastores, hosts, clusters/omnistack_clusters, cluster groups, external stores, certificates, and long-running tasks. The API is served on-appliance by the Management Virtual Appliance (MVA) and authenticated with an OAuth2 password grant that issues read/write bearer tokens. HPE publishes first-party SDKs for Python, Go, and PowerShell plus Ansible modules on the HewlettPackard GitHub org.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simplivity.png
layout: provider
mcp_servers:
- description: ''
  name: simplivity-mcp.yml
  slug: simplivity-mcpyml
modified: '2026-07-21'
name: SimpliVity
nav: Providers
network: true
overview: 'SimpliVity publishes 10 APIs on the [APIs.io](https://apis.io/) network, including backups API, cluster_groups API, datastores API, and 7 more. Tagged areas include Company, Big Data, Hyperconverged Infrastructure, Virtualization, and Backup.


  SimpliVity''s developer surface includes documentation, API reference, and 18 more developer resources.'
random_paper: 70
scopes:
- name: Simplivity Scopes
  scope_count: 2
  slug: simplivity-scopes
  summary_line: 2 scopes · password
score:
  band: emerging
  composite: 27.2
  delta: -0.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 43.3
    developer_ergonomics: 25.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 27.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Simplivity Authentication
  slug: simplivity-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Simplivity Domain Security
  slug: simplivity-domain-security
  summary_line: TLSv1.3 · DMARC
slug: simplivity
tags:
- Company
- Big Data
- Hyperconverged Infrastructure
- Virtualization
- Backup
- Disaster Recovery
- Data Center
- Storage
- Cloud Infrastructure
- HPE
website: https://www.hpe.com/us/en/hpe-simplivity.html
---
