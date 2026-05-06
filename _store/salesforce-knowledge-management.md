---
name: Salesforce Knowledge Management
description: API for managing knowledge articles, categories, and data in Salesforce Knowledge. Enables creating, reading, updating, publishing, and archiving knowledge articles for customer self-service and agent-assisted support scenarios across multiple channels including internal app, public knowledge base, and customer portals.
image: https://www.salesforce.com/content/dam/web/en_us/www/images/sf-logo.svg
url: https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/
created: '2024'
modified: '2026-05-02'
specificationVersion: '0.18'
tags:
  - Articles
  - CRM
  - Customer Service
  - Documentation
  - Knowledge Management
  - Support
apis:
  - name: Salesforce Knowledge REST API
    description: REST API for accessing and managing Salesforce Knowledge articles, categories, and knowledge base content. Enables creating, reading, updating, publishing, and archiving knowledge articles for customer self-service and agent-assisted support scenarios.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/sf-logo.svg
    humanURL: https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/
    baseURL: https://yourInstance.salesforce.com/services/data/v59.0/support
    tags:
      - Articles
      - Knowledge
      - REST
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/knowledge_development.htm
      - type: OpenAPI
        url: openapi/salesforce-knowledge-management-rest-api-openapi.yml
      - type: Authentication
        url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_authentication.htm
    contact:
      - type: Support
        url: https://help.salesforce.com/
      - type: Community
        url: https://trailblazers.salesforce.com/
  - name: Salesforce Knowledge SOAP API
    description: SOAP API for managing knowledge articles with enterprise integration.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/sf-logo.svg
    humanURL: https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/
    baseURL: https://yourInstance.salesforce.com/services/Soap/c/59.0
    tags:
      - Enterprise
      - Knowledge
      - SOAP
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_knowledge.htm
      - type: WSDL
        url: https://yourInstance.salesforce.com/services/wsdl/class/KnowledgeArticleVersion
      - type: Authentication
        url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_quickstart_intro.htm
common:
  - type: Getting Started
    url: https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/knowledge_development_intro.htm
  - type: Authentication
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm
  - type: Rate Limits
    url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm
  - type: SDKs
    url: https://developer.salesforce.com/tools/sdks
  - type: Status
    url: https://status.salesforce.com/
  - type: Terms of Service
    url: https://www.salesforce.com/company/legal/agreements/
  - type: Privacy Policy
    url: https://www.salesforce.com/company/privacy/
  - type: Trailhead Learning
    url: https://trailhead.salesforce.com/en/content/learn/modules/knowledge-basics
  - type: GitHub Organization
    url: https://github.com/salesforce
  - type: Spectral Rules
    url: rules/salesforce-knowledge-management-rules.yml
  - type: Capabilities
    url: capabilities/knowledge-management.yaml
  - type: JSON Schema
    url: json-schema/salesforce-knowledge-management-article-schema.json
    title: Knowledge Article Schema
  - type: JSON Schema
    url: json-schema/salesforce-knowledge-management-category-schema.json
    title: Knowledge Category Schema
  - type: JSON-LD Context
    url: json-ld/salesforce-knowledge-management-context.jsonld
  - type: Vocabulary
    url: vocabulary/salesforce-knowledge-management-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
