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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.8
  scored_at: '2026-08-19'
api_count: 16
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
- description: Operations on Account business objects including customer and prospect organizations with associated contacts, opportunities, and addresses
  name: Oracle Siebel Accounts API
  slug: oracle-siebel-accounts-api
- description: Operations on Activity business objects for managing tasks, appointments, call logs, and other scheduled items
  name: Oracle Siebel Activities API
  slug: oracle-siebel-activities-api
- description: Invocation of Siebel business services and their methods for executing server-side business logic including integration object operations
  name: Oracle Siebel Business Services API
  slug: oracle-siebel-business-services-api
- description: Operations on Contact business objects representing individual people associated with accounts and organizations
  name: Oracle Siebel Contacts API
  slug: oracle-siebel-contacts-api
- description: Discovery endpoints that return OpenAPI-compatible metadata describing available resources, fields, and operations
  name: Oracle Siebel Metadata API
  slug: oracle-siebel-metadata-api
- description: Operations on Opportunity business objects for managing sales pipeline, deals, and revenue forecasting
  name: Oracle Siebel Opportunities API
  slug: oracle-siebel-opportunities-api
- description: Operations on Order business objects for managing sales orders, order line items, and order fulfillment
  name: Oracle Siebel Orders API
  slug: oracle-siebel-orders-api
- description: Operations on Product business objects for product catalog management including pricing and product hierarchies
  name: Oracle Siebel Products API
  slug: oracle-siebel-products-api
- description: Access to Siebel repository objects including applets, views, business components, and other metadata through workspace-based paths
  name: Oracle Siebel Repository API
  slug: oracle-siebel-repository-api
- description: Operations on Service Request business objects for customer service case management and issue tracking
  name: Oracle Siebel Service Requests API
  slug: oracle-siebel-service-requests-api
artifact_total: 41
asyncapis:
- description: Event-driven integration framework enabling real-time communication between Oracle Siebel CRM and external systems using Apache Kafka. The Event Pub/Sub system supports publishing events from Siebel t
  name: Oracle Siebel CRM Event Pub/Sub
  slug: oracle-siebel-event-pubsub-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Oracle Siebel REST Accounts API
  slug: open-oracle-siebel-accounts-api
- collection_type: open
  name: Oracle Siebel REST Activities API
  slug: open-oracle-siebel-activities-api
- collection_type: open
  name: Oracle Siebel REST Business Services API
  slug: open-oracle-siebel-business-services-api
- collection_type: open
  name: Oracle Siebel REST Contacts API
  slug: open-oracle-siebel-contacts-api
- collection_type: open
  name: Oracle Siebel REST Metadata API
  slug: open-oracle-siebel-metadata-api
- collection_type: open
  name: Oracle Siebel REST Opportunities API
  slug: open-oracle-siebel-opportunities-api
- collection_type: open
  name: Oracle Siebel REST Orders API
  slug: open-oracle-siebel-orders-api
- collection_type: open
  name: Oracle Siebel REST Products API
  slug: open-oracle-siebel-products-api
- collection_type: open
  name: Oracle Siebel REST Repository API
  slug: open-oracle-siebel-repository-api
- collection_type: open
  name: Oracle Siebel REST Service Requests API
  slug: open-oracle-siebel-service-requests-api
common:
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/oracle-siebel-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oracle-siebel-authentication.yml
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
- group: build
  title: ''
  type: Packages
  url: packages/oracle-siebel-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/oracle-siebel-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/oracle-siebel-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oracle-siebel-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/oracle-siebel-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/oracle-siebel-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/oracle-siebel-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/oracle-siebel-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/oracle-siebel-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/oracle-siebel-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/oracle-siebel-cli.yml
- group: design
  title: ''
  type: Components
  url: components/oracle-siebel-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/oracle-siebel-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/oracle-siebel-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/oracle-siebel-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/oracle-siebel-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/oracle-siebel-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/oracle-siebel-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/oracle-siebel-finops.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.oracle.com/cd/E95904_01/books/RestAPI/overview-of-using-the-siebel-rest-api.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oracle.com/us/corporate/pricing/price-lists/index.html
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
mcp_servers:
- description: ''
  name: oracle-siebel-mcp.yml
  slug: oracle-siebel-mcpyml
modified: '2026-08-13'
name: Oracle Siebel
nav: Providers
network: true
overview: 'Oracle Siebel publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Event Pub/Sub API, Accounts API, Activities API, and 8 more. Tagged areas include CRM, Customer Management, Enterprise Software, Marketing Automation, and Oracle.


  The Oracle Siebel catalog on APIs.io includes 1 event-driven AsyncAPI specification and 2 Spectral governance rulesets.


  Oracle Siebel''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, engineering blog, changelog, and 36 more developer resources.'
plans:
- name: Oracle Siebel Plans Pricing
  plan_count: 3
  slug: oracle-siebel-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Oracle Siebel Rate Limits
  slug: oracle-siebel-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Oracle Siebel API Rules
  rule_count: 9
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 9
  slug: oracle-siebel-asyncapi-spectral-rules
- effective_rule_count: 4
  extends: []
  name: Oracle Siebel API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: oracle-siebel-jsonschema-spectral-rules
scopes:
- name: Oracle Siebel Scopes
  scope_count: 0
  slug: oracle-siebel-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 68.0
  delta: -4.3
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 28.0
    contract_quality: 68.1
    developer_ergonomics: 70.8
    discoverability: 72.2
    governance: 28.0
    operational_transparency: 84.2
  previous_composite: 72.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/screenshots/oracle-siebel-2026-06-20T191147.png
security:
- kind: authentication
  name: Oracle Siebel Authentication
  slug: oracle-siebel-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Oracle Siebel Domain Security
  slug: oracle-siebel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Oracle Siebel Vulnerability Disclosure
  slug: oracle-siebel-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Oracle Siebel Trust Center
  slug: oracle-siebel-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, PCI DSS, HIPAA, FedRAMP, GDPR, Cyber Essentials Plus, HMG Cloud Security Principles
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
