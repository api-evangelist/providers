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
modified: '2026-04-19'
position: Consumer
segments:
  - Workflows
description: Appian is a low-code automation platform that accelerates the creation of high-impact business applications. The platform combines intelligent automation and enterprise low-code development to help organizations build apps and workflows rapidly.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
  - FN: Appian Corporation
    email: support@appian.com
    url: https://www.appian.com
specificationVersion: '0.19'
common:
  - url: https://community.appian.com
    type: Portal
  - url: https://docs.appian.com
    type: Documentation
  - url: https://docs.appian.com/suite/help/latest/Getting_Started.html
    type: Getting Started
  - url: https://docs.appian.com/suite/help/latest/Web_API_Authentication.html
    type: Authentication
  - url: https://community.appian.com/support
    type: Support
  - url: https://appian.com/blog
    type: Blog
  - url: https://appian.com/platform/pricing.html
    type: Pricing
  - url: https://www.appian.com/terms-of-service.html
    type: Terms of Service
  - url: https://www.appian.com/privacy.html
    type: Privacy Policy
  - url: https://appian.com/developers
    type: DeveloperPortal
  - url: https://github.com/appian
    type: GitHubOrganization
  - url: https://community.appian.com/b/appmarket
    type: Marketplace
  - url: https://academy.appian.com/
    type: Training
  - url: https://community.appian.com/learn/courses
    type: Courses
  - url: https://status.appiancloud.com/
    type: StatusPage
  - url: https://trustcenter.appian.com/
    type: TrustCenter
  - url: https://appian.com/support/resources/trust/security
    type: Security
  - url: https://appian.com/support/resources/trust/compliance
    type: Compliance
  - url: https://appian.com/contact-us
    type: Contact
  - url: https://x.com/Appian
    type: X
  - url: https://www.linkedin.com/company/appian-corporation
    type: LinkedIn
  - url: https://docs.appian.com/suite/help/25.4/connected-system-plug-in-landing.html
    type: SDKs
  - url: https://github.com/appian/integration-sdk-examples
    type: SDKExamples
  - url: https://appian.com/landing/community-edition/get-started
    type: Sandbox
  - url: https://docs.appian.com/suite/help/25.4/Web_API_Authentication.html
    type: APIAuthentication
  - url: https://docs.appian.com/suite/help/25.4/Appian_Release_Notes.html
    type: Change Log
  - url: https://appian.com/products/platform/whats-new
    type: WhatsNew
  - url: https://community.appian.com/p/login2
    type: Login
  - url: https://docs.appian.com/suite/help/25.4/extending-appian.html
    type: ExtendingAppian
  - url: https://docs.appian.com/suite/help/25.4/csp-javadocs.html
    type: JavaDocs
  - url: https://docs.appian.com/suite/help/25.4/ui-sdk-overview.html
    type: UISDKs
  - url: https://www.appian.com
    type: Website
  - type: JSONLD
    url: json-ld/appian-context.jsonld
  - type: JSONSchema
    url: json-schema/application-package-details-package-list-response-schema.json
  - type: JSONSchema
    url: json-schema/application-package-details-package-schema.json
  - type: JSONSchema
    url: json-schema/deployment-rest-database-script-schema.json
  - type: JSONSchema
    url: json-schema/deployment-rest-deployment-request-schema.json
  - type: JSONSchema
    url: json-schema/deployment-rest-deployment-response-schema.json
  - type: JSONSchema
    url: json-schema/deployment-rest-deployment-status-schema.json
  - type: JSONSchema
    url: json-schema/deployment-rest-export-configuration-schema.json
  - type: JSONSchema
    url: json-schema/deployment-rest-export-deployment-result-schema.json
  - type: JSONSchema
    url: json-schema/deployment-rest-import-configuration-schema.json
  - type: JSONSchema
    url: json-schema/deployment-rest-import-deployment-result-schema.json
  - type: JSONSchema
    url: json-schema/deployment-rest-import-summary-count-schema.json
  - type: JSONSchema
    url: json-schema/deployment-rest-inspection-error-schema.json
  - type: JSONSchema
    url: json-schema/deployment-rest-inspection-problems-schema.json
  - type: JSONSchema
    url: json-schema/deployment-rest-inspection-request-schema.json
  - type: JSONSchema
    url: json-schema/deployment-rest-inspection-response-schema.json
  - type: JSONSchema
    url: json-schema/deployment-rest-inspection-result-schema.json
  - type: JSONSchema
    url: json-schema/deployment-rest-inspection-warning-schema.json
  - type: JSONStructure
    url: json-structure/application-package-details-package-list-response-structure.json
  - type: JSONStructure
    url: json-structure/application-package-details-package-structure.json
  - type: JSONStructure
    url: json-structure/deployment-rest-database-script-structure.json
  - type: JSONStructure
    url: json-structure/deployment-rest-deployment-request-structure.json
  - type: JSONStructure
    url: json-structure/deployment-rest-deployment-response-structure.json
  - type: JSONStructure
    url: json-structure/deployment-rest-deployment-status-structure.json
  - type: JSONStructure
    url: json-structure/deployment-rest-export-configuration-structure.json
  - type: JSONStructure
    url: json-structure/deployment-rest-export-deployment-result-structure.json
  - type: JSONStructure
    url: json-structure/deployment-rest-import-configuration-structure.json
  - type: JSONStructure
    url: json-structure/deployment-rest-import-deployment-result-structure.json
  - type: JSONStructure
    url: json-structure/deployment-rest-import-summary-count-structure.json
  - type: JSONStructure
    url: json-structure/deployment-rest-inspection-error-structure.json
  - type: JSONStructure
    url: json-structure/deployment-rest-inspection-problems-structure.json
  - type: JSONStructure
    url: json-structure/deployment-rest-inspection-request-structure.json
  - type: JSONStructure
    url: json-structure/deployment-rest-inspection-response-structure.json
  - type: JSONStructure
    url: json-structure/deployment-rest-inspection-result-structure.json
  - type: JSONStructure
    url: json-structure/deployment-rest-inspection-warning-structure.json
  - type: Example
    url: examples/application-package-details-package-example.json
  - type: Example
    url: examples/application-package-details-package-list-response-example.json
  - type: Example
    url: examples/deployment-rest-database-script-example.json
  - type: Example
    url: examples/deployment-rest-deployment-request-example.json
  - type: Example
    url: examples/deployment-rest-deployment-response-example.json
  - type: Example
    url: examples/deployment-rest-deployment-status-example.json
  - type: Example
    url: examples/deployment-rest-export-configuration-example.json
  - type: Example
    url: examples/deployment-rest-export-deployment-result-example.json
  - type: Example
    url: examples/deployment-rest-import-configuration-example.json
  - type: Example
    url: examples/deployment-rest-import-deployment-result-example.json
  - type: Example
    url: examples/deployment-rest-import-summary-count-example.json
  - type: Example
    url: examples/deployment-rest-inspection-error-example.json
  - type: Example
    url: examples/deployment-rest-inspection-problems-example.json
  - type: Example
    url: examples/deployment-rest-inspection-request-example.json
  - type: Example
    url: examples/deployment-rest-inspection-response-example.json
  - type: Example
    url: examples/deployment-rest-inspection-result-example.json
  - type: Example
    url: examples/deployment-rest-inspection-warning-example.json
  - type: Features
    data:
      - name: Low-Code Application Development
        description: Build process-driven business applications with low-code design tools.
      - name: Process Automation
        description: Automate business processes with workflow designer, robotic process automation, and AI.
      - name: Deployment REST API
        description: Programmatic CI/CD deployment of Appian applications and packages.
      - name: Web APIs
        description: Expose Appian data and services to external systems via REST web services.
      - name: RPA Integration
        description: Robotic process automation for automating repetitive front-end tasks.
      - name: Integration SDK
        description: Java-based SDK for building connected system plug-ins to integrate with third-party services.
      - name: UI SDK
        description: Web technology SDK for building custom component plug-ins to extend Appian interfaces.
      - name: AppMarket
        description: Marketplace for sharing and distributing Appian plug-ins and extensions.
      - name: OpenAPI Export
        description: Export Web APIs as OpenAPI 3.0.1 specifications for documentation sharing.
  - type: UseCases
    data:
      - name: Process Automation
        description: Automate complex business workflows across departments with low-code design.
      - name: Application Deployment Automation
        description: Automate Appian application deployment pipelines using the Deployment REST API.
      - name: External System Integration
        description: Expose Appian data to external systems via Web APIs and Integration SDK.
      - name: Enterprise RPA
        description: Automate repetitive front-end tasks using the Appian RPA platform.
      - name: Custom UI Extension
        description: Extend Appian interfaces with custom components built using the UI SDK.
  - type: Integrations
    data:
      - name: Salesforce
        description: Connect Appian to Salesforce CRM for data synchronization and process automation.
      - name: SAP
        description: Integrate Appian with SAP enterprise systems for process automation.
      - name: ServiceNow
        description: Connect Appian workflows with ServiceNow ITSM processes.
      - name: DocuSign
        description: Integrate electronic signature workflows with Appian processes.
      - name: AWS
        description: Connect Appian to Amazon Web Services via Integration SDK connectors.
---
