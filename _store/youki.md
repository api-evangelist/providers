---
aid: youki
name: Youki
description: youki is an open source container runtime written in Rust that implements the OCI runtime specification as a memory-safe alternative to runc, with rootless container support, cgroups v1 and v2, seccomp filtering, and systemd integration. Maintained as a CNCF sandbox project under the youki-dev organization, youki is adopted by container engines such as containerd, Podman, and Docker for executing OCI-compliant workloads.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Containers
  - Container Runtime
  - OCI
  - Rust
  - CNCF
  - Cloud Native
  - Kubernetes
url: https://raw.githubusercontent.com/api-evangelist/youki/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: youki:youki
    name: Youki Container Runtime
    description: youki is a container runtime written in Rust that implements the OCI runtime specification, providing a memory-safe and high-performance alternative to runc. It supports rootless containers, cgroups v1 and v2, seccomp filtering, capabilities, and Linux namespaces, and integrates with container engines including containerd, Podman, Docker, and Kubernetes.
    humanURL: https://github.com/youki-dev/youki
    tags:
      - Container Runtime
      - OCI
      - Rust
    properties:
      - type: Documentation
        url: https://youki-dev.github.io/youki/
      - type: GettingStarted
        url: https://youki-dev.github.io/youki/user/basic_usage.html
      - type: GitHubRepository
        url: https://github.com/youki-dev/youki
      - type: ReleaseNotes
        url: https://github.com/youki-dev/youki/releases
      - type: ChangeLog
        url: https://github.com/youki-dev/youki/blob/main/CHANGELOG.md
      - type: CLI
        url: https://crates.io/crates/youki
        title: youki CLI
      - type: SDK
        url: https://crates.io/crates/libcontainer
        title: libcontainer (Rust)
      - type: SDK
        url: https://crates.io/crates/libcgroups
        title: libcgroups (Rust)
      - type: SDK
        url: https://crates.io/crates/liboci-cli
        title: liboci-cli (Rust)
      - type: CodeExamples
        url: https://github.com/youki-dev/youki/tree/main/tools/wasm-sample
        title: WebAssembly Sample
      - type: Tutorials
        url: https://youki-dev.github.io/youki/user/webassembly.html
        title: Running WebAssembly Workloads
      - type: JSONSchema
        url: json-schema/oci-runtime-config-schema.json
        title: OCI Runtime Config Schema
      - type: JSONSchema
        url: json-schema/oci-runtime-state-schema.json
        title: OCI Runtime State Schema
      - type: JSONSchema
        url: json-schema/oci-runtime-features-schema.json
        title: OCI Runtime Features Schema
      - type: JSONSchema
        url: json-schema/oci-runtime-config-linux.json
        title: OCI Runtime Linux Config Schema
      - type: JSONSchema
        url: json-schema/oci-runtime-config-windows.json
        title: OCI Runtime Windows Config Schema
      - type: JSONSchema
        url: json-schema/oci-runtime-config-solaris.json
        title: OCI Runtime Solaris Config Schema
      - type: JSONSchema
        url: json-schema/oci-runtime-config-freebsd.json
        title: OCI Runtime FreeBSD Config Schema
      - type: JSONSchema
        url: json-schema/oci-runtime-config-zos.json
        title: OCI Runtime z/OS Config Schema
      - type: JSONSchema
        url: json-schema/oci-runtime-config-vm.json
        title: OCI Runtime VM Config Schema
      - type: JSONSchema
        url: json-schema/oci-runtime-features-linux.json
        title: OCI Runtime Linux Features Schema
      - type: JSONSchema
        url: json-schema/oci-runtime-defs.json
        title: OCI Runtime Common Definitions
      - type: JSONSchema
        url: json-schema/oci-runtime-defs-linux.json
        title: OCI Runtime Linux Definitions
      - type: JSONSchema
        url: json-schema/oci-runtime-defs-windows.json
        title: OCI Runtime Windows Definitions
      - type: JSONSchema
        url: json-schema/oci-runtime-defs-vm.json
        title: OCI Runtime VM Definitions
      - type: JSONSchema
        url: json-schema/oci-runtime-defs-zos.json
        title: OCI Runtime z/OS Definitions
      - type: JSONSchema
        url: json-schema/oci-runtime-defs-freebsd.json
        title: OCI Runtime FreeBSD Definitions
      - type: JSONStructure
        url: json-structure/oci-runtime-config-structure.json
        title: OCI Runtime Config Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-state-structure.json
        title: OCI Runtime State Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-features-structure.json
        title: OCI Runtime Features Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-config-linux-structure.json
        title: OCI Runtime Linux Config Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-config-windows-structure.json
        title: OCI Runtime Windows Config Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-config-solaris-structure.json
        title: OCI Runtime Solaris Config Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-config-freebsd-structure.json
        title: OCI Runtime FreeBSD Config Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-config-zos-structure.json
        title: OCI Runtime z/OS Config Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-config-vm-structure.json
        title: OCI Runtime VM Config Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-features-linux-structure.json
        title: OCI Runtime Linux Features Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-defs-structure.json
        title: OCI Runtime Common Definitions Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-defs-linux-structure.json
        title: OCI Runtime Linux Definitions Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-defs-windows-structure.json
        title: OCI Runtime Windows Definitions Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-defs-vm-structure.json
        title: OCI Runtime VM Definitions Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-defs-zos-structure.json
        title: OCI Runtime z/OS Definitions Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-defs-freebsd-structure.json
        title: OCI Runtime FreeBSD Definitions Structure
      - type: Example
        url: examples/oci-runtime-config-example.json
        title: OCI Runtime Config Example
      - type: Example
        url: examples/oci-runtime-state-example.json
        title: OCI Runtime State Example
      - type: Example
        url: examples/oci-runtime-features-example.json
        title: OCI Runtime Features Example
      - type: Example
        url: examples/oci-runtime-config-linux-example.json
        title: OCI Runtime Linux Config Example
      - type: Example
        url: examples/oci-runtime-config-windows-example.json
        title: OCI Runtime Windows Config Example
      - type: Example
        url: examples/oci-runtime-config-solaris-example.json
        title: OCI Runtime Solaris Config Example
      - type: Example
        url: examples/oci-runtime-config-freebsd-example.json
        title: OCI Runtime FreeBSD Config Example
      - type: Example
        url: examples/oci-runtime-config-zos-example.json
        title: OCI Runtime z/OS Config Example
      - type: Example
        url: examples/oci-runtime-config-vm-example.json
        title: OCI Runtime VM Config Example
      - type: Example
        url: examples/oci-runtime-features-linux-example.json
        title: OCI Runtime Linux Features Example
      - type: Example
        url: examples/oci-runtime-defs-example.json
        title: OCI Runtime Common Definitions Example
      - type: Example
        url: examples/oci-runtime-defs-linux-example.json
        title: OCI Runtime Linux Definitions Example
      - type: Example
        url: examples/oci-runtime-defs-windows-example.json
        title: OCI Runtime Windows Definitions Example
      - type: Example
        url: examples/oci-runtime-defs-vm-example.json
        title: OCI Runtime VM Definitions Example
      - type: Example
        url: examples/oci-runtime-defs-zos-example.json
        title: OCI Runtime z/OS Definitions Example
      - type: Example
        url: examples/oci-runtime-defs-freebsd-example.json
        title: OCI Runtime FreeBSD Definitions Example
      - type: JSON-LD
        url: json-ld/youki-oci-runtime-context.jsonld
        title: OCI Runtime JSON-LD Context
  - aid: youki:oci-spec-rs
    name: OCI Spec for Rust
    description: oci-spec-rs is a Rust implementation of the OCI Runtime, Image, and Distribution Specifications, providing the data structures and types consumed by youki and other Rust-based container tooling.
    humanURL: https://github.com/youki-dev/oci-spec-rs
    tags:
      - OCI
      - Rust
      - Specification
    properties:
      - type: GitHubRepository
        url: https://github.com/youki-dev/oci-spec-rs
      - type: SDK
        url: https://crates.io/crates/oci-spec
        title: oci-spec (Rust)
      - type: Documentation
        url: https://docs.rs/oci-spec
        title: oci-spec API Docs
      - type: JSONSchema
        url: json-schema/oci-runtime-config-schema.json
        title: OCI Runtime Config Schema
      - type: JSONSchema
        url: json-schema/oci-runtime-state-schema.json
        title: OCI Runtime State Schema
      - type: JSONSchema
        url: json-schema/oci-runtime-features-schema.json
        title: OCI Runtime Features Schema
      - type: JSONSchema
        url: json-schema/oci-image-config-schema.json
        title: OCI Image Config Schema
      - type: JSONSchema
        url: json-schema/oci-image-manifest-schema.json
        title: OCI Image Manifest Schema
      - type: JSONSchema
        url: json-schema/oci-image-index-schema.json
        title: OCI Image Index Schema
      - type: JSONSchema
        url: json-schema/oci-image-layout-schema.json
        title: OCI Image Layout Schema
      - type: JSONSchema
        url: json-schema/oci-image-content-descriptor.json
        title: OCI Image Content Descriptor Schema
      - type: JSONSchema
        url: json-schema/oci-image-defs.json
        title: OCI Image Common Definitions
      - type: JSONSchema
        url: json-schema/oci-image-defs-descriptor.json
        title: OCI Image Descriptor Definitions
      - type: JSONStructure
        url: json-structure/oci-runtime-config-structure.json
        title: OCI Runtime Config Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-state-structure.json
        title: OCI Runtime State Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-features-structure.json
        title: OCI Runtime Features Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-config-linux-structure.json
        title: OCI Runtime Linux Config Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-config-windows-structure.json
        title: OCI Runtime Windows Config Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-config-solaris-structure.json
        title: OCI Runtime Solaris Config Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-config-freebsd-structure.json
        title: OCI Runtime FreeBSD Config Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-config-zos-structure.json
        title: OCI Runtime z/OS Config Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-config-vm-structure.json
        title: OCI Runtime VM Config Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-features-linux-structure.json
        title: OCI Runtime Linux Features Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-defs-structure.json
        title: OCI Runtime Common Definitions Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-defs-linux-structure.json
        title: OCI Runtime Linux Definitions Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-defs-windows-structure.json
        title: OCI Runtime Windows Definitions Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-defs-vm-structure.json
        title: OCI Runtime VM Definitions Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-defs-zos-structure.json
        title: OCI Runtime z/OS Definitions Structure
      - type: JSONStructure
        url: json-structure/oci-runtime-defs-freebsd-structure.json
        title: OCI Runtime FreeBSD Definitions Structure
      - type: JSONStructure
        url: json-structure/oci-image-config-structure.json
        title: OCI Image Config Structure
      - type: JSONStructure
        url: json-structure/oci-image-manifest-structure.json
        title: OCI Image Manifest Structure
      - type: JSONStructure
        url: json-structure/oci-image-index-structure.json
        title: OCI Image Index Structure
      - type: JSONStructure
        url: json-structure/oci-image-layout-structure.json
        title: OCI Image Layout Structure
      - type: JSONStructure
        url: json-structure/oci-image-content-descriptor-structure.json
        title: OCI Image Content Descriptor Structure
      - type: JSONStructure
        url: json-structure/oci-image-defs-structure.json
        title: OCI Image Common Definitions Structure
      - type: JSONStructure
        url: json-structure/oci-image-defs-descriptor-structure.json
        title: OCI Image Descriptor Definitions Structure
      - type: Example
        url: examples/oci-runtime-config-example.json
        title: OCI Runtime Config Example
      - type: Example
        url: examples/oci-runtime-state-example.json
        title: OCI Runtime State Example
      - type: Example
        url: examples/oci-runtime-features-example.json
        title: OCI Runtime Features Example
      - type: Example
        url: examples/oci-runtime-config-linux-example.json
        title: OCI Runtime Linux Config Example
      - type: Example
        url: examples/oci-runtime-config-windows-example.json
        title: OCI Runtime Windows Config Example
      - type: Example
        url: examples/oci-runtime-config-solaris-example.json
        title: OCI Runtime Solaris Config Example
      - type: Example
        url: examples/oci-runtime-config-freebsd-example.json
        title: OCI Runtime FreeBSD Config Example
      - type: Example
        url: examples/oci-runtime-config-zos-example.json
        title: OCI Runtime z/OS Config Example
      - type: Example
        url: examples/oci-runtime-config-vm-example.json
        title: OCI Runtime VM Config Example
      - type: Example
        url: examples/oci-runtime-features-linux-example.json
        title: OCI Runtime Linux Features Example
      - type: Example
        url: examples/oci-runtime-defs-example.json
        title: OCI Runtime Common Definitions Example
      - type: Example
        url: examples/oci-runtime-defs-linux-example.json
        title: OCI Runtime Linux Definitions Example
      - type: Example
        url: examples/oci-runtime-defs-windows-example.json
        title: OCI Runtime Windows Definitions Example
      - type: Example
        url: examples/oci-runtime-defs-vm-example.json
        title: OCI Runtime VM Definitions Example
      - type: Example
        url: examples/oci-runtime-defs-zos-example.json
        title: OCI Runtime z/OS Definitions Example
      - type: Example
        url: examples/oci-runtime-defs-freebsd-example.json
        title: OCI Runtime FreeBSD Definitions Example
      - type: Example
        url: examples/oci-image-config-example.json
        title: OCI Image Config Example
      - type: Example
        url: examples/oci-image-manifest-example.json
        title: OCI Image Manifest Example
      - type: Example
        url: examples/oci-image-index-example.json
        title: OCI Image Index Example
      - type: Example
        url: examples/oci-image-layout-example.json
        title: OCI Image Layout Example
      - type: Example
        url: examples/oci-image-content-descriptor-example.json
        title: OCI Image Content Descriptor Example
      - type: Example
        url: examples/oci-image-defs-example.json
        title: OCI Image Common Definitions Example
      - type: Example
        url: examples/oci-image-defs-descriptor-example.json
        title: OCI Image Descriptor Definitions Example
      - type: JSON-LD
        url: json-ld/youki-oci-runtime-context.jsonld
        title: OCI Runtime JSON-LD Context
      - type: JSON-LD
        url: json-ld/youki-oci-image-context.jsonld
        title: OCI Image JSON-LD Context
