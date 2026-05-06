---
aid: adaptigent
url: https://raw.githubusercontent.com/api-evangelist/adaptigent/refs/heads/main/apis.yml
name: Adaptigent
created: '2025-03-01'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Mainframe
  - Integration
  - API Gateway
  - Legacy Systems
  - Enterprise
  - No Code
  - Middleware
description: Adaptigent (formerly GT Software) is a technology company founded in 1982 that specializes in mainframe integration and API enablement solutions. Their flagship product, Adaptive Integration Fabric (formerly Ivory Suite), empowers enterprises to expose legacy mainframe systems as modern REST and SOAP APIs without writing any code. Using a patented no-code, drag-and-drop environment, the platform enables integration of IBM z/OS and z/VSE mainframe applications with modern distributed systems, supporting both inbound and outbound integration flows in real time. Adaptigent serves industries including finance, government, manufacturing, and healthcare, offering a usage-based subscription pricing model.
apis:
  - aid: adaptigent:adaptive-integration-fabric
    name: Adaptive Integration Fabric API
    tags:
      - Mainframe
      - Integration
      - REST API
      - SOAP
      - No Code
    humanURL: https://www.adaptigent.com/products/core-systems-integration/
    description: The Adaptive Integration Fabric (formerly Ivory Suite) enables enterprises to rapidly expose IBM z/OS and z/VSE mainframe applications as REST or SOAP web services without programming. Using the Fabric Studio drag-and-drop interface, users design integration flows that become deployed as API endpoints through the Fabric Runtime. Supports both inbound API calls into the mainframe and outbound API calls from mainframe COBOL and PL/I programs to external REST or SOAP services. Available on Red Hat Marketplace.
    properties:
      - type: Documentation
        url: https://www.adaptigent.com/products/core-systems-integration/
      - type: GettingStarted
        url: https://www.adaptigent.com/project/api-enabling-your-mainframe-with-adaptigent/
common:
  - type: Website
    url: https://www.adaptigent.com
  - type: Portal
    url: https://www.adaptigent.com
  - type: Pricing
    url: https://www.adaptigent.com/resources/pricing/
  - type: Partners
    url: https://www.adaptigent.com/about/partners/
  - type: Blog
    url: https://www.adaptigent.com/blog/
  - type: Contact
    url: https://www.adaptigent.com/contact/
  - type: Features
    data:
      - name: No-Code API Development
        description: Patented drag-and-drop visual environment enables non-programmers to create sophisticated REST and SOAP APIs from mainframe applications without writing any code.
      - name: Inbound And Outbound Integration
        description: Supports bidirectional integration flows — modern applications can call mainframe services via API, and COBOL/PL/I mainframe programs can make outbound calls to external REST or SOAP services.
      - name: Real-Time Mainframe Data Access
        description: Provides real-time access to legacy data sources and transaction systems, enabling modern applications to consume mainframe data instantly without batch processing.
      - name: IBM z/OS And z/VSE Support
        description: Natively supports IBM z/OS and z/VSE mainframe platforms, enabling REST API enablement for COBOL and PL/I programs on these systems.
      - name: REST And SOAP API Generation
        description: Automatically generates industry-standard REST and SOAP web service endpoints from mainframe subroutines and programs, with no additional MIPS usage.
      - name: Usage-Based Subscription Pricing
        description: Flexible pricing model based on actual resource consumption, allowing organizations to scale integration usage without fixed licensing fees.
      - name: Red Hat Marketplace Availability
        description: Available on Red Hat Marketplace, enabling enterprise customers to deploy and manage Adaptive Integration Fabric within their Red Hat OpenShift environments.
  - type: UseCases
    data:
      - name: Mainframe API Modernization
        description: Enterprises with legacy IBM mainframe systems can expose core business logic and data as modern REST APIs, enabling mobile apps, web applications, and microservices to consume mainframe capabilities.
      - name: Financial Core System Integration
        description: Banks and financial institutions can connect core banking systems on the mainframe to fraud detection services, digital banking platforms, and fintech APIs in real time.
      - name: Government Legacy System Modernization
        description: Government agencies can modernize access to mission-critical legacy systems by exposing them as standard APIs without replacing or re-coding existing mainframe applications.
      - name: Manufacturing Supply Chain Integration
        description: Manufacturers can link inventory, transportation, and parts systems running on legacy platforms with modern ERP and supply chain management systems through API integration.
      - name: Hybrid Cloud Mainframe Connectivity
        description: Organizations adopting hybrid cloud strategies can bridge on-premises mainframe data with cloud-based applications and services using Adaptive Integration Fabric as the middleware layer.
  - type: Integrations
    data:
      - name: IBM z/OS
        description: Native integration with IBM z/OS mainframe operating system.
      - name: IBM z/VSE
        description: Native integration with IBM z/VSE mainframe operating system.
      - name: Red Hat OpenShift
        description: Available on Red Hat Marketplace for deployment in OpenShift environments.
      - name: REST APIs
        description: Consumes and produces standard REST APIs for integration with modern distributed systems.
      - name: SOAP Web Services
        description: Generates SOAP web service endpoints from mainframe programs for compatibility with enterprise service-oriented architecture.
maintainers:
  - FN: Kin Lane
    X-twitter: apievangelist
    email: info@apievangelist.com
---
