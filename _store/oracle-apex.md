---
aid: oracle-apex
name: Oracle APEX
description: Oracle Application Express (APEX) is a low-code development platform that enables you to build scalable, secure enterprise apps with world-class features.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/oracle-apex/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
type: Index
position: Consumer
access: 3rd-Party
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
apis:
  - name: Oracle APEX REST Data Services API
    description: RESTful API for Oracle APEX applications enabling data access and manipulation through REST endpoints.
    image: https://www.oracle.com/a/ocom/img/apex-logo.png
    humanURL: https://apex.oracle.com/
    baseURL: https://apex.oracle.com/pls/apex/
    tags:
      - Data Services
      - Database
      - Low-Code
      - REST
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/database/oracle/apex/latest/htmdb/
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
    humanURL: https://apex.oracle.com/
    baseURL: https://apex.oracle.com/pls/apex/
    tags:
      - Database
      - Development
      - SQL
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/database/oracle/apex/latest/
      - type: Tutorials
        url: https://apex.oracle.com/en/learn/tutorials/
      - type: APIReference
        url: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/
    contact:
      - FN: Oracle APEX Support
        email: apex-info_us@oracle.com
        url: https://apex.oracle.com/community
  - name: Oracle APEX Application API
    description: API for managing APEX applications, pages, and components.
    image: https://www.oracle.com/a/ocom/img/apex-logo.png
    humanURL: https://apex.oracle.com/
    baseURL: https://apex.oracle.com/pls/apex/
    tags:
      - Applications
      - Development
      - Management
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/database/oracle/apex/latest/aeapi/
      - type: APIReference
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
    humanURL: https://www.oracle.com/database/technologies/appdev/rest.html
    baseURL: https://example.com/ords/_/db-api/stable/
    tags:
      - Integration
      - ORDS
      - REST
      - Web Services
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/
      - type: APIReference
        url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/25.2/orrst/index.html
      - type: FAQ
        url: https://www.oracle.com/tools/technologies/faq-rest-data-services.html
    contact:
      - FN: Oracle APEX Support
        email: apex-info_us@oracle.com
        url: https://apex.oracle.com/community
  - name: Oracle APEX Cloud REST API
    description: REST APIs for provisioning and managing Oracle APEX instances in Oracle Cloud Infrastructure, including workspace and application lifecycle management.
    image: https://www.oracle.com/a/ocom/img/apex-logo.png
    humanURL: https://docs.oracle.com/en/cloud/paas/apex/rest-apis.html
    baseURL: https://apex.oracle.com/pls/apex/
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
    contact:
      - FN: Oracle APEX Support
        email: apex-info_us@oracle.com
        url: https://apex.oracle.com/community
  - name: Oracle APEX Export and Import API
    description: PL/SQL and REST APIs for exporting and importing APEX applications, workspaces, and components using APEX_EXPORT and related packages.
    image: https://www.oracle.com/a/ocom/img/apex-logo.png
    humanURL: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/APEX_EXPORT.html
    baseURL: https://apex.oracle.com/pls/apex/
    tags:
      - Applications
      - Deployment
      - Export
      - Import
      - PL/SQL
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/APEX_EXPORT.html
      - type: APIReference
        url: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/
    contact:
      - FN: Oracle APEX Support
        email: apex-info_us@oracle.com
        url: https://apex.oracle.com/community
  - name: Oracle APEX Approval and Workflow API
    description: PL/SQL APIs for managing approvals, human tasks, and workflows in APEX applications using the APEX_APPROVAL and workflow packages.
    image: https://www.oracle.com/a/ocom/img/apex-logo.png
    humanURL: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/
    baseURL: https://apex.oracle.com/pls/apex/
    tags:
      - Approval
      - Automation
      - Human Tasks
      - PL/SQL
      - Workflow
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/database/oracle/apex/23.2/aeapi/APEX_APPROVAL.html
      - type: APIReference
        url: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/
    contact:
      - FN: Oracle APEX Support
        email: apex-info_us@oracle.com
        url: https://apex.oracle.com/community
  - name: Oracle APEX Utility API
    description: The APEX_UTIL PL/SQL package provides utility functions for user management, authentication, session management, and other common APEX operations.
    image: https://www.oracle.com/a/ocom/img/apex-logo.png
    humanURL: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/
    baseURL: https://apex.oracle.com/pls/apex/
    tags:
      - Authentication
      - PL/SQL
      - Session
      - User Management
      - Utility
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/
      - type: APIReference
        url: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/APEX_UTIL.html
    contact:
      - FN: Oracle APEX Support
        email: apex-info_us@oracle.com
        url: https://apex.oracle.com/community
  - name: Oracle APEX Generative AI API
    description: APIs for integrating generative AI capabilities into APEX applications, including chat, text generation, and vector embeddings introduced in APEX 24.2.
    image: https://www.oracle.com/a/ocom/img/apex-logo.png
    humanURL: https://apex.oracle.com/en/platform/features/whats-new-242/
    baseURL: https://apex.oracle.com/pls/apex/
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
    humanURL: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/25.2/
    baseURL: https://example.com/ords/
    tags:
      - Database
      - Management
      - Monitoring
      - ORDS
      - REST
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/25.2/
      - type: APIReference
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
    humanURL: https://docs.oracle.com/database/apex-5.1/AEAPI/Using-REST-Administration-Interface-API.htm
    baseURL: https://apex.oracle.com/pls/apex/
    tags:
      - Administration
      - Automation
      - Instance Management
      - REST
    properties:
      - type: Documentation
        url: https://docs.oracle.com/database/apex-5.1/AEAPI/Using-REST-Administration-Interface-API.htm
      - type: APIReference
        url: https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/
    contact:
      - FN: Oracle APEX Support
        email: apex-info_us@oracle.com
        url: https://apex.oracle.com/community
