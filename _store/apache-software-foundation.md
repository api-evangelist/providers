---
aid: apache-software-foundation
name: Apache Software Foundation
description: APIs for the Apache Software Foundation (ASF), a nonprofit organization that supports the development of open-source software projects under the Apache License, providing governance, legal protection, and infrastructure for over 350 projects. The ASF exposes public APIs for project discovery, committee governance data, member information, and organizational structure through its Projects API and Whimsy Public Data API.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - ASF
  - Open Source
  - Governance
  - Projects
  - Apache
created: '2025-01-01'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-software-foundation/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-software-foundation:projects-api
    name: Apache Software Foundation Projects API
    description: The Apache Software Foundation Projects API provides read-only access to JSON data about ASF projects, committees, releases, and podlings. The data is served as static JSON files from projects.apache.org and includes comprehensive information about the foundation's structure, project metadata, committee membership, release histories, and incubating podlings.
    humanURL: https://projects.apache.org/
    tags:
      - Committees
      - Open Source
      - Projects
      - Releases
      - Podlings
    properties:
      - type: Documentation
        url: https://projects.apache.org/
      - type: OpenAPI
        url: openapi/apache-software-foundation-projects-api-openapi.yml
      - type: JSONSchema
        url: json-schema/apache-software-foundation-project-schema.json
      - type: JSONSchema
        url: json-schema/apache-software-foundation-committee-schema.json
      - type: JSONSchema
        url: json-schema/apache-software-foundation-podling-schema.json
  - aid: apache-software-foundation:whimsy-api
    name: Apache Software Foundation Whimsy Public Data API
    description: The Apache Whimsy Public Data API provides access to publicly available information about the Apache Software Foundation's organizational structure. It exposes data about committees, members, committers, and ICLA (Individual Contributor License Agreement) information. The data is maintained by the ASF Secretary and Whimsy tooling.
    humanURL: https://whimsy.apache.org/public/
    tags:
      - Governance
      - Members
      - Open Source
      - Committees
    properties:
      - type: Documentation
        url: https://whimsy.apache.org/public/
      - type: OpenAPI
        url: openapi/apache-software-foundation-whimsy-api-openapi.yml
common:
  - type: Portal
    url: https://www.apache.org/
  - type: Blog
    url: https://blogs.apache.org/
  - type: Documentation
    url: https://www.apache.org/foundation/
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: SpectralRules
    url: rules/apache-software-foundation-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-software-foundation-vocabulary.yaml
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: Features
    data:
      - name: Project Directory
        description: Comprehensive directory of all 350+ ASF top-level projects with metadata.
      - name: Committee Data
        description: Project Management Committee membership, chair, and governance information.
      - name: Podling Tracking
        description: Apache Incubator podling status, mentors, and graduation tracking.
      - name: Release History
        description: Release version and date history for all ASF projects.
      - name: Whimsy Member Data
        description: Public member, committer, and ICLA data from the ASF Whimsy system.
  - type: UseCases
    data:
      - name: Apache Project Discovery
        description: Discover and explore all Apache Software Foundation projects programmatically.
      - name: Governance Transparency
        description: Access committee membership and governance data for ASF organizational research.
      - name: Release Monitoring
        description: Track release histories and versions across all ASF projects.
      - name: Incubator Tracking
        description: Monitor Apache Incubator podlings and their progression to top-level projects.
  - type: Integrations
    data:
      - name: Apache GitHub Organization
        description: All ASF project repositories hosted under the apache GitHub organization.
      - name: ASF JIRA
        description: Issue tracking at issues.apache.org for all ASF project bug reports and features.
      - name: Apache Confluence
        description: Wiki documentation at cwiki.apache.org for ASF project and foundation docs.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
