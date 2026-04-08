---
aid: apache-software-foundation
url: https://raw.githubusercontent.com/api-evangelist/apache-software-foundation/refs/heads/main/apis.yml
apis:
- aid: apache-software-foundation:projects-api
  name: Apache Software Foundation Projects API
  tags:
  - Committees
  - Open Source
  - Projects
  humanURL: https://projects.apache.org/
  properties:
  - url: https://projects.apache.org/
    type: Documentation
  - url: openapi/apache-software-foundation-projects-api-openapi.yml
    type: OpenAPI
  - url: json-schema/apache-software-foundation-project-schema.json
    type: JSONSchema
  - url: json-schema/apache-software-foundation-committee-schema.json
    type: JSONSchema
  - url: json-schema/apache-software-foundation-podling-schema.json
    type: JSONSchema
  description: The Apache Software Foundation Projects API provides read-only access to JSON data about ASF projects, committees, releases, and podlings. The data is served as static JSON files from projects.apache.org and includes comprehensive information about the foundation's structure, project metadata, committee membership, release histories, and incubating podlings.
- aid: apache-software-foundation:whimsy-api
  name: Apache Software Foundation Whimsy Public Data API
  tags:
  - Governance
  - Members
  - Open Source
  humanURL: https://whimsy.apache.org/public/
  properties:
  - url: https://whimsy.apache.org/public/
    type: Documentation
  - url: openapi/apache-software-foundation-whimsy-api-openapi.yml
    type: OpenAPI
  description: The Apache Whimsy Public Data API provides access to publicly available information about the Apache Software Foundation's organizational structure. It exposes data about committees, members, committers, and ICLA (Individual Contributor License Agreement) information. The data is maintained by the ASF Secretary and Whimsy tooling.
name: Apache Software Foundation
tags:
- ASF
- Open Source
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for the Apache Software Foundation (ASF), a nonprofit organization that supports the development of open-source software projects under the Apache license, providing governance, legal protection, and infrastructure for over 350 projects.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

