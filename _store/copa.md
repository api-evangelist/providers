---
aid: copa
url: https://raw.githubusercontent.com/api-evangelist/copa/refs/heads/main/apis.yml
name: Copa (Project Copacetic)
x-type: opensource
description: Project Copacetic (Copa) is an open source command line tool that patches container images directly using BuildKit, without requiring a full image rebuild. Copa parses vulnerability scan reports from Trivy and other scanners, applies the corresponding OS package updates via the appropriate package manager (apt, apk, dnf, tdnf, yum, zypper), and produces a new container image with a patched layer. Copa supports multi-platform images, distroless images, and custom scanner plugins through the Vulnerability Exchange (VEX) and pluggable scanner interface.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - BuildKit
  - CLI
  - CNCF Sandbox
  - Container Patching
  - Containers
  - Open Source
  - Security
  - Trivy
  - Vulnerability Management
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: copa:cli
    name: Copa CLI
    description: The copa command line interface used to patch container images. The core subcommand `copa patch` accepts an image reference and an optional vulnerability report and produces a new tagged image with OS-level package vulnerabilities remediated via BuildKit.
    humanURL: https://project-copacetic.github.io/copacetic/website/
    baseURL: https://project-copacetic.github.io
    tags:
      - CLI
      - Patching
    properties:
      - type: Documentation
        url: https://project-copacetic.github.io/copacetic/website/
      - type: Reference
        url: https://project-copacetic.github.io/copacetic/website/quick-start/
      - type: GitHubRepository
        url: https://github.com/project-copacetic/copacetic
      - type: License
        url: https://github.com/project-copacetic/copacetic/blob/main/LICENSE
      - type: Issue Tracker
        url: https://github.com/project-copacetic/copacetic/issues
    x-features:
      - '`copa patch -i IMAGE` patches all outdated OS packages'
      - '`copa patch -r REPORT.json -i IMAGE` patches based on a Trivy report'
      - Multi-platform image patching
      - Distroless image support
      - Pluggable scanner plugins
      - VEX (Vulnerability Exchange) document generation
    x-useCases:
      - Remediating OS-level CVEs in third-party container images
      - Continuously patching base images during security incidents
      - Inserting Copa into CI/CD pipelines after Trivy scans
  - aid: copa:scanner-plugins
    name: Copa Scanner Plugin Interface
    description: Copa exposes a plugin interface that allows third-party vulnerability scanners to feed reports into the patcher. Out of the box, Copa supports Trivy JSON reports and provides documentation for adding new scanner plugins.
    humanURL: https://project-copacetic.github.io/copacetic/website/scanner-plugins/
    baseURL: https://project-copacetic.github.io
    tags:
      - Plugins
      - Scanners
      - Trivy
    properties:
      - type: Documentation
        url: https://project-copacetic.github.io/copacetic/website/scanner-plugins/
      - type: Reference
        url: https://github.com/project-copacetic/copacetic/tree/main/pkg/vex
    x-features:
      - Trivy JSON parser built in
      - Pluggable interface for additional scanners
      - Standardized intermediate representation of vulnerability reports
    x-useCases:
      - Integrating internal vulnerability scanners with Copa
      - Using Grype, Snyk, or Anchore reports as Copa input
  - aid: copa:vex
    name: Copa VEX Output
    description: Copa can emit a Vulnerability Exchange (VEX) document describing which CVEs were patched. VEX documents help security teams and downstream consumers verify that an image has been remediated and track residual risk.
    humanURL: https://project-copacetic.github.io/copacetic/website/output/
    baseURL: https://project-copacetic.github.io
    tags:
      - OpenVEX
      - SBOM
      - VEX
    properties:
      - type: Documentation
        url: https://project-copacetic.github.io/copacetic/website/output/
      - type: Reference
        url: https://github.com/openvex/spec
    x-features:
      - Emits OpenVEX-compatible documents
      - Records patched CVE identifiers and statuses
      - Pairs with SBOMs for supply chain transparency
    x-useCases:
      - Communicating remediation status downstream
      - Reducing scanner noise from CVEs already patched in place
common:
  - type: Website
    url: https://project-copacetic.github.io/copacetic/website/
  - type: Documentation
    url: https://project-copacetic.github.io/copacetic/website/quick-start/
  - type: GitHubRepository
    url: https://github.com/project-copacetic/copacetic
  - type: GitHub Organization
    url: https://github.com/project-copacetic
  - type: Issue Tracker
    url: https://github.com/project-copacetic/copacetic/issues
  - type: Change Log
    url: https://github.com/project-copacetic/copacetic/releases
  - type: License
    url: https://github.com/project-copacetic/copacetic/blob/main/LICENSE
  - type: Community
    url: https://github.com/project-copacetic/copacetic/blob/main/CONTRIBUTING.md
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
