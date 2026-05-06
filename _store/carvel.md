---
aid: carvel
name: Carvel
description: Carvel is a set of reliable, single-purpose, composable command-line tools that help build, configure, and deploy applications to Kubernetes. The toolset includes ytt for YAML templating, kapp for application lifecycle management, kbld for immutable image references, imgpkg for OCI bundling, vendir for vendored configuration, and kapp-controller for GitOps-style continuous delivery.
type: Index
x-type: opensource
position: Consumer
access: Open Source
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CLI
  - Configuration
  - Containers
  - Deployment
  - GitOps
  - Kubernetes
  - Package Management
  - Templating
url: https://raw.githubusercontent.com/api-evangelist/carvel/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-23'
specificationVersion: '0.19'
apis:
  - aid: carvel:ytt
    name: ytt
    description: ytt is a templating tool that understands YAML structure, letting you use familiar YAML constructs and Python-like language (Starlark) to template Kubernetes configuration. Supports overlays, data values, and functions without text-based substitution.
    humanURL: https://carvel.dev/ytt/
    tags:
      - Configuration
      - Kubernetes
      - Templating
      - YAML
    properties:
      - type: Documentation
        url: https://carvel.dev/ytt/docs/latest/
      - type: GitHub Repository
        url: https://github.com/carvel-dev/ytt
      - type: Playground
        url: https://carvel.dev/ytt/#playground
    x-features:
      - YAML-structure-aware templating
      - Starlark-based programming model
      - Overlays to patch existing YAML
      - Data values for parameterization
      - Schema validation for data values
      - Reusable functions and libraries
    x-use-cases:
      - Parameterizing Kubernetes manifests
      - Patching third-party YAML without forking
      - Generating multi-environment configuration
      - Creating reusable configuration libraries
  - aid: carvel:kapp
    name: kapp
    description: kapp is a CLI tool that installs, upgrades, and deletes multiple Kubernetes resources as a single application. It provides change set previews, resource ordering, and convergence detection for predictable deployments.
    humanURL: https://carvel.dev/kapp/
    tags:
      - Deployment
      - Kubernetes
      - Lifecycle
    properties:
      - type: Documentation
        url: https://carvel.dev/kapp/docs/latest/
      - type: GitHub Repository
        url: https://github.com/carvel-dev/kapp
    x-features:
      - Change-set preview before apply
      - Resource ordering and waiting
      - Label-based application grouping
      - Convergence detection on deploy
      - Garbage collection of removed resources
    x-use-cases:
      - Deploying Kubernetes applications atomically
      - Previewing infrastructure changes before apply
      - Managing application lifecycle without Helm
  - aid: carvel:kbld
    name: kbld
    description: kbld builds or references container images in Kubernetes configuration in an immutable way by resolving image tags to digests and optionally building images from source during the deployment pipeline.
    humanURL: https://carvel.dev/kbld/
    tags:
      - Container Images
      - Immutable
      - Kubernetes
    properties:
      - type: Documentation
        url: https://carvel.dev/kbld/docs/latest/
      - type: GitHub Repository
        url: https://github.com/carvel-dev/kbld
    x-features:
      - Resolve image tags to digests
      - Build images from source with Docker/pack
      - Push to registries during deploy
      - Integration with ytt and kapp
    x-use-cases:
      - Ensuring immutable image references
      - Building and deploying images in one pipeline
      - Auditing which images are actually deployed
  - aid: carvel:imgpkg
    name: imgpkg
    description: imgpkg bundles and distributes application configuration and container images as OCI artifacts via Docker registries, enabling relocation across registries including air-gapped environments.
    humanURL: https://carvel.dev/imgpkg/
    tags:
      - Bundles
      - Container Images
      - OCI
      - Registry
    properties:
      - type: Documentation
        url: https://carvel.dev/imgpkg/docs/latest/
      - type: GitHub Repository
        url: https://github.com/carvel-dev/imgpkg
    x-features:
      - OCI-compliant bundles
      - Bundle relocation between registries
      - Air-gapped deployment support
      - Lock files for reproducibility
    x-use-cases:
      - Distributing Kubernetes app bundles
      - Air-gapped deployments
      - Registry-to-registry mirroring
  - aid: carvel:vendir
    name: vendir
    description: vendir declaratively states what files should be in a directory, syncing from upstream sources such as Git repositories, HTTP archives, Helm charts, and OCI images. Enables reproducible vendored configuration.
    humanURL: https://carvel.dev/vendir/
    tags:
      - Configuration
      - Vendoring
    properties:
      - type: Documentation
        url: https://carvel.dev/vendir/docs/latest/
      - type: GitHub Repository
        url: https://github.com/carvel-dev/vendir
    x-features:
      - Declarative sync from Git, HTTP, Helm, OCI
      - Lock files for reproducibility
      - Selective inclusion of files
      - Integration with overlays via ytt
    x-use-cases:
      - Vendoring third-party Kubernetes configuration
      - Pinning upstream Helm charts
      - Reproducible configuration builds
  - aid: carvel:kapp-controller
    name: kapp-controller
    description: kapp-controller is a Kubernetes controller that provides GitOps-style continuous delivery for applications and packages using Carvel tools. It introduces PackageRepository, Package, PackageInstall, and App custom resources for package management.
    humanURL: https://carvel.dev/kapp-controller/
    tags:
      - CRD
      - GitOps
      - Kubernetes
      - Package Management
    properties:
      - type: Documentation
        url: https://carvel.dev/kapp-controller/docs/latest/
      - type: GitHub Repository
        url: https://github.com/carvel-dev/kapp-controller
    x-features:
      - App and Package CRDs
      - PackageRepository for distribution
      - GitOps continuous reconciliation
      - ytt, kbld, and kapp integration
      - Versioning and constraints for packages
    x-use-cases:
      - Kubernetes package management
      - GitOps-driven continuous delivery
      - Distributing internal platform packages
  - aid: carvel:secretgen-controller
    name: secretgen-controller
    description: secretgen-controller provides CRDs to generate Kubernetes Secrets, export and import secrets across namespaces, and manage certificate and password creation declaratively.
    humanURL: https://github.com/carvel-dev/secretgen-controller
    tags:
      - CRD
      - Kubernetes
      - Secrets
    properties:
      - type: GitHub Repository
        url: https://github.com/carvel-dev/secretgen-controller
    x-features:
      - Generate Certificates, Passwords, RSA Keys, SSH Keys
      - Cross-namespace secret export/import
      - Declarative secret management via CRDs
    x-use-cases:
      - Generating bootstrap credentials
      - Sharing secrets across namespaces
      - Declarative certificate management
common:
  - type: Website
    url: https://carvel.dev/
  - type: Documentation
    url: https://carvel.dev/docs/latest/
  - type: GitHub Organization
    url: https://github.com/carvel-dev
  - type: Blog
    url: https://carvel.dev/blog/
  - type: Slack
    url: https://kubernetes.slack.com/archives/CH8KCCKA5
  - type: Community
    url: https://carvel.dev/community/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
