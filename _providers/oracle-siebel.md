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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.3
  scored_at: '2026-10-03'
api_count: 1
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
- baseURL: https://{siebel-server}/siebel/v1.0
  baseurl_source: declared
  description: Operations on Account business objects including customer and prospect organizations with associated contacts, opportunities, and addresses
  name: Oracle Siebel Accounts API
  phrasing_intents:
  - id: listAccounts
    intent: List accounts
    question: How can I pull a list of all customer accounts out of Siebel CRM?
  - id: createAccount
    intent: Create a new account
    question: How do I add a brand-new customer account to the CRM?
  - id: getAccount
    intent: Get one account by its ID
    question: How do I look up a single account when I already have its row ID?
  - id: upsertAccount
    intent: Update or insert an account by ID
    question: How do I change the status of an existing account?
  - id: deleteAccount
    intent: Delete an account
    question: How do I permanently remove an account from the Siebel database?
  - id: listAccountContacts
    intent: List the contacts under an account
    question: Who are the people linked to a particular customer account?
  - id: upsertAccountContact
    intent: Add or update a contact under an account
    question: How do I attach a new person to an existing customer account?
  - id: listAccountOpportunities
    intent: List the opportunities under an account
    question: What deals are open for a specific customer account?
  phrasing_ops: 8
  slug: oracle-siebel-accounts-api
- baseURL: https://{siebel-server}/siebel/v1.0
  baseurl_source: declared
  description: Operations on Activity business objects for managing tasks, appointments, call logs, and other scheduled items
  name: Oracle Siebel Activities API
  phrasing_intents:
  - id: listActivities
    intent: List activities
    question: How can I see all the tasks, calls and appointments logged in Siebel?
  - id: createActivity
    intent: Log a new activity
    question: How do I log a new call or task in the CRM?
  - id: getActivity
    intent: Get one activity by its ID
    question: How do I pull up the details of one specific activity?
  - id: upsertActivity
    intent: Update or insert an activity by ID
    question: How do I mark an existing activity as done?
  - id: deleteActivity
    intent: Delete an activity
    question: How do I remove an activity that was logged by mistake?
  phrasing_ops: 5
  slug: oracle-siebel-activities-api
- baseURL: https://{siebel-server}/siebel/v1.0
  baseurl_source: declared
  description: Invocation of Siebel business services and their methods for executing server-side business logic including integration object operations
  name: Oracle Siebel Business Services API
  phrasing_intents:
  - id: invokeBusinessService
    intent: Run a business service method
    question: How do I call a Siebel business service method over REST?
  - id: describeBusinessServices
    intent: List all business services and their methods
    question: Which business services can I call on this Siebel server?
  - id: describeBusinessService
    intent: Describe one business service
    question: What input and output arguments does a particular business service method expect?
  phrasing_ops: 3
  slug: oracle-siebel-business-services-api
- baseURL: https://{siebel-server}/siebel/v1.0
  baseurl_source: declared
  description: Operations on Contact business objects representing individual people associated with accounts and organizations
  name: Oracle Siebel Contacts API
  phrasing_intents:
  - id: listAccountContacts
    intent: List the contacts under an account
    question: Who are the people linked to a particular customer account?
  - id: upsertAccountContact
    intent: Add or update a contact under an account
    question: How do I attach a new person to an existing customer account?
  - id: listContacts
    intent: List contacts
    question: How can I export every contact across all accounts in the CRM?
  - id: createContact
    intent: Create a standalone contact
    question: How do I add a new person to the contact list without picking an account first?
  - id: getContact
    intent: Get one contact by its ID
    question: How do I retrieve a single contact when I know its row ID?
  - id: upsertContact
    intent: Update or insert a contact by ID
    question: How do I update a contact's job title after they get promoted?
  - id: deleteContact
    intent: Delete a contact
    question: How do I delete a person from the contacts list entirely?
  phrasing_ops: 7
  slug: oracle-siebel-contacts-api
- baseURL: https://{siebel-server}/siebel/v1.0
  baseurl_source: declared
  description: Discovery endpoints that return OpenAPI-compatible metadata describing available resources, fields, and operations
  name: Oracle Siebel Metadata API
  phrasing_intents:
  - id: describeBusinessServices
    intent: List all business services and their methods
    question: Which business services can I call on this Siebel server?
  - id: describeBusinessService
    intent: Describe one business service
    question: What input and output arguments does a particular business service method expect?
  - id: describeWorkspace
    intent: List repository objects in a workspace
    question: Which applets, views and other repository objects exist in a workspace?
  - id: describeBusinessComponent
    intent: Describe a business component's fields
    question: What fields and data types does a business component have?
  phrasing_ops: 4
  slug: oracle-siebel-metadata-api
- baseURL: https://{siebel-server}/siebel/v1.0
  baseurl_source: declared
  description: Operations on Opportunity business objects for managing sales pipeline, deals, and revenue forecasting
  name: Oracle Siebel Opportunities API
  phrasing_intents:
  - id: listAccountOpportunities
    intent: List the opportunities under an account
    question: What deals are open for a specific customer account?
  - id: listOpportunities
    intent: List opportunities
    question: How can I see every sales opportunity in the pipeline, across all accounts?
  - id: createOpportunity
    intent: Create a new opportunity
    question: How do I open a new sales opportunity in the CRM?
  - id: getOpportunity
    intent: Get one opportunity by its ID
    question: How do I look up a single deal by its row ID?
  - id: upsertOpportunity
    intent: Update or insert an opportunity by ID
    question: How do I move an existing deal to the next sales stage?
  - id: deleteOpportunity
    intent: Delete an opportunity
    question: How do I remove a dead deal from the pipeline permanently?
  phrasing_ops: 6
  slug: oracle-siebel-opportunities-api
