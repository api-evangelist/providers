---
aid: autocad
url: https://raw.githubusercontent.com/api-evangelist/autocad/refs/heads/main/apis.yml
apis:
- name: AutoCAD API
  description: Core API for AutoCAD automation, drawing manipulation, and entity management.
  image: https://www.autodesk.com/products/autocad/overview
  humanURL: https://www.autodesk.com/developer-network/platform-technologies/autocad
  baseURL: https://developer.api.autodesk.com
  tags:
  - Automation
  - CAD
  - Drawing
  - Entities
  properties:
  - type: Documentation
    url: https://help.autodesk.com/view/OARX/2024/ENU/
  - type: OpenAPI
    url: https://developer.api.autodesk.com/autocad/openapi.json
  - type: Authentication
    url: https://forge.autodesk.com/en/docs/oauth/v2/reference/http/
  - type: Getting Started
    url: https://tutorials.autodesk.io/
  - type: API Overview
    url: https://aps.autodesk.com/developer/overview/autocad
  contact:
  - FN: Autodesk Developer Support
    email: forge.help@autodesk.com
    url: https://forge.autodesk.com/en/support/get-help/
- name: AutoCAD I/O API
  description: Cloud-based API for processing AutoCAD drawings without AutoCAD installation.
  image: https://www.autodesk.com/products/autocad/overview
  humanURL: https://forge.autodesk.com/en/docs/design-automation/v3/developers_guide/overview/
  baseURL: https://developer.api.autodesk.com/da/us-east/v3
  tags:
  - Automation
  - Batch Processing
  - Cloud
  - Design Automation
  properties:
  - type: Documentation
    url: https://forge.autodesk.com/en/docs/design-automation/v3/
  - type: API Reference
    url: https://forge.autodesk.com/en/docs/design-automation/v3/reference/http/
  - type: Tutorials
    url: https://forge.autodesk.com/en/docs/design-automation/v3/tutorials/
  - type: Change Log
    url: https://aps.autodesk.com/en/docs/design-automation/v3/change_history/acad_release_notes
  - type: API Overview
    url: https://aps.autodesk.com/developer/overview/automation-api
  contact:
  - FN: Autodesk Forge Support
    email: forge.help@autodesk.com
    url: https://forge.autodesk.com/en/support/
- name: AutoCAD Data Management API
  description: API for managing AutoCAD files, versions, and collaboration workflows.
  image: https://www.autodesk.com/products/autocad/overview
  humanURL: https://forge.autodesk.com/en/docs/data/v2/developers_guide/overview/
  baseURL: https://developer.api.autodesk.com/data/v1
  tags:
  - Collaboration
  - File Management
  - Storage
  - Version Control
  properties:
  - type: Documentation
    url: https://forge.autodesk.com/en/docs/data/v2/
  - type: API Reference
    url: https://forge.autodesk.com/en/docs/data/v2/reference/http/
  - type: Getting Started
    url: https://forge.autodesk.com/en/docs/data/v2/tutorials/
  - type: API Overview
    url: https://aps.autodesk.com/developer/overview/data-management-api
  contact:
  - FN: Autodesk Developer Support
    email: forge.help@autodesk.com
    url: https://aps.autodesk.com/get-help
- name: AutoCAD Design Automation API
  description: Cloud-based API that enables running AutoCAD scripts, AutoLISP routines, and custom add-ins in the cloud to automate drawing creation, modification, and batch processing workflows at scale.
  image: https://www.autodesk.com/products/autocad/overview
  humanURL: https://aps.autodesk.com/apis-and-services/autocad-automation-api
  baseURL: https://developer.api.autodesk.com/da/us-east/v3
  tags:
  - AutoLISP
  - Batch Processing
  - Cloud
  - Design Automation
  - Scripting
  properties:
  - type: Documentation
    url: https://aps.autodesk.com/en/docs/design-automation/v3
  - type: API Reference
    url: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/
  - type: Getting Started
    url: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/
  - type: API Overview
    url: https://aps.autodesk.com/developer/overview/automation-api
  - type: Change Log
    url: https://aps.autodesk.com/en/docs/design-automation/v3/change_history/acad_release_notes
  contact:
  - FN: Autodesk Developer Support
    email: forge.help@autodesk.com
    url: https://aps.autodesk.com/get-help
