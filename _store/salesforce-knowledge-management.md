---
aid: salesforce-knowledge-management
url: https://raw.githubusercontent.com/api-evangelist/salesforce-knowledge-management/refs/heads/main/apis.yml
apis:
- name: Salesforce Knowledge REST API
  description: REST API for accessing and managing knowledge articles and their metadata.
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
    url: https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_rest_knowledge.htm
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
name: Salesforce Knowledge Management
tags:
- Articles
- CRM
- Documentation
- Knowledge Management
- Support
type: Contract
image: https://www.salesforce.com/content/dam/web/en_us/www/images/sf-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: API for managing knowledge articles, categories, and data in Salesforce Knowledge.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

