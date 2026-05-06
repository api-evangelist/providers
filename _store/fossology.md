---
aid: fossology
name: FOSSology
description: FOSSology is a Linux Foundation project providing open source license compliance software that scans source code for licenses, copyrights, and export control information. It helps organizations manage their open source license obligations through automated scanning, human clearing workflows, and SPDX/compliance reporting via a self-hosted REST API.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Compliance
  - Licensing
  - Linux Foundation
  - Scanning
  - SPDX
  - Open Source
created: '2026-03-16'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/fossology/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: fossology:fossology-api
    name: FOSSology API
    description: Programmatic access to FOSSology license scanning, copyright analysis, clearing workflow, SPDX/compliance report generation, obligations, users, groups, and instance maintenance via a self-hosted REST API.
    humanURL: https://www.fossology.org/get-started/
    baseURL: http://localhost/repo/api/v1
    tags:
      - Compliance
      - Licensing
      - Scanning
      - SPDX
    properties:
      - type: Documentation
        url: https://www.fossology.org/get-started/
      - type: Documentation
        name: Basic REST API Calls
        url: https://www.fossology.org/get-started/basic-rest-api-calls/
      - type: Documentation
        name: REST API Wiki
        url: https://github.com/fossology/fossology/wiki/FOSSology-REST-API
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/fossology/refs/heads/main/openapi/fossology-openapi.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/fossology/refs/heads/main/rules/fossology-rules.yml
      - type: Capabilities
        url: https://raw.githubusercontent.com/api-evangelist/fossology/refs/heads/main/capabilities/fossology-capabilities.yml
      - type: JSONSchema
        name: Upload Schema
        url: https://raw.githubusercontent.com/api-evangelist/fossology/refs/heads/main/json-schema/fossology-upload.json
      - type: JSONSchema
        name: License Schema
        url: https://raw.githubusercontent.com/api-evangelist/fossology/refs/heads/main/json-schema/fossology-license.json
      - type: JSONSchema
        name: Job Schema
        url: https://raw.githubusercontent.com/api-evangelist/fossology/refs/heads/main/json-schema/fossology-job.json
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/fossology/refs/heads/main/json-ld/fossology-context.jsonld
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/fossology/refs/heads/main/vocabulary/fossology-vocabulary.yml
      - type: Example
        name: Upload Example
        url: https://raw.githubusercontent.com/api-evangelist/fossology/refs/heads/main/examples/fossology-upload-example.json
      - type: Example
        name: License Example
        url: https://raw.githubusercontent.com/api-evangelist/fossology/refs/heads/main/examples/fossology-license-example.json
      - type: SourceCode
        url: https://github.com/fossology/fossology
common:
  - type: Documentation
    name: FOSSology Documentation
    description: Official documentation for FOSSology.
    url: https://www.fossology.org/get-started/
  - type: GitHubOrg
    name: FOSSology GitHub
    description: Source code and repositories for FOSSology.
    url: https://github.com/fossology
  - type: Wiki
    name: FOSSology Wiki
    url: https://github.com/fossology/fossology/wiki
  - type: License
    name: GPL-2.0-only
    url: https://github.com/fossology/fossology/blob/master/LICENSE
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