- name: AutoCAD Model Derivative API
  description: API for translating AutoCAD design files into formats like SVF and SVF2 for rendering in the Viewer SDK, extracting metadata, object hierarchy, properties, and generating thumbnails.
  image: https://www.autodesk.com/products/autocad/overview
  humanURL: https://aps.autodesk.com/developer/overview/model-derivative-api
  baseURL: https://developer.api.autodesk.com/modelderivative/v2
  tags:
  - File Conversion
  - Metadata
  - Model Derivative
  - Thumbnails
  - Translation
  properties:
  - type: Documentation
    url: https://aps.autodesk.com/en/docs/model-derivative/v2
  - type: API Overview
    url: https://aps.autodesk.com/developer/overview/model-derivative-api
  - type: Change Log
    url: https://aps.autodesk.com/en/docs/model-derivative/v2/change_history/changelog
  contact:
  - FN: Autodesk Developer Support
    email: forge.help@autodesk.com
    url: https://aps.autodesk.com/get-help
- name: AutoCAD Viewer SDK
  description: JavaScript library for creating web applications that view and interact with 2D and 3D AutoCAD design models in any browser, supporting various file formats with extensive customization options.
  image: https://www.autodesk.com/products/autocad/overview
  humanURL: https://aps.autodesk.com/developer/overview/viewer-sdk
  baseURL: https://developer.api.autodesk.com
  tags:
  - 2D Visualization
  - 3D Visualization
  - JavaScript
  - Viewer
  - WebGL
  properties:
  - type: Documentation
    url: https://aps.autodesk.com/en/docs/viewer/v7
  - type: API Overview
    url: https://aps.autodesk.com/developer/overview/viewer-sdk
  - type: Developers Guide
    url: https://aps.autodesk.com/en/docs/viewer/v2/developers_guide/overview/
  contact:
  - FN: Autodesk Developer Support
    email: forge.help@autodesk.com
    url: https://aps.autodesk.com/get-help
- name: AutoCAD Webhooks API
  description: API enabling applications to listen for and receive notifications when specific events occur in AutoCAD data and workflows, supporting event-driven architectures.
  image: https://www.autodesk.com/products/autocad/overview
  humanURL: https://aps.autodesk.com/developer/overview/webhooks-api
  baseURL: https://developer.api.autodesk.com/webhooks/v1
  tags:
  - Events
  - Notifications
  - Real-Time
  - Webhooks
  properties:
  - type: Documentation
    url: https://aps.autodesk.com/en/docs/webhooks/v1
  - type: API Reference
    url: https://aps.autodesk.com/en/docs/webhooks/v1/reference/
  - type: Tutorials
    url: https://aps.autodesk.com/en/docs/webhooks/v1/tutorials/
  - type: API Overview
    url: https://aps.autodesk.com/developer/overview/webhooks-api
  contact:
  - FN: Autodesk Developer Support
    email: forge.help@autodesk.com
    url: https://aps.autodesk.com/get-help
- name: AutoCAD Authentication API
  description: OAuth 2.0-based authentication API for securing access to AutoCAD and Autodesk Platform Services APIs, supporting both 2-legged and 3-legged authentication workflows.
  image: https://www.autodesk.com/products/autocad/overview
  humanURL: https://aps.autodesk.com/developer/overview/authentication-api
  baseURL: https://developer.api.autodesk.com/authentication/v2
  tags:
  - Authentication
  - Authorization
  - OAuth
  - Security
  properties:
  - type: Documentation
    url: https://aps.autodesk.com/en/docs/oauth/v2
  - type: Getting Started
    url: https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/basics
  - type: API Overview
    url: https://aps.autodesk.com/developer/overview/authentication-api
  contact:
  - FN: Autodesk Developer Support
    email: forge.help@autodesk.com
    url: https://aps.autodesk.com/get-help
