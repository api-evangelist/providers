---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 27
  human_in_the_loop: 1
  name: Oracle Apex Agentic Access
  operation_count: 59
  slug: oracle-apex-agentic-access
  summary_line: 59 operations · 27 acting · 1 human-in-the-loop
api_count: 21
apis:
- description: RESTful API for Oracle APEX applications enabling data access and manipulation through REST endpoints.
  name: Oracle APEX REST Data Services API
  slug: oracle-apex-rest-data-services-api
- description: API for accessing SQL Workshop functionality programmatically.
  name: Oracle APEX SQL Workshop API
  slug: oracle-apex-sql-workshop-api
- description: API for managing APEX applications, pages, and components.
  name: Oracle APEX Application API
  slug: oracle-apex-application-api
- description: REST API framework integrated with APEX for creating RESTful services including modules, templates, handlers, privileges, roles, OAuth clients, and AutoREST-enabled objects.
  name: Oracle REST Data Services (ORDS) API
  slug: oracle-rest-data-services-ords-api
- description: REST APIs for provisioning and managing Oracle APEX instances in Oracle Cloud Infrastructure, including workspace and application lifecycle management.
  name: Oracle APEX Cloud REST API
  slug: oracle-apex-cloud-rest-api
- description: PL/SQL and REST APIs for exporting and importing APEX applications, workspaces, and components using APEX_EXPORT and related packages.
  name: Oracle APEX Export and Import API
  slug: oracle-apex-export-and-import-api
- description: PL/SQL APIs for managing approvals, human tasks, and workflows in APEX applications using the APEX_APPROVAL and workflow packages.
  name: Oracle APEX Approval and Workflow API
  slug: oracle-apex-approval-and-workflow-api
- description: The APEX_UTIL PL/SQL package provides utility functions for user management, authentication, session management, and other common APEX operations.
  name: Oracle APEX Utility API
  slug: oracle-apex-utility-api
- description: APIs for integrating generative AI capabilities into APEX applications, including chat, text generation, and vector embeddings introduced in APEX 24.2.
  name: Oracle APEX Generative AI API
  slug: oracle-apex-generative-ai-api
- description: REST API for Oracle Database management and monitoring operations through ORDS, including pluggable database management, data export, and performance monitoring.
  name: Oracle ORDS Database API
  slug: oracle-ords-database-api
- description: REST Administration API enabling APEX instance administrators to perform administrative functions over REST and HTTP protocols for machine-to-machine communication.
  name: Oracle APEX REST Administration API
  slug: oracle-apex-rest-administration-api
- description: AutoREST object management. AutoREST enables automatic REST access to database tables and views.
  name: Oracle APEX AutoREST API
  slug: oracle-apex-autorest-api
- description: REST template handler management. A handler implements an HTTP method on a template with source code.
  name: Oracle APEX Handlers API
  slug: oracle-apex-handlers-api
- description: REST module management. A module is a container for one or more templates with an associated base path.
  name: Oracle APEX Modules API
  slug: oracle-apex-modules-api
- description: ORDS OAuth client management. OAuth clients enable third-party applications to access protected resources.
  name: Oracle APEX OAuth Clients API
  slug: oracle-apex-oauth-clients-api
- description: ORDS schema overview and REST object summaries.
  name: Oracle APEX Overview API
  slug: oracle-apex-overview-api
- description: REST handler parameter management. Parameters define input bindings for handlers.
  name: Oracle APEX Parameters API
  slug: oracle-apex-parameters-api
- description: ORDS privilege management. Privileges control access to REST modules and URL patterns.
  name: Oracle APEX Privileges API
  slug: oracle-apex-privileges-api
- description: ORDS configuration property management.
  name: Oracle APEX Properties API
  slug: oracle-apex-properties-api
- description: ORDS role management. Roles group privileges for assignment to users and OAuth clients.
  name: Oracle APEX Roles API
  slug: oracle-apex-roles-api
- description: REST module template management. A template defines a URI pattern within a module for routing requests.
  name: Oracle APEX Templates API
  slug: oracle-apex-templates-api
artifact_total: 61
collections:
- collection_type: open
  name: Oracle REST Data Services (ORDS) REST API
  slug: open-ords-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-apex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-apex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oracle-apex-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/oracle-apex-scopes.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/database/oracle/apex/
- group: company
  title: ''
  type: Blog
  url: https://blogs.oracle.com/apex/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle/apex
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/OracleAPEX
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oracle.com/application-development/apex/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://apex.oracle.com/en/learn/getting-started/
- group: learn
  title: ''
  type: Tutorials
  url: https://apex.oracle.com/en/learn/tutorials/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://apex.oracle.com/en/learn/documentation/release-notes/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.oracle.com/en/database/oracle/apex/24.2/api-references.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/privacy-policy/
- group: operate
  title: ''
  type: FAQ
  url: https://www.oracle.com/tools/technologies/faq-rest-data-services.html
- group: operate
  title: ''
  type: Support
  url: https://apex.oracle.com/community
- group: start
  title: ''
  type: Signup
  url: https://docs.oracle.com/en/cloud/paas/apex/gsadd/sign-up-for-apex-service.html
