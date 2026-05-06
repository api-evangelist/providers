---
specificationVersion: '0.18'
name: ForgeRock
description: ForgeRock, now part of Ping Identity, provides digital identity and access management solutions for secure authentication, authorization, and identity governance across cloud and hybrid environments.
url: https://www.forgerock.com
type: Index
image: https://www.forgerock.com/themes/custom/forgerock/logo.svg
tags:
  - Access Management
  - Authentication
  - Authorization
  - Identity Governance
  - Identity Management
  - OAuth
  - OpenID Connect
created: '2024'
modified: '2026-04-28'
apis:
  - name: ForgeRock Identity Cloud REST API
    description: REST API for managing identities, authentication, and authorization in ForgeRock Identity Cloud, providing access management and identity management endpoints for Advanced Identity Cloud tenant environments.
    baseURL: https://{tenant}.forgeblocks.com
    humanURL: https://backstage.forgerock.com/docs/idcloud/latest
    tags:
      - Access Management
      - Authentication
      - Cloud
      - Identity
      - REST
    properties:
      - type: Documentation
        url: https://backstage.forgerock.com/docs/idcloud/latest/
      - type: OpenAPI
        url: openapi/forgerock-identity-cloud-openapi.yml
      - type: OpenAPI
        url: https://backstage.forgerock.com/docs/idcloud/latest/openapi/
      - type: API Reference
        url: https://apidocs.id.forgerock.io/
      - type: Getting Started
        url: https://backstage.forgerock.com/docs/idcloud/latest/home.html
      - type: Authentication
        url: https://backstage.forgerock.com/docs/idcloud/latest/developer-docs/authenticate-to-rest-api-overview.html
      - type: SDKs
        url: https://backstage.forgerock.com/docs/idcloud/latest/end-user/sdks.html
  - name: ForgeRock Access Management API
    description: API for authentication, authorization, session management, and policy evaluation. Supports OAuth 2.0 and OpenID Connect flows for secure token-based access.
    baseURL: https://{deployment}/am
    humanURL: https://backstage.forgerock.com/docs/am/7.3
    tags:
      - Access Management
      - Authentication
      - Authorization
      - OAuth
      - Sessions
    properties:
      - type: Documentation
        url: https://backstage.forgerock.com/docs/am/7.3/
      - type: OpenAPI
        url: openapi/forgerock-access-management-openapi.yml
      - type: API Reference
        url: https://backstage.forgerock.com/docs/am/7.3/apidocs/
      - type: Authentication
        url: https://backstage.forgerock.com/docs/am/7/authentication-guide/
      - type: Getting Started
        url: https://backstage.forgerock.com/docs/am/7.1/REST-guide/basic-rest-authentication.html
      - type: Change Log
        url: https://backstage.forgerock.com/docs/am/7/release-notes/
  - name: ForgeRock Identity Management API
    description: REST API for CRUD operations on managed objects and identity lifecycle management. Supports provisioning, synchronization, reconciliation, and workflow-driven identity operations.
    baseURL: https://{deployment}/openidm
    humanURL: https://backstage.forgerock.com/docs/idm/7.4
    tags:
      - Identity Management
      - Lifecycle Management
      - Provisioning
      - Synchronization
    properties:
      - type: Documentation
        url: https://backstage.forgerock.com/docs/idm/7.4/
      - type: OpenAPI
        url: openapi/forgerock-identity-management-openapi.yml
      - type: REST API Guide
        url: https://backstage.forgerock.com/docs/idm/7.4/rest-api-reference/
      - type: Getting Started
        url: https://backstage.forgerock.com/docs/idm/7.4/getting-started/
      - type: Change Log
        url: https://backstage.forgerock.com/docs/idm/7.4/release-notes/preface.html
  - name: ForgeRock Identity Gateway API
    description: API for reverse proxy functionality, policy enforcement, and request transformation. Integrates web applications, APIs, and microservices with the ForgeRock Identity Platform.
    baseURL: https://{deployment}/ig
    humanURL: https://backstage.forgerock.com/docs/ig/7.3
    tags:
      - API Security
      - Gateway
      - Policy Enforcement
      - Reverse Proxy
    properties:
      - type: Documentation
        url: https://backstage.forgerock.com/docs/ig/7.3/
      - type: OpenAPI
        url: openapi/forgerock-identity-gateway-openapi.yml
      - type: Reference
        url: https://backstage.forgerock.com/docs/ig/7.3/reference/
      - type: Getting Started
        url: https://backstage.forgerock.com/docs/ig/7/gateway-guide/
  - name: ForgeRock Directory Services API
    description: LDAP and REST API for directory operations and data management. Provides HDAP endpoints for accessing directory data as JSON resources.
    baseURL: https://{deployment}/ds
    humanURL: https://backstage.forgerock.com/docs/ds/7.4
    tags:
      - Data Storage
      - Directory
      - HDAP
      - LDAP
    properties:
      - type: Documentation
        url: https://backstage.forgerock.com/docs/ds/7.4/
      - type: OpenAPI
        url: openapi/forgerock-directory-services-openapi.yml
      - type: REST API
        url: https://backstage.forgerock.com/docs/ds/7.4/rest-guide/
      - type: Getting Started
        url: https://backstage.forgerock.com/docs/ds/7.4/getting-started/rest.html
      - type: Reference
        url: https://backstage.forgerock.com/docs/ds/7.4/rest-guide/rest-operations.html
  - name: ForgeRock Identity Governance API
    description: REST API for identity governance operations including access reviews, certifications, role management, and policy enforcement. Provides endpoints for managing entitlements and compliance workflows.
    baseURL: https://{deployment}/iga
    humanURL: https://backstage.forgerock.com/docs/identity-governance/7.1/api-guide/preface.html
    tags:
      - Access Reviews
      - Compliance
      - Entitlements
      - Identity Governance
    properties:
      - type: Documentation
        url: https://backstage.forgerock.com/docs/identity-governance/7.1/api-guide/preface.html
      - type: OpenAPI
        url: openapi/forgerock-identity-governance-openapi.yml
      - type: API Reference
        url: https://backstage.forgerock.com/docs/idcloud/latest/identity-governance/rest-api/endpoints/rest-iga.html
  - name: ForgeRock Autonomous Identity API
    description: REST API for the Autonomous Identity analytics platform that uses AI-driven analysis to determine confidence scores, predictions, and recommendations for entitlement assignments.
    baseURL: https://{deployment}/autoid
    humanURL: https://backstage.forgerock.com/docs/autonomous-identity/2022.11.0/api-guide/preface.html
    tags:
      - Analytics
      - Artificial Intelligence
      - Autonomous Identity
      - Entitlements
    properties:
      - type: Documentation
        url: https://backstage.forgerock.com/docs/autonomous-identity/2022.11.0/api-guide/preface.html
      - type: OpenAPI
        url: openapi/forgerock-autonomous-identity-openapi.yml
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
common:
  - type: Portal
    url: https://backstage.forgerock.com
  - type: Documentation
    url: https://backstage.forgerock.com/docs
  - type: Getting Started
    url: https://community.forgerock.com/c/getting-started-guides/36
  - type: Authentication
    url: https://backstage.forgerock.com/docs/idcloud/latest/developer-docs/authenticate-to-rest-api-overview.html
  - type: Blog
    url: https://www.forgerock.com/blog
  - type: Status
    url: https://status.id.forgerock.io
  - type: Support
    url: https://backstage.forgerock.com/support
  - type: Terms of Service
    url: https://www.forgerock.com/terms
  - type: Privacy Policy
    url: https://www.forgerock.com/privacy-policy
  - type: GitHub Organization
    url: https://github.com/ForgeRock
  - type: Community
    url: https://community.forgerock.com/
  - type: Website
    url: https://www.forgerock.com
  - type: Login
    url: https://backstage.forgerock.com/account
  - type: Sign Up
    url: https://backstage.forgerock.com/account/register
  - type: SDKs
    url: https://docs.pingidentity.com/sdks/latest/index.html
  - type: JSON-LD Context
    url: json-ld/forgerock-context.jsonld
  - type: JSON Schema
    url: json-schema/forgerock-managed-user-schema.json
  - type: JSON Schema
    url: json-schema/forgerock-session-schema.json
  - type: JSON Schema
    url: json-schema/forgerock-policy-schema.json
  - type: JSON Schema
    url: json-schema/forgerock-oauth2-token-schema.json
  - type: JSON Schema
    url: json-schema/forgerock-managed-role-schema.json
  - type: JSON Schema
    url: json-schema/forgerock-entitlement-schema.json
  - type: JSON Schema
    url: json-schema/forgerock-directory-entry-schema.json
---