- name: AutoCAD ObjectARX SDK
  description: C++ SDK providing object-oriented interfaces for deep integration with AutoCAD internals, enabling creation of custom objects, commands, and extensions with full access to the AutoCAD runtime environment.
  image: https://www.autodesk.com/products/autocad/overview
  humanURL: https://aps.autodesk.com/developer/overview/objectarx-autocad-sdk
  tags:
  - C++
  - Custom Objects
  - Desktop
  - ObjectARX
  - SDK
  properties:
  - type: Documentation
    url: https://help.autodesk.com/view/OARX/2025/ENU/
  - type: SDK Overview
    url: https://aps.autodesk.com/developer/overview/objectarx-autocad-sdk
  - type: SDK Licensing
    url: https://aps.autodesk.com/developer/overview/autocad-objectarx-sdk-licensing
  contact:
  - FN: Autodesk Developer Support
    email: forge.help@autodesk.com
    url: https://aps.autodesk.com/get-help
- name: AutoCAD .NET API
  description: Managed .NET API for building custom AutoCAD applications and plugins using C# or VB.NET, providing access to drawing manipulation, entity management, and user interface customization running on .NET 8.0 in AutoCAD 2026.
  image: https://www.autodesk.com/products/autocad/overview
  humanURL: https://help.autodesk.com/view/OARX/2025/ENU/?guid=GUID-390A47DB-77AF-433A-994C-2AFBBE9996AE
  tags:
  - .NET
  - C#
  - Desktop
  - Managed API
  - Plugin
  properties:
  - type: Documentation
    url: https://help.autodesk.com/view/OARX/2025/ENU/?guid=GUID-390A47DB-77AF-433A-994C-2AFBBE9996AE
  - type: Getting Started
    url: https://help.autodesk.com/view/OARX/2025/ENU/?guid=GUID-4E1AAFA9-740E-4097-800C-CAED09CDFF12
  contact:
  - FN: Autodesk Developer Support
    email: forge.help@autodesk.com
    url: https://aps.autodesk.com/get-help
- name: AutoCAD AutoLISP API
  description: Programming environment for extending AutoCAD with custom commands and routines using the LISP language, including Visual LISP development tools for creating, debugging, and deploying AutoLISP programs.
  image: https://www.autodesk.com/products/autocad/overview
  humanURL: https://help.autodesk.com/view/OARX/2025/ENU/?guid=GUID-49AAEA0E-C422-48C4-87F0-52FCA491BF2C
  tags:
  - AutoLISP
  - Customization
  - Desktop
  - Scripting
  - Visual LISP
  properties:
  - type: Documentation
    url: https://help.autodesk.com/view/OARX/2025/ENU/?guid=GUID-49AAEA0E-C422-48C4-87F0-52FCA491BF2C
  - type: Developers Guide
    url: https://help.autodesk.com/view/OARX/2025/ENU/?guid=GUID-265AADB3-FB89-4D34-AA9D-6ADF70FF7D4B
  contact:
  - FN: Autodesk Developer Support
    email: forge.help@autodesk.com
    url: https://aps.autodesk.com/get-help
- name: AutoCAD JavaScript API
  description: JavaScript API for connecting web-based applications with AutoCAD, enabling HTML5-based user interface components including modal dialogs, palettes, and document windows within AutoCAD.
  image: https://www.autodesk.com/products/autocad/overview
  humanURL: https://help.autodesk.com/view/OARX/2025/ENU/?guid=adsk_jsref_javascript_reference_guide
  tags:
  - Desktop
  - HTML5
  - JavaScript
  - UI
  - Web
  properties:
  - type: Documentation
    url: https://help.autodesk.com/view/OARX/2025/ENU/?guid=adsk_jsref_javascript_reference_guide
  - type: Getting Started
    url: https://help.autodesk.com/view/OARX/2023/ENU/?guid=adsk_jsdev_autocad_javascript_api_about
  contact:
  - FN: Autodesk Developer Support
    email: forge.help@autodesk.com
    url: https://aps.autodesk.com/get-help
name: AutoCAD
tags:
- 3D Modeling
- Architecture
- CAD
- Design
- Drawing
- Engineering
type: Contract
image: https://www.autodesk.com/products/autocad/overview
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for Autodesk AutoCAD, providing programmatic access to CAD design, drawing, and automation capabilities through Autodesk Platform Services (APS, formerly Forge) and desktop development environments including AutoLISP, ObjectARX, .NET, and JavaScript.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

