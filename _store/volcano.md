---
aid: volcano
url: https://raw.githubusercontent.com/api-evangelist/volcano/refs/heads/main/apis.yml
apis:
- aid: volcano:volcano-api
  name: Volcano Batch Scheduling API
  description: Volcano extends Kubernetes with CRDs for batch workload management. The Job resource defines batch workloads with multiple task types and lifecycle policies. Queue resources manage job scheduling with weight-based fair sharing and resource quotas. Volcano supports gang scheduling ensuring all pods in a group are scheduled together, and integrates with frameworks like TensorFlow, PyTorch, Spark, and MPI.
  humanURL: https://volcano.sh/en/docs/
  properties:
  - type: Documentation
    url: https://volcano.sh/en/docs/
  - type: Reference
    url: https://volcano.sh/en/docs/vcjob/
  - type: Getting Started
    url: https://volcano.sh/en/docs/installation/
  - type: OpenAPI
    url: openapi/volcano-job-openapi.yml
  - type: JSONSchema
    url: json-schema/volcano-job-schema.json
  tags:
  - Batch Scheduling
  - Gang Scheduling
  - Queues
- aid: volcano:volcano-queue-api
  name: Volcano Queue API
  description: Kubernetes CRD for defining and managing job queues in Volcano. Queues collect PodGroups and support weight-based fair-share scheduling and resource quotas, providing the primary mechanism for multi-tenant resource partitioning and priority-based job admission.
  humanURL: https://volcano.sh/en/docs/v1-10-0/queue/
  properties:
  - type: Documentation
    url: https://volcano.sh/en/docs/v1-10-0/queue/
  - type: OpenAPI
    url: openapi/volcano-queue-openapi.yml
  tags:
  - Batch Scheduling
  - Kubernetes
  - Multi-Tenancy
  - Queues
  - Resource Management
- aid: volcano:volcano-podgroup-api
  name: Volcano PodGroup API
  description: Kubernetes CRD that represents a group of pods with strong association, used as the unit of gang scheduling in Volcano. PodGroups define the minimum number of pods that must be scheduled together, enabling all-or-nothing scheduling semantics for distributed training and computing workloads.
  humanURL: https://volcano.sh/en/docs/podgroup/
  properties:
  - type: Documentation
    url: https://volcano.sh/en/docs/podgroup/
  - type: OpenAPI
    url: openapi/volcano-podgroup-openapi.yml
  tags:
  - Batch Scheduling
  - Distributed Computing
  - Gang Scheduling
  - Kubernetes
  - Pod Management
name: Volcano
tags:
- Batch Processing
- Cloud Native
- HPC
- Incubating
- Kubernetes
- Scheduling
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Volcano is a CNCF incubating batch processing and high-performance computing (HPC) scheduler for Kubernetes. It provides advanced scheduling capabilities including gang scheduling, fair-share scheduling, queue management, and job lifecycle management for batch workloads such as machine learning training, big data processing, and scientific computing.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

