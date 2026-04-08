---
aid: microsoft-office-integration
url: https://raw.githubusercontent.com/api-evangelist/microsoft-office-integration/refs/heads/main/apis.yml
apis:
- aid: microsoft-office-integration:management-activity-api
  name: Microsoft Office 365 Management Activity API
  tags:
  - Auditing
  - Compliance
  - Office 365
  - Security
  humanURL: https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-reference
  properties:
  - url: https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-reference
    type: Documentation
  - url: openapi/microsoft-office-management-activity-api-openapi.yml
    type: OpenAPI
  - url: json-schema/subscription.json
    type: JSONSchema
  - url: json-schema/activity-record.json
    type: JSONSchema
  - url: json-schema/content-blob.json
    type: JSONSchema
  - url: json-ld/microsoft-office-integration-context.jsonld
    type: JSONLD
  description: The Office 365 Management Activity API provides information about various user, admin, system, and policy actions and events from Office 365 and Microsoft Entra activity logs. It enables customers and partners to create or enhance operations, security, and compliance-monitoring solutions. The API supports subscription management, content retrieval, webhook notifications, and DLP sensitive type lookups across content types including Azure AD, Exchange, SharePoint, and General audit logs.
- aid: microsoft-office-integration:service-communications-api
  name: Microsoft Office 365 Service Communications API
  tags:
  - Incidents
  - Monitoring
  - Office 365
  - Service Health
  humanURL: https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-service-communications-api-reference
  properties:
  - url: https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-service-communications-api-reference
    type: Documentation
  - url: openapi/microsoft-office-service-communications-api-openapi.yml
    type: OpenAPI
  - url: json-schema/service.json
    type: JSONSchema
  - url: json-schema/workload-status.json
    type: JSONSchema
  - url: json-schema/message.json
    type: JSONSchema
  - url: json-ld/microsoft-office-integration-context.jsonld
    type: JSONLD
  description: The Office 365 Service Communications API provides tenant administrators and partners with real-time service health information and Message Center communications. It enables access to the list of subscribed services, current and historical service status, incident details, and planned maintenance notifications for Office 365, Yammer, Dynamics CRM, and Microsoft Intune cloud services.
name: Microsoft Office Integration
tags:
- Microsoft 365
- Microsoft Office Integration
- Office 365
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for Microsoft Office Integration, connecting Microsoft Office components and systems for seamless data exchange and end-to-end workflows across multiple technologies and platforms. The Office 365 Management APIs provide a single extensibility platform for management tasks including service communications, security, compliance, reporting, and auditing, using common industry-standard approaches including OAuth v2, OData v4, and JSON.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

