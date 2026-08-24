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
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.6
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Akri Agentic Access
  operation_count: 1
  slug: akri-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Prometheus metrics endpoints for Akri Agent, Controller, and broker pods
  name: Akri Metrics API
  slug: akri-metrics-api
artifact_total: 53
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Akri Metrics API
  slug: open-akri-metrics-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/project-akri/akri/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/project-akri/akri/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/project-akri/akri/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/project-akri/akri/blob/main/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/project-akri/akri/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/akri-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/akri-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/project-akri
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/project-akri/akri
- group: docs
  title: ''
  type: Documentation
  url: https://docs.akri.sh/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.akri.sh/user-guide/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/project-akri/akri/blob/main/CHANGELOG.md
- group: build
  title: Helm Chart
  type: SDKs
  url: https://artifacthub.io/packages/helm/akri-helm-charts/akri
- group: build
  title: Example Brokers and Applications
  type: CodeExamples
  url: https://github.com/project-akri/examples
- group: build
  title: Discovery Handler Template (Rust)
  type: SDKs
  url: https://github.com/project-akri/akri-discovery-handler-template
- group: design
  title: ''
  type: SpectralRules
  url: rules/akri-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/akri-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/akri-akri-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.akri.sh/llms.txt
created: '2025-01-01'
description: Akri is a CNCF Sandbox project that exposes heterogeneous leaf devices (such as IP cameras and USB devices) as resources in a Kubernetes cluster. It enables dynamic discovery and utilization of IoT edge devices through protocol-specific Discovery Handlers for ONVIF, OPC UA, and udev, with automatic workload scheduling and high availability.
examples:
- key_count: 3
  name: Akri Akri Broker Pod Count Example
  slug: akri-akri-broker-pod-count-example
- key_count: 4
  name: Akri Akri Configuration Example
  slug: akri-akri-configuration-example
- key_count: 3
  name: Akri Akri Discovery Response Result Example
  slug: akri-akri-discovery-response-result-example
- key_count: 3
  name: Akri Akri Discovery Response Time Example
  slug: akri-akri-discovery-response-time-example
- key_count: 3
  name: Akri Akri Instance Count Example
  slug: akri-akri-instance-count-example
- key_count: 4
  name: Akri Akri Instance Example
  slug: akri-akri-instance-example
features:
- description: Automatically discovers heterogeneous leaf devices (IP cameras, USB devices, industrial sensors) across Kubernetes cluster nodes using protocol-specific Discovery Handlers.
  name: Dynamic Device Discovery
- description: Discovers IP cameras via ONVIF standards and RTSP streams, with filtering by IP address, MAC address, ONVIF scopes, and device UUIDs.
  name: ONVIF Discovery Handler
- description: Discovers industrial automation servers and Local Discovery Servers via OPC UA protocol, supporting x509 certificate authentication for secure connections.
  name: OPC UA Discovery Handler
- description: Discovers locally attached hardware (USB devices, cameras, microphones) on Linux nodes using udev rules with kernel device name and capability filtering.
  name: udev Discovery Handler
- description: Automatically schedules broker Pods or Jobs per discovered device based on Akri Configuration specifications, managing the full workload lifecycle.
  name: Automatic Workload Scheduling
- description: Multiple nodes can access a single leaf device, ensuring service continuity if a node fails. Supports multi-node device reservation.
  name: High Availability
- description: 'Two CRDs: configurations.akri.sh for discovery specification and instances.akri.sh representing each discovered device as a Kubernetes resource.'
  name: Kubernetes Custom Resources
- description: Community can implement custom Discovery Handlers as DaemonSets using the akri-discovery-handler-template, enabling support for any device protocol.
  name: Extensible Discovery Handler Framework
- description: Built-in Prometheus metrics on port 8080 for instance count, discovery response results, discovery latency, and broker pod count, with Grafana visualization support.
  name: Prometheus Metrics
- description: Supports Linux nodes on amd64, arm64v8, and arm32v7 architectures with Kubernetes v1.16+, K3s, and MicroK8s distributions.
  name: Multi-Architecture Support
finops:
- name: Akri Finops
  service_category: API
  slug: akri-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/akri.png
integrations:
- description: Native Prometheus metrics integration via ServiceMonitor and PodMonitor custom resources, with Grafana visualization support.
  name: Prometheus
- description: Official Helm chart packaging for deploying Akri Controller, Agent DaemonSet, and Discovery Handler DaemonSets.
  name: Helm
