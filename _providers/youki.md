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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: youki is a container runtime written in Rust that implements the OCI runtime specification, providing a memory-safe and high-performance alternative to runc. It supports rootless containers, cgroups v
  name: Youki Container Runtime
  slug: youki
- description: oci-spec-rs is a Rust implementation of the OCI Runtime, Image, and Distribution Specifications, providing the data structures and types consumed by youki and other Rust-based container tooling.
  name: OCI Spec for Rust
  slug: oci-spec-rs
artifact_total: 101
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/youki-dev/youki/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/youki-dev/youki/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/youki-dev/youki/blob/main/CODE-OF-CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/youki-dev/youki/blob/main/LICENSE
- group: docs
  title: ''
  type: Documentation
  url: https://youki-dev.github.io/youki/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/youki-dev
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/youki-dev/youki
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/youki-dev/youki/releases
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/youki-dev/youki/blob/main/CHANGELOG.md
- group: operate
  title: ''
  type: Support
  url: https://youki-dev.github.io/youki/community/introduction.html
- group: design
  title: Youki Vocabulary
  type: Vocabulary
  url: vocabulary/youki-vocabulary.yaml
created: '2026-03-26'
description: youki is an open source container runtime written in Rust that implements the OCI runtime specification as a memory-safe alternative to runc, with rootless container support, cgroups v1 and v2, seccomp filtering, and systemd integration. Maintained as a CNCF sandbox project under the youki-dev organization, youki is adopted by container engines such as containerd, Podman, and Docker for executing OCI-compliant workloads.
examples:
- key_count: 9
  name: Oci Image Config Example
  slug: oci-image-config-example
- key_count: 7
  name: Oci Image Content Descriptor Example
  slug: oci-image-content-descriptor-example
- key_count: 5
  name: Oci Image Defs Descriptor Example
  slug: oci-image-defs-descriptor-example
- key_count: 14
  name: Oci Image Defs Example
  slug: oci-image-defs-example
- key_count: 6
  name: Oci Image Index Example
  slug: oci-image-index-example
- key_count: 1
  name: Oci Image Layout Example
  slug: oci-image-layout-example
- key_count: 7
  name: Oci Image Manifest Example
  slug: oci-image-manifest-example
- key_count: 14
  name: Oci Runtime Config Example
  slug: oci-runtime-config-example
- key_count: 1
  name: Oci Runtime Config Freebsd Example
  slug: oci-runtime-config-freebsd-example
- key_count: 1
  name: Oci Runtime Config Linux Example
  slug: oci-runtime-config-linux-example
- key_count: 1
  name: Oci Runtime Config Solaris Example
  slug: oci-runtime-config-solaris-example
- key_count: 1
  name: Oci Runtime Config Vm Example
  slug: oci-runtime-config-vm-example
- key_count: 1
  name: Oci Runtime Config Windows Example
  slug: oci-runtime-config-windows-example
- key_count: 1
  name: Oci Runtime Config Zos Example
  slug: oci-runtime-config-zos-example
- key_count: 25
  name: Oci Runtime Defs Example
  slug: oci-runtime-defs-example
- key_count: 3
  name: Oci Runtime Defs Freebsd Example
  slug: oci-runtime-defs-freebsd-example
- key_count: 28
  name: Oci Runtime Defs Linux Example
  slug: oci-runtime-defs-linux-example
- key_count: 2
  name: Oci Runtime Defs Vm Example
  slug: oci-runtime-defs-vm-example
- key_count: 1
  name: Oci Runtime Defs Windows Example
  slug: oci-runtime-defs-windows-example
- key_count: 2
  name: Oci Runtime Defs Zos Example
  slug: oci-runtime-defs-zos-example
- key_count: 7
  name: Oci Runtime Features Example
  slug: oci-runtime-features-example
- key_count: 1
  name: Oci Runtime Features Linux Example
  slug: oci-runtime-features-linux-example
- key_count: 5
  name: Oci Runtime State Example
  slug: oci-runtime-state-example
features:
- description: Implements the Open Container Initiative (OCI) runtime specification, allowing youki to run any OCI-compliant container alongside or in place of runc.
  name: OCI Runtime Spec Compliance
- description: Written entirely in Rust to deliver memory safety and stronger isolation guarantees than C-based container runtimes.
  name: Memory-Safe Rust Implementation
- description: Enables running containers without root privileges to reduce host attack surface for development and multi-tenant scenarios.
  name: Rootless Containers
