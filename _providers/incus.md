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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 147
  human_in_the_loop: 0
  name: Incus Agentic Access
  operation_count: 291
  slug: incus-agentic-access
  summary_line: 291 operations · 147 acting
api_count: 22
apis:
- description: The certificates API from Incus — 4 operation(s) for certificates.
  name: Incus certificates API
  slug: incus-certificates-api
- description: The cluster API from Incus — 7 operation(s) for cluster.
  name: Incus cluster API
  slug: incus-cluster-api
- description: The cluster-groups API from Incus — 3 operation(s) for cluster-groups.
  name: Incus cluster-groups API
  slug: incus-cluster-groups-api
- description: The images API from Incus — 14 operation(s) for images.
  name: Incus images API
  slug: incus-images-api
- description: The instances API from Incus — 28 operation(s) for instances.
  name: Incus instances API
  slug: incus-instances-api
- description: The Metadata API from Incus — 1 operation(s) for metadata.
  name: Incus Metadata API
  slug: incus-metadata-api
- description: The metrics API from Incus — 1 operation(s) for metrics.
  name: Incus metrics API
  slug: incus-metrics-api
- description: The network-acls API from Incus — 4 operation(s) for network-acls.
  name: Incus network-acls API
  slug: incus-network-acls-api
- description: The network-address-sets API from Incus — 3 operation(s) for network-address-sets.
  name: Incus network-address-sets API
  slug: incus-network-address-sets-api
- description: The network-allocations API from Incus — 1 operation(s) for network-allocations.
  name: Incus network-allocations API
  slug: incus-network-allocations-api
- description: The network-forwards API from Incus — 3 operation(s) for network-forwards.
  name: Incus network-forwards API
  slug: incus-network-forwards-api
- description: The network-integrations API from Incus — 3 operation(s) for network-integrations.
  name: Incus network-integrations API
  slug: incus-network-integrations-api
- description: The network-load-balancers API from Incus — 4 operation(s) for network-load-balancers.
  name: Incus network-load-balancers API
  slug: incus-network-load-balancers-api
- description: The network-peers API from Incus — 3 operation(s) for network-peers.
  name: Incus network-peers API
  slug: incus-network-peers-api
- description: The network-zones API from Incus — 6 operation(s) for network-zones.
  name: Incus network-zones API
  slug: incus-network-zones-api
- description: The networks API from Incus — 5 operation(s) for networks.
  name: Incus networks API
  slug: incus-networks-api
- description: The operations API from Incus — 7 operation(s) for operations.
  name: Incus operations API
  slug: incus-operations-api
- description: The profiles API from Incus — 3 operation(s) for profiles.
  name: Incus profiles API
  slug: incus-profiles-api
- description: The projects API from Incus — 5 operation(s) for projects.
  name: Incus projects API
  slug: incus-projects-api
- description: The server API from Incus — 5 operation(s) for server.
  name: Incus server API
  slug: incus-server-api
- description: The storage API from Incus — 39 operation(s) for storage.
  name: Incus storage API
  slug: incus-storage-api
- description: The warnings API from Incus — 3 operation(s) for warnings.
  name: Incus warnings API
  slug: incus-warnings-api
artifact_total: 29
collections:
- collection_type: open
  name: Incus external REST API
  slug: open-incus
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/incus-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/incus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://linuxcontainers.org/incus/
- group: docs
  title: ''
  type: Documentation
  url: https://linuxcontainers.org/incus/docs/main/
- group: start
  title: ''
  type: GettingStarted
  url: https://linuxcontainers.org/incus/docs/main/tutorial/first_steps/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/lxc/incus
- group: operate
  title: ''
  type: Forums
  url: https://discuss.linuxcontainers.org/
- group: operate
  title: ''
  type: Issues
  url: https://github.com/lxc/incus/issues
- group: company
  title: ''
  type: Blog
  url: https://linuxcontainers.org/incus/news.rss
created: '2026-03-26'
description: Incus is a modern open source system container and virtual machine manager maintained by LinuxContainers.org as a community-led fork of Canonical's LXD. It provides a unified experience for running and managing system containers and VMs across single hosts and clusters, with image-based deployment, live migration, snapshots, projects, and a comprehensive RESTful API for automation and tooling integration.
finops:
- name: Incus Finops
  service_category: API
  slug: incus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/incus.png
layout: provider
modified: '2026-05-19'
name: Incus
nav: Providers
network: true
overview: 'Incus publishes 22 APIs on the [APIs.io](https://apis.io/) network, including certificates API, cluster API, cluster-groups API, and 19 more. Tagged areas include Containers, Virtual Machines, Virtualization, Linux, and Open Source.


  The Incus catalog on APIs.io includes 1 Spectral governance ruleset.


  Incus'' developer surface includes documentation, getting-started guide, engineering blog, and 6 more developer resources.'
plans:
- name: Incus Plans Pricing
  plan_count: 3
  slug: incus-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 5
  name: Incus Rate Limits
  slug: incus-rate-limits
rules:
- name: Incus API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: incus-rules
score:
  band: thin
  composite: 32.2
  delta: -3.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 32.3
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 10.4
    operational_transparency: 31.6
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/incus/refs/heads/main/screenshots/incus-2026-06-20T183310.png
security:
- kind: domain-security
  name: Incus Domain Security
  slug: incus-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: incus
tags:
- Containers
- Virtual Machines
- Virtualization
- Linux
- Open Source
website: https://linuxcontainers.org/incus/
---
