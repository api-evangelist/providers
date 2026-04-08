---
aid: perforce
url: https://raw.githubusercontent.com/api-evangelist/perforce/refs/heads/main/apis.yml
apis:
- name: Perforce Helix Core API
  description: REST API for Helix Core version control system, providing programmatic access to repository operations, file management, and versioning capabilities.
  image: https://www.perforce.com/sites/default/files/helix-core-icon.png
  humanURL: https://www.perforce.com/products/helix-core
  baseURL: https://api.perforce.com/helix-core/v1
  tags:
  - DevOps
  - SCM
  - Source Control
  - Version Control
  properties:
  - type: Documentation
    url: https://www.perforce.com/manuals/p4api/
  - type: OpenAPI
    url: https://api.perforce.com/helix-core/openapi.json
  - type: Authentication
    url: https://www.perforce.com/manuals/p4api/Content/P4API/authentication.html
  - type: Swagger
    url: https://api.perforce.com/helix-core/swagger
  - type: GettingStarted
    url: https://www.perforce.com/products/helix-core/learning-resources
- name: Perforce P4 REST API
  description: Technology Preview REST API introduced with P4 Server 2025.2, providing a new way to automate workflows and integrate P4 with other tools via standard HTTP endpoints for server info, depots, files, and changelists.
  image: https://www.perforce.com/sites/default/files/helix-core-icon.png
  humanURL: https://help.perforce.com/helix-core/server-apps/p4sag/current/Content/P4SAG/p4-rest-api.html
  baseURL: https://p4server.example.com/api/v0
  tags:
  - Automation
  - DevOps
  - REST API
  - Version Control
  properties:
  - type: Documentation
    url: https://help.perforce.com/helix-core/server-apps/p4sag/current/Content/P4SAG/p4-rest-api.html
  - type: ChangeLog
    url: https://help.perforce.com/helix-core/server-apps/cmdref/2025.2/Content/CmdRef/whats-new-2025-2.html
- name: Perforce Helix Swarm API
  description: REST API for Helix Swarm code review and collaboration platform, enabling automated code review workflows and team collaboration.
  image: https://www.perforce.com/sites/default/files/helix-swarm-icon.png
  humanURL: https://www.perforce.com/products/helix-swarm
  baseURL: https://swarm.example.com/api/v10
  tags:
  - Code Review
  - Collaboration
  - Workflow
  properties:
  - type: Documentation
    url: https://www.perforce.com/manuals/swarm/Content/Swarm/swarm-apidoc.html
  - type: API Reference
    url: https://www.perforce.com/manuals/swarm/api/index.html
  - type: Authentication
    url: https://www.perforce.com/manuals/swarm/Content/Swarm/swarm-apidoc_endpoints.html
  - type: APIVersions
    url: https://help.perforce.com/helix-core/helix-swarm/swarm/current/Content/Swarm/swarm-apidoc_api_versions.html
  - type: APIEndpoints
    url: https://help.perforce.com/helix-core/helix-swarm/swarm/current/Content/Swarm/swarm-apidoc_endpoints.html
  - type: OpenAPI
    url: openapi/perforce-helix-swarm-openapi.yml
  - type: JSONSchema
    url: json-schema/perforce-review-schema.json
  - type: JSONLD
    url: json-ld/perforce-context.jsonld
- name: Perforce Hansoft API
  description: API for Hansoft agile project management, providing access to project planning, tracking, and reporting capabilities.
  image: https://www.perforce.com/sites/default/files/hansoft-icon.png
  humanURL: https://www.perforce.com/products/hansoft
  baseURL: https://hansoft.example.com/api
  tags:
  - Agile
  - Planning
  - Project Management
  properties:
  - type: Documentation
    url: https://www.perforce.com/manuals/hansoft-sdk/
  - type: SDK
    url: https://www.perforce.com/downloads/hansoft-sdk
- name: Perforce P4 Plan API
  description: GraphQL and REST API for P4 Plan (formerly Hansoft) agile project management, supporting queries, mutations, and real-time subscriptions for planning views, sprints, tasks, and user management.
  image: https://www.perforce.com/sites/default/files/hansoft-icon.png
  humanURL: https://www.perforce.com/products/hansoft
  baseURL: https://p4plan.example.com/api
  tags:
  - Agile
  - GraphQL
  - Planning
  - Project Management
  properties:
  - type: Documentation
    url: https://help.perforce.com/hansoft/current/Content/hansoftapi/index.html
  - type: RESTDocumentation
    url: https://help.perforce.com/hansoft/current/Content/hansoftapi/helixplan-api-rest-docs.html
  - type: Installation
    url: https://help.perforce.com/hansoft/current/Content/hansoftapi/installing-hansoft-api-service.htm
  - type: Download
    url: https://www.perforce.com/downloads/helix-plan-api
  - type: SDK
    url: https://www.perforce.com/downloads/helix-plan-sdk
  - type: ReleaseNotes
    url: https://cache.hansoft.com/releasenotes/helix-plan-api.html
