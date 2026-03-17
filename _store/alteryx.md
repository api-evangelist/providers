---
name: Alteryx
description: Alteryx is an analytics automation platform that enables data analysts and scientists to break data barriers, deliver insights, and experience the thrill of getting to the answer faster.
image: https://www.alteryx.com/sites/default/files/alteryx-logo-2021.svg
url: https://www.alteryx.com
created: 2024-01-15 00:00:00+00:00
modified: '2026-03-16'
specificationVersion: '0.19'
tags:
- analytics
- data science
- automation
- ETL
- machine learning
- predictive analytics
- data preparation
- data engineering
apis:
- name: Alteryx Server API
  description: REST API for managing workflows, schedules, and jobs on Alteryx Server. Provides Subscription, User V2, Admin V1, Admin V2, and V3 API endpoints for creating, updating, searching, and deleting users, user groups, schedules, credentials, collections, workflows, and Server connections.
  image: https://www.alteryx.com/sites/default/files/alteryx-logo-2021.svg
  humanURL: https://help.alteryx.com/current/en/server/api-overview.html
  baseURL: https://your-server/webapi
  tags:
  - workflows
  - automation
  - scheduling
  - jobs
  - server
  properties:
  - type: Documentation
    url: https://help.alteryx.com/current/en/server/api-overview.html
  - type: OpenAPI
    url: https://help.alteryx.com/developer-help/server-api-reference
  - type: Authentication
    url: https://help.alteryx.com/current/en/server/api-overview/alteryx-server-api-v3/server-api-configuration-and-authorization.html
  - type: PostmanCollection
    url: https://documenter.getpostman.com/view/14766220/TzeUmTWD
  - type: GettingStarted
    url: https://help.alteryx.com/current/en/developer-help/apis/get-started-with-apis.html
  contact:
  - FN: Alteryx Support
    email: support@alteryx.com
    url: https://community.alteryx.com
- name: Alteryx Server API V3
  description: The V3 Admin API for Alteryx Server uses OAuth 2 authentication and implements POST, PUT, GET, and DELETE functionality for modifying assets, users, credentials, and connections so admins can automate tasks and integrate Server with their existing API automation tools.
  image: https://www.alteryx.com/sites/default/files/alteryx-logo-2021.svg
  humanURL: https://help.alteryx.com/current/en/server/api-overview/alteryx-server-api-v3.html
  baseURL: https://your-server/webapi/v3
  tags:
  - server
  - admin
  - oauth2
  - workflows
  - users
  - credentials
  properties:
  - type: Documentation
    url: https://help.alteryx.com/current/en/server/api-overview/alteryx-server-api-v3.html
  - type: Authentication
    url: https://help.alteryx.com/current/en/server/api-overview/alteryx-server-api-v3/server-api-configuration-and-authorization.html
  - type: OpenAPI
    url: openapi/alteryx-server-api-v3.yml
  - type: JSONSchema
    url: json-schema/alteryx-workflow-schema.json
  - type: JSONLD
    url: json-ld/alteryx-context.jsonld
  contact:
  - FN: Alteryx Support
    email: support@alteryx.com
    url: https://community.alteryx.com
- name: Alteryx Server API V1
  description: The V1 API for Alteryx Server provides endpoints for admins including the Migratable Endpoint for migrating workflows across Server environments and the Auditlog Endpoint for tracking changes to system entities.
  image: https://www.alteryx.com/sites/default/files/alteryx-logo-2021.svg
  humanURL: https://help.alteryx.com/current/en/server/api-overview/alteryx-server-api-v1.html
  baseURL: https://your-server/webapi/v1
  tags:
  - server
  - admin
  - migration
  - audit
  properties:
  - type: Documentation
    url: https://help.alteryx.com/current/en/server/api-overview/alteryx-server-api-v1.html
  contact:
  - FN: Alteryx Support
    email: support@alteryx.com
    url: https://community.alteryx.com
- name: Alteryx Gallery API
  description: API for interacting with Alteryx Analytics Gallery for workflow sharing and execution
  image: https://www.alteryx.com/sites/default/files/alteryx-logo-2021.svg
  humanURL: https://help.alteryx.com/developer-help/gallery-api-overview
  baseURL: https://gallery.alteryx.com/api
  tags:
  - gallery
  - workflows
  - sharing
  - public API
  properties:
  - type: Documentation
    url: https://help.alteryx.com/developer-help/gallery-api-overview
  - type: OpenAPI
    url: https://help.alteryx.com/developer-help/gallery-api-reference
  - type: Authentication
    url: https://help.alteryx.com/developer-help/gallery-api-authentication
  contact:
  - FN: Alteryx Support
    email: support@alteryx.com
    url: https://community.alteryx.com
