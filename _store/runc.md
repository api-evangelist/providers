---
aid: runc
name: Runc
description: runc is a CLI tool for spawning and running containers on Linux according to the OCI (Open Container Initiative) specification. It is the reference implementation of the OCI runtime specification and is used as the default low-level container runtime by Docker, containerd, Podman, and other container platforms. runc manages container lifecycle operations including creating, starting, pausing, resuming, killing, and deleting containers. It implements the OCI Runtime Specification and exposes a command-line interface that higher-level runtimes use to manage individual container instances. runc also supports checkpoint/restore via CRIU, rootless containers (no root privileges needed via user namespaces), cgroup v2, seccomp syscall filtering, AppArmor, SELinux, and Intel Memory Protection Extensions. The current stable release line is 1.3.x (runc 1.5.0 expected late April 2026).
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Container Runtime
  - Containers
  - Linux
  - OCI
  - Open Source
  - CNCF
  - Open Container Initiative
  - Cloud Native
url: https://raw.githubusercontent.com/api-evangelist/runc/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: runc:runc
    name: Runc
    description: 'runc is a CLI tool for spawning and running containers on Linux according to the OCI (Open Container Initiative) specification. It is the reference implementation of the OCI runtime specification, providing a lightweight and portable container runtime that can be used independently or embedded into higher-level container systems like Docker and containerd. runc implements the full OCI Runtime Spec lifecycle: create, start, state, kill, delete. It also supports checkpoint/restore via CRIU, rootless containers, and cgroup v2. The container configuration is defined in a config.json file following the OCI Runtime Specification schema.'
    humanURL: https://github.com/opencontainers/runc
    tags:
      - Container Runtime
      - Containers
      - Linux
      - OCI
      - Open Source
      - CNCF
      - Open Container Initiative
      - Cloud Native
    properties:
      - type: Documentation
        url: https://github.com/opencontainers/runc/blob/main/README.md
      - type: Getting Started
        url: https://github.com/opencontainers/runc#creating-an-oci-bundle
      - type: GitHub Repository
        url: https://github.com/opencontainers/runc
      - type: Specification
        url: https://github.com/opencontainers/runtime-spec
      - type: Releases
        url: https://github.com/opencontainers/runc/releases
      - type: License
        url: https://github.com/opencontainers/runc/blob/main/LICENSE
      - type: Security
        url: https://github.com/opencontainers/runc/blob/main/SECURITY.md
      - type: Changelog
        url: https://github.com/opencontainers/runc/blob/main/CHANGELOG.md
      - type: JSONSchema
        url: json-schema/runc-container-config-schema.json
      - type: JSONStructure
        url: json-structure/runc-container-config-structure.json
      - type: JSONLD
        url: json-ld/runc-context.jsonld
      - type: Example
        url: examples/runc-container-config-example.json
      - type: Vocabulary
        url: vocabulary/runc-vocabulary.yml
common:
  - type: Website
    url: https://opencontainers.org/
  - type: GitHub Organization
    url: https://github.com/opencontainers
  - type: GitHub Repository
    url: https://github.com/opencontainers/runc
  - type: Blog
    url: https://opencontainers.org/posts/blog/
  - type: Documentation
    url: https://github.com/opencontainers/runc/blob/main/README.md
  - type: Specification
    url: https://github.com/opencontainers/runtime-spec
  - type: Security
    url: https://github.com/opencontainers/runc/blob/main/SECURITY.md
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
