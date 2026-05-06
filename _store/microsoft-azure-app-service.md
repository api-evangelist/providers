---
aid: microsoft-azure-app-service
name: Microsoft Azure App Service
description: Microsoft Azure App Service is a fully managed platform-as-a-service (PaaS) for building, deploying, and scaling web apps, REST APIs, and mobile backends. It supports multiple languages and frameworks, offers built-in auto-scaling and load balancing, and includes integrated authentication, continuous deployment, custom domain, and SSL certificate management.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - App Service
  - Hosting
  - Microsoft Azure
  - PaaS
  - Web Apps
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-app-service/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-azure-app-service:azure-app-service-api
    name: Azure App Service API
    description: The Azure App Service REST API enables programmatic management of web apps, app service plans, deployment slots, custom domains, SSL certificates, and application settings. It supports continuous deployment, auto-scaling, authentication configuration, and hybrid connections through Azure Resource Manager endpoints.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/rest/api/appservice/
    baseURL: https://management.azure.com/
    tags:
      - App Service
      - Hosting
      - PaaS
      - Web Apps
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/appservice/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/rest/api/appservice/operation-groups
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/app-service/overview-authentication-authorization
      - type: SDK
        url: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/appservice
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/app-service/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/
  - type: TermsOfService
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
  - type: StatusPage
    url: https://status.azure.com/
  - type: GitHubOrganization
    url: https://github.com/Azure
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
