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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 29
  human_in_the_loop: 1
  name: Firecracker Agentic Access
  operation_count: 38
  slug: firecracker-agentic-access
  summary_line: 38 operations · 29 acting · 1 human-in-the-loop
api_count: 19
apis:
- description: The Actions API from Firecracker — 1 operation(s) for actions.
  name: Firecracker Actions API
  slug: firecracker-actions-api
- description: The Balloon API from Firecracker — 5 operation(s) for balloon.
  name: Firecracker Balloon API
  slug: firecracker-balloon-api
- description: The Boot Source API from Firecracker — 1 operation(s) for boot source.
  name: Firecracker Boot Source API
  slug: firecracker-boot-source-api
- description: The Cpu Config API from Firecracker — 1 operation(s) for cpu config.
  name: Firecracker Cpu Config API
  slug: firecracker-cpu-config-api
- description: The Drives API from Firecracker — 1 operation(s) for drives.
  name: Firecracker Drives API
  slug: firecracker-drives-api
- description: The Entropy API from Firecracker — 1 operation(s) for entropy.
  name: Firecracker Entropy API
  slug: firecracker-entropy-api
- description: The Firecracker API API from Firecracker — 1 operation(s) for firecracker api.
  name: Firecracker Firecracker API API
  slug: firecracker-firecracker-api-api
- description: The Hotplug API from Firecracker — 1 operation(s) for hotplug.
  name: Firecracker Hotplug API
  slug: firecracker-hotplug-api
- description: The Logger API from Firecracker — 1 operation(s) for logger.
  name: Firecracker Logger API
  slug: firecracker-logger-api
- description: The Machine Config API from Firecracker — 1 operation(s) for machine config.
  name: Firecracker Machine Config API
  slug: firecracker-machine-config-api
- description: The Metrics API from Firecracker — 1 operation(s) for metrics.
  name: Firecracker Metrics API
  slug: firecracker-metrics-api
- description: The Mmds API from Firecracker — 2 operation(s) for mmds.
  name: Firecracker Mmds API
  slug: firecracker-mmds-api
- description: The Network Interfaces API from Firecracker — 1 operation(s) for network interfaces.
  name: Firecracker Network Interfaces API
  slug: firecracker-network-interfaces-api
- description: The Pmem API from Firecracker — 1 operation(s) for pmem.
  name: Firecracker Pmem API
  slug: firecracker-pmem-api
- description: The Serial API from Firecracker — 1 operation(s) for serial.
  name: Firecracker Serial API
  slug: firecracker-serial-api
- description: The Snapshot API from Firecracker — 2 operation(s) for snapshot.
  name: Firecracker Snapshot API
  slug: firecracker-snapshot-api
- description: The Version API from Firecracker — 1 operation(s) for version.
  name: Firecracker Version API
  slug: firecracker-version-api
- description: The Vm API from Firecracker — 2 operation(s) for vm.
  name: Firecracker Vm API
  slug: firecracker-vm-api
- description: The Vsock API from Firecracker — 1 operation(s) for vsock.
  name: Firecracker Vsock API
  slug: firecracker-vsock-api
artifact_total: 23
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/firecracker-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://firecracker-microvm.github.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/firecracker-microvm
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/firecracker-microvm/firecracker
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/firecracker-microvm/firecracker/tree/main/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/firecracker-microvm/firecracker/blob/main/docs/getting-started.md
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/firecracker-microvm/firecracker/blob/main/CHANGELOG.md
- group: operate
  title: ''
  type: FAQ
  url: https://github.com/firecracker-microvm/firecracker/blob/main/FAQ.md
- group: auth
  title: ''
  type: Security
  url: https://github.com/firecracker-microvm/firecracker/blob/main/SECURITY.md
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/opensource/tag/firecracker/
- group: operate
  title: ''
  type: Slack
  url: https://join.slack.com/t/firecracker-microvm/shared_invite/zt-2tc0mfxpc-tU~HYAYSzLDl5XGGJU3YIg
- group: other
  title: ''
  type: Email
  url: mailto:firecracker-maintainers@amazon.com
created: '2026-03-26'
description: Firecracker is an open source virtual machine monitor (VMM) built by Amazon Web Services that uses KVM to create and manage lightweight microVMs. Designed for serverless computing and container workloads, it provides the security and isolation of traditional VMs with the speed and resource efficiency of containers. Firecracker exposes a RESTful management API over a Unix Domain Socket, specified in OpenAPI (Swagger 2.0).
finops:
- name: Firecracker Finops
  service_category: API
  slug: firecracker-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/firecracker.png
layout: provider
modified: '2026-05-19'
name: Firecracker
nav: Providers
network: true
overview: 'Firecracker publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Balloon API, Boot Source API, and 16 more. Tagged areas include Containers, MicroVMs, Open Source, Serverless, and Virtualization.


  Firecracker''s developer surface includes documentation, getting-started guide, changelog, FAQ, engineering blog, and 7 more developer resources.'
plans:
- name: Firecracker Plans Pricing
  plan_count: 3
  slug: firecracker-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 5
  name: Firecracker Rate Limits
  slug: firecracker-rate-limits
score:
  band: thin
  composite: 38.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 37.7
    developer_ergonomics: 21.7
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 63.2
  previous_composite: 38.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/firecracker/refs/heads/main/screenshots/firecracker-2026-06-20T181228.png
slug: firecracker
tags:
- Containers
- MicroVMs
- Open Source
- Serverless
- Virtualization
- KVM
website: https://firecracker-microvm.github.io/
---
