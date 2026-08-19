---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
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
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Longhorn Agentic Access
  operation_count: 34
  slug: longhorn-agentic-access
  summary_line: 34 operations · 18 acting
api_count: 9
apis:
- description: Backing image management for volumes that use pre-populated disk images as their base data. Backing images are immutable and can be shared across multiple volumes in the same namespace.
  name: Longhorn BackingImages API
  slug: longhorn-backingimages-api
- description: Backup operations for storing volume snapshots to external storage targets such as S3-compatible storage or NFS. Backups can be restored to new volumes for disaster recovery.
  name: Longhorn Backups API
  slug: longhorn-backups-api
- description: Engine image management for the Longhorn storage engine. Engine images are OCI images containing the Longhorn engine binary and are used to upgrade or manage storage engine versions.
  name: Longhorn EngineImages API
  slug: longhorn-engineimages-api
- description: Node management for the Longhorn storage cluster including listing nodes, updating disk configurations, enabling or disabling scheduling, and managing node tags for workload placement.
  name: Longhorn Nodes API
  slug: longhorn-nodes-api
- description: Recurring job management for scheduling automated snapshot and backup operations on a cron-based schedule. Recurring jobs can be applied to individual volumes or all volumes via groups.
  name: Longhorn RecurringJobs API
  slug: longhorn-recurringjobs-api
- description: System-wide Longhorn settings management including backup targets, replica counts, node scheduling policies, data locality settings, and storage over-provisioning configuration.
  name: Longhorn Settings API
  slug: longhorn-settings-api
- description: 'Snapshot operations for volumes including creating, listing, deleting, reverting to, and purging snapshots. Snapshots capture the state of a volume at a point in time and can be used as the basis for '
  name: Longhorn Snapshots API
  slug: longhorn-snapshots-api
- description: System-level backup and restore operations for the entire Longhorn configuration including all volumes, settings, and resource definitions.
  name: Longhorn SystemBackups API
  slug: longhorn-systembackups-api
- description: Volume lifecycle management including creating, attaching, detaching, expanding, and deleting volumes. Also includes volume actions such as activating, canceling expansion, and managing replicas.
  name: Longhorn Volumes API
  slug: longhorn-volumes-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Longhorn Manager BackingImages API
  slug: open-longhorn-backingimages-api
- collection_type: open
  name: Longhorn Manager BackingImages Backups API
  slug: open-longhorn-backups-api
- collection_type: open
  name: Longhorn Manager BackingImages EngineImages API
  slug: open-longhorn-engineimages-api
- collection_type: open
  name: Longhorn Manager API
  slug: open-longhorn-manager-api
- collection_type: open
  name: Longhorn Manager BackingImages Nodes API
  slug: open-longhorn-nodes-api
- collection_type: open
  name: Longhorn Manager BackingImages RecurringJobs API
  slug: open-longhorn-recurringjobs-api
- collection_type: open
  name: Longhorn Manager BackingImages Settings API
  slug: open-longhorn-settings-api
- collection_type: open
  name: Longhorn Manager BackingImages Snapshots API
  slug: open-longhorn-snapshots-api
- collection_type: open
  name: Longhorn Manager BackingImages SystemBackups API
  slug: open-longhorn-systembackups-api
- collection_type: open
  name: Longhorn Manager BackingImages Volumes API
  slug: open-longhorn-volumes-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/longhorn/longhorn/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/longhorn/longhorn/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/longhorn/longhorn/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/longhorn/longhorn/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/longhorn/longhorn/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/longhorn-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/longhorn-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/longhorn-authentication.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/longhorn-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/longhorn-volume-schema.json
- group: company
  title: ''
  type: Website
  url: https://longhorn.io/
- group: docs
  title: ''
  type: Documentation
  url: https://longhorn.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://longhorn.io/docs/1.11.1/deploy/install/
- group: company
  title: ''
  type: Blog
  url: https://longhorn.io/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/longhorn/longhorn/releases
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/longhorn
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/longhorn/longhorn
- group: operate
  title: ''
  type: Community
  url: https://longhorn.io/community/
created: '2026-03-16'
description: Longhorn is a CNCF incubating lightweight, reliable, and easy-to-use distributed block storage system for Kubernetes. It creates a dedicated storage controller for each volume and replicates data across multiple nodes for high availability. Longhorn supports snapshots, backups to S3-compatible storage, disaster recovery, and recurring backup schedules.
finops:
- name: Longhorn Finops
  service_category: API
  slug: longhorn-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/longhorn.png
json_schemas:
- name: Longhorn Volume
  property_count: 19
  slug: longhorn-volume
jsonld:
- class_count: 3
  name: Longhorn Context
  property_count: 12
  slug: longhorn-context
layout: provider
modified: '2026-05-19'
name: Longhorn
nav: Providers
network: true
overview: 'Longhorn publishes 9 APIs on the [APIs.io](https://apis.io/) network, including BackingImages API, Backups API, EngineImages API, and 6 more. Tagged areas include Backup, Block Storage, Cloud Native, Incubating, and Kubernetes.


  The Longhorn catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Longhorn''s developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, and 13 more developer resources.'
plans:
- name: Longhorn Plans Pricing
  plan_count: 3
  slug: longhorn-plans-pricing
random_paper: 126
rate_limits:
- limit_count: 5
  name: Longhorn Rate Limits
  slug: longhorn-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Longhorn API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: longhorn-jsonschema-spectral-rules
score:
  band: developing
  composite: 41.8
  delta: -5.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 67.9
    developer_ergonomics: 40.5
    discoverability: 72.2
    governance: 9.8
    operational_transparency: 39.5
  previous_composite: 47.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/longhorn/refs/heads/main/screenshots/longhorn-2026-06-20T184706.png
security:
- kind: authentication
  name: Longhorn Authentication
  slug: longhorn-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Longhorn Domain Security
  slug: longhorn-domain-security
  summary_line: TLSv1.3 · HSTS
slug: longhorn
tags:
- Backup
- Block Storage
- Cloud Native
- Incubating
- Kubernetes
- Persistent Volumes
website: https://longhorn.io/
---
