---
aid: shuffle
name: Shuffle
description: Shuffle is an open source security automation platform (SOAR) built for and by security professionals. The platform enables security teams to orchestrate workflows across their entire security tool stack using a no-code/low-code interface powered by OpenAPI integrations. Shuffle provides workflow automation, app integration, webhook triggers, scheduled executions, file storage, and organization management via a comprehensive REST API. It follows the Unix philosophy of doing one thing well — connecting security tools through REST APIs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Security
  - Workflows
  - Automation
  - SOAR
  - Orchestration
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/shuffle/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: shuffle:shuffle-api
    name: Shuffle API
    description: The Shuffle REST API provides programmatic access to all platform capabilities including workflow management, app integration, execution control, user and organization management, file storage, datastore operations, and webhook triggers. Authentication uses a Bearer token from the user's profile settings. The API is available for both the cloud service at shuffler.io and self-hosted on-premises deployments.
    humanURL: https://shuffler.io/docs/API
    baseURL: https://shuffler.io/api/v1
    tags:
      - Security
      - Workflows
      - Automation
      - SOAR
      - Orchestration
    properties:
      - type: Documentation
        url: https://shuffler.io/docs
      - type: ApiReference
        url: https://shuffler.io/docs/API
      - type: GettingStarted
        url: https://shuffler.io/docs/getting_started
      - type: GitHubOrganization
        url: https://github.com/Shuffle
      - type: OpenSource
        url: https://github.com/Shuffle/Shuffle
      - type: Pricing
        url: https://shuffler.io/pricing
      - type: SignUp
        url: https://shuffler.io
      - type: Blog
        url: https://medium.com/shuffle-automation
      - type: Discord
        url: https://discord.com/invite/B2CBzUm
      - type: OpenAPI
        url: openapi/shuffle-openapi.yml
      - type: JSONSchema
        url: json-schema/shuffle-workflow-schema.json
      - type: JSONSchema
        url: json-schema/shuffle-execution-schema.json
      - type: JSONStructure
        url: json-structure/shuffle-workflow-structure.json
      - type: JSONLD
        url: json-ld/shuffle-context.jsonld
      - type: SpectralRules
        url: rules/shuffle-rules.yml
      - type: NaftikoCapabilities
        url: capabilities/security-workflow-automation.yaml
      - type: Vocabulary
        url: vocabulary/shuffle-vocabulary.yml
    contact:
      - FN: Shuffle Support
        url: https://shuffler.io/docs
        email: frikky@shuffler.io
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
