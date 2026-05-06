---
aid: qlikview
name: QlikView
description: QlikView is a business intelligence and data visualization platform that enables users to create guided analytics applications and dashboards for data discovery.
type: Index
image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo-2x.png
url: https://raw.githubusercontent.com/api-evangelist/qlikview/refs/heads/main/apis.yml
tags:
  - Analytics
  - Business Intelligence
  - Dashboards
  - Data Discovery
  - Data Visualization
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
apis:
  - name: QlikView Server API
    description: Server-side API for managing QlikView Server operations, documents, and sessions.
    image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo-2x.png
    humanURL: https://help.qlik.com/en-US/qlikview/
    baseURL: http://qlikview-server:4799/QMS/Service
    tags:
      - Administration
      - Documents
      - Server Management
      - Sessions
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/qlikview-developer/November2023/Subsystems/Server/Content/QV_Server/sv-reference-QMS-API.htm
      - type: OpenAPI
        url: https://help.qlik.com/en-US/qlikview-developer/APIs/
      - type: GettingStartedGuide
        url: https://help.qlik.com/en-US/qlikview-developer/September2025/Content/QV_HelpSites/APIsAndSDKs.htm
    contact:
      - FN: Qlik Support
        email: support@qlik.com
        url: https://community.qlik.com/
  - name: QlikView Management API (QMS API)
    description: SOAP-based API for QlikView management and administration tasks.
    image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo-2x.png
    humanURL: https://help.qlik.com/en-US/qlikview/
    baseURL: http://qlikview-server:4799/QMS/Service
    tags:
      - Administration
      - Configuration
      - Management
      - SOAP
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/qlikview-developer/November2023/Subsystems/Server/Content/QV_Server/sv-qms-api-interface.htm
      - type: WSDL
        url: http://qlikview-server:4799/QMS/Service?wsdl
      - type: SDK
        url: https://help.qlik.com/en-US/qlikview-developer/November2023/Content/QV_QlikViewSDK/QV_SDK_Introduction.htm
      - type: APIReference
        url: https://help.qlik.com/en-US/qlikview-developer/September2025/Subsystems/QMSAPIref/Content/Home.htm
      - type: InterfaceReference
        url: https://help.qlik.com/en-US/qlikview-developer/September2025/Subsystems/QMSAPIref/Content/PIX.Services.V12.IQMS.htm
    contact:
      - FN: Qlik Support
        email: support@qlik.com
        url: https://community.qlik.com/
  - name: QlikView AccessPoint API
    description: Web-based API for QlikView AccessPoint portal functionality.
    image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo-2x.png
    humanURL: https://help.qlik.com/en-US/qlikview/
    baseURL: http://qlikview-server/QvAJAXZfc/
    tags:
      - AJAX
      - Frontend
      - User Access
      - Web Portal
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/qlikview-developer/November2023/Subsystems/AJAX/Content/QV_AJAX/ajax-api-introduction.htm
      - type: JavaScript API
        url: https://help.qlik.com/en-US/qlikview-developer/November2023/Subsystems/AJAX/Content/QV_AJAX/qva-getdocumentlist.htm
      - type: JavaScriptLibrary
        url: https://help.qlik.com/en-US/qlikview-developer/September2025/apis/js%20API/
    contact:
      - FN: Qlik Support
        email: support@qlik.com
        url: https://community.qlik.com/
  - name: QlikView Workbench API
    description: API for integrating QlikView objects into web applications and portals.
    image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo-2x.png
    humanURL: https://help.qlik.com/en-US/qlikview/
    baseURL: http://qlikview-server/QvAJAXZfc/
    tags:
      - .NET
      - Embedding
      - Web Integration
      - Workbench
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/qlikview-developer/November2023/Subsystems/Workbench/Content/QV_Workbench/workbench-introduction.htm
      - type: ASP.NET Controls
        url: https://help.qlik.com/en-US/qlikview-developer/November2023/Subsystems/Workbench/Content/QV_Workbench/server-side-controls.htm
    contact:
      - FN: Qlik Support
        email: support@qlik.com
        url: https://community.qlik.com/
  - name: QlikView Plugin API
    description: COM-based API for creating custom objects and extensions in QlikView.
    image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo-2x.png
    humanURL: https://help.qlik.com/en-US/qlikview/
    baseURL: local
    tags:
      - COM
      - Custom Objects
      - Extensions
      - Plugins
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/qlikview-developer/November2023/Subsystems/PluginAPI/Content/QV_PluginAPI/plugin-api-introduction.htm
      - type: SDK
        url: https://community.qlik.com/t5/Developers/ct-p/qlik-developers
    contact:
      - FN: Qlik Support
        email: support@qlik.com
        url: https://community.qlik.com/
  - name: QlikView OCX API (Automation API)
    description: ActiveX/COM API for automating QlikView Desktop operations.
    image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo-2x.png
    humanURL: https://help.qlik.com/en-US/qlikview/
    baseURL: local
    tags:
      - ActiveX
      - Automation
      - COM
      - Desktop
      - Scripting
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/qlikview-developer/November2023/Subsystems/OCX/Content/QV_OCX/ocx-introduction.htm
      - type: Reference Guide
        url: https://help.qlik.com/en-US/qlikview-developer/November2023/Subsystems/OCX/Content/QV_OCX/ocx-api-reference.htm
    contact:
      - FN: Qlik Support
        email: support@qlik.com
        url: https://community.qlik.com/
  - name: QlikView QVX SDK API
    description: The Qlik data eXchange (QVX) SDK enables developers to build custom connectors for integrating external data sources into QlikView, using a high-performance file and stream format for data input.
    image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo-2x.png
    humanURL: https://help.qlik.com/en-US/qlikview-developer/September2025/Content/QV_HelpSites/APIsAndSDKs.htm
    baseURL: local
    tags:
      - Custom Connectors
      - Data Integration
      - Data Sources
      - QVX
      - SDK
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/qlikview-developer/September2025/Subsystems/QVXSDKAPI/Content/QV_QVXSDKAPI/Getting-started.htm
      - type: APIReference
        url: https://help.qlik.com/en-US/qlikview-developer/September2025/Subsystems/QVXSDKAPI/Content/QV_QVXSDKAPI/QlikView%20QVX%20File%20Format/command-pipe.htm
    contact:
      - FN: Qlik Support
        email: support@qlik.com
        url: https://community.qlik.com/
  - name: QlikView JavaScript API
    description: JavaScript API library for building websites containing QlikView content and for developing custom extension objects that extend QlikView visualization capabilities.
    image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo-2x.png
    humanURL: https://help.qlik.com/en-US/qlikview-developer/September2025/Content/QV_HelpSites/APIsAndSDKs.htm
    baseURL: http://qlikview-server/QvAJAXZfc/
    tags:
      - AJAX
      - Extensions
      - JavaScript
      - Visualization
      - Web Development
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/qlikview-developer/September2025/apis/js%20API/
      - type: GettingStartedGuide
        url: https://help.qlik.com/en-US/qlikview-developer/September2025/Content/QV_HelpSites/APIsAndSDKs.htm
    contact:
      - FN: Qlik Support
        email: support@qlik.com
        url: https://community.qlik.com/
  - name: QlikView Authentication API (Ticket API)
    description: Authentication API providing Custom Ticket Exchange (CTE) for secure single sign-on access to QlikView Server, allowing third-party systems to request authentication tokens on behalf of users.
    image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo-2x.png
    humanURL: https://help.qlik.com/en-US/qlikview-developer/September2025/Content/QV_HelpSites/APIsAndSDKs.htm
    baseURL: http://qlikview-server/QvAJAXZfc/
    tags:
      - Authentication
      - Custom Ticket Exchange
      - Security
      - Single Sign-On
      - Tickets
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/qlikview-developer/September2025/Content/QV_HelpSites/APIsAndSDKs.htm
      - type: Support
        url: https://community.qlik.com/t5/Official-Support-Articles/Customized-Authentication-in-QlikView/ta-p/1710763
    contact:
      - FN: Qlik Support
        email: support@qlik.com
        url: https://community.qlik.com/
  - name: QlikView Distribution Service API (IQDS)
    description: API interface for the QlikView Distribution Service, providing programmatic access to document distribution, task management, and scheduled reload operations including External Document Exchange (EDX) triggers.
    image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo-2x.png
    humanURL: https://help.qlik.com/en-US/qlikview-developer/September2025/Subsystems/QMSAPIref/Content/PIX.Services.IQDS.htm
    baseURL: http://qlikview-server:4799/QMS/Service
    tags:
      - Distribution
      - Document Reload
      - EDX
      - Scheduling
      - Task Management
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/qlikview-developer/September2025/Subsystems/QMSAPIref/Content/PIX.Services.IQDS.htm
      - type: APIReference
        url: https://help.qlik.com/en-US/qlikview-developer/September2025/Subsystems/QMSAPIref/Content/Home.htm
    contact:
      - FN: Qlik Support
        email: support@qlik.com
        url: https://community.qlik.com/