common:
  - type: Documentation
    url: https://youki-dev.github.io/youki/
  - type: GitHubOrganization
    url: https://github.com/youki-dev
  - type: GitHubRepository
    url: https://github.com/youki-dev/youki
  - type: ReleaseNotes
    url: https://github.com/youki-dev/youki/releases
  - type: ChangeLog
    url: https://github.com/youki-dev/youki/blob/main/CHANGELOG.md
  - type: Support
    url: https://youki-dev.github.io/youki/community/introduction.html
  - type: Vocabulary
    url: vocabulary/youki-vocabulary.yaml
    title: Youki Vocabulary
  - type: Features
    data:
      - name: OCI Runtime Spec Compliance
        description: Implements the Open Container Initiative (OCI) runtime specification, allowing youki to run any OCI-compliant container alongside or in place of runc.
      - name: Memory-Safe Rust Implementation
        description: Written entirely in Rust to deliver memory safety and stronger isolation guarantees than C-based container runtimes.
      - name: Rootless Containers
        description: Enables running containers without root privileges to reduce host attack surface for development and multi-tenant scenarios.
      - name: Cgroups v1 and v2 Support
        description: Supports both legacy cgroups v1 and modern cgroups v2 hierarchies for resource management on Linux.
      - name: Seccomp Filtering
        description: Applies seccomp BPF filters to restrict syscalls available to containers and harden the runtime surface.
      - name: Systemd Integration
        description: Integrates with systemd as a cgroup manager and supports systemd-managed container processes.
      - name: Linux Namespaces and Capabilities
        description: Manages mount, UTS, IPC, user, PID, network, and cgroup namespaces and supports capabilities such as CAP_BPF, CAP_PERFMON, and CAP_CHECKPOINT_RESTORE.
      - name: Performance
        description: Benchmarks show youki performing roughly twice as fast as runc for container create-to-delete cycles.
      - name: CNCF Sandbox Project
        description: Maintained as a Cloud Native Computing Foundation sandbox project with open governance, public roadmap, and community contributors.
  - type: UseCases
    data:
      - name: Drop-In runc Replacement
        description: Use youki as a drop-in replacement for runc in container engines to gain memory safety and performance benefits with no workload changes.
      - name: Rootless Container Workflows
        description: Run containers as a non-root user for development, CI, or multi-tenant environments where elevated privileges are not desirable.
      - name: Kubernetes Workloads via containerd
        description: Use youki under containerd to execute Kubernetes pods and workloads in production clusters.
      - name: Podman and Docker Container Execution
        description: Configure Podman or Docker to invoke youki as the low-level OCI runtime for image execution.
      - name: Container Runtime Research and Education
        description: Explore and prototype container runtime features in a memory-safe codebase suitable for systems research, security analysis, and teaching.
  - type: Integrations
    data:
      - name: containerd
        description: containerd has passed end-to-end testing against youki, enabling its use as the OCI runtime for Kubernetes and other workloads orchestrated by containerd.
      - name: Podman
        description: Podman can be configured to use youki as its OCI runtime for both rootless and rootful container execution.
      - name: Docker
        description: Docker can call youki as the low-level OCI runtime in place of runc for compatible workloads via daemon.json configuration.
      - name: Kubernetes
        description: Kubernetes clusters can run youki indirectly through container runtimes such as containerd or CRI-O.
      - name: crun
        description: youki sits alongside crun as a modern alternative to runc, focused on memory-safe systems programming in Rust.
      - name: systemd
        description: Integrates with systemd for cgroup management and lifecycle control of container processes.
      - name: oci-spec-rs
        description: Built on oci-spec-rs, the Rust implementation of the OCI Runtime, Image, and Distribution specifications maintained by the same organization.
  - type: Solutions
    data:
      - name: Cloud Native Container Platforms
        description: Provides a CNCF sandbox container runtime for cloud-native platforms looking to adopt a memory-safe OCI runtime under containerd or CRI-O.
      - name: Secure Multi-Tenant Hosts
        description: Pairs rootless containers, seccomp filtering, and Rust memory safety to harden multi-tenant container hosts against runtime exploits.
      - name: Edge and Embedded Workloads
        description: A lightweight, high-performance runtime suitable for edge and embedded deployments where resource use and predictable performance matter.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
