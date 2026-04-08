---
aid: oracle-apex
url: https://raw.githubusercontent.com/api-evangelist/oracle-apex/refs/heads/main/apis.yml
apis:
- name: Oracle APEX REST Data Services API
  description: RESTful API for Oracle APEX applications enabling data access and manipulation through REST endpoints.
  image: https://www.oracle.com/a/ocom/img/apex-logo.png
  humanUrl: https://apex.oracle.com/
  baseUrl: https://apex.oracle.com/pls/apex/
  tags:
  - Data Services
  - Database
  - Low-Code
  - REST
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/oracle/apex/latest/htmdb/
  - type: OpenAPI
    url: https://docs.oracle.com/en/database/oracle/apex/latest/aelig/rest-data-services.html
  - type: Authentication
    url: https://docs.oracle.com/en/database/oracle/apex/latest/htmdb/authentication.html
  - type: GettingStarted
    url: https://apex.oracle.com/en/learn/getting-started/
  contact:
  - FN: Oracle APEX Support
    email: apex-info_us@oracle.com
    url: https://apex.oracle.com/community
- name: Oracle APEX SQL Workshop API
  description: API for accessing SQL Workshop functionality programmatically.
  image: https://www.oracle.com/a/ocom/img/apex-logo.png
  humanUrl: https://apex.oracle.com/
  baseUrl: https://apex.oracle.com/pls/apex/
  tags:
  - Database
  - Development
  - SQL
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/oracle/apex/latest/
  - type: Tutorials
    url: https://apex.oracle.com/en/learn/tutorials/
  - type: API Reference
    url: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/
  contact:
  - FN: Oracle APEX Support
    email: apex-info_us@oracle.com
    url: https://apex.oracle.com/community
- name: Oracle APEX Application API
  description: API for managing APEX applications, pages, and components.
  image: https://www.oracle.com/a/ocom/img/apex-logo.png
  humanUrl: https://apex.oracle.com/
  baseUrl: https://apex.oracle.com/pls/apex/
  tags:
  - Applications
  - Development
  - Management
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/oracle/apex/latest/aeapi/
  - type: API Reference
    url: https://docs.oracle.com/en/database/oracle/apex/latest/aeapi/APEX_APPLICATION.html
  - type: GettingStarted
    url: https://apex.oracle.com/en/learn/getting-started/
  contact:
  - FN: Oracle APEX Support
    email: apex-info_us@oracle.com
    url: https://apex.oracle.com/community
- name: Oracle REST Data Services (ORDS) API
  description: REST API framework integrated with APEX for creating RESTful services including modules, templates, handlers, privileges, roles, OAuth clients, and AutoREST-enabled objects.
  image: https://www.oracle.com/a/ocom/img/apex-logo.png
  humanUrl: https://www.oracle.com/database/technologies/appdev/rest.html
  baseUrl: https://example.com/ords/_/db-api/stable/
  tags:
  - Integration
  - ORDS
  - REST
  - Web Services
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/
  - type: Installation Guide
    url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/latest/installation-guide/
  - type: Developer Guide
    url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/latest/developer-guide/
  - type: API Reference
    url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/25.2/orrst/index.html
  - type: OpenAPI
    url: openapi/ords-rest-api-openapi.json
  - type: FAQ
    url: https://www.oracle.com/tools/technologies/faq-rest-data-services.html
  contact:
  - FN: Oracle APEX Support
    email: apex-info_us@oracle.com
    url: https://apex.oracle.com/community
- name: Oracle APEX Cloud REST API
  description: REST APIs for provisioning and managing Oracle APEX instances in Oracle Cloud Infrastructure, including workspace and application lifecycle management.
  image: https://www.oracle.com/a/ocom/img/apex-logo.png
  humanUrl: https://docs.oracle.com/en/cloud/paas/apex/rest-apis.html
  baseUrl: https://apex.oracle.com/pls/apex/
  tags:
  - Administration
  - Cloud
  - Oracle Cloud
  - Provisioning
  - REST
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/cloud/paas/apex/rest-apis.html
  - type: GettingStarted
    url: https://docs.oracle.com/en/cloud/paas/apex/gsadd/sign-up-for-apex-service.html
  - type: Developer Guide
    url: https://docs.oracle.com/en/cloud/paas/apex/
  contact:
  - FN: Oracle APEX Support
    email: apex-info_us@oracle.com
    url: https://apex.oracle.com/community
