---
aid: microsoft-projects
url: https://raw.githubusercontent.com/api-evangelist/microsoft-projects/refs/heads/main/apis.yml
apis:
- name: Microsoft Project for the Web API
  description: REST API for managing projects, tasks, resources, and assignments in Microsoft Project for the web.
  image: https://www.microsoft.com/en-us/microsoft-365/project/project-management-software
  humanUrl: https://docs.microsoft.com/en-us/project/
  baseUrl: https://graph.microsoft.com/v1.0/
  tags:
  - Assignments
  - Collaboration
  - Projects
  - Resources
  - Tasks
  properties:
  - type: X-documentation
    url: https://docs.microsoft.com/en-us/graph/api/resources/project-rome-overview
  - type: X-openapi
    url: https://developer.microsoft.com/en-us/graph/docs/api-reference/v1.0/resources/project
  - type: X-authentication
    url: https://docs.microsoft.com/en-us/graph/auth/
  - type: X-rate-limits
    url: https://docs.microsoft.com/en-us/graph/throttling
  contact:
  - FN: Microsoft Graph Support
    email: graphsdksupport@microsoft.com
    url: https://developer.microsoft.com/en-us/graph/support
- name: Microsoft Project Online API
  description: REST API for Microsoft Project Online, providing access to project data, timesheets, and enterprise project management features.
  image: https://www.microsoft.com/en-us/microsoft-365/project/project-management-software
  humanUrl: https://docs.microsoft.com/en-us/project/project-online
  baseUrl: https://{tenant}.sharepoint.com/sites/pwa/_api/ProjectServer/
  tags:
  - Enterprise
  - Portfolio
  - Project-Online
  - Reporting
  - Timesheets
  properties:
  - type: X-documentation
    url: https://docs.microsoft.com/en-us/previous-versions/office/project-javascript-api/jj712820(v=office.15)
  - type: X-openapi
    url: https://docs.microsoft.com/en-us/openspecs/sharepoint_protocols/ms-pjsoi/
  - type: X-authentication
    url: https://docs.microsoft.com/en-us/sharepoint/dev/sp-add-ins/authorization-and-authentication-of-sharepoint-add-ins
  - type: X-sdk
    url: https://docs.microsoft.com/en-us/project/api/project-csom-overview
  contact:
  - FN: Project Online Support
    email: support@microsoft.com
    url: https://support.microsoft.com/project
- name: Microsoft Project Desktop CSOM API
  description: Client-side object model for programmatically interacting with Microsoft Project desktop applications.
  image: https://www.microsoft.com/en-us/microsoft-365/project/project-management-software
  humanUrl: https://docs.microsoft.com/en-us/office/client-developer/project/
  baseUrl: N/A
  tags:
  - Add-Ins
  - Automation
  - Csom
  - Desktop
  - Vba
  properties:
  - type: X-documentation
    url: https://docs.microsoft.com/en-us/office/client-developer/project/project-programming-references
  - type: X-sdk
    url: https://docs.microsoft.com/en-us/visualstudio/vsto/office-solutions-development-overview-vsto
  - type: X-samples
    url: https://github.com/OfficeDev/Project-Samples
  contact:
  - FN: Office Developer Support
    email: officedevfeedback@microsoft.com
    url: https://developer.microsoft.com/en-us/office
name: Microsoft Project APIs
tags:
- Collaboration
- Enterprise
- Microsoft
- Portfolio-Management
- Project-Management
- Resources
- Tasks
type: Contract
image: https://www.microsoft.com/en-us/microsoft-365/project/project-management-software
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A collection of APIs for Microsoft Project, enabling project management, task tracking, resource allocation, and collaboration capabilities.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

