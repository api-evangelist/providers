---
aid: akri
url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/apis.yml
name: Akri
tags:
  - Device Management
  - Edge Computing
  - IoT
  - Kubernetes
  - CNCF
  - Open Source
  - OPC UA
  - ONVIF
  - udev
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
description: Akri is a CNCF Sandbox project that exposes heterogeneous leaf devices (such as IP cameras and USB devices) as resources in a Kubernetes cluster. It enables dynamic discovery and utilization of IoT edge devices through protocol-specific Discovery Handlers for ONVIF, OPC UA, and udev, with automatic workload scheduling and high availability.
created: '2025-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: akri:metrics-api
    name: Akri Metrics API
    tags:
      - Monitoring
      - Prometheus
      - Metrics
      - Observability
    properties:
      - url: https://docs.akri.sh/
        type: Documentation
      - url: https://github.com/project-akri/akri
        type: GitHubRepository
      - url: openapi/akri-metrics-openapi.yaml
        type: OpenAPI
      - url: json-schema/akri-prometheus-metrics-schema.json
        type: JSONSchema
      - url: json-schema/akri-akri-instance-count-schema.json
        type: JSONSchema
      - url: json-schema/akri-akri-discovery-response-result-schema.json
        type: JSONSchema
      - url: json-schema/akri-akri-discovery-response-time-schema.json
        type: JSONSchema
      - url: json-schema/akri-akri-broker-pod-count-schema.json
        type: JSONSchema
      - url: json-schema/akri-akri-configuration-schema.json
        type: JSONSchema
      - url: json-schema/akri-akri-instance-schema.json
        type: JSONSchema
      - url: json-structure/akri-prometheus-metrics-structure.json
        type: JSONStructure
      - url: json-structure/akri-akri-instance-count-structure.json
        type: JSONStructure
      - url: json-structure/akri-akri-discovery-response-result-structure.json
        type: JSONStructure
      - url: json-structure/akri-akri-discovery-response-time-structure.json
        type: JSONStructure
      - url: json-structure/akri-akri-broker-pod-count-structure.json
        type: JSONStructure
      - url: json-structure/akri-akri-configuration-structure.json
        type: JSONStructure
      - url: json-structure/akri-akri-instance-structure.json
        type: JSONStructure
      - url: examples/akri-prometheus-metrics-example.json
        type: Example
      - url: examples/akri-akri-instance-count-example.json
        type: Example
      - url: examples/akri-akri-discovery-response-result-example.json
        type: Example
      - url: examples/akri-akri-discovery-response-time-example.json
        type: Example
      - url: examples/akri-akri-broker-pod-count-example.json
        type: Example
      - url: examples/akri-akri-configuration-example.json
        type: Example
      - url: examples/akri-akri-instance-example.json
        type: Example
    humanURL: https://docs.akri.sh/
    baseURL: http://localhost:8080
    description: Akri exposes Prometheus metrics on port 8080 at /metrics for the Agent, Controller, and broker pods. Metrics include instance count, discovery response results and latency, and broker pod count. Supports Prometheus Operator ServiceMonitor for metric scraping.