- baseURL: https://{siebel-server}/siebel/v1.0
  baseurl_source: declared
  description: Operations on Order business objects for managing sales orders, order line items, and order fulfillment
  name: Oracle Siebel Orders API
  phrasing_intents:
  - id: listOrders
    intent: List sales orders
    question: How can I pull the list of orders from Siebel order entry?
  phrasing_ops: 1
  slug: oracle-siebel-orders-api
- baseURL: https://{siebel-server}/siebel/v1.0
  baseurl_source: declared
  description: Operations on Product business objects for product catalog management including pricing and product hierarchies
  name: Oracle Siebel Products API
  phrasing_intents:
  - id: listProducts
    intent: List products in the catalog
    question: How can I see every product in the Siebel product catalog?
  phrasing_ops: 1
  slug: oracle-siebel-products-api
- baseURL: https://{siebel-server}/siebel/v1.0
  baseurl_source: declared
  description: Access to Siebel repository objects including applets, views, business components, and other metadata through workspace-based paths
  name: Oracle Siebel Repository API
  phrasing_intents:
  - id: describeWorkspace
    intent: List repository objects in a workspace
    question: Which applets, views and other repository objects exist in a workspace?
  - id: getRepositoryObject
    intent: Get a repository object's definition
    question: How do I read the definition of one applet or view in a workspace?
  phrasing_ops: 2
  slug: oracle-siebel-repository-api
- baseURL: https://{siebel-server}/siebel/v1.0
  baseurl_source: declared
  description: Operations on Service Request business objects for customer service case management and issue tracking
  name: Oracle Siebel Service Requests API
  phrasing_intents:
  - id: listServiceRequests
    intent: List service requests
    question: How can I see all open customer support tickets?
  - id: createServiceRequest
    intent: Open a new service request
    question: How do I open a new support ticket for a customer?
  - id: getServiceRequest
    intent: Get one service request by its ID
    question: How do I check the details of a specific support ticket?
  - id: upsertServiceRequest
    intent: Update or insert a service request by ID
    question: How do I close out or change the status of an existing ticket?
  - id: deleteServiceRequest
    intent: Delete a service request
    question: How do I delete a duplicate support ticket?
  phrasing_ops: 5
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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/capabilities/oracle-siebel-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/oracle-siebel-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/OracleSiebel/ConfiguringSiebel/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/OracleSiebel/ConfiguringSiebel/releases
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/oracle/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/scopes/oracle-siebel-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/oracle-siebel-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/authentication/oracle-siebel-authentication.yml
  title: ''
  type: Authentication
  url: authentication/oracle-siebel-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/oracle-siebel/overview
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/security/oracle-siebel-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/packages/oracle-siebel-packages.yml
  title: ''
  type: Packages
  url: packages/oracle-siebel-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/mcp/oracle-siebel-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/oracle-siebel-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/mcp/oracle-siebel-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/oracle-siebel-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/llms/oracle-siebel-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/oracle-siebel-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/conventions/oracle-siebel-conventions.yml
  title: ''
  type: Conventions
  url: conventions/oracle-siebel-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/errors/oracle-siebel-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/oracle-siebel-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/data-model/oracle-siebel-data-model.yml
  title: ''
  type: DataModel
  url: data-model/oracle-siebel-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/lifecycle/oracle-siebel-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/oracle-siebel-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/lifecycle/oracle-siebel-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/oracle-siebel-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/changelog/oracle-siebel-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/oracle-siebel-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/cli/oracle-siebel-cli.yml
  title: ''
  type: CLI
  url: cli/oracle-siebel-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/components/oracle-siebel-components.yml
  title: ''
  type: Components
  url: components/oracle-siebel-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/conformance/oracle-siebel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/oracle-siebel-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/security/oracle-siebel-trust-center.yml
  title: ''
  type: Compliance
  url: security/oracle-siebel-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/security/oracle-siebel-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/oracle-siebel-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/security/oracle-siebel-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/oracle-siebel-vulnerability-disclosure.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/plans/oracle-siebel-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/oracle-siebel-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/rate-limits/oracle-siebel-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/oracle-siebel-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/finops/oracle-siebel-finops.yml
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
  name: Siebel AI Connectors — MCP Servers
  slug: siebel-ai-connectors-mcp-servers
modified: '2026-08-21'
name: Oracle Siebel
nav: Providers
network: true
overview: 'Oracle Siebel publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Event Pub/Sub API, Accounts API, Activities API, and 13 more. Tagged areas include CRM, Customer Management, Enterprise Software, Marketing Automation, and Oracle.


  The Oracle Siebel catalog on APIs.io includes 1 event-driven AsyncAPI specification and 2 Spectral governance rulesets.


  Oracle Siebel''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, engineering blog, changelog, and 40 more developer resources.'
plans:
- name: Oracle Siebel Plans Pricing
  plan_count: 3
  slug: oracle-siebel-plans-pricing
random_paper: 5
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
  composite: 70.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 59.9
    catalog_earned_first_party: 12.0
    catalog_gap: 55.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 60.8
    developer_ergonomics: 67.3
    discoverability: 63.3
    operational_transparency: 84.2
  previous_composite: 70.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 33.3
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
- Real-Time
website: https://www.oracle.com/applications/siebel/
---
