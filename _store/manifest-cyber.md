---
aid: manifest-cyber
name: Manifest Cyber
description: Manifest Cyber provides a cybersecurity platform with an official public API for accessing software bill of materials (SBOM) data, vulnerability analysis, and supply chain security information used by Manifest's frontend apps and internal ETL pipelines.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
position: Consuming
tags:
  - Cybersecurity
  - SBOM
  - Supply Chain Security
  - Vulnerability Management
url: https://raw.githubusercontent.com/api-evangelist/manifest-cyber/refs/heads/main/apis.yml
created: '2025-02-12'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: manifest-cyber:manifest-cyber-api
    name: Manifest Cyber API
    description: The official public API for the Manifest Cyber platform v1. Used by Manifest's frontend apps and internal ETL processes to access SBOM data, vulnerability analysis, and software supply chain security information.
    humanURL: https://api-docs.manifestcyber.com/
    baseURL: https://app.manifestcyber.com/api/v1
    tags:
      - Cybersecurity
      - SBOM
      - Vulnerability Management
      - Supply Chain
    properties:
      - type: Documentation
        url: https://api-docs.manifestcyber.com/
common:
  - type: Website
    url: https://manifestcyber.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
