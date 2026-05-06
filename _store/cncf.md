---
aid: cncf
url: https://raw.githubusercontent.com/api-evangelist/cncf/refs/heads/main/apis.yml
name: CNCF
x-type: opensource
tags:
  - Cloud Native
  - Containers
  - Kubernetes
  - Open Source
  - Standards
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-01'
modified: '2026-04-23'
specificationVersion: '0.19'
description: The Cloud Native Computing Foundation (CNCF) is part of the Linux Foundation and hosts critical components of the global cloud-native technology infrastructure - including Kubernetes, Prometheus, Envoy, etcd, OpenTelemetry, CloudEvents, gRPC, and CNI. CNCF stewards open-source project governance and publishes the Cloud Native Interactive Landscape, a community-curated dataset (landscape.yml) of cloud-native projects and products with metadata such as GitHub stars, contributor counts, funding, and headquarters location.
apis:
  - aid: cncf:cncf-landscape
    name: CNCF Cloud Native Interactive Landscape
    tags:
      - Catalog
      - Cloud Native
      - Landscape
      - Open Data
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://landscape.cncf.io/
    properties:
      - url: https://landscape.cncf.io/
        type: Documentation
      - url: https://github.com/cncf/landscape
        type: GitHubRepository
      - url: https://github.com/cncf/landscape/blob/master/landscape.yml
        type: Dataset
      - url: https://github.com/cncf/landscape2
        type: GitHubRepository
    description: The CNCF Cloud Native Interactive Landscape is the canonical map of the cloud-native ecosystem. The landscape is generated daily from landscape.yml and enriched with data from Crunchbase and GitHub. The underlying dataset (project name, category, maturity, GitHub repo, Crunchbase entry, headquarters, etc.) is published as YAML in the cncf/landscape repo and rendered with the cncf/landscape2 generator, providing a structured, machine-readable catalog of hundreds of cloud-native projects and products.
    x-features:
      - name: Project Catalog
        description: Hundreds of cloud-native projects and products with structured metadata.
      - name: Maturity Levels
        description: Graduated, Incubating, Sandbox, and Archived classifications.
      - name: GitHub Metrics
        description: GitHub stars, contributors, and commit activity per project.
      - name: Categories and Subcategories
        description: Provisioning, Runtime, Orchestration, App Definition, Observability, etc.
    x-useCases:
      - name: Tool Discovery
        description: Help engineers find cloud-native tools that match their requirements.
      - name: Landscape Analysis
        description: Track ecosystem growth, project maturity, and adoption signals.
      - name: Procurement and Vendor Selection
        description: Evaluate CNCF projects and vendors when standardizing tooling.
  - aid: cncf:cncf-projects
    name: CNCF Hosted Projects (Standards Steward)
    tags:
      - Kubernetes
      - Open Source
      - Standards
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cncf.io/projects/
    properties:
      - url: https://www.cncf.io/projects/
        type: Documentation
      - url: https://github.com/cncf
        type: GitHubOrganization
    description: CNCF stewards an open-source project portfolio whose APIs underpin much of modern cloud infrastructure - Kubernetes API, OpenTelemetry, CloudEvents, gRPC, CNI, CSI, OCI image and runtime specs, Prometheus exposition format, etcd, Envoy xDS, and many more. Each project owns its own API specs and contracts; CNCF provides the governance and home for these cloud-native standards.
    x-features:
      - name: Open Governance
        description: Open governance for hosted cloud-native projects.
      - name: Maturity Track
        description: Sandbox to Incubating to Graduated maturity track.
      - name: Standards Stewardship
        description: Stewardship of foundational cloud-native API standards.
common:
  - url: https://www.cncf.io/
    type: Website
  - url: https://landscape.cncf.io/
    name: CNCF Cloud Native Landscape
    type: Landscape
  - url: https://www.cncf.io/projects/
    name: Graduated and Incubating Projects
    type: Catalog
  - url: https://www.cncf.io/blog/
    name: CNCF Blog
    type: Blog
  - url: https://github.com/cncf
    name: CNCF on GitHub
    type: GitHubOrganization
  - url: https://www.cncf.io/all-cncf/
    name: All CNCF Sites
    type: About
  - url: https://www.linuxfoundation.org/privacy/
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://twitter.com/CloudNativeFdn
    name: CNCF on X
    type: X
  - url: https://www.linkedin.com/company/cloud-native-computing-foundation/
    name: CNCF on LinkedIn
    type: LinkedIn
  - url: https://www.youtube.com/c/cloudnativefdn
    name: CNCF on YouTube
    type: YouTube
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
