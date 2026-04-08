---
aid: appian
url: https://raw.githubusercontent.com/api-evangelist/appian/refs/heads/main/apis.yml
apis:
- aid: appian:appian
  name: Appian Application Package Details API
  tags:
  - Deployment
  - Packages
  humanURL: https://docs.appian.com/suite/help/25.4/Application_Package_Details_API.html
  properties:
  - url: https://docs.appian.com/suite/help/25.4/Application_Package_Details_API.html
    type: Documentation
  - url: https://docs.appian.com/suite/help/25.4/Application_Package_Details_API.html
    type: Reference
  - url: https://docs.appian.com/suite/help/25.4/Web_API_Authentication.html
    type: Authentication
  description: This endpoint uses the UUID of an application to retrieve data about any in-flight packages for the application. It can be used to link packages to change management systems or get identifiers for packages to use for a deployment.
- aid: appian:deployment-rest-api
  name: Appian Deployment REST API
  tags:
  - CI/CD
  - Deployment
  - Packages
  humanURL: https://docs.appian.com/suite/help/25.4/Deployment_Rest_API.html
  properties:
  - url: https://docs.appian.com/suite/help/25.4/Deployment_Rest_API.html
    type: Documentation
  - url: https://docs.appian.com/suite/help/25.4/Export_Package_API.html
    type: Reference
  - url: https://docs.appian.com/suite/help/25.4/Web_API_Authentication.html
    type: Authentication
  description: The Appian Deployment REST API provides endpoints for exporting, inspecting, and importing applications and packages. It enables automation of CI/CD pipelines including exports, inspections, and imports, and supports post-deployment processes for external deployments.
- aid: appian:web-apis
  name: Appian Web APIs
  tags:
  - Integration
  - REST
  - Web API
  humanURL: https://docs.appian.com/suite/help/25.4/Web_APIs.html
  properties:
  - url: https://docs.appian.com/suite/help/25.4/Web_APIs.html
    type: Documentation
  - url: https://docs.appian.com/suite/help/25.4/Web_API_Tutorial.html
    type: Tutorial
  - url: https://docs.appian.com/suite/help/25.4/Designing_Web_APIs.html
    type: GettingStartedGuide
  - url: https://docs.appian.com/suite/help/25.4/Web_API_Authentication.html
    type: Authentication
  - url: https://docs.appian.com/suite/help/25.4/passing-a-web-api-document-into-a-process-model.html
    type: Reference
  description: Appian Web APIs expose Appian data and services to external systems through REST web services. Each Web API associates a URL and HTTP method combination with an expression, supporting GET, POST, PUT, DELETE, and PATCH methods. Web APIs support OpenAPI 3.0.1 specification export for documentation sharing.
- aid: appian:rpa-rest-api
  name: Appian RPA REST API
  tags:
  - Robotic Process Automation
  - RPA
  humanURL: https://docs.appian.com/suite/help/25.4/rpa-9.18/api-architecture.html
  properties:
  - url: https://docs.appian.com/suite/help/25.4/rpa-9.18/api-architecture.html
    type: Documentation
  - url: https://docs.appian.com/suite/help/25.4/rpa-9.18/api-get-robotic-task-schedule-instructions.html
    type: Reference
  - url: https://docs.appian.com/suite/help/25.4/Web_API_Authentication.html
    type: Authentication
  - url: https://docs.appian.com/suite/help/25.4/rpa-9.18/api-architecture.html
    type: Deprecation Notice
  description: The Appian RPA REST API exposes robotic process automation functionality to external systems. Endpoints are accessed via the format https://.appiancloud.com/rpa/rest/oo/ and authenticated using a Bearer token with an API key in the Authorization header. RPA Queues and Scheduling are deprecated and will be removed in Appian 26.1.
- aid: appian:integration-sdk
  name: Appian Integration SDK
  tags:
  - Connected Systems
  - Integration
  - Plug-Ins
  - SDK
  humanURL: https://docs.appian.com/suite/help/25.4/connected-system-plug-in-landing.html
  properties:
  - url: https://docs.appian.com/suite/help/25.4/connected-system-plug-in-landing.html
    type: Documentation
  - url: https://docs.appian.com/suite/help/25.4/csp-javadocs.html
    type: Reference
  - url: https://github.com/appian/integration-sdk-examples
    type: GitHubRepository
  description: The Appian Integration SDK enables developers to build connected system plug-ins that extend Appian's low-code integration capabilities. Plug-ins are built using Java and allow designers to interact with third-party services through a guided point-and-click interface. They can be distributed through the Appian AppMarket.
- aid: appian:ui-sdk
  name: Appian UI SDK
  tags:
  - Components
  - Plug-Ins
  - SDK
  - UI
  humanURL: https://docs.appian.com/suite/help/25.4/ui-sdk-overview.html
  properties:
  - url: https://docs.appian.com/suite/help/25.4/ui-sdk-overview.html
    type: Documentation
  - url: https://docs.appian.com/suite/help/25.4/component-plugins.html
    type: Reference
  - url: https://docs.appian.com/suite/help/25.4/develop-first-component.html
    type: Getting Started
  - url: https://docs.appian.com/suite/help/25.4/ui-sdk-versions.html
    type: Change Log
  description: The Appian UI SDK lets developers design custom component plug-ins to extend Appian interfaces by adding new components that integrate with external systems. Components are built using standard web technologies including HTML, JavaScript, and CSS, and can leverage third-party libraries.
- aid: appian:appian-suite-api
  name: Appian Suite API
  tags:
  - Extensibility
  - Java
  - Plug-Ins
  humanURL: https://docs.appian.com/suite/help/25.4/extending-appian.html
  properties:
  - url: https://docs.appian.com/suite/help/25.4/extending-appian.html
    type: Documentation
  - url: https://docs.appian.com/suite/help/25.4/Custom_Smart_Service_Plug-ins.html
    type: Reference
  - url: https://docs.appian.com/suite/help/25.4/Custom_Function_Plug-ins.html
    type: Reference
  description: The Appian Suite API provides Java-based access to platform capabilities for managing processes, documents, users, and groups. It supports building smart service plug-ins, function plug-ins, data type plug-ins, and servlet plug-ins to extend the Appian platform using annotated Java classes.
name: Appian
tags:
- Automation
- BPM
- Business Process Management
- Enterprise Software
- Low-Code
- Process Automation
- RPA
- Workflow
type: Index
image: https://www.appian.com/favicon.ico
access: 3rd-Party
created: '2025-02-08'
modified: '2026-04-07'
position: Consumer
description: Appian is a low-code automation platform that accelerates the creation of high-impact business applications. The platform combines intelligent automation and enterprise low-code development to help organizations build apps and workflows rapidly.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