- description: Supports both legacy cgroups v1 and modern cgroups v2 hierarchies for resource management on Linux.
  name: Cgroups v1 and v2 Support
- description: Applies seccomp BPF filters to restrict syscalls available to containers and harden the runtime surface.
  name: Seccomp Filtering
- description: Integrates with systemd as a cgroup manager and supports systemd-managed container processes.
  name: Systemd Integration
- description: Manages mount, UTS, IPC, user, PID, network, and cgroup namespaces and supports capabilities such as CAP_BPF, CAP_PERFMON, and CAP_CHECKPOINT_RESTORE.
  name: Linux Namespaces and Capabilities
- description: Benchmarks show youki performing roughly twice as fast as runc for container create-to-delete cycles.
  name: Performance
- description: Maintained as a Cloud Native Computing Foundation sandbox project with open governance, public roadmap, and community contributors.
  name: CNCF Sandbox Project
finops:
- name: Youki Finops
  service_category: API
  slug: youki-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/youki.png
integrations:
- description: containerd has passed end-to-end testing against youki, enabling its use as the OCI runtime for Kubernetes and other workloads orchestrated by containerd.
  name: containerd
- description: Podman can be configured to use youki as its OCI runtime for both rootless and rootful container execution.
  name: Podman
- description: Docker can call youki as the low-level OCI runtime in place of runc for compatible workloads via daemon.json configuration.
  name: Docker
- description: Kubernetes clusters can run youki indirectly through container runtimes such as containerd or CRI-O.
  name: Kubernetes
- description: youki sits alongside crun as a modern alternative to runc, focused on memory-safe systems programming in Rust.
  name: crun
- description: Integrates with systemd for cgroup management and lifecycle control of container processes.
  name: systemd
- description: Built on oci-spec-rs, the Rust implementation of the OCI Runtime, Image, and Distribution specifications maintained by the same organization.
  name: oci-spec-rs
json_schemas:
- name: Oci Image Config
  property_count: 10
  slug: oci-image-config
- name: Oci Image Content Descriptor
  property_count: 7
  slug: oci-image-content-descriptor
- name: Oci Image Defs Descriptor
  property_count: 0
  slug: oci-image-defs-descriptor
- name: Oci Image Defs
  property_count: 0
  slug: oci-image-defs
- name: Oci Image Index
  property_count: 6
  slug: oci-image-index
- name: Oci Image Layout
  property_count: 1
  slug: oci-image-layout
- name: Oci Image Manifest
  property_count: 7
  slug: oci-image-manifest
- name: Oci Runtime Config Freebsd
  property_count: 0
  slug: oci-runtime-config-freebsd
- name: Oci Runtime Config Linux
  property_count: 0
  slug: oci-runtime-config-linux
- name: Oci Runtime Config
  property_count: 14
  slug: oci-runtime-config
- name: Oci Runtime Config Solaris
  property_count: 0
  slug: oci-runtime-config-solaris
- name: Oci Runtime Config Vm
  property_count: 0
  slug: oci-runtime-config-vm
- name: Oci Runtime Config Windows
  property_count: 0
  slug: oci-runtime-config-windows
- name: Oci Runtime Config Zos
  property_count: 0
  slug: oci-runtime-config-zos
- name: Oci Runtime Defs Freebsd
  property_count: 0
  slug: oci-runtime-defs-freebsd
- name: Oci Runtime Defs Linux
  property_count: 0
  slug: oci-runtime-defs-linux
- name: Oci Runtime Defs Vm
  property_count: 0
  slug: oci-runtime-defs-vm
- name: Oci Runtime Defs Windows
  property_count: 0
  slug: oci-runtime-defs-windows
- name: Oci Runtime Defs Zos
  property_count: 0
  slug: oci-runtime-defs-zos
- name: Oci Runtime Defs
  property_count: 0
  slug: oci-runtime-defs
- name: Oci Runtime Features Linux
  property_count: 0
  slug: oci-runtime-features-linux
- name: Oci Runtime Features
  property_count: 7
  slug: oci-runtime-features
- name: Oci Runtime State
  property_count: 6
  slug: oci-runtime-state
json_structures:
- name: Oci Image Config Structure
  property_count: 10
  slug: oci-image-config-structure
- name: Oci Image Content Descriptor Structure
  property_count: 7
  slug: oci-image-content-descriptor-structure
- name: Oci Image Defs Descriptor Structure
  property_count: 0
  slug: oci-image-defs-descriptor-structure
- name: Oci Image Defs Structure
  property_count: 0
  slug: oci-image-defs-structure
