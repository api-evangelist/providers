---
aid: jetbrains
url: https://raw.githubusercontent.com/api-evangelist/jetbrains/refs/heads/main/apis.yml
apis:
- aid: jetbrains:space-api
  name: JetBrains Space HTTP API
  tags:
  - Collaboration
  - Developer Tools
  - Project Management
  humanURL: https://www.jetbrains.com/help/space/http-api-model.html
  properties:
  - url: https://www.jetbrains.com/help/space/http-api-model.html
    type: Documentation
  - url: openapi/jetbrains-space-openapi.yml
    type: OpenAPI
  - url: json-schema/project.json
    type: JSONSchema
  - url: json-schema/user.json
    type: JSONSchema
  - url: json-ld/jetbrains-context.jsonld
    type: JSONLD
  description: The JetBrains Space HTTP API provides programmatic access to Space functionality including projects, teams, chats, documents, code reviews, packages, and automation jobs. The API uses JSON format and supports OAuth 2.0 authentication. An HTTP API playground is available within Space for interactive exploration of all available endpoints.
- aid: jetbrains:teamcity-api
  name: JetBrains TeamCity REST API
  tags:
  - Build Automation
  - CI/CD
  - Developer Tools
  humanURL: https://www.jetbrains.com/help/teamcity/rest/teamcity-rest-api-documentation.html
  properties:
  - url: https://www.jetbrains.com/help/teamcity/rest/teamcity-rest-api-documentation.html
    type: Documentation
  - url: openapi/jetbrains-teamcity-openapi.yml
    type: OpenAPI
  - url: json-schema/build.json
    type: JSONSchema
  - url: json-schema/build-agent.json
    type: JSONSchema
  - url: json-schema/project.json
    type: JSONSchema
  - url: json-ld/jetbrains-context.jsonld
    type: JSONLD
  description: The TeamCity REST API provides programmatic access to TeamCity CI/CD server functionality. It allows management of projects, build configurations, builds, agents, VCS roots, users, and more. The API uses locators for flexible filtering and supports both JSON and XML formats. The full Swagger specification is available via the /app/rest/swagger.json endpoint.
- aid: jetbrains:youtrack-api
  name: JetBrains YouTrack REST API
  tags:
  - Developer Tools
  - Issue Tracking
  - Project Management
  humanURL: https://www.jetbrains.com/help/youtrack/devportal/youtrack-rest-api.html
  properties:
  - url: https://www.jetbrains.com/help/youtrack/devportal/youtrack-rest-api.html
    type: Documentation
  - url: openapi/jetbrains-youtrack-openapi.yml
    type: OpenAPI
  - url: json-schema/issue.json
    type: JSONSchema
  - url: json-schema/project.json
    type: JSONSchema
  - url: json-schema/user.json
    type: JSONSchema
  - url: json-ld/jetbrains-context.jsonld
    type: JSONLD
  description: The YouTrack REST API lets you perform programmatic actions in the issue tracker, including creating, modifying, and querying issues, managing projects, agile boards, work items, and more. The API uses JSON format and supports both permanent token and OAuth 2.0 authentication. A Postman collection is available for interactive exploration.
- aid: jetbrains:hub-api
  name: JetBrains Hub REST API
  tags:
  - Authentication
  - Authorization
  - Identity Management
  humanURL: https://www.jetbrains.com/help/youtrack/devportal/hub-rest-api-reference.html
  properties:
  - url: https://www.jetbrains.com/help/youtrack/devportal/hub-rest-api-reference.html
    type: Documentation
  - url: openapi/jetbrains-hub-openapi.yml
    type: OpenAPI
  - url: json-schema/user.json
    type: JSONSchema
  - url: json-ld/jetbrains-context.jsonld
    type: JSONLD
  description: The JetBrains Hub REST API provides programmatic access to Hub, the centralized authentication and authorization service for JetBrains tools. It allows management of users, groups, projects, roles, permissions, and OAuth 2.0 services. Hub serves as the identity provider for YouTrack, TeamCity, and other connected JetBrains services.
- aid: jetbrains:marketplace-api
  name: JetBrains Marketplace API
  tags:
  - Developer Tools
  - Marketplace
  - Plugins
  humanURL: https://plugins.jetbrains.com/docs/marketplace/api-reference.html
  properties:
  - url: https://plugins.jetbrains.com/docs/marketplace/api-reference.html
    type: Documentation
  - url: openapi/jetbrains-marketplace-openapi.yml
    type: OpenAPI
  - url: json-schema/plugin.json
    type: JSONSchema
  - url: json-ld/jetbrains-context.jsonld
    type: JSONLD
  description: The JetBrains Marketplace API provides programmatic access to the plugin marketplace for JetBrains IDEs. It allows listing plugins by IDE compatibility, searching for plugins, uploading new plugins and updates, downloading plugin files, and checking plugin licenses. The API serves both plugin developers and consumers integrating with the JetBrains plugin ecosystem.
name: JetBrains
tags:
- CI/CD
- Developer Tools
- IDE
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: JetBrains is a software development company that provides integrated development environments, CI/CD tools, issue tracking, and team collaboration platforms for software developers. Their product suite includes IntelliJ IDEA, TeamCity, YouTrack, Space, Hub, and the JetBrains Marketplace, all of which offer APIs for programmatic integration and automation of development workflows.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

