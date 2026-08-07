---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 4
apis:
- description: COM-based Automation Interface providing programmatic access to Enterprise Architect repositories, models, packages, elements, diagrams, connectors, attributes, and tagged values. Supports creating, r
  name: Enterprise Architect Automation Interface
  slug: automation-interface
- description: Framework for building custom add-ins that extend Enterprise Architect with new functionality. Add-ins can respond to application events, add custom menu items, and integrate with external systems usi
  name: Enterprise Architect Add-In Framework
  slug: add-in-framework
- description: Built-in scripting engine supporting JavaScript, JScript, and VBScript for automating tasks within Enterprise Architect. Scripts can access the full automation interface to manipulate models, generate
  name: Enterprise Architect Scripting
  slug: scripting
- description: HTTP-based API provided by the Sparx Systems Pro Cloud Server for remote access to Enterprise Architect repositories. Enables integration with web-based clients, third-party tools, and automation syst
  name: Pro Cloud Server API
  slug: pro-cloud-server-api
artifact_total: 26
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sparx-enterprise-architect-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://sparxsystems.com/enterprise_architect_user_guide/17.0/
- group: start
  title: ''
  type: GettingStarted
  url: https://sparxsystems.com/enterprise_architect_user_guide/17.0/getting_started.htm
- group: commercial
  title: ''
  type: Pricing
  url: https://sparxsystems.com/products/ea/pricing.html
- group: operate
  title: ''
  type: Support
  url: https://sparxsystems.com/support/
- group: operate
  title: ''
  type: FAQ
  url: https://sparxsystems.com/resources/faq/
- group: learn
  title: ''
  type: Training
  url: https://sparxsystems.com/training/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://sparxsystems.com/products/ea/release_notes.html
- group: company
  title: ''
  type: Blog
  url: https://sparxsystems.com/resources/blog/
- group: other
  title: ''
  type: X
  url: https://x.com/SparxSystems
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sparx-systems/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/SparxSystems
created: '2026-03-16'
description: Sparx Enterprise Architect is a comprehensive modeling, design, and management platform for enterprise architecture, software engineering, and systems engineering. It provides automation APIs including a COM Automation Interface, Add-In Framework, and scripting capabilities for programmatic access to models, diagrams, elements, connectors, and repository management.
features:
- description: Comprehensive support for all 14 UML 2.5 diagram types for software and systems design.
  name: UML Modeling
- description: Native ArchiMate 3.2 modeling for enterprise architecture frameworks.
  name: ArchiMate Support
- description: Business process modeling with BPMN 2.0 for workflow and process documentation.
  name: BPMN Process Modeling
- description: Generate source code in C++, Java, C#, Python, PHP, and other languages from UML models.
  name: Code Generation
- description: Import existing codebases to create UML models from source code automatically.
  name: Reverse Engineering
- description: Execute and simulate state machines and activity diagrams for validation.
  name: Model Simulation
- description: Generate rich documentation from models in RTF, HTML, PDF, and DOCX formats.
  name: Document Generation
- description: Multi-user repository access with role-based security and version control integration.
  name: Team Collaboration
finops:
- name: Sparx Enterprise Architect Finops
  service_category: API
  slug: sparx-enterprise-architect-finops
image: /assets/icons/sparx-enterprise-architect.png
integrations:
- description: Integrate with Atlassian Jira for requirements traceability and issue tracking.
  name: Jira
- description: Connect to Azure DevOps for work item synchronization and version control.
  name: Azure DevOps
- description: Version control model packages with Git repositories.
  name: Git
- description: Integrate with Eclipse IDE for model-driven Java development.
  name: Eclipse
- description: Integrate with Microsoft Visual Studio for .NET development workflows.
  name: Visual Studio
layout: provider
modified: '2026-04-18'
name: Sparx Enterprise Architect
nav: Providers
network: true
overview: 'Sparx Enterprise Architect publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Enterprise Architecture, Modeling, Software Engineering, Systems Engineering, and UML.


  Sparx Enterprise Architect''s developer surface includes documentation, getting-started guide, pricing, support, FAQ, training material, release notes, and 5 more developer resources.'
plans:
- name: Sparx Enterprise Architect Plans Pricing
  plan_count: 3
  slug: sparx-enterprise-architect-plans-pricing
random_paper: 89
rate_limits:
- limit_count: 5
  name: Sparx Enterprise Architect Rate Limits
  slug: sparx-enterprise-architect-rate-limits
score:
  band: emerging
  composite: 27.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 27.9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sparx-enterprise-architect/refs/heads/main/screenshots/sparx-enterprise-architect-2026-06-20T194248.png
security:
- kind: domain-security
  name: Sparx Enterprise Architect Domain Security
  slug: sparx-enterprise-architect-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sparx-enterprise-architect
tags:
- Enterprise Architecture
- Modeling
- Software Engineering
- Systems Engineering
- UML
use_cases:
- description: Define and maintain enterprise architecture models aligned with TOGAF, Zachman, or ArchiMate frameworks.
  name: Enterprise Architecture Governance
- description: Create detailed software designs with UML class, sequence, and component diagrams.
  name: Software Design Documentation
- description: Capture, trace, and manage requirements from stakeholder needs through to implementation.
  name: Requirements Management
- description: Model database schemas with ER diagrams and generate DDL scripts for multiple databases.
  name: Database Design
- description: Use models as the primary artifact for generating code, tests, and documentation.
  name: Model-Driven Development
---
