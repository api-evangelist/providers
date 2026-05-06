---
aid: traceable
name: Traceable
description: Traceable is an API security and observability platform that provides API discovery, threat detection, and protection across the full application lifecycle. It uses context-aware AI to detect and block API-based attacks while providing deep visibility into API behavior and risk. Traceable exposes public GraphQL APIs for configuration, analytics, and operational data access, as well as an MCP server with 12 tools for AI-assisted security workflows.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Discovery
  - API Protection
  - API Security
  - API Testing
  - Observability
  - Security
  - Threat Detection
created: '2025-01-08'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/traceable/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: traceable:traceable-platform-graphql
    name: Traceable Platform GraphQL API
    description: The Traceable Platform GraphQL API provides programmatic access to API security configuration and operational data. Supports queries for API discovery analytics, vulnerability data, threat activity, entity scoping, and API test suite management. Authentication uses a platform API token passed in the Authorization header.
    humanURL: https://docs.traceable.ai/docs/public-apis
    baseURL: https://api.traceable.ai
    tags:
      - API Discovery
      - API Security
      - GraphQL
      - Threat Detection
      - Vulnerability Management
    properties:
      - type: Documentation
        url: https://docs.traceable.ai/docs/public-apis
      - type: OpenAPI
        url: openapi/traceable-platform-openapi.yml
      - type: JSONSchema
        url: json-schema/traceable-api-entity-schema.json
      - type: JSONStructure
        url: json-structure/traceable-api-entity-structure.json
      - type: JSONLd
        url: json-ld/traceable-context.jsonld
      - type: SpectralRules
        url: rules/traceable-rules.yml
      - type: NaftikoCapabilities
        url: capabilities/api-security-operations.yaml
      - type: Vocabulary
        url: vocabulary/traceable-vocabulary.yml
      - type: GraphQL
        url: https://api.traceable.ai/graphql
      - type: APISpecDownload
        url: https://docs.traceable.ai/docs/download-api-spec
  - aid: traceable:traceable-platform
    name: Traceable API Security Platform
    description: Traceable provides an intelligent API security platform offering API discovery, threat detection and protection, and API security testing. It uses distributed tracing and context-aware AI to understand API behavior, detect threats, and protect APIs across the full application lifecycle. The platform supports REST, SOAP, gRPC, GraphQL, and WebSocket APIs.
    humanURL: https://www.traceable.ai
    tags:
      - API Discovery
      - API Security
      - API Testing
      - Observability
      - Threat Detection
    properties:
      - type: Documentation
        url: https://docs.traceable.ai
      - type: APIDiscovery
        url: https://www.traceable.ai/product/api-discovery
      - type: ThreatDetection
        url: https://www.traceable.ai/product/threat-detection
      - type: APISecurityTesting
        url: https://www.traceable.ai/product/api-security-testing
      - type: MCPServer
        url: https://docs.traceable.ai/docs/traceable-mcp-server
  - aid: traceable:traceable-ast
    name: Traceable Active Security Testing
    description: Traceable Active Security Testing (AST) provides automated API security testing with GraphQL-based configuration for scan creation, suite management, and CI/CD pipeline integration. Supports GitHub Actions, GitLab CI, and Jenkins integrations.
    humanURL: https://docs.traceable.ai/docs/en/ast-getting-started
    tags:
      - API Security Testing
      - CI/CD
      - DAST
      - Security Automation
    properties:
      - type: Documentation
        url: https://docs.traceable.ai/docs/en/ast-getting-started
      - type: GitHubAction
        url: https://github.com/Traceableai/ast-action
      - type: JenkinsPlugin
        url: https://github.com/Traceableai/traceable-xast-jenkins-plugin
      - type: GraphQLScanAPI
        url: https://docs.traceable.ai/docs/scans-using-graphql-api
      - type: GraphQLSuiteAPI
        url: https://docs.traceable.ai/docs/suites-using-graphql-api
common:
  - type: Website
    url: https://www.traceable.ai
  - type: Documentation
    url: https://docs.traceable.ai
  - type: Blog
    url: https://www.traceable.ai/blog
  - type: About
    url: https://www.traceable.ai/company
  - type: Contact
    url: https://www.traceable.ai/contact
  - type: Demo
    url: https://www.traceable.ai/request-demo
  - type: Partners
    url: https://www.traceable.ai/partners
  - type: Resources
    url: https://www.traceable.ai/resources
  - type: LinkedIn
    url: https://www.linkedin.com/company/traboraceable/
  - type: Twitter
    url: https://twitter.com/ATraceableAI
  - type: GitHub
    url: https://github.com/Traceableai
  - type: MCPServer
    url: https://docs.traceable.ai/docs/traceable-mcp-server
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
