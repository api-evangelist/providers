---
aid: microsoft-intune
url: https://raw.githubusercontent.com/api-evangelist/microsoft-intune/refs/heads/main/apis.yml
apis:
- name: Microsoft Intune API
  description: The Microsoft Graph API for Intune enables programmatic access to Intune information and actions for your tenant. The API performs the same Intune operations as those available through the Azure Portal.
  image: https://docs.microsoft.com/en-us/mem/intune/fundamentals/media/what-is-intune/intune-logo.png
  humanURL: https://docs.microsoft.com/en-us/graph/api/resources/intune-graph-overview
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Applications
  - Compliance
  - Devices
  - Groups
  - Policies
  - Users
  properties:
  - type: X-documentation
    url: https://docs.microsoft.com/en-us/graph/api/resources/intune-graph-overview
  - type: X-openapi
    url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
  - type: X-openapi-intune
    url: openapi/microsoft-intune-openapi.yml
  - type: X-json-schema-managed-device
    url: json-schema/microsoft-intune-managed-device-schema.json
  - type: X-json-ld-context
    url: json-ld/microsoft-intune-context.jsonld
  - type: X-authentication
    url: https://docs.microsoft.com/en-us/graph/auth/
  - type: X-postman-collection
    url: https://www.postman.com/microsoftgraph/workspace/microsoft-graph/overview
  - type: X-rate-limits
    url: https://docs.microsoft.com/en-us/graph/throttling
  - type: X-change-log
    url: https://docs.microsoft.com/en-us/graph/changelog
  - type: X-sdks
    url: https://docs.microsoft.com/en-us/graph/sdks/sdks-overview
  - type: X-pricing
    url: https://www.microsoft.com/en-us/security/business/microsoft-intune-pricing
  - type: X-getting-started
    url: https://learn.microsoft.com/en-us/graph/intune-concept-overview
  - type: X-permissions
    url: https://learn.microsoft.com/en-us/graph/permissions-reference
  contact:
  - type: X-support
    url: https://docs.microsoft.com/en-us/mem/get-support
  - type: X-twitter
    url: https://twitter.com/MSIntune
  - type: X-status
    url: https://status.azure.com/
- name: Intune Data Warehouse API
  description: The Intune Data Warehouse API provides access to your Intune data in a machine-readable format for use in your favorite analytics tool. You can use the API to generate reports that provide insight into your mobile environment.
  humanURL: https://docs.microsoft.com/en-us/mem/intune/developer/reports-nav-create-intune-reports
  baseURL: https://api.manage.microsoft.com/
  tags:
  - Analytics
  - Data Warehouse
  - Odata
  - Reporting
  properties:
  - type: X-documentation
    url: https://docs.microsoft.com/en-us/mem/intune/developer/reports-nav-intune-data-warehouse
  - type: X-authentication
    url: https://docs.microsoft.com/en-us/mem/intune/developer/reports-proc-data-rest
  - type: X-data-model
    url: https://docs.microsoft.com/en-us/mem/intune/developer/reports-ref-data-model
- name: Intune Device Management API
  description: The Microsoft Graph Device Management API enables programmatic management of devices enrolled in Intune, including listing managed devices, performing remote actions such as wipe and retire, and retrieving device compliance state and configuration status.
  humanURL: https://learn.microsoft.com/en-us/graph/api/resources/intune-devices-manageddevice?view=graph-rest-1.0
  baseURL: https://graph.microsoft.com/v1.0/deviceManagement
  tags:
  - Device Compliance
  - Devices
  - Managed Devices
  - Remote Actions
  properties:
  - type: X-documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/intune-devices-manageddevice?view=graph-rest-1.0
  - type: X-openapi
    url: openapi/microsoft-intune-openapi.yml
  - type: X-json-schema
    url: json-schema/microsoft-intune-managed-device-schema.json
  - type: X-json-ld-context
    url: json-ld/microsoft-intune-context.jsonld
  - type: X-list-endpoint
    url: https://learn.microsoft.com/en-us/graph/api/intune-devices-manageddevice-list?view=graph-rest-1.0
  - type: X-getting-started
    url: https://learn.microsoft.com/en-us/graph/intune-concept-overview
