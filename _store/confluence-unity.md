---
aid: confluence-unity
url: https://raw.githubusercontent.com/api-evangelist/confluence-unity/refs/heads/main/apis.yml
apis:
- name: Confluence Unity REST API
  description: REST API for managing spaces, pages, content, and users in Confluence Unity.
  image: https://www.atlassian.com/dam/jcr:confluence-logo.png
  humanURL: https://confluence.unity.com/display/API
  baseURL: https://confluence.unity.com/rest/api
  tags:
  - Content
  - Pages
  - REST
  - Spaces
  properties:
  - type: Documentation
    url: https://confluence.unity.com/rest/api/docs
  - type: OpenAPI
    url: https://confluence.unity.com/rest/api/openapi.json
  - type: Authentication
    url: https://confluence.unity.com/display/API/Authentication
  contact:
  - FN: Confluence Unity Support
    email: support@unity.com
    url: https://confluence.unity.com/support
- name: Confluence Unity Content API
  description: API for creating, reading, updating, and deleting content in Confluence.
  baseURL: https://confluence.unity.com/rest/api/content
  tags:
  - Blog Posts
  - Content
  - CRUD
  - Pages
  properties:
  - type: Documentation
    url: https://confluence.unity.com/rest/api/content/docs
  - type: Swagger
    url: https://confluence.unity.com/rest/api/content/swagger.json
- name: Confluence Unity Search API
  description: API for searching content across Confluence spaces.
  baseURL: https://confluence.unity.com/rest/api/search
  tags:
  - CQL
  - Query
  - Search
  properties:
  - type: Documentation
    url: https://confluence.unity.com/rest/api/search/docs
name: Confluence Unity
tags:
- Collaboration
- Content Management
- Documentation
- Knowledge Base
- Wiki
type: Contract
image: https://www.atlassian.com/dam/jcr:confluence-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: API for Confluence Unity - A collaboration and documentation platform.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