common:
  - type: Portal
    url: https://help.qlik.com/en-US/qlikview-developer/
  - type: APIReference
    url: https://help.qlik.com/en-US/qlikview-developer/September2025/Subsystems/QMSAPIref/Content/Home.htm
  - type: Support
    url: https://community.qlik.com/
  - type: Training
    url: https://www.qlik.com/us/services/training
  - type: Pricing
    url: https://www.qlik.com/us/pricing
  - type: ReleaseNotes
    url: https://community.qlik.com/t5/Release-Notes/tkb-p/ReleaseNotes
  - type: GitHubOrganization
    url: https://github.com/qlik-oss
  - type: DeveloperPortal
    url: https://qlik.dev/
  - type: Features
    data:
      - name: Associative Data Model
        description: Explore data relationships dynamically with QlikView's patented associative engine.
      - name: In-Memory Processing
        description: Fast analytics with in-memory data compression and calculation.
      - name: Guided Analytics
        description: Build guided analytics applications with interactive dashboards and drill-down capabilities.
      - name: Data Visualization
        description: Rich set of chart types and visualization objects for data exploration and presentation.
      - name: Custom Extensions
        description: Extend QlikView with custom objects, connectors, and plugins using the Plugin and QVX APIs.
      - name: AJAX Client
        description: Web-based access to QlikView documents through the AJAX Zero Footprint Client.
      - name: Document Distribution
        description: Schedule and distribute QlikView documents and reports via the Distribution Service.
      - name: Custom Ticket Authentication
        description: Integrate single sign-on with custom authentication systems using the Ticket API.
  - type: UseCases
    data:
      - name: Business Intelligence Dashboards
        description: Build interactive BI dashboards for sales, finance, and operations analytics.
      - name: Embedded Analytics
        description: Embed QlikView analytics objects into existing web applications and portals.
      - name: Automated Reporting
        description: Schedule and distribute data-driven reports to stakeholders across the organization.
      - name: Data Discovery
        description: Enable self-service data discovery and exploration for business users.
      - name: Custom Data Connectors
        description: Build custom connectors to integrate QlikView with proprietary data sources.
  - type: Integrations
    data:
      - name: Qlik Sense
        description: Migrate and extend QlikView applications to the modern Qlik Sense platform.
      - name: SQL Databases
        description: Connect to SQL Server, Oracle, MySQL, PostgreSQL and other relational databases.
      - name: SAP
        description: Extract and visualize SAP data with native SAP connectors.
      - name: Salesforce
        description: Integrate with Salesforce CRM data for sales analytics and reporting.
      - name: Active Directory
        description: Authenticate users and manage access through Active Directory integration.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