common:
  - type: Documentation
    url: https://docs.oracle.com/en/database/oracle/apex/
  - type: Blog
    url: https://blogs.oracle.com/apex/
  - type: GitHubOrganization
    url: https://github.com/oracle/apex
  - type: YouTube
    url: https://www.youtube.com/c/OracleAPEX
  - type: Pricing
    url: https://www.oracle.com/application-development/apex/pricing/
  - type: GettingStarted
    url: https://apex.oracle.com/en/learn/getting-started/
  - type: Tutorials
    url: https://apex.oracle.com/en/learn/tutorials/
  - type: ReleaseNotes
    url: https://apex.oracle.com/en/learn/documentation/release-notes/
  - type: APIReference
    url: https://docs.oracle.com/en/database/oracle/apex/24.2/api-references.html
  - type: TermsOfService
    url: https://www.oracle.com/legal/terms/
  - type: PrivacyPolicy
    url: https://www.oracle.com/legal/privacy/privacy-policy/
  - type: FAQ
    url: https://www.oracle.com/tools/technologies/faq-rest-data-services.html
  - type: Support
    url: https://apex.oracle.com/community
  - type: SignUp
    url: https://docs.oracle.com/en/cloud/paas/apex/gsadd/sign-up-for-apex-service.html
  - type: Features
    data:
      - name: Low-Code Application Development
        description: Visual drag-and-drop application builder for creating enterprise web applications without extensive coding.
      - name: RESTful Web Services
        description: Built-in ORDS integration for exposing database objects and custom logic as REST APIs.
      - name: Generative AI Integration
        description: Native AI capabilities including chat, text generation, and vector embeddings for intelligent applications.
      - name: Workflow and Approvals
        description: Built-in workflow engine with human task management and approval chains for business process automation.
      - name: Progressive Web Apps
        description: Build installable progressive web applications with offline capabilities and native-like user experience.
      - name: Oracle Cloud Integration
        description: Seamless deployment and management on Oracle Cloud Infrastructure with automated provisioning.
  - type: UseCases
    data:
      - name: Enterprise Application Development
        description: Rapidly build and deploy internal enterprise applications for HR, finance, and operations.
      - name: Database REST API Creation
        description: Expose Oracle Database tables and views as RESTful services using ORDS AutoREST.
      - name: Workflow Automation
        description: Automate business approval processes and multi-step workflows with the APEX workflow engine.
      - name: Data Management Portals
        description: Build self-service data entry and management portals for business users with built-in validation.
      - name: AI-Enhanced Applications
        description: Integrate generative AI features into business applications for intelligent data processing and insights.
  - type: Integrations
    data:
      - name: Oracle Database
        description: Native integration with Oracle Database for data access, PL/SQL execution, and database object management.
      - name: Oracle Cloud Infrastructure
        description: Deploy APEX applications on OCI with autonomous database and cloud-native infrastructure services.
      - name: Oracle REST Data Services
        description: ORDS provides the REST API layer for APEX applications and database services.
      - name: Oracle Identity Cloud
        description: Single sign-on and identity management integration for enterprise authentication.
      - name: Microsoft Active Directory
        description: LDAP-based authentication and user synchronization with Active Directory environments.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