created: '2024-01-01'
description: Oracle Application Express (APEX) is a low-code development platform that enables you to build scalable, secure enterprise apps with world-class features.
features:
- description: Visual drag-and-drop application builder for creating enterprise web applications without extensive coding.
  name: Low-Code Application Development
- description: Built-in ORDS integration for exposing database objects and custom logic as REST APIs.
  name: RESTful Web Services
- description: Native AI capabilities including chat, text generation, and vector embeddings for intelligent applications.
  name: Generative AI Integration
- description: Built-in workflow engine with human task management and approval chains for business process automation.
  name: Workflow and Approvals
- description: Build installable progressive web applications with offline capabilities and native-like user experience.
  name: Progressive Web Apps
- description: Seamless deployment and management on Oracle Cloud Infrastructure with automated provisioning.
  name: Oracle Cloud Integration
finops:
- name: Oracle Apex Finops
  service_category: Application Development / Low-Code
  slug: oracle-apex-finops
image: /assets/icons/oracle-apex.png
integrations:
- description: Native integration with Oracle Database for data access, PL/SQL execution, and database object management.
  name: Oracle Database
- description: Deploy APEX applications on OCI with autonomous database and cloud-native infrastructure services.
  name: Oracle Cloud Infrastructure
- description: ORDS provides the REST API layer for APEX applications and database services.
  name: Oracle REST Data Services
- description: Single sign-on and identity management integration for enterprise authentication.
  name: Oracle Identity Cloud
- description: LDAP-based authentication and user synchronization with Active Directory environments.
  name: Microsoft Active Directory
json_schemas:
- name: Oracle APEX Application
  property_count: 27
  slug: oracle-apex-application
- name: AutoRestEnable
  property_count: 4
  slug: oracle-apex-autorestenable
- name: HandlerCreate
  property_count: 8
  slug: oracle-apex-handlercreate
- name: ItemsCollection
  property_count: 6
  slug: oracle-apex-itemscollection
- name: LinkRelation
  property_count: 2
  slug: oracle-apex-linkrelation
- name: ModuleCreate
  property_count: 7
  slug: oracle-apex-modulecreate
- name: OAuthClientCreate
  property_count: 8
  slug: oracle-apex-oauthclientcreate
- name: ParameterCreate
  property_count: 6
  slug: oracle-apex-parametercreate
- name: PrivilegeCreate
  property_count: 8
  slug: oracle-apex-privilegecreate
- name: ResourceItem
  property_count: 1
  slug: oracle-apex-resourceitem
- name: RoleCreate
  property_count: 2
  slug: oracle-apex-rolecreate
- name: TemplateCreate
  property_count: 7
  slug: oracle-apex-templatecreate
- name: TemplateUpdate
  property_count: 5
  slug: oracle-apex-templateupdate
json_structures:
- name: Oracle Apex Structure
  property_count: 0
  slug: oracle-apex-structure
jsonld:
- class_count: 5
  name: Oracle Apex Context
  property_count: 21
  slug: oracle-apex-context
layout: provider
modified: '2026-05-19'
name: Oracle APEX
nav: Providers
network: true
overview: 'Oracle APEX publishes 10 APIs on the [APIs.io](https://apis.io/) network, including AutoREST API, Handlers API, Modules API, and 7 more. Tagged areas include APEX, Cloud, Database, Development Platform, and Enterprise.


  The Oracle APEX catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Oracle APEX''s developer surface includes authentication, documentation, engineering blog, YouTube channel, pricing, getting-started guide, release notes, and 11 more developer resources.'
plans:
- name: Oracle Apex Plans Pricing
  plan_count: 3
  slug: oracle-apex-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 4
  name: Oracle Apex Rate Limits
  slug: oracle-apex-rate-limits
rules:
- name: Oracle APEX API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: oracle-apex-jsonschema-spectral-rules
scopes:
- name: Oracle Apex Scopes
  scope_count: 0
  slug: oracle-apex-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.7
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 70.3
    developer_ergonomics: 43.5
    discoverability: 55.0
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 61.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-apex/refs/heads/main/screenshots/oracle-apex-2026-06-20T191118.png
security:
- kind: authentication
  name: Oracle Apex Authentication
  slug: oracle-apex-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Oracle Apex Domain Security
  slug: oracle-apex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oracle-apex
tags:
- APEX
- Cloud
- Database
- Development Platform
- Enterprise
- Generative AI
- Low-Code
- Oracle
- ORDS
- PL/SQL
- REST API
- Web Applications
- Workflow
use_cases:
- description: Rapidly build and deploy internal enterprise applications for HR, finance, and operations.
  name: Enterprise Application Development
- description: Expose Oracle Database tables and views as RESTful services using ORDS AutoREST.
  name: Database REST API Creation
- description: Automate business approval processes and multi-step workflows with the APEX workflow engine.
  name: Workflow Automation
- description: Build self-service data entry and management portals for business users with built-in validation.
  name: Data Management Portals
- description: Integrate generative AI features into business applications for intelligent data processing and insights.
  name: AI-Enhanced Applications
---
