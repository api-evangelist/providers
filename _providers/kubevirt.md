---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 18
  human_in_the_loop: 1
  name: Kubevirt Agentic Access
  operation_count: 32
  slug: kubevirt-agentic-access
  summary_line: 32 operations · 18 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: Operations for managing DataSource resources. A DataSource references an existing DataVolume or VolumeSnapshot as a source for cloning into new DataVolumes.
  name: KubeVirt DataSources API
  slug: kubevirt-datasources-api
- description: Operations for managing DataVolume resources. A DataVolume is a managed PersistentVolumeClaim with an integrated import/clone pipeline that automatically populates the volume from a specified source.
  name: KubeVirt DataVolumes API
  slug: kubevirt-datavolumes-api
- description: Operations for managing StorageProfile resources. StorageProfiles describe the capabilities of a StorageClass and provide default clone and access mode strategies.
  name: KubeVirt StorageProfiles API
  slug: kubevirt-storageprofiles-api
- description: Operations for managing live migration of VirtualMachineInstances from one node to another without downtime.
  name: KubeVirt VirtualMachineInstanceMigrations API
  slug: kubevirt-virtualmachineinstancemigrations-api
- description: Operations for managing VirtualMachineInstance (VMI) resources. A VirtualMachineInstance represents a running virtual machine and tracks its actual state.
  name: KubeVirt VirtualMachineInstances API
  slug: kubevirt-virtualmachineinstances-api
- description: Operations for managing VirtualMachine (VM) resources. A VirtualMachine defines the desired state and configuration of a virtual machine, providing lifecycle management and persistence across restarts
  name: KubeVirt VirtualMachines API
  slug: kubevirt-virtualmachines-api
- description: Subresource endpoints for accessing VM consoles via VNC, serial console, and USB redirection.
  name: KubeVirt VMConsole API
  slug: kubevirt-vmconsole-api
- description: Subresource operations for VM lifecycle management including start, stop, pause, unpause, restart, migrate, and adding/removing volumes.
  name: KubeVirt VMLifecycle API
  slug: kubevirt-vmlifecycle-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: KubeVirt Containerized Data Importer API
  slug: open-kubevirt-cdi
- collection_type: open
  name: KubeVirt Containerized Data Importer DataSources API
  slug: open-kubevirt-datasources-api
- collection_type: open
  name: KubeVirt Containerized Data Importer DataSources DataVolumes API
  slug: open-kubevirt-datavolumes-api
- collection_type: open
  name: KubeVirt Containerized Data Importer DataSources StorageProfiles API
  slug: open-kubevirt-storageprofiles-api
- collection_type: open
  name: KubeVirt Containerized Data Importer DataSources VirtualMachineInstanceMigrations API
  slug: open-kubevirt-virtualmachineinstancemigrations-api
- collection_type: open
  name: KubeVirt Containerized Data Importer DataSources VirtualMachineInstances API
  slug: open-kubevirt-virtualmachineinstances-api
- collection_type: open
  name: KubeVirt Containerized Data Importer DataSources VirtualMachines API
  slug: open-kubevirt-virtualmachines-api
- collection_type: open
  name: KubeVirt VM Management API
  slug: open-kubevirt-vm
- collection_type: open
  name: KubeVirt Containerized Data Importer DataSources VMConsole API
  slug: open-kubevirt-vmconsole-api
- collection_type: open
  name: KubeVirt Containerized Data Importer DataSources VMLifecycle API
  slug: open-kubevirt-vmlifecycle-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/kubevirt/containerized-data-importer/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/kubevirt/containerized-data-importer/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/kubevirt/containerized-data-importer/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/kubevirt/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/kubevirt/containerized-data-importer/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/kubevirt/containerized-data-importer/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kubevirt-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kubevirt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kubevirt.io/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/kubevirt-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/kubevirt-vm-schema.json
- group: docs
  title: ''
  type: Documentation
  url: https://kubevirt.io/user-guide/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kubevirt
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/kubevirt/kubevirt
- group: company
  title: ''
  type: Blog
  url: https://kubevirt.io/blogs/
- group: operate
  title: ''
  type: Community
  url: https://github.com/kubevirt/community
created: '2026-03-16'
description: KubeVirt is a CNCF incubating project that extends Kubernetes to run traditional virtual machines alongside containers. It allows users to create, manage, and run VMs using the same Kubernetes APIs and tools used for containers. KubeVirt is ideal for migrating legacy workloads to Kubernetes without requiring application rewriting.
finops:
- name: Kubevirt Finops
  service_category: API
  slug: kubevirt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kubevirt.png
json_schemas:
- name: KubeVirt VirtualMachine
  property_count: 5
  slug: kubevirt-vm
jsonld:
- class_count: 0
  name: Kubevirt Context
  property_count: 10
  slug: kubevirt-context
layout: provider
modified: '2026-05-19'
name: KubeVirt
nav: Providers
network: true
overview: 'KubeVirt publishes 8 APIs on the [APIs.io](https://apis.io/) network, including DataSources API, DataVolumes API, StorageProfiles API, and 5 more. Tagged areas include Cloud Native, Incubating, Kubernetes, Migration, and Virtual Machines.


  The KubeVirt catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  KubeVirt''s developer surface includes documentation, engineering blog, and 14 more developer resources.'
plans:
- name: Kubevirt Plans Pricing
  plan_count: 3
  slug: kubevirt-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Kubevirt Rate Limits
  slug: kubevirt-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: KubeVirt API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: kubevirt-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.3
  delta: -7.2
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 60.5
    developer_ergonomics: 14.3
    discoverability: 72.2
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/kubevirt/refs/heads/main/screenshots/kubevirt-2026-06-20T184209.png
security:
- kind: domain-security
  name: Kubevirt Domain Security
  slug: kubevirt-domain-security
  summary_line: TLSv1.3
slug: kubevirt
tags:
- Cloud Native
- Incubating
- Kubernetes
- Migration
- Virtual Machines
- Virtualization
website: https://kubevirt.io/
---
