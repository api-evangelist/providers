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
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Weave Net Agentic Access
  operation_count: 13
  slug: weave-net-agentic-access
  summary_line: 13 operations · 9 acting
api_count: 5
apis:
- description: The DNS API from Weave Net — 2 operation(s) for dns.
  name: Weave Net DNS API
  slug: weave-net-dns-api
- description: The IPAM API from Weave Net — 3 operation(s) for ipam.
  name: Weave Net IPAM API
  slug: weave-net-ipam-api
- description: The Network API from Weave Net — 1 operation(s) for network.
  name: Weave Net Network API
  slug: weave-net-network-api
- description: The Peers API from Weave Net — 2 operation(s) for peers.
  name: Weave Net Peers API
  slug: weave-net-peers-api
- description: The Status API from Weave Net — 1 operation(s) for status.
  name: Weave Net Status API
  slug: weave-net-status-api
artifact_total: 51
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Weave Net HTTP DNS API
  slug: open-weave-net-dns-api
- collection_type: open
  name: Weave Net HTTP DNS IPAM API
  slug: open-weave-net-ipam-api
- collection_type: open
  name: Weave Net HTTP DNS Network API
  slug: open-weave-net-network-api
- collection_type: open
  name: Weave Net HTTP DNS Peers API
  slug: open-weave-net-peers-api
- collection_type: open
  name: Weave Net HTTP DNS Status API
  slug: open-weave-net-status-api
- collection_type: open
  name: Weave Net HTTP API
  slug: open-weave-net
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/weave-net-agentic-access.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/weaveworks
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/weaveworks/weave
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/weaveworks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/weaveworks/weave/blob/master/LICENSE
- group: auth
  title: ''
  type: Security
  url: https://github.com/weaveworks/weave/blob/master/SECURITY.md
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/weaveworks/weave/blob/master/CHANGELOG.md
- group: operate
  title: ''
  type: Support
  url: https://github.com/weaveworks/weave/issues
- group: design
  title: ''
  type: SpectralRules
  url: rules/weave-net-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/weave-net-vocabulary.yml
created: '2026-03-26'
description: Weave Net is an open source container networking plugin that creates a virtual network connecting Docker containers and Kubernetes pods across multiple hosts. It provides automatic IP address management (IPAM), DNS resolution via WeaveDNS, network policy enforcement, and optional encryption for container-to-container communication. The Weave Net daemon exposes a local HTTP API on port 6784 for programmatic network management. Weave Net is maintained by Weaveworks and is archived but remains widely used in production environments.
examples:
- key_count: 2
  name: Weave Net Connect Request Example
  slug: weave-net-connect-request-example
- key_count: 3
  name: Weave Net Connection Info Example
  slug: weave-net-connection-info-example
- key_count: 2
  name: Weave Net Dns Status Example
  slug: weave-net-dns-status-example
- key_count: 4
  name: Weave Net Ipam Status Example
  slug: weave-net-ipam-status-example
- key_count: 3
  name: Weave Net Peer Info Example
  slug: weave-net-peer-info-example
- key_count: 3
  name: Weave Net Router Status Example
  slug: weave-net-router-status-example
- key_count: 1
  name: Weave Net Status Response Example
  slug: weave-net-status-response-example
features:
- description: Creates a virtual network connecting containers across multiple hosts without requiring any configuration of the physical network.
  name: Container Overlay Network
- description: Automatically allocates IP addresses to containers from a configurable subnet using distributed consensus.
  name: Automatic IPAM
- description: Built-in DNS resolution for containers by hostname, making services discoverable by name on the Weave network.
  name: WeaveDNS
- description: Optional encryption of all network traffic using NaCl for secure container-to-container communication.
  name: Network Encryption
- description: Native Kubernetes CNI plugin for pod-to-pod networking across nodes.
  name: Kubernetes Integration
- description: Docker network plugin for seamless multi-host Docker container networking.
  name: Docker Integration
- description: Kernel-level packet forwarding using Open vSwitch for high-performance networking.
  name: Fast Datapath
finops:
- name: Weave Net Finops
  service_category: API
  slug: weave-net-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/weave-net.png
json_schemas:
- name: ConnectRequest
  property_count: 2
  slug: weave-net-connect-request
- name: ConnectionInfo
  property_count: 3
  slug: weave-net-connection-info
- name: DNSStatus
  property_count: 2
  slug: weave-net-dns-status
- name: IPAMStatus
  property_count: 4
  slug: weave-net-ipam-status
- name: PeerInfo
  property_count: 3
  slug: weave-net-peer-info
- name: RouterStatus
  property_count: 3
  slug: weave-net-router-status
- name: StatusResponse
  property_count: 4
  slug: weave-net-status-response
json_structures:
- name: Weave Net Connect Request Structure
  property_count: 2
  slug: weave-net-connect-request-structure
- name: Weave Net Connection Info Structure
  property_count: 3
  slug: weave-net-connection-info-structure
- name: Weave Net Dns Status Structure
  property_count: 2
  slug: weave-net-dns-status-structure
- name: Weave Net Ipam Status Structure
  property_count: 4
  slug: weave-net-ipam-status-structure
- name: Weave Net Peer Info Structure
  property_count: 3
  slug: weave-net-peer-info-structure
- name: Weave Net Router Status Structure
  property_count: 3
  slug: weave-net-router-status-structure
- name: Weave Net Status Response Structure
  property_count: 4
  slug: weave-net-status-response-structure
jsonld:
- class_count: 8
  name: Weave Net Context
  property_count: 19
  slug: weave-net-context
layout: provider
modified: '2026-05-19'
name: Weave Net
nav: Providers
network: true
overview: 'Weave Net publishes 5 APIs on the [APIs.io](https://apis.io/) network, including DNS API, IPAM API, Network API, and 2 more. Tagged areas include Containers, Networking, Kubernetes, Docker, and IPAM.


  The Weave Net catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Weave Net''s developer surface includes changelog, support, and 8 more developer resources.'
plans:
- name: Weave Net Plans Pricing
  plan_count: 3
  slug: weave-net-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Weave Net Rate Limits
  slug: weave-net-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Weave Net API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: weave-net-jsonschema-spectral-rules
- effective_rule_count: 68
  extends:
  - spectral:oas
  name: Weave Net API Rules
  rule_count: 27
  severity_counts:
    error: 8
    hint: 0
    info: 6
    warn: 13
  slug: weave-net-spectral-rules
score:
  band: emerging
  composite: 26.0
  delta: -5.5
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 25.0
    contract_quality: 20.6
    developer_ergonomics: 4.8
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 39.5
  previous_composite: 31.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/weave-net/refs/heads/main/screenshots/weave-net-2026-06-20T201316.png
slug: weave-net
tags:
- Containers
- Networking
- Kubernetes
- Docker
- IPAM
- Open Source
- CNCF
use_cases:
- description: Connect Docker containers across multiple physical or virtual machines without complex network configuration.
  name: Multi-Host Docker Networking
- description: Provide pod-to-pod networking for Kubernetes clusters as a CNI-compliant network plugin.
  name: Kubernetes Pod Networking
- description: Automate container IP allocation and release in orchestration workflows.
  name: Automated IP Management
- description: Enable container service discovery by DNS name using WeaveDNS.
  name: Service Discovery
---