- name: Oci Image Index Structure
  property_count: 6
  slug: oci-image-index-structure
- name: Oci Image Layout Structure
  property_count: 1
  slug: oci-image-layout-structure
- name: Oci Image Manifest Structure
  property_count: 7
  slug: oci-image-manifest-structure
- name: Oci Runtime Config Freebsd Structure
  property_count: 0
  slug: oci-runtime-config-freebsd-structure
- name: Oci Runtime Config Linux Structure
  property_count: 0
  slug: oci-runtime-config-linux-structure
- name: Oci Runtime Config Solaris Structure
  property_count: 0
  slug: oci-runtime-config-solaris-structure
- name: Oci Runtime Config Structure
  property_count: 14
  slug: oci-runtime-config-structure
- name: Oci Runtime Config Vm Structure
  property_count: 0
  slug: oci-runtime-config-vm-structure
- name: Oci Runtime Config Windows Structure
  property_count: 0
  slug: oci-runtime-config-windows-structure
- name: Oci Runtime Config Zos Structure
  property_count: 0
  slug: oci-runtime-config-zos-structure
- name: Oci Runtime Defs Freebsd Structure
  property_count: 0
  slug: oci-runtime-defs-freebsd-structure
- name: Oci Runtime Defs Linux Structure
  property_count: 0
  slug: oci-runtime-defs-linux-structure
- name: Oci Runtime Defs Structure
  property_count: 0
  slug: oci-runtime-defs-structure
- name: Oci Runtime Defs Vm Structure
  property_count: 0
  slug: oci-runtime-defs-vm-structure
- name: Oci Runtime Defs Windows Structure
  property_count: 0
  slug: oci-runtime-defs-windows-structure
- name: Oci Runtime Defs Zos Structure
  property_count: 0
  slug: oci-runtime-defs-zos-structure
- name: Oci Runtime Features Linux Structure
  property_count: 0
  slug: oci-runtime-features-linux-structure
- name: Oci Runtime Features Structure
  property_count: 7
  slug: oci-runtime-features-structure
- name: Oci Runtime State Structure
  property_count: 6
  slug: oci-runtime-state-structure
jsonld:
- class_count: 7
  name: Youki Oci Image Context
  property_count: 38
  slug: youki-oci-image-context
- class_count: 20
  name: Youki Oci Runtime Context
  property_count: 106
  slug: youki-oci-runtime-context
layout: provider
modified: '2026-05-03'
name: Youki
nav: Providers
network: true
overview: 'Youki publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Containers, Container Runtime, OCI, Rust, and CNCF.


  The Youki catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Youki''s developer surface includes documentation, release notes, changelog, support, and 7 more developer resources.'
plans:
- name: Youki Plans Pricing
  plan_count: 3
  slug: youki-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Youki Rate Limits
  slug: youki-rate-limits
rules:
- effective_rule_count: 3
  extends: []
  name: Youki API Rules
  rule_count: 3
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 1
  slug: youki-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 70.3
    catalog_earned_first_party: 0.0
    catalog_gap: 44.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 34.7
    developer_ergonomics: 42.9
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 75.0
  previous_composite: 38.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
slug: youki
solutions:
- description: Provides a CNCF sandbox container runtime for cloud-native platforms looking to adopt a memory-safe OCI runtime under containerd or CRI-O.
  name: Cloud Native Container Platforms
- description: Pairs rootless containers, seccomp filtering, and Rust memory safety to harden multi-tenant container hosts against runtime exploits.
  name: Secure Multi-Tenant Hosts
- description: A lightweight, high-performance runtime suitable for edge and embedded deployments where resource use and predictable performance matter.
  name: Edge and Embedded Workloads
tags:
- Containers
- Container Runtime
- OCI
- Rust
- CNCF
- Cloud-Native
- Kubernetes
use_cases:
- description: Use youki as a drop-in replacement for runc in container engines to gain memory safety and performance benefits with no workload changes.
  name: Drop-In runc Replacement
- description: Run containers as a non-root user for development, CI, or multi-tenant environments where elevated privileges are not desirable.
  name: Rootless Container Workflows
- description: Use youki under containerd to execute Kubernetes pods and workloads in production clusters.
  name: Kubernetes Workloads via containerd
- description: Configure Podman or Docker to invoke youki as the low-level OCI runtime for image execution.
  name: Podman and Docker Container Execution
- description: Explore and prototype container runtime features in a memory-safe codebase suitable for systems research, security analysis, and teaching.
  name: Container Runtime Research and Education
---
