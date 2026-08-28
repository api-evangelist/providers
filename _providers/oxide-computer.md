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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Oxide Region API is the public REST contract of the Oxide control plane (Nexus). It is an OpenAPI 3.0.3 document with 217 paths, 315 operations and 469 schemas, organized by the resources an opera
  name: Oxide Region API
  slug: oxide-computer-region-api
artifact_total: 7
asyncapis:
- description: ''
  name: Oxide Computer Alerts Webhooks
  slug: oxide-computer-alerts-webhooks
common:
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
overview: 'Oxide publishes 1 API on the [APIs.io](https://apis.io/) network: Region API. Tagged areas include Cloud Computing, Infrastructure, Compute, Virtualization, and Networking.


  The Oxide catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Oxide''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, release notes, and 21 more developer resources.'
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
  composite: 43.6
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 16.7
    contract_quality: 45.6
    developer_ergonomics: 73.2
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 36.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
- Open Source
website: https://oxide.computer
---
