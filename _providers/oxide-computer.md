---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Anti-affinity groups give control over instance placement.
  name: Oxide Affinity API
  slug: oxide-computer-affinity-api
- description: API for console authentication
  name: Oxide Console Auth API
  slug: oxide-computer-console-auth-api
- description: Information pertaining to the current user.
  name: Oxide Current User API
  slug: oxide-computer-current-user-api
- description: Virtual disks are used to store instance-local data which includes the operating system.
  name: Oxide Disks API
  slug: oxide-computer-disks-api
- description: Experimental, unstable interfaces, primarily for use by Oxide personnel
  name: Oxide Experimental API
  slug: oxide-computer-experimental-api
- description: External subnets that can be attached to instances.
  name: Oxide External Subnets API
  slug: oxide-computer-external-subnets-api
- description: Floating IPs allow a project to allocate well-known IPs to instances.
  name: Oxide Floating Ips API
  slug: oxide-computer-floating-ips-api
- description: Images are read-only virtual disks that may be used to boot virtual machines.
  name: Oxide Images API
  slug: oxide-computer-images-api
- description: Virtual machine instances are the basic unit of computation. These operations are used for provisioning, controlling, and destroying instances.
  name: Oxide Instances API
  slug: oxide-computer-instances-api
- description: IP pools are collections of external IPs that can be allocated and attached to instances.
  name: Oxide Ip Pools API
  slug: oxide-computer-ip-pools-api
- description: Authentication endpoints
  name: Oxide Login API
  slug: oxide-computer-login-api
- description: Silo-scoped metrics
  name: Oxide Metrics API
  slug: oxide-computer-metrics-api
- description: System-wide IAM policy
  name: Oxide Policy API
  slug: oxide-computer-policy-api
- description: Projects are a grouping of associated resources such as instances and disks within a silo for purposes of billing and access control.
  name: Oxide Projects API
  slug: oxide-computer-projects-api
- description: Silos represent a logical partition of users and resources.
  name: Oxide Silos API
  slug: oxide-computer-silos-api
- description: Snapshots of virtual disks at a particular point in time.
  name: Oxide Snapshots API
  slug: oxide-computer-snapshots-api
- description: Subnet pools are collections of external subnets that can be allocated and attached to instances.
  name: Oxide Subnet Pools API
  slug: oxide-computer-subnet-pools-api
- description: Alerts deliver notifications for events that occur on the Oxide rack
  name: Oxide System/alerts API
  slug: oxide-computer-system-alerts-api
- description: These endpoints relate to audit logs.
  name: Oxide System/audit Log API
  slug: oxide-computer-system-audit-log-api
- description: These operations pertain to hardware inventory and management. Racks are the unit of expansion of an Oxide deployment. Racks are in turn composed of sleds, switches, power supplies, and a cabled backp
  name: Oxide System/hardware API
  slug: oxide-computer-system-hardware-api
- description: IP pools are collections of external IPs. Linking a pool to a silo makes it available for allocation by users in that silo.
  name: Oxide System/ip Pools API
  slug: oxide-computer-system-ip-pools-api
- description: 'Metrics provide insight into the operation of the Oxide deployment. These include telemetry on hardware and software components that can be used to understand the current state as well as to diagnose '
  name: Oxide System/metrics API
  slug: oxide-computer-system-metrics-api
- description: This provides rack-level network configuration.
  name: Oxide System/networking API
  slug: oxide-computer-system-networking-api
- description: Silos represent a logical partition of users and resources.
  name: Oxide System/silos API
  slug: oxide-computer-system-silos-api
- description: Endpoints related to system health
  name: Oxide System/status API
  slug: oxide-computer-system-status-api
- description: Subnet pools are collections of external subnets. Linking a pool to a silo makes it available for allocation by users in that silo.
  name: Oxide System/subnet Pools API
  slug: oxide-computer-system-subnet-pools-api
- description: Support bundles collect debugging information from the rack for use by Oxide support.
  name: Oxide System/support Bundles API
  slug: oxide-computer-system-support-bundles-api
- description: Upload and manage system updates
  name: Oxide System/update API
  slug: oxide-computer-system-update-api
- description: API clients use device access tokens for authentication.
  name: Oxide Tokens API
  slug: oxide-computer-tokens-api
- description: Virtual Private Clouds (VPCs) provide isolated network environments for managing and deploying services.
  name: Oxide Vpcs API
  slug: oxide-computer-vpcs-api
artifact_total: 36
asyncapis:
- description: ''
  name: Oxide Computer Alerts Webhooks
  slug: oxide-computer-alerts-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/oxide-computer-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/oxide-computer-region-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://oxide.computer
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.oxide.computer
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oxide.computer
- group: docs
  title: ''
  type: APIReference
  url: https://docs.oxide.computer/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oxide.computer/guides/quickstart
- group: company
  title: ''
  type: Blog
  url: https://oxide.computer/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oxidecomputer
- group: operate
  title: ''
  type: Support
  url: https://oxide.computer/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oxide.computer/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/oxide-computer-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.oxide.computer/release-notes/system
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/oxide-computer-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/oxide-computer-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/oxide-computer-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/oxide-computer-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oxide-computer-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/oxide-computer-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/oxide-computer-security.txt
- group: auth
  title: ''
  type: Security
  url: security/oxide-computer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/oxide-computer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oxide-computer-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/oxide-computer-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/oxide-computer-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/oxide-computer-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/oxide-computer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/oxide-computer-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/oxide-computer-alerts-webhooks.yml
created: '2026-08-26'
description: 'Oxide Computer Company builds a rack-scale cloud computer: integrated server sleds (Gimlet), a rack-level switch (Sidecar), Oxide''s own illumos distribution (Helios), the Propolis/bhyve hypervisor and the Crucible distributed block store, all driven by a single control plane called Nexus. Nexus exposes the Oxide Region API, a 315-operation OpenAPI 3.0.3 REST contract covering silos, projects, instances, disks, snapshots, images, VPCs, subnets, firewall rules, floating and ephemeral IPs, IP pools, affinity groups, alerts and webhook receivers, audit log, metrics/OxQL, hardware inventory, BGP/BFD networking, SAML and SCIM identity, support bundles and system update. Because the product is a rack a customer owns, the API is served from the customer''s own control-plane domain rather than a vendor-hosted endpoint. Oxide publishes first-party Rust, TypeScript and Go SDKs, an `oxide` CLI, a Terraform provider and a Packer plugin, and develops essentially the entire stack in the
  open on GitHub.'
image: https://oxide.computer/favicon.png
layout: provider
modified: '2026-08-26'
name: Oxide
nav: Providers
network: true
overview: 'Oxide publishes 30 APIs on the [APIs.io](https://apis.io/) network, including Affinity API, Console Auth API, Current User API, and 27 more. Tagged areas include Cloud Computing, Infrastructure, Compute, Virtualization, and Networking.


  The Oxide catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Oxide''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, release notes, and 23 more developer resources.'
plans:
- name: Oxide Computer Plans Pricing
  plan_count: 0
  slug: oxide-computer-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Oxide Computer Rate Limits
  slug: oxide-computer-rate-limits
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 48.3
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 41.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 30
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Oxide Computer Authentication
  slug: oxide-computer-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Oxide Computer Domain Security
  slug: oxide-computer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Oxide Computer Vulnerability Disclosure
  slug: oxide-computer-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: oxide-computer
tags:
- Cloud Computing
- Infrastructure
- Compute
- Virtualization
- Networking
- Storage
- Hardware
- On-Premise
- Private Cloud
- Open-Source
website: https://oxide.computer
---