- name: Oracle APEX Export and Import API
  description: PL/SQL and REST APIs for exporting and importing APEX applications, workspaces, and components using APEX_EXPORT and related packages.
  image: https://www.oracle.com/a/ocom/img/apex-logo.png
  humanUrl: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/APEX_EXPORT.html
  baseUrl: https://apex.oracle.com/pls/apex/
  tags:
  - Applications
  - Deployment
  - Export
  - Import
  - PL/SQL
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/APEX_EXPORT.html
  - type: API Reference
    url: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/
  - type: Blog
    url: https://blogs.oracle.com/apex/building-a-rest-api-to-deploy-apex-apps
  contact:
  - FN: Oracle APEX Support
    email: apex-info_us@oracle.com
    url: https://apex.oracle.com/community
- name: Oracle APEX Approval and Workflow API
  description: PL/SQL APIs for managing approvals, human tasks, and workflows in APEX applications using the APEX_APPROVAL and workflow packages.
  image: https://www.oracle.com/a/ocom/img/apex-logo.png
  humanUrl: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/
  baseUrl: https://apex.oracle.com/pls/apex/
  tags:
  - Approval
  - Automation
  - Human Tasks
  - PL/SQL
  - Workflow
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/oracle/apex/23.2/aeapi/APEX_APPROVAL.html
  - type: API Reference
    url: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/
  contact:
  - FN: Oracle APEX Support
    email: apex-info_us@oracle.com
    url: https://apex.oracle.com/community
- name: Oracle APEX Utility API
  description: The APEX_UTIL PL/SQL package provides utility functions for user management, authentication, session management, and other common APEX operations.
  image: https://www.oracle.com/a/ocom/img/apex-logo.png
  humanUrl: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/
  baseUrl: https://apex.oracle.com/pls/apex/
  tags:
  - Authentication
  - PL/SQL
  - Session
  - User Management
  - Utility
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/
  - type: API Reference
    url: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/APEX_UTIL.html
  contact:
  - FN: Oracle APEX Support
    email: apex-info_us@oracle.com
    url: https://apex.oracle.com/community
- name: Oracle APEX Generative AI API
  description: APIs for integrating generative AI capabilities into APEX applications, including chat, text generation, and vector embeddings introduced in APEX 24.2.
  image: https://www.oracle.com/a/ocom/img/apex-logo.png
  humanUrl: https://apex.oracle.com/en/platform/features/whats-new-242/
  baseUrl: https://apex.oracle.com/pls/apex/
  tags:
  - AI
  - Generative AI
  - Machine Learning
  - PL/SQL
  - Vector Search
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/
  - type: ReleaseNotes
    url: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/changes-in-this-release.html
  - type: Features
    url: https://apex.oracle.com/en/platform/features/whats-new-242/
  contact:
  - FN: Oracle APEX Support
    email: apex-info_us@oracle.com
    url: https://apex.oracle.com/community
- name: Oracle ORDS Database API
  description: REST API for Oracle Database management and monitoring operations through ORDS, including pluggable database management, data export, and performance monitoring.
  image: https://www.oracle.com/a/ocom/img/apex-logo.png
  humanUrl: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/25.2/
  baseUrl: https://example.com/ords/
  tags:
  - Database
  - Management
  - Monitoring
  - ORDS
  - REST
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/25.2/
  - type: API Reference
    url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/25.2/orrst/toc.htm
  - type: GettingStarted
    url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/25.2/
  contact:
  - FN: Oracle APEX Support
    email: apex-info_us@oracle.com
    url: https://apex.oracle.com/community
- name: Oracle APEX REST Administration API
  description: REST Administration API enabling APEX instance administrators to perform administrative functions over REST and HTTP protocols for machine-to-machine communication.
  image: https://www.oracle.com/a/ocom/img/apex-logo.png
  humanUrl: https://docs.oracle.com/database/apex-5.1/AEAPI/Using-REST-Administration-Interface-API.htm
  baseUrl: https://apex.oracle.com/pls/apex/
  tags:
  - Administration
  - Automation
  - Instance Management
  - REST
  properties:
  - type: Documentation
    url: https://docs.oracle.com/database/apex-5.1/AEAPI/Using-REST-Administration-Interface-API.htm
  - type: API Reference
    url: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/
  contact:
  - FN: Oracle APEX Support
    email: apex-info_us@oracle.com
    url: https://apex.oracle.com/community
name: Oracle APEX
tags:
- APEX
- Cloud
- Database
- Development Platform
- Enterprise
- Generative AI
- Low-Code
- Oracle
- ORDS
- PL/SQL
- REST API
- Web Applications
- Workflow
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Oracle Application Express (APEX) is a low-code development platform that enables you to build scalable, secure enterprise apps with world-class features.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

