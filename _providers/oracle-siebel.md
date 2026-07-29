---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
api_count: 7
apis:
- description: SOAP-based web services for enterprise integration with Siebel CRM, supporting complex business operations and workflows. Siebel provides both inbound web services for external clients to access Siebe
  name: Oracle Siebel SOAP Web Services
  slug: oracle-siebel-soap-web-services
- description: APIs for creating and consuming custom business services within the Siebel platform for specialized business logic. Business services encapsulate reusable business logic that can be invoked through sc
  name: Oracle Siebel Business Service API
  slug: oracle-siebel-business-service-api
- description: 'Integration services for connecting Siebel with external systems using various protocols and data formats. Siebel EAI provides bidirectional, real-time, and batch integration solutions with pre-built '
  name: Oracle Siebel EAI (Enterprise Application Integration)
  slug: oracle-siebel-eai-enterprise-application-integration
- description: Programmatic interfaces for accessing Siebel business objects, business components, and application objects using Siebel eScript, Siebel Visual Basic, or the Siebel Java Data Bean. The Object Interfac
  name: Oracle Siebel Object Interfaces API
  slug: oracle-siebel-object-interfaces-api
- description: 'Client-side JavaScript API for customizing the Siebel Open UI user interface. The API provides well-defined customization points for styling, layout, and user interface design, allowing developers to '
  name: Oracle Siebel Open UI JavaScript API
  slug: oracle-siebel-open-ui-javascript-api
- description: Event-driven integration framework enabling real-time communication between Siebel CRM and external systems using Apache Kafka. The Event Pub/Sub API supports publishing events from Siebel to Kafka to
  name: Oracle Siebel Event Pub/Sub API
  slug: oracle-siebel-event-pubsub-api
- description: The Siebel Rest API from Oracle Siebel — 0 operation(s) for siebel rest.
  name: Oracle Siebel Siebel Rest API
  slug: oracle-siebel-rest-api
artifact_total: 16
asyncapis:
- description: Event-driven integration framework enabling real-time communication between Oracle Siebel CRM and external systems using Apache Kafka. The Event Pub/Sub system supports publishing events from Siebel t
  name: Oracle Siebel CRM Event Pub/Sub
  slug: oracle-siebel-event-pubsub-asyncapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/oracle-siebel/overview
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-siebel-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://docs.oracle.com/cd/G15000_01/SiebelInfoPortal/
- group: company
  title: ''
  type: Website
  url: https://www.oracle.com/applications/siebel/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/applications/siebel/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/cd/F26413_61/books/FundOUI/index.html
- group: auth
  title: ''
  type: Authentication
  url: https://docs.oracle.com/cd/F26413_26/books/Secur/single-sign-on-authentication.html
- group: auth
  title: ''
  type: Security
  url: https://docs.oracle.com/cd/F26413_26/books/Secur/index.html
- group: operate
  title: ''
  type: Support
  url: https://www.oracle.com/support/premier/software/siebel/
- group: operate
  title: ''
  type: Community
  url: https://community.oracle.com/customerconnect/categories/onprem-siebel-crm
- group: company
  title: ''
  type: Blog
  url: https://blogs.oracle.com/siebelcrm/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.oracle.com/cd/F26413_61/homepage.htm
- group: learn
  title: ''
  type: Training
  url: https://learn.oracle.com/ols/home/38497
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com/
- group: start
  title: ''
  type: Login
  url: https://support.oracle.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OracleSiebel
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OracleSiebel/ConfiguringSiebel
created: '2024-01-01'
description: Oracle Siebel CRM APIs provide programmatic access to customer relationship management functionality including sales, marketing, and service automation capabilities. Siebel CRM offers REST, SOAP, scripting, and event-driven integration interfaces for building integrations with enterprise systems.
finops:
- name: Oracle Siebel Finops
  service_category: CRM
  slug: oracle-siebel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle-siebel.png
json_schemas:
- name: Oracle Siebel CRM Account
  property_count: 22
  slug: oracle-siebel-account
- name: Oracle Siebel CRM Contact
  property_count: 20
  slug: oracle-siebel-contact
layout: provider
modified: '2026-04-28'
name: Oracle Siebel
nav: Providers
network: true
overview: 'Oracle Siebel publishes 1 API on the [APIs.io](https://apis.io/) network: Siebel Rest API. Tagged areas include CRM, Customer Management, Enterprise Software, Marketing Automation, and Oracle.


  The Oracle Siebel catalog on APIs.io includes 1 event-driven AsyncAPI specification and 2 Spectral governance rulesets.


  Oracle Siebel''s developer surface includes developer portal, documentation, getting-started guide, authentication, support, engineering blog, changelog, and 12 more developer resources.'
plans:
- name: Oracle Siebel Plans Pricing
  plan_count: 3
  slug: oracle-siebel-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 3
  name: Oracle Siebel Rate Limits
  slug: oracle-siebel-rate-limits
rules:
- name: Oracle Siebel API Rules
  rule_count: 9
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 9
  slug: oracle-siebel-asyncapi-spectral-rules
- name: Oracle Siebel API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: oracle-siebel-jsonschema-spectral-rules
score:
  band: strong
  composite: 60.6
  delta: -5.3
  facets:
    commercial_clarity: 73.7
    contract_quality: 51.6
    developer_ergonomics: 50.0
    discoverability: 64.8
    governance: 52.1
    operational_transparency: 78.9
  previous_composite: 65.9
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/screenshots/oracle-siebel-2026-06-20T191147.png
security:
- kind: domain-security
  name: Oracle Siebel Domain Security
  slug: oracle-siebel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oracle-siebel
tags:
- CRM
- Customer Management
- Enterprise Software
- Marketing Automation
- Oracle
- Sales Automation
- Service Automation
website: https://www.oracle.com/applications/siebel/
---