- description: Extends the Kubernetes Device Plugin Framework with edge-specific capabilities for heterogeneous leaf device management.
  name: Kubernetes Device Plugin Framework
- description: Built-in ONVIF protocol support for discovering and managing standards-compliant IP cameras and video devices.
  name: ONVIF
- description: Built-in OPC UA protocol support for industrial automation device discovery with certificate-based security.
  name: OPC UA
- description: Built-in udev integration for discovering locally attached hardware devices on Linux Kubernetes nodes.
  name: Linux udev
- description: CNCF Sandbox project integrating with cloud native tooling including K3s, MicroK8s, and standard Kubernetes distributions.
  name: CNCF Ecosystem
json_schemas:
- name: AkriBrokerPodCount
  property_count: 3
  slug: akri-akri-broker-pod-count
- name: AkriConfiguration
  property_count: 4
  slug: akri-akri-configuration
- name: AkriDiscoveryResponseResult
  property_count: 3
  slug: akri-akri-discovery-response-result
- name: AkriDiscoveryResponseTime
  property_count: 3
  slug: akri-akri-discovery-response-time
- name: AkriInstanceCount
  property_count: 3
  slug: akri-akri-instance-count
- name: AkriInstance
  property_count: 4
  slug: akri-akri-instance
- name: PrometheusMetrics
  property_count: 0
  slug: akri-prometheus-metrics
json_structures:
- name: Akri Akri Broker Pod Count Structure
  property_count: 3
  slug: akri-akri-broker-pod-count-structure
- name: Akri Akri Configuration Structure
  property_count: 4
  slug: akri-akri-configuration-structure
- name: Akri Akri Discovery Response Result Structure
  property_count: 3
  slug: akri-akri-discovery-response-result-structure
- name: Akri Akri Discovery Response Time Structure
  property_count: 3
  slug: akri-akri-discovery-response-time-structure
- name: Akri Akri Instance Count Structure
  property_count: 3
  slug: akri-akri-instance-count-structure
- name: Akri Akri Instance Structure
  property_count: 4
  slug: akri-akri-instance-structure
- name: Akri Prometheus Metrics Structure
  property_count: 0
  slug: akri-prometheus-metrics-structure
jsonld:
- class_count: 6
  name: Akri Akri Context
  property_count: 19
  slug: akri-akri-context
layout: provider
modified: '2026-05-19'
name: Akri
nav: Providers
network: true
overview: 'Akri publishes 1 API on the [APIs.io](https://apis.io/) network: Metrics API. Tagged areas include Device Management, Edge Computing, IoT, Kubernetes, and CNCF.


  The Akri catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Akri''s developer surface includes documentation, getting-started guide, changelog, code examples, and 15 more developer resources.'
plans:
- name: Akri Plans Pricing
  plan_count: 3
  slug: akri-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Akri Rate Limits
  slug: akri-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Akri API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: akri-jsonschema-spectral-rules
- effective_rule_count: 68
  extends:
  - spectral:oas
  name: Akri API Rules
  rule_count: 27
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 14
  slug: akri-spectral-rules
score:
  band: thin
  composite: 27.6
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 28.8
    contract_quality: 26.4
    developer_ergonomics: 28.6
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 39.5
  previous_composite: 27.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/screenshots/akri-2026-06-20T171456.png
security:
- kind: domain-security
  name: Akri Domain Security
  slug: akri-domain-security
  summary_line: TLSv1.3 · HSTS
slug: akri
tags:
- Device Management
- Edge Computing
- IoT
- Kubernetes
- CNCF
- Open-Source
- OPC UA
- ONVIF
- udev
use_cases:
- description: Expose and manage IoT leaf devices such as IP cameras and USB sensors as first-class Kubernetes resources for edge computing workloads.
  name: Edge IoT Device Management
- description: Connect industrial OPC UA servers and automation equipment to Kubernetes clusters for real-time monitoring and control workflows.
  name: Industrial Automation Integration
- description: Deploy ONVIF-compliant IP camera brokers automatically as cameras are discovered, enabling distributed computer vision processing.
  name: Computer Vision at the Edge
- description: Automatically schedule GPU, FPGA, or specialized hardware workloads based on real-time device availability across cluster nodes.
  name: Dynamic Hardware Resource Scheduling
- description: Manage fleets of diverse edge devices with different protocols from a single Kubernetes control plane using unified Configuration resources.
  name: Heterogeneous Device Fleet Management
---
