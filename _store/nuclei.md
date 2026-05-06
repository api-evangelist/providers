---
aid: nuclei
name: Nuclei
description: Nuclei is an open source vulnerability scanner from ProjectDiscovery that uses YAML-based templates to find security issues in APIs, web apps, and infrastructure. It supports multiple protocols (HTTP, DNS, TCP, file), parallel scanning, CI/CD integration, and ships with thousands of community-contributed templates. The ProjectDiscovery Cloud Platform exposes a REST API for managing templates, scans, vulnerabilities, leaks, asset discovery, exports, and more.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Security Testing
  - Testing
  - Vulnerability Scanner
  - DAST
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/nuclei/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: nuclei:nuclei
    name: Nuclei
    description: Nuclei is an open source vulnerability scanner from ProjectDiscovery that uses YAML-based templates to find security issues in APIs, web apps, and infrastructure.
    humanURL: https://nuclei.projectdiscovery.io
    tags:
      - Security Testing
      - Testing
      - Vulnerability Scanner
    properties:
      - type: Documentation
        url: https://docs.projectdiscovery.io/tools/nuclei/overview
      - type: GitHubRepository
        url: https://github.com/projectdiscovery/nuclei
  - aid: nuclei:projectdiscovery-cloud-api
    name: ProjectDiscovery Cloud Platform API
    description: REST API for the ProjectDiscovery Cloud Platform (PDCP) covering Nuclei templates, scans, vulnerabilities, leaks, asset discovery, configurations, exports, audit logs, and utilities. Authentication uses API keys passed via the X-Api-Key header.
    humanURL: https://docs.projectdiscovery.io/api-reference/introduction
    baseURL: https://api.projectdiscovery.io
    tags:
      - Security Testing
      - Vulnerability Scanner
      - Templates
      - Scans
      - Cloud
    properties:
      - type: Documentation
        url: https://docs.projectdiscovery.io/api-reference/introduction
      - type: Portal
        url: https://cloud.projectdiscovery.io/
      - type: OpenAPI
        url: openapi/nuclei-openapi.yml
common:
  - type: Website
    url: https://nuclei.projectdiscovery.io
  - type: Documentation
    url: https://docs.projectdiscovery.io/tools/nuclei/overview
  - type: Reference
    url: https://docs.projectdiscovery.io/api-reference/introduction
  - type: GitHubOrganization
    url: https://github.com/projectdiscovery
  - type: GitHubRepository
    url: https://github.com/projectdiscovery/nuclei
  - type: Templates
    url: https://github.com/projectdiscovery/nuclei-templates
  - type: Cloud
    url: https://cloud.projectdiscovery.io/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
