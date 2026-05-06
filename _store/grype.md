---
aid: grype
name: Grype
description: Grype is an open source vulnerability scanner for container images and filesystems developed by Anchore. It works with Syft-generated SBOMs and supports major OS package ecosystems and language-specific packages including Go, Java, JavaScript, Python, Ruby, Rust, and .NET.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Container Images
  - Containers
  - Open Source
  - SBOM
  - Security
  - Vulnerability Scanning
url: https://raw.githubusercontent.com/api-evangelist/grype/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: grype:grype
    name: Grype
    description: Grype is an open source vulnerability scanner for container images and filesystems developed by Anchore. It scans container images, filesystems, and SBOMs for known vulnerabilities, supporting Docker, OCI, and Singularity image formats.
    humanURL: https://github.com/anchore/grype
    tags:
      - Container Images
      - Containers
      - SBOM
      - Security
      - Vulnerability Scanning
    properties:
      - type: Documentation
        url: https://github.com/anchore/grype/blob/main/README.md
      - type: Getting Started
        url: https://oss.anchore.com/docs/guides/vulnerability/getting-started/
common:
  - type: Website
    url: https://anchore.com/
  - type: Documentation
    url: https://github.com/anchore/grype/blob/main/README.md
  - type: Getting Started
    url: https://oss.anchore.com/docs/guides/vulnerability/getting-started/
  - type: GitHub Organization
    url: https://github.com/anchore
  - type: Open Source
    url: https://anchore.com/opensource/
  - type: Blog
    url: https://anchore.com/blog/
  - type: Pricing
    url: https://anchore.com/pricing/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