common:
  - url: https://github.com/project-akri
    type: GitHubOrganization
  - url: https://github.com/project-akri/akri
    type: GitHubRepository
  - url: https://docs.akri.sh/
    type: Documentation
  - url: https://docs.akri.sh/user-guide/getting-started
    type: GettingStarted
  - url: https://github.com/project-akri/akri/blob/main/CHANGELOG.md
    type: ChangeLog
  - url: https://artifacthub.io/packages/helm/akri-helm-charts/akri
    type: SDK
    title: Helm Chart
  - url: https://github.com/project-akri/examples
    type: CodeExamples
    title: Example Brokers and Applications
  - url: https://github.com/project-akri/akri-discovery-handler-template
    type: SDK
    title: Discovery Handler Template (Rust)
  - url: rules/akri-spectral-rules.yml
    type: SpectralRules
  - url: vocabulary/akri-vocabulary.yaml
    type: Vocabulary
  - url: json-ld/akri-akri-context.jsonld
    type: JSONLD
  - url: capabilities/shared/metrics.yaml
    type: NaftikoCapability
    title: Akri Metrics Shared Capability
  - url: capabilities/edge-device-monitoring.yaml
    type: NaftikoCapability
    title: Edge Device Monitoring Workflow
  - type: Features
    data:
      - name: Dynamic Device Discovery
        description: Automatically discovers heterogeneous leaf devices (IP cameras, USB devices, industrial sensors) across Kubernetes cluster nodes using protocol-specific Discovery Handlers.
      - name: ONVIF Discovery Handler
        description: Discovers IP cameras via ONVIF standards and RTSP streams, with filtering by IP address, MAC address, ONVIF scopes, and device UUIDs.
      - name: OPC UA Discovery Handler
        description: Discovers industrial automation servers and Local Discovery Servers via OPC UA protocol, supporting x509 certificate authentication for secure connections.
      - name: udev Discovery Handler
        description: Discovers locally attached hardware (USB devices, cameras, microphones) on Linux nodes using udev rules with kernel device name and capability filtering.
      - name: Automatic Workload Scheduling
        description: Automatically schedules broker Pods or Jobs per discovered device based on Akri Configuration specifications, managing the full workload lifecycle.
      - name: High Availability
        description: Multiple nodes can access a single leaf device, ensuring service continuity if a node fails. Supports multi-node device reservation.
      - name: Kubernetes Custom Resources
        description: 'Two CRDs: configurations.akri.sh for discovery specification and instances.akri.sh representing each discovered device as a Kubernetes resource.'
      - name: Extensible Discovery Handler Framework
        description: Community can implement custom Discovery Handlers as DaemonSets using the akri-discovery-handler-template, enabling support for any device protocol.
      - name: Prometheus Metrics
        description: Built-in Prometheus metrics on port 8080 for instance count, discovery response results, discovery latency, and broker pod count, with Grafana visualization support.
      - name: Multi-Architecture Support
        description: Supports Linux nodes on amd64, arm64v8, and arm32v7 architectures with Kubernetes v1.16+, K3s, and MicroK8s distributions.
  - type: UseCases
    data:
      - name: Edge IoT Device Management
        description: Expose and manage IoT leaf devices such as IP cameras and USB sensors as first-class Kubernetes resources for edge computing workloads.
      - name: Industrial Automation Integration
        description: Connect industrial OPC UA servers and automation equipment to Kubernetes clusters for real-time monitoring and control workflows.
      - name: Computer Vision at the Edge
        description: Deploy ONVIF-compliant IP camera brokers automatically as cameras are discovered, enabling distributed computer vision processing.
      - name: Dynamic Hardware Resource Scheduling
        description: Automatically schedule GPU, FPGA, or specialized hardware workloads based on real-time device availability across cluster nodes.
      - name: Heterogeneous Device Fleet Management
        description: Manage fleets of diverse edge devices with different protocols from a single Kubernetes control plane using unified Configuration resources.
  - type: Integrations
    data:
      - name: Prometheus
        description: Native Prometheus metrics integration via ServiceMonitor and PodMonitor custom resources, with Grafana visualization support.
      - name: Helm
        description: Official Helm chart packaging for deploying Akri Controller, Agent DaemonSet, and Discovery Handler DaemonSets.
      - name: Kubernetes Device Plugin Framework
        description: Extends the Kubernetes Device Plugin Framework with edge-specific capabilities for heterogeneous leaf device management.
      - name: ONVIF
        description: Built-in ONVIF protocol support for discovering and managing standards-compliant IP cameras and video devices.
      - name: OPC UA
        description: Built-in OPC UA protocol support for industrial automation device discovery with certificate-based security.
      - name: Linux udev
        description: Built-in udev integration for discovering locally attached hardware devices on Linux Kubernetes nodes.
      - name: CNCF Ecosystem
        description: CNCF Sandbox project integrating with cloud native tooling including K3s, MicroK8s, and standard Kubernetes distributions.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
