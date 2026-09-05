---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-09-04'
api_count: 4
apis:
- description: On-appliance REST API exposed by every SC//HyperCore (HC3) clustered node for automating virtual machines, virtual disks, networks, snapshots, snapshot schedules, replication, node and cluster operati
  name: SC//HyperCore REST API
  slug: schypercore-rest-api
- baseURL: https://api.scalecomputing.com
  baseurl_source: declared
  description: Manage Fleet Manager API access independently of users
  name: Scale Computing API Keys API
  slug: scale-computing-api-keys-api
- baseURL: https://api.scalecomputing.com
  baseurl_source: declared
  description: The Clusters API from Scale Computing — 10 operation(s) for clusters.
  name: Scale Computing Clusters API
  slug: scale-computing-clusters-api
- baseURL: https://api.scalecomputing.com
  baseurl_source: declared
  description: Issues reported by SC//HyperCore clusters
  name: Scale Computing Conditions API
  slug: scale-computing-conditions-api
- baseURL: https://api.scalecomputing.com
  baseurl_source: declared
  description: The Health API from Scale Computing — 1 operation(s) for health.
  name: Scale Computing Health API
  slug: scale-computing-health-api
- baseURL: https://api.scalecomputing.com
  baseurl_source: declared
  description: Historical tracking of CPU, RAM and Storage metrics across your fleet
  name: Scale Computing Metrics API
  slug: scale-computing-metrics-api
- baseURL: https://api.scalecomputing.com
  baseurl_source: declared
  description: The Nodes API from Scale Computing — 5 operation(s) for nodes.
  name: Scale Computing Nodes API
  slug: scale-computing-nodes-api
- baseURL: https://api.scalecomputing.com
  baseurl_source: declared
  description: Audit log of many user and system-generated events in Fleet Manager
  name: Scale Computing Organization Activities API
  slug: scale-computing-organization-activities-api
- baseURL: https://api.scalecomputing.com
  baseurl_source: declared
  description: The Organization API from Scale Computing — 2 operation(s) for organization.
  name: Scale Computing Organization API
  slug: scale-computing-organization-api
- baseURL: https://api.scalecomputing.com
  baseurl_source: declared
  description: The Organization Salesforce Account API from Scale Computing — 1 operation(s) for organization salesforce account.
  name: Scale Computing Organization Salesforce Account API
  slug: scale-computing-organization-salesforce-account-api
- baseURL: https://api.scalecomputing.com
  baseurl_source: declared
  description: The OrganizationRoles API from Scale Computing — 2 operation(s) for organizationroles.
  name: Scale Computing Organization Roles API
  slug: scale-computing-organizationroles-api
- baseURL: https://api.scalecomputing.com
  baseurl_source: declared
  description: The Organizations API from Scale Computing — 4 operation(s) for organizations.
  name: Scale Computing Organizations API
  slug: scale-computing-organizations-api
- baseURL: https://api.scalecomputing.com
  baseurl_source: declared
  description: The OrganizationUser API from Scale Computing — 1 operation(s) for organizationuser.
  name: Scale Computing Organization User API
  slug: scale-computing-organizationuser-api
- baseURL: https://api.scalecomputing.com
  baseurl_source: declared
  description: The OrganizationUsers API from Scale Computing — 1 operation(s) for organizationusers.
  name: Scale Computing Organization Users API
  slug: scale-computing-organizationusers-api
- baseURL: https://api.scalecomputing.com
  baseurl_source: declared
  description: The Salesforce API from Scale Computing — 1 operation(s) for salesforce.
  name: Scale Computing Salesforce API
  slug: scale-computing-salesforce-api
- baseURL: https://api.scalecomputing.com
  baseurl_source: declared
  description: The Staged Clusters API from Scale Computing — 4 operation(s) for staged clusters.
  name: Scale Computing Staged Clusters API
  slug: scale-computing-staged-clusters-api
- baseURL: https://api.scalecomputing.com
  baseurl_source: declared
  description: The Users API from Scale Computing — 13 operation(s) for users.
  name: Scale Computing Users API
  slug: scale-computing-users-api
- baseURL: https://api.scalecomputing.com
  baseurl_source: declared
  description: Virtual Machines on SC//HyperCore clusters
  name: Scale Computing Vms API
  slug: scale-computing-vms-api
artifact_total: 25
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/scale-computing-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/scale-computing-fleet-manager-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/scale-computing-core-overlay.yaml
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
  type: X-MCPServerCandidate
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
modified: '2026-08-26'
name: Scale Computing
nav: Providers
network: true
overview: 'Scale Computing publishes 17 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Clusters API, Conditions API, and 14 more. Tagged areas include Edge Computing, Hyperconverged Infrastructure, Virtualization, Infrastructure Management, and Fleet Management.


  Scale Computing''s developer surface includes documentation, API reference, support, engineering blog, pricing, authentication, and 25 more developer resources.'
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
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 40.1
    developer_ergonomics: 54.2
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 5.3
  previous_composite: 37.1
  provenance:
    conformance: derived
    contracts:
      callable: 41.2
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scale-computing/refs/heads/main/screenshots/scale-computing-2026-09-02T154508.png
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
website: https://www.scalecomputing.com/
---
