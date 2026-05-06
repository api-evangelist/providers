---
aid: simplelocalize
name: SimpleLocalize
description: SimpleLocalize is a web-based translation management platform that helps small and growing teams save time on handling localization files and translation strings. It provides a REST API for managing translations, languages, projects, and customers, along with integrations for CI/CD pipelines, frameworks, and AI-powered tools.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Localization
  - Translation
  - Internationalization
created: '2025-02-08'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/simplelocalize/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: simplelocalize:translation-api
    name: SimpleLocalize Translation API
    description: The SimpleLocalize Translation API provides REST endpoints to create, read, update, and delete translations. It supports querying translations by key, language, namespace, text content, review status, and customer ID. The API also supports bulk import and export of translation files in 30+ formats including JSON, YAML, XLIFF, Android XML, iOS Strings, and more.
    humanURL: https://simplelocalize.io/docs/api/get-started/
    baseURL: https://api.simplelocalize.io
    tags:
      - Translation
      - Localization
      - Import
      - Export
    properties:
      - type: Documentation
        url: https://simplelocalize.io/docs/api/get-started/
      - type: OpenAPI
        url: https://api.simplelocalize.io/openapi/docs
      - type: SwaggerUI
        url: https://api.simplelocalize.io/openapi/ui
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/simplelocalize/refs/heads/main/openapi/simplelocalize-openapi.yml
    contact:
      - FN: SimpleLocalize Support
        url: https://simplelocalize.io/contact/
  - aid: simplelocalize:language-api
    name: SimpleLocalize Language API
    description: The SimpleLocalize Language API provides endpoints to create, list, update, and delete languages within a project. Each language is identified by a unique key and requires API key authentication via the X-SimpleLocalize-Token header.
    humanURL: https://simplelocalize.io/docs/api/language-api/
    baseURL: https://api.simplelocalize.io
    tags:
      - Languages
      - Localization
    properties:
      - type: Documentation
        url: https://simplelocalize.io/docs/api/language-api/
  - aid: simplelocalize:projects-api
    name: SimpleLocalize Projects API
    description: The SimpleLocalize Projects API allows creation and listing of translation projects. It uses Personal Token authentication (Bearer) rather than API keys, enabling multi-project management workflows.
    humanURL: https://simplelocalize.io/docs/api/translation-project-management/
    baseURL: https://api.simplelocalize.io
    tags:
      - Projects
      - Management
    properties:
      - type: Documentation
        url: https://simplelocalize.io/docs/api/translation-project-management/
  - aid: simplelocalize:customer-api
    name: SimpleLocalize Customer API
    description: The SimpleLocalize Customer API enables creation and management of customer-specific translations. Customers represent end-user segments with their own translation overrides, identified by a unique customer key.
    humanURL: https://simplelocalize.io/docs/api/customer-specific-api/
    baseURL: https://api.simplelocalize.io
    tags:
      - Customers
      - Localization
    properties:
      - type: Documentation
        url: https://simplelocalize.io/docs/api/customer-specific-api/
common:
  - type: Website
    url: https://simplelocalize.io/
  - type: Documentation
    url: https://simplelocalize.io/docs/
  - type: Pricing
    url: https://simplelocalize.io/pricing/
  - type: Blog
    url: https://simplelocalize.io/blog/
  - type: GitHubOrg
    url: https://github.com/simplelocalize
  - type: CLI
    url: https://github.com/simplelocalize/simplelocalize-cli
  - type: GithubAction
    url: https://github.com/simplelocalize/github-action-cli
  - type: VSCodeExtension
    url: https://github.com/simplelocalize/vscode-simplelocalize
  - type: MCP
    url: https://github.com/simplelocalize/simplelocalize-mcp-server
  - type: SDK
    url: https://github.com/simplelocalize/simplelocalize-cli-npm
  - type: TermsOfService
    url: https://simplelocalize.io/terms-of-service/
  - type: PrivacyPolicy
    url: https://simplelocalize.io/privacy-policy/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
