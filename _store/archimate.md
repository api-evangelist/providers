---
aid: archimate
url: https://raw.githubusercontent.com/api-evangelist/archimate/refs/heads/main/apis.yml
apis:
- name: ArchiMate Model Exchange API
  description: API for exchanging ArchiMate models between tools and repositories using the Open Group ArchiMate Model Exchange File Format.
  image: https://www.opengroup.org/archimate-forum/archimate-overview
  humanURL: https://www.opengroup.org/archimate-forum/archimate-overview
  baseURL: https://api.example.com/archimate/v1
  tags:
  - Enterprise Architecture
  - Model Exchange
  - XML
  properties:
  - type: Documentation
    url: https://pubs.opengroup.org/architecture/archimate3-doc/
  - type: OpenAPI
    url: https://api.example.com/archimate/openapi.json
  - type: Swagger
    url: https://api.example.com/archimate/swagger.json
  - type: Schema
    url: https://www.opengroup.org/xsd/archimate/
  contact:
  - FN: The Open Group
    email: archimate-forum@opengroup.org
    url: https://www.opengroup.org/archimate-forum
- name: ArchiMate Repository API
  description: RESTful API for accessing and managing ArchiMate models, elements, relationships, and views stored in a central repository.
  image: https://www.opengroup.org/archimate-forum/archimate-overview
  humanURL: https://www.opengroup.org/archimate-forum
  baseURL: https://api.example.com/archimate/repository/v1
  tags:
  - CRUD Operations
  - Model Management
  - Repository
  - REST API
  properties:
  - type: Documentation
    url: https://pubs.opengroup.org/architecture/archimate3-doc/
  - type: OpenAPI
    url: https://api.example.com/archimate/repository/openapi.yaml
  - type: Authentication
    url: https://api.example.com/archimate/auth
  contact:
  - FN: The Open Group
    email: archimate-forum@opengroup.org
name: ArchiMate
tags:
- Application Architecture
- Architecture Framework
- Business Architecture
- Enterprise Architecture
- Modeling
- Technology Architecture
type: Contract
image: https://www.opengroup.org/archimate-forum/archimate-overview
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: ArchiMate is an open and independent enterprise architecture modeling language to support the description, analysis and visualization of architecture within and across business domains in an unambiguous way.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