- name: Perforce Helix ALM REST API
  description: REST API for Helix ALM application lifecycle management platform, enabling automation of tasks and development of integrations for requirements management, issue tracking, and test case management.
  image: https://www.perforce.com/sites/default/files/helix-alm-icon.png
  humanURL: https://www.perforce.com/products/helix-alm
  baseURL: https://helixalm.example.com/helix-alm/api/v0
  tags:
  - Application Lifecycle Management
  - Issue Tracking
  - Requirements Management
  - Test Management
  properties:
  - type: Documentation
    url: https://help.perforce.com/helix-alm/helixalm/current/restapi/Default.htm
  - type: API Reference
    url: https://help.perforce.com/helix-alm/helixalm/current/rest-api/index.html
  - type: GettingStarted
    url: https://help.perforce.com/helix-alm/helixalm/2019.3.0/restapi/Content/RESTAPI/GettingStarted.htm
- name: Perforce Helix TeamHub API
  description: REST API for Helix TeamHub source code repository management platform, providing access to repositories, projects, users, and company resources across Git, Mercurial, Subversion, and other repository types.
  image: https://www.perforce.com/sites/default/files/helix-teamhub-icon.png
  humanURL: https://www.perforce.com/products/helix-teamhub
  baseURL: https://teamhub.example.com/api/v1
  tags:
  - Collaboration
  - Git
  - Repositories
  - Source Code Management
  properties:
  - type: Documentation
    url: https://help.perforce.com/helix-core/helix-teamhub/current/Content/HTH-API/api-v1.html
  - type: APIv2Documentation
    url: https://help.perforce.com/helix-core/helix-teamhub/current/Content/HTH-API/api-v2.html
  - type: GettingStarted
    url: https://help.perforce.com/helix-core/helix-teamhub/2025.5.0/Content/HTH-API/getting-started.html
  - type: Webhooks
    url: https://help.perforce.com/helix-core/helix-teamhub/current/Content/HTH-User/webhooks-general.html
- name: Perforce P4 DAM REST API
  description: REST API for P4 DAM (Digital Asset Management), enabling integration with digital asset workflows for finding, reviewing, sharing, and managing versioned assets stored in Helix Core.
  image: https://www.perforce.com/sites/default/files/helix-dam-icon.png
  humanURL: https://www.perforce.com/products/helix-dam
  baseURL: https://dam.example.com/api
  tags:
  - Asset Management
  - Digital Asset Management
  - Media
  - Version Control
  properties:
  - type: Documentation
    url: https://help.perforce.com/helix-core/helix-dam/current/api/
  - type: Webhooks
    url: https://help.perforce.com/helix-core/helix-dam/current/Content/HelixDAM-User/using-webhooks.html
  - type: ProductDocumentation
    url: https://help.perforce.com/helix-core/helix-dam/current/
- name: Perforce P4 Search API
  description: REST API for P4 Search, providing indexing and search capabilities across Helix Core servers to support code review, file content search, and changelist description search.
  image: https://www.perforce.com/sites/default/files/helix-core-icon.png
  humanURL: https://help.perforce.com/helix-core/integrations-plugins/p4search/current/Content/P4Search/overview.html
  baseURL: https://p4search.example.com/api
  tags:
  - Code Search
  - Indexing
  - Search
  properties:
  - type: Documentation
    url: https://help.perforce.com/helix-core/integrations-plugins/p4search/current/Content/P4Search/api-endpoints.html
  - type: Swagger
    url: https://help.perforce.com/helix-core/integrations-plugins/p4search/current/Content/P4Search/api-endpoints-current.html
  - type: Authentication
    url: https://help.perforce.com/helix-core/integrations-plugins/p4search/current/Content/P4Search/api-authentication.html
- name: Perforce Helix Authentication Service API
  description: REST API for the Helix Authentication Service, a Node.js based authentication protocol integration service supporting OpenID Connect and SAML 2.0 for authenticating users across Perforce products.
  image: https://www.perforce.com/sites/default/files/helix-core-icon.png
  humanURL: https://help.perforce.com/helix-core/integrations-plugins/helix-auth-svc/current/
  baseURL: https://auth.example.com
  tags:
  - Authentication
  - Identity
  - OpenID Connect
  - SAML
  - SSO
  properties:
  - type: Documentation
    url: https://help.perforce.com/helix-core/integrations-plugins/helix-auth-svc/current/
  - type: API Reference
    url: https://github.com/perforce/helix-authentication-service/blob/main/docs/REST_API.md
  - type: GitHubRepository
    url: https://github.com/perforce/helix-authentication-service
  - type: Download
    url: https://www.perforce.com/downloads/helix-authentication-service
name: Perforce
tags:
- API
type: Contract
image: https://www.perforce.com/sites/default/files/perforce-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Perforce Software provides enterprise-scale development tools, including version control, application lifecycle management, agile planning, and static analysis solutions for development teams.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

