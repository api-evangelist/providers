---
aid: voiden
name: Voiden
description: Voiden is an offline-first, Git-native API workspace that unifies API design, testing, and documentation in plain Markdown .void files stored alongside your codebase. It uses composable, reusable blocks (endpoints, auth, headers, params, bodies) that behave like code — inheritable, versionable, and composable — eliminating copy-paste drift across API definitions. Supports REST, GraphQL, WebSocket, and gRPC. Built on Electron (TypeScript), Apache 2.0 licensed.
type: Index
url: https://voiden.md/
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Design
  - API Testing
  - API Documentation
  - Developer Tools
  - Git Native
  - Markdown
created: '2026-01-02'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: voiden:voiden-tool
    name: Voiden Desktop Tool
    description: Voiden is a desktop application (Electron/TypeScript) for API design, testing, and documentation using .void file format — plain Markdown with structured request blocks. Features reusable blocks with inheritance and composition, Git-native versioning, batch request execution with assertions, OpenAPI and Postman import, pre/post-request scripting (JavaScript, Python, shell), and offline-first operation. No public REST API.
    humanURL: https://voiden.md/
    tags:
      - Desktop App
      - API Workspace
      - Developer Tools
    properties:
      - type: Documentation
        url: https://voiden.md/
      - type: GitHubRepository
        url: https://github.com/VoidenHQ/voiden
      - type: JSONSchema
        url: json-schema/voiden-void-file-schema.json
common:
  - type: Website
    url: https://voiden.md/
  - type: GitHubRepository
    url: https://github.com/VoidenHQ/voiden
  - type: JSONSchema
    url: json-schema/voiden-void-file-schema.json
  - type: JSONStructure
    url: json-structure/voiden-void-file-structure.json
  - type: JSON-LD
    url: json-ld/voiden-context.jsonld
  - type: Vocabulary
    url: vocabulary/voiden-vocabulary.yml
  - type: Blog
    url: https://voiden.md/blog/
  - type: License
    url: https://github.com/VoidenHQ/voiden/blob/main/LICENSE
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