- name: Alteryx Connect API
  description: API for Alteryx Connect data catalog and collaboration platform
  image: https://www.alteryx.com/sites/default/files/alteryx-logo-2021.svg
  humanURL: https://help.alteryx.com/developer-help/connect-api
  baseURL: https://your-connect-server/api
  tags:
  - data catalog
  - metadata
  - collaboration
  - governance
  properties:
  - type: Documentation
    url: https://help.alteryx.com/developer-help/connect-api
  - type: Authentication
    url: https://help.alteryx.com/developer-help/connect-authentication
  contact:
  - FN: Alteryx Support
    email: support@alteryx.com
    url: https://community.alteryx.com
- name: Alteryx AlteryxEngine API
  description: The AlteryxEngine API allows you to call into the Alteryx Engine to build applications that can programmatically execute Alteryx Designer workflows. Workflows and applications can be executed as a separate child process or in-process.
  image: https://www.alteryx.com/sites/default/files/alteryx-logo-2021.svg
  humanURL: https://help.alteryx.com/current/en/developer-help/apis/alteryxengine-api-overview.html
  baseURL: https://your-server/api
  tags:
  - engine
  - workflows
  - designer
  - execution
  properties:
  - type: Documentation
    url: https://help.alteryx.com/current/en/developer-help/apis/alteryxengine-api-overview.html
  - type: GettingStarted
    url: https://help.alteryx.com/current/en/developer-help/apis/alteryxengine-api-overview/alteryxengine-api-example.html
  contact:
  - FN: Alteryx Support
    email: support@alteryx.com
    url: https://community.alteryx.com
- name: Alteryx Designer Cloud API
  description: REST API for Alteryx Designer Cloud (powered by Trifacta) providing data preparation, transformation, and pipeline management capabilities. Enables programmatic access to data preparation workflows and job execution.
  image: https://www.alteryx.com/sites/default/files/alteryx-logo-2021.svg
  humanURL: https://help.alteryx.com/dataprep/en/developer/api-reference.html
  baseURL: https://api.trifacta.com
  tags:
  - data preparation
  - cloud
  - trifacta
  - transformation
  - pipelines
  properties:
  - type: Documentation
    url: https://help.alteryx.com/dataprep/en/developer/api-reference.html
  - type: APIReference
    url: https://api.trifacta.com/
  - type: Authentication
    url: https://help.alteryx.com/Dataprep/en/developer/api-reference/manage-api-access-tokens.html
  contact:
  - FN: Alteryx Support
    email: support@alteryx.com
    url: https://community.alteryx.com
common:
- type: Portal
  url: https://help.alteryx.com/current/en/developer-help.html
- type: Getting Started
  url: https://help.alteryx.com/current/en/developer-help/apis/get-started-with-apis.html
- type: APIs
  url: https://help.alteryx.com/current/en/developer-help/apis.html
- type: Authentication
  url: https://help.alteryx.com/current/en/server/api-overview/alteryx-server-api-v3/server-api-configuration-and-authorization.html
- type: SDK
  url: https://help.alteryx.com/current/en/developer-help/platform-sdk.html
- type: PythonSDK
  url: https://help.alteryx.com/current/en/developer-help/platform-sdk/ayx-python-sdk-v2.html
- type: Status
  url: https://status.alteryx.com
- type: Support
  url: https://community.alteryx.com
- type: Blog
  url: https://community.alteryx.com/t5/Engine-Works/bg-p/engine-works
- type: Twitter
  url: https://twitter.com/alteryx
- type: LinkedIn
  url: https://www.linkedin.com/company/alteryx
- type: GitHub
  url: https://github.com/alteryx
- type: Pricing
  url: https://www.alteryx.com/products/pricing
- type: Trust
  url: https://www.alteryx.com/trust
- type: Terms of Service
  url: https://www.alteryx.com/terms-and-conditions
- type: Privacy Policy
  url: https://www.alteryx.com/privacy-policy
- type: Legal
  url: https://www.alteryx.com/legal
maintainers:
- FN: Kin Lane
  email: kin@apievangelist.com
  url: https://www.alteryx.com
---