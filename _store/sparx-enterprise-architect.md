---
aid: sparx-enterprise-architect
name: Sparx Enterprise Architect
description: Sparx Enterprise Architect is a comprehensive modeling, design, and management platform for enterprise architecture, software engineering, and systems engineering. It provides automation APIs including a COM Automation Interface, Add-In Framework, and scripting capabilities for programmatic access to models, diagrams, elements, connectors, and repository management.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/sparx-enterprise-architect/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-18'
specificationVersion: '0.19'
access: 3rd-Party
tags:
  - Enterprise Architecture
  - Modeling
  - Software Engineering
  - Systems Engineering
  - UML
apis:
  - aid: sparx-enterprise-architect:automation-interface
    name: Enterprise Architect Automation Interface
    description: COM-based Automation Interface providing programmatic access to Enterprise Architect repositories, models, packages, elements, diagrams, connectors, attributes, and tagged values. Supports creating, reading, updating, and deleting model elements through the Repository, Element, Diagram, Package, and Connector object hierarchy.
    humanURL: https://sparxsystems.com/enterprise_architect_user_guide/17.0/automation.htm
    tags:
      - Automation
      - COM
      - Diagrams
      - Elements
      - Models
      - Repository
    properties:
      - type: Documentation
        url: https://sparxsystems.com/enterprise_architect_user_guide/17.0/automation.htm
      - type: APIReference
        url: https://sparxsystems.com/enterprise_architect_user_guide/17.0/automation_and_scripting/automation_interface.htm
  - aid: sparx-enterprise-architect:add-in-framework
    name: Enterprise Architect Add-In Framework
    description: Framework for building custom add-ins that extend Enterprise Architect with new functionality. Add-ins can respond to application events, add custom menu items, and integrate with external systems using COM interop from .NET, Java, or other languages.
    humanURL: https://sparxsystems.com/enterprise_architect_user_guide/17.0/add-ins_2.htm
    tags:
      - Add-Ins
      - Extensions
      - Plugins
    properties:
      - type: Documentation
        url: https://sparxsystems.com/enterprise_architect_user_guide/17.0/add-ins_2.htm
  - aid: sparx-enterprise-architect:scripting
    name: Enterprise Architect Scripting
    description: Built-in scripting engine supporting JavaScript, JScript, and VBScript for automating tasks within Enterprise Architect. Scripts can access the full automation interface to manipulate models, generate reports, validate models, and perform bulk operations.
    humanURL: https://sparxsystems.com/enterprise_architect_user_guide/17.0/scripting.htm
    tags:
      - Automation
      - JavaScript
      - Scripting
      - VBScript
    properties:
      - type: Documentation
        url: https://sparxsystems.com/enterprise_architect_user_guide/17.0/scripting.htm
  - aid: sparx-enterprise-architect:pro-cloud-server-api
    name: Pro Cloud Server API
    description: HTTP-based API provided by the Sparx Systems Pro Cloud Server for remote access to Enterprise Architect repositories. Enables integration with web-based clients, third-party tools, and automation systems via REST-like endpoints for model queries and operations.
    humanURL: https://sparxsystems.com/enterprise_architect_user_guide/17.0/pcs_overview.htm
    tags:
      - Cloud
      - HTTP
      - Remote Access
      - Repository
    properties:
      - type: Documentation
        url: https://sparxsystems.com/enterprise_architect_user_guide/17.0/pcs_overview.htm
common:
  - type: Documentation
    url: https://sparxsystems.com/enterprise_architect_user_guide/17.0/
  - type: GettingStarted
    url: https://sparxsystems.com/enterprise_architect_user_guide/17.0/getting_started.htm
  - type: Pricing
    url: https://sparxsystems.com/products/ea/pricing.html
  - type: Support
    url: https://sparxsystems.com/support/
  - type: FAQ
    url: https://sparxsystems.com/resources/faq/
  - type: Training
    url: https://sparxsystems.com/training/
  - type: ReleaseNotes
    url: https://sparxsystems.com/products/ea/release_notes.html
  - type: Blog
    url: https://sparxsystems.com/resources/blog/
  - type: X
    url: https://x.com/SparxSystems
  - type: LinkedIn
    url: https://www.linkedin.com/company/sparx-systems/
  - type: YouTube
    url: https://www.youtube.com/user/SparxSystems
  - type: Features
    data:
      - name: UML Modeling
        description: Comprehensive support for all 14 UML 2.5 diagram types for software and systems design.
      - name: ArchiMate Support
        description: Native ArchiMate 3.2 modeling for enterprise architecture frameworks.
      - name: BPMN Process Modeling
        description: Business process modeling with BPMN 2.0 for workflow and process documentation.
      - name: Code Generation
        description: Generate source code in C++, Java, C#, Python, PHP, and other languages from UML models.
      - name: Reverse Engineering
        description: Import existing codebases to create UML models from source code automatically.
      - name: Model Simulation
        description: Execute and simulate state machines and activity diagrams for validation.
      - name: Document Generation
        description: Generate rich documentation from models in RTF, HTML, PDF, and DOCX formats.
      - name: Team Collaboration
        description: Multi-user repository access with role-based security and version control integration.
  - type: UseCases
    data:
      - name: Enterprise Architecture Governance
        description: Define and maintain enterprise architecture models aligned with TOGAF, Zachman, or ArchiMate frameworks.
      - name: Software Design Documentation
        description: Create detailed software designs with UML class, sequence, and component diagrams.
      - name: Requirements Management
        description: Capture, trace, and manage requirements from stakeholder needs through to implementation.
      - name: Database Design
        description: Model database schemas with ER diagrams and generate DDL scripts for multiple databases.
      - name: Model-Driven Development
        description: Use models as the primary artifact for generating code, tests, and documentation.
  - type: Integrations
    data:
      - name: Jira
        description: Integrate with Atlassian Jira for requirements traceability and issue tracking.
      - name: Azure DevOps
        description: Connect to Azure DevOps for work item synchronization and version control.
      - name: Git
        description: Version control model packages with Git repositories.
      - name: Eclipse
        description: Integrate with Eclipse IDE for model-driven Java development.
      - name: Visual Studio
        description: Integrate with Microsoft Visual Studio for .NET development workflows.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
