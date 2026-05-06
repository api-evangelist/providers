---
name: Microsoft Endpoint Configuration Management
description: Microsoft Endpoint Configuration Management (formerly System Center Configuration Manager) provides comprehensive management of devices and applications across an enterprise. It enables IT administrators to manage PCs, servers, and mobile devices, deploy software, manage compliance, and protect data.
image: https://docs.microsoft.com/en-us/mem/configmgr/core/media/configmgr-logo.png
url: https://learn.microsoft.com/en-us/intune/configmgr/
created: '2024'
modified: '2026-04-28'
specificationVersion: '0.18'
tags:
  - Compliance
  - Configuration Management
  - Device Management
  - Endpoint Management
  - Mobile Device Management
  - Patch Management
  - Software Deployment
apis:
  - name: Configuration Manager REST API
    description: REST API for managing Configuration Manager resources including collections, deployments, applications, and device queries. The administration service is based on the OData v4 protocol and supports both WMI and versioned OData routes.
    image: https://docs.microsoft.com/en-us/mem/configmgr/core/media/configmgr-logo.png
    humanURL: https://learn.microsoft.com/en-us/intune/configmgr/develop/adminservice/overview
    baseURL: https://{siteserver}/AdminService
    tags:
      - Admin Service
      - Configuration Manager
      - REST API
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/intune/configmgr/develop/adminservice/overview
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/intune/configmgr/develop/adminservice/set-up
      - type: OpenAPI
        url: openapi/microsoft-endpoint-configuration-management-configmgr-rest-api-openapi.yml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/intune/configmgr/develop/adminservice/set-up#enable-secure-https-communication
      - type: Reference
        url: https://learn.microsoft.com/en-us/intune/configmgr/develop/adminservice/usage
      - type: Change Log
        url: https://learn.microsoft.com/en-us/intune/configmgr/develop/adminservice/release-notes
  - name: Configuration Manager PowerShell Cmdlets
    description: PowerShell module for Configuration Manager automation and scripting, providing over 1100 cmdlets for all major management tasks including device collections, software deployment, and compliance settings.
    humanURL: https://learn.microsoft.com/en-us/powershell/sccm/overview?view=sccm-ps
    tags:
      - Automation
      - Configuration Manager
      - PowerShell
      - Scripting
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/powershell/sccm/overview?view=sccm-ps
      - type: Reference
        url: https://learn.microsoft.com/en-us/powershell/module/configurationmanager/?view=sccm-ps
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/intune/configmgr/core/servers/manage/admin-console
      - type: Change Log
        url: https://learn.microsoft.com/en-us/intune/configmgr/core/plan-design/changes/whats-new-incremental-versions
  - name: Configuration Manager SDK
    description: Software Development Kit for extending and integrating with Configuration Manager, including WMI providers, class schemas, and programming interfaces for custom solutions.
    humanURL: https://learn.microsoft.com/en-us/intune/configmgr/develop/
    tags:
      - Configuration Manager
      - Development
      - SDK
      - WMI
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/intune/configmgr/develop/
      - type: Reference
        url: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/configuration-manager-reference
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/intune/configmgr/develop/core/understand/getting-started-with-configuration-manager-programming
      - type: Change Log
        url: https://learn.microsoft.com/en-us/intune/configmgr/core/plan-design/changes/whats-new-incremental-versions
  - name: Microsoft Intune Graph API
    description: Microsoft Graph API endpoints for Intune device management, enabling programmatic access to manage devices, apps, compliance policies, and configuration profiles. Supports both v1.0 and beta endpoints.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/intune-graph-overview?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Compliance
      - Device Management
      - Intune
      - Microsoft Graph
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/intune-graph-overview?view=graph-rest-1.0
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/graph/intune-concept-overview
      - type: OpenAPI
        url: openapi/microsoft-endpoint-configuration-management-intune-graph-api-openapi.yml
      - type: JSONSchema
        url: json-schema/microsoft-endpoint-configuration-management-device-schema.json
      - type: JSONSchema
        url: json-schema/microsoft-endpoint-configuration-management-compliance-policy-schema.json
      - type: JSONSchema
        url: json-schema/microsoft-endpoint-configuration-management-application-schema.json
      - type: JSONSchema
        url: json-schema/microsoft-endpoint-configuration-management-configuration-profile-schema.json
      - type: JSONLD
        url: json-ld/microsoft-endpoint-configuration-management-context.jsonld
      - type: Reference
        url: https://learn.microsoft.com/en-us/graph/intune-concept-overview
      - type: Authentication
        url: https://learn.microsoft.com/en-us/intune/intune-service/developer/intune-graph-apis
      - type: Change Log
        url: https://developer.microsoft.com/en-us/graph/changelog
      - type: SDKs
        url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
      - type: PostmanCollection
        url: https://www.postman.com/microsoftgraph/workspace/microsoft-graph/overview
  - name: Intune Data Warehouse API
    description: OData-based REST API that provides access to Intune reporting data in a machine-readable format. Enables building custom reports and analytics for enterprise mobile environment insights.
    humanURL: https://learn.microsoft.com/en-us/intune/intune-service/developer/reports-nav-intune-data-warehouse
    baseURL: https://fef.{location}.manage.microsoft.com/ReportingService/DataWarehouseFEService
    tags:
      - Data Warehouse
      - Intune
      - OData
      - Reporting
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/intune/intune-service/developer/reports-nav-intune-data-warehouse
      - type: OpenAPI
        url: openapi/microsoft-endpoint-configuration-management-intune-data-warehouse-api-openapi.yml
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/intune/intune-service/developer/reports-api-url
      - type: Authentication
        url: https://learn.microsoft.com/en-us/intune/intune-service/developer/intune-graph-apis
      - type: Reference
        url: https://learn.microsoft.com/en-us/intune/intune-service/developer/reports-proc-data-rest
      - type: Change Log
        url: https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/whats-new
  - name: Intune App SDK
    description: SDKs for iOS and Android that enable mobile apps to support Intune app protection policies. Allows developers to integrate mobile application management features into line-of-business and partner apps.
    humanURL: https://learn.microsoft.com/en-us/intune/intune-service/developer/app-sdk-get-started
    tags:
      - App Protection
      - Intune
      - Mobile Apps
      - SDK
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/intune/intune-service/developer/app-sdk
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/intune/intune-service/developer/app-sdk-get-started
      - type: Reference
        url: https://learn.microsoft.com/en-us/intune/intune-service/developer/app-sdk-ios-phase1
      - type: GitHub Organization
        url: https://github.com/msintuneappsdk
  - name: Intune Reporting Export API
    description: Microsoft Graph API endpoints for exporting Intune reports programmatically. Supports exporting device, compliance, and app management reports in CSV or JSON format using asynchronous export jobs.
    humanURL: https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/reports-export-graph-apis
    baseURL: https://graph.microsoft.com/v1.0/deviceManagement/reports
    tags:
      - Export
      - Intune
      - Microsoft Graph
      - Reporting
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/reports-export-graph-apis
      - type: OpenAPI
        url: openapi/microsoft-endpoint-configuration-management-intune-reporting-export-api-openapi.yml
      - type: Reference
        url: https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/reports-export-graph-available-reports
      - type: Authentication
        url: https://learn.microsoft.com/en-us/intune/intune-service/developer/intune-graph-apis
  - name: Intune App Wrapping Tool
    description: Command-line tools for iOS and Android that enable existing line-of-business apps to be managed by Intune app protection policies without requiring source code changes.
    humanURL: https://learn.microsoft.com/en-us/intune/intune-service/developer/apps-prepare-mobile-application-management
    tags:
      - Android
      - App Protection
      - Intune
      - iOS
      - Mobile Apps
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/intune/intune-service/developer/apps-prepare-mobile-application-management
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/intune/intune-service/developer/app-wrapper-prepare-ios
      - type: Reference
        url: https://learn.microsoft.com/en-us/intune/intune-service/developer/app-wrapper-prepare-android
      - type: GitHub Organization
        url: https://github.com/microsoftconnect
  - name: Intune PowerShell SDK
    description: PowerShell module providing native cmdlet support for invoking the Microsoft Intune Graph API. Enables IT administrators to automate device management, app deployment, and compliance policy operations through scripting.
    humanURL: https://github.com/microsoft/Intune-PowerShell-SDK
    tags:
      - Automation
      - Intune
      - PowerShell
      - SDK
    properties:
      - type: Documentation
        url: https://github.com/microsoft/Intune-PowerShell-SDK
      - type: Getting Started
        url: https://github.com/microsoft/mggraph-intune-samples
      - type: SDKs
        url: https://learn.microsoft.com/en-us/graph/sdks/sdk-installation
common:
  - type: Portal
    url: https://endpoint.microsoft.com/
  - type: Console
    url: https://intune.microsoft.com/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/intune/intune-service/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/intune/configmgr/core/understand/introduction
  - type: Authentication
    url: https://learn.microsoft.com/en-us/intune/intune-service/developer/intune-graph-apis
  - type: Blog
    url: https://techcommunity.microsoft.com/t5/microsoft-endpoint-manager-blog/bg-p/MicrosoftEndpointManagerBlog
  - type: Support
    url: https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/contact-assisted-support
  - type: Status
    url: https://status.azure.com/
  - type: Change Log
    url: https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/whats-new
  - type: Pricing
    url: https://www.microsoft.com/en-us/security/business/microsoft-intune-pricing
  - type: Sign Up
    url: https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/free-trial-sign-up
  - type: Login
    url: https://intune.microsoft.com/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/
  - type: Terms of Service
    url: https://www.microsoft.com/licensing/terms/
  - type: GitHub Organization
    url: https://github.com/microsoftgraph
  - type: Community
    url: https://techcommunity.microsoft.com/category/microsoftintune/blog/microsoftintuneblog
  - type: Website
    url: https://learn.microsoft.com/en-us/intune/configmgr/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
