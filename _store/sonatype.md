---
aid: sonatype
name: Sonatype
description: Sonatype provides software supply chain management solutions including Sonatype Lifecycle (IQ Server), Sonatype Repository Firewall, SBOM Manager, and Nexus Repository. The Lifecycle Public REST API provides 188 endpoints for application portfolio management, policy enforcement, vulnerability reporting, component analysis, SBOM generation, source control integration, and software composition analysis across the SDLC.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Software Supply Chain
  - Security
  - Vulnerability Management
  - SBOM
  - Software Composition Analysis
  - DevSecOps
url: https://raw.githubusercontent.com/api-evangelist/sonatype/refs/heads/main/apis.yml
created: '2025-02-12'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: sonatype:sonatype-lifecycle-api
    name: Sonatype Lifecycle API
    description: The Sonatype Lifecycle Public REST API (v1.201.0) provides 188 endpoints for managing applications, organizations, policies, policy violations, waivers, vulnerability analysis, SBOM generation (SPDX, CycloneDX), scan management, component search, reports, source control integration, users, roles, and user tokens. Used by DevSecOps teams to automate software supply chain security and compliance workflows.
    humanURL: https://help.sonatype.com/en/iq-api-reference.html
    baseURL: https://{iq-server-host}/
    tags:
      - Software Supply Chain
      - Security
      - Policy
      - Vulnerability Management
      - SBOM
      - Software Composition Analysis
      - Applications
      - Organizations
    properties:
      - type: Documentation
        url: https://help.sonatype.com/en/iq-api-reference.html
      - type: Reference
        url: https://help.sonatype.com/en/rest-apis.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sonatype/refs/heads/main/openapi/sonatype-lifecycle-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/sonatype/refs/heads/main/json-schema/sonatype-application-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/sonatype/refs/heads/main/json-schema/sonatype-policy-violation-schema.json
    contact:
      - FN: Sonatype Support
        url: https://support.sonatype.com/
common:
  - type: Portal
    url: https://www.sonatype.com/
  - type: Documentation
    url: https://help.sonatype.com/
  - type: Website
    url: https://www.sonatype.com/
  - type: GitHub
    url: https://github.com/sonatype-nexus-community
  - type: Blog
    url: https://www.sonatype.com/blog
  - type: Changelog
    url: https://help.sonatype.com/en/sonatype-iq-server-2025-release-notes.html
  - type: Support
    url: https://support.sonatype.com/
  - type: Pricing
    url: https://www.sonatype.com/products/pricing
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