- name: Intune Device Configuration API
  description: The Microsoft Graph Device Configuration API allows you to define and deploy device configuration policies across enrolled devices, including operating system platform and versioning, domain membership, and configuration setting management through configuration service providers (CSPs).
  humanURL: https://learn.microsoft.com/en-us/graph/api/resources/intune-deviceconfig-deviceconfiguration?view=graph-rest-1.0
  baseURL: https://graph.microsoft.com/v1.0/deviceManagement/deviceConfigurations
  tags:
  - CSP
  - Device Configuration
  - Policies
  - Settings
  properties:
  - type: X-documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/intune-deviceconfig-deviceconfiguration?view=graph-rest-1.0
  - type: X-openapi
    url: openapi/microsoft-intune-openapi.yml
  - type: X-json-ld-context
    url: json-ld/microsoft-intune-context.jsonld
  - type: X-graph-apis
    url: https://learn.microsoft.com/en-us/intune/intune-service/developer/graph-apis-used-by-intune-device-configuration-windows
- name: Intune Device Compliance API
  description: The Microsoft Graph Device Compliance API enables you to define and enforce device compliance policies, such as password complexity, encryption, and threat protection levels, and retrieve compliance state for managed devices.
  humanURL: https://learn.microsoft.com/en-us/graph/api/resources/intune-deviceconfig-devicecompliancepolicy?view=graph-rest-1.0
  baseURL: https://graph.microsoft.com/v1.0/deviceManagement/deviceCompliancePolicies
  tags:
  - Compliance
  - Device Compliance
  - Policies
  - Security
  properties:
  - type: X-documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/intune-deviceconfig-devicecompliancepolicy?view=graph-rest-1.0
  - type: X-openapi
    url: openapi/microsoft-intune-openapi.yml
  - type: X-json-ld-context
    url: json-ld/microsoft-intune-context.jsonld
  - type: X-overview
    url: https://learn.microsoft.com/en-us/intune/intune-service/protect/device-compliance-get-started
- name: Intune Device Enrollment API
  description: The Microsoft Graph Device Enrollment API enables you to enroll organization-owned or corporate-owned devices for management with Intune, supporting various enrollment methods depending on device type and organizational needs.
  humanURL: https://learn.microsoft.com/en-us/graph/api/resources/intune-enrollment-conceptual?view=graph-rest-1.0
  baseURL: https://graph.microsoft.com/v1.0/deviceManagement
  tags:
  - Corporate Devices
  - Enrollment
  - Onboarding
  properties:
  - type: X-documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/intune-enrollment-conceptual?view=graph-rest-1.0
  - type: X-onboarding
    url: https://learn.microsoft.com/en-us/graph/api/resources/intune-onboarding-conceptual?view=graph-rest-1.0
- name: Intune Mobile App Management API
  description: The Microsoft Graph Mobile App Management (MAM) API enables you to manage app protection policies, deploy apps to devices, configure app settings, and manage app usage policies to protect organizational data within mobile applications.
  humanURL: https://learn.microsoft.com/en-us/graph/api/resources/intune-mam-conceptual?view=graph-rest-beta
  baseURL: https://graph.microsoft.com/beta/deviceAppManagement
  tags:
  - App Protection
  - Applications
  - MAM
  - Mobile App Management
  properties:
  - type: X-documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/intune-mam-conceptual?view=graph-rest-beta
  - type: X-app-protection-overview
    url: https://learn.microsoft.com/en-us/intune/intune-service/apps/app-protection-policy
  - type: X-app-configuration
    url: https://learn.microsoft.com/en-us/intune/intune-service/apps/app-configuration-policies-overview
- name: Intune Reports Export API
  description: The Intune Reports Export API enables you to export Intune reporting data using Microsoft Graph API export jobs. You can create export jobs to generate reports that provide insight into device compliance, app usage, and other aspects of your managed environment.
  humanURL: https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/reports-export-graph-apis
  baseURL: https://graph.microsoft.com/v1.0/deviceManagement/reports
  tags:
  - Analytics
  - Compliance Reports
  - Export
  - Reports
  properties:
  - type: X-documentation
    url: https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/reports-export-graph-apis
  - type: X-available-reports
    url: https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/reports-export-graph-available-reports
  - type: X-create-export-job
    url: https://learn.microsoft.com/en-us/graph/api/intune-reporting-devicemanagementexportjob-create?view=graph-rest-1.0
name: Microsoft Intune
tags:
- App Protection
- Azure
- Compliance
- Device Configuration
- Endpoint Management
- Enrollment
- MAM
- MDM
- Microsoft Graph
- Mobile Application Management
- Mobile Device Management
- Security
type: Contract
image: https://docs.microsoft.com/en-us/mem/intune/fundamentals/media/what-is-intune/intune-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft Intune is a cloud-based service that focuses on mobile device management (MDM) and mobile application management (MAM). It helps organizations control how their devices are used, including mobile phones, tablets, and laptops, and enables management of apps on those devices.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

