---
aid: software-ag
name: Software AG
description: Software AG provides enterprise integration and API management through webMethods, a platform for connecting applications, processes, and people across hybrid cloud and on-premises environments. The webMethods platform includes API Gateway, Developer Portal, Integration Server, and cloud-native integration services. Software AG was acquired by IBM in 2024.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Management
  - Enterprise Integration
  - iPaaS
  - webMethods
  - Integration Platform
  - API Gateway
url: https://raw.githubusercontent.com/api-evangelist/software-ag/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: software-ag:webmethods-api-gateway
    name: webMethods API Gateway Service Management API
    description: The webMethods API Gateway Service Management API provides REST endpoints for managing APIs within the API Gateway platform. It supports creating, reading, updating, and deleting REST, SOAP, WebSocket, and OData APIs, as well as managing policies, applications, and gateway endpoints.
    humanURL: https://documentation.softwareag.com/webmethods/compendiums/v10-5/C_API_Management/api-mgmt-comp/co-oview_what_is_api_portal.html
    baseURL: http://localhost:5555/rest/apigateway
    tags:
      - API Management
      - API Gateway
      - Enterprise Integration
      - webMethods
    properties:
      - type: Documentation
        url: https://documentation.softwareag.com/webmethods/compendiums/v10-5/C_API_Management/api-mgmt-comp/gtw_manage_apis.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/software-ag/refs/heads/main/openapi/webmethods-api-gateway-openapi.yml
      - type: GitHubRepository
        url: https://github.com/SoftwareAG/webmethods-api-gateway
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/software-ag/refs/heads/main/json-schema/webmethods-api-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/software-ag/refs/heads/main/json-structure/webmethods-api-structure.json
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/software-ag/refs/heads/main/rules/webmethods-api-gateway-rules.yml
      - type: NaftikoCapabilities
        url: https://raw.githubusercontent.com/api-evangelist/software-ag/refs/heads/main/capabilities/api-management.yaml
  - aid: software-ag:webmethods-developer-portal
    name: webMethods Developer Portal
    description: The webMethods Developer Portal provides a marketplace for publishing and discovering REST, SOAP, and OData APIs for third-party developers and partners. It enables developer onboarding, API subscription management, and API consumption analytics.
    humanURL: https://www.softwareag.com/en_corporate/resources/api/ds/webmethods-developer-portal.html
    baseURL: https://www.softwareag.com/
    tags:
      - Developer Portal
      - API Management
      - API Marketplace
      - webMethods
    properties:
      - type: Documentation
        url: https://documentation.softwareag.com/webmethods/compendiums/v10-5/C_API_Management/api-mgmt-comp/co-oview_what_is_api_portal.html
      - type: GitHubRepository
        url: https://github.com/SoftwareAG/webmethods-developer-portal
  - aid: software-ag:webmethods-integration-server
    name: webMethods Integration Server
    description: The webMethods Integration Server is a comprehensive integration platform that enables connectivity between enterprise applications, databases, legacy systems, and cloud services. It provides flow services, adapters, and REST API exposure for business process integration.
    humanURL: https://documentation.softwareag.com/
    baseURL: https://www.softwareag.com/
    tags:
      - Integration
      - Enterprise
      - Middleware
      - webMethods
      - iPaaS
    properties:
      - type: Documentation
        url: https://documentation.softwareag.com/
common:
  - type: Portal
    url: https://developer.softwareag.com/
  - type: Website
    url: https://www.softwareag.com/
  - type: GitHubOrganization
    url: https://github.com/SoftwareAG
  - type: Documentation
    url: https://documentation.softwareag.com/
  - type: Blog
    url: https://techcommunity.softwareag.com/
  - type: LinkedIn
    url: https://www.linkedin.com/company/software-ag
  - type: Twitter
    url: https://twitter.com/SoftwareAG
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/software-ag/refs/heads/main/json-ld/software-ag-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/software-ag/refs/heads/main/vocabulary/software-ag-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
