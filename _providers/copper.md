---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Copper Agentic Access
  operation_count: 31
  slug: copper-agentic-access
  summary_line: 31 operations · 25 acting
api_count: 7
apis:
- description: Activity log entries
  name: Copper Activities API
  slug: copper-activities-api
- description: Company records management
  name: Copper Companies API
  slug: copper-companies-api
- description: Lead records and conversion
  name: Copper Leads API
  slug: copper-leads-api
- description: Sales opportunity pipelines
  name: Copper Opportunities API
  slug: copper-opportunities-api
- description: People (contacts) management
  name: Copper People API
  slug: copper-people-api
- description: Task records management
  name: Copper Tasks API
  slug: copper-tasks-api
- description: Event subscription webhooks
  name: Copper Webhooks API
  slug: copper-webhooks-api
artifact_total: 65
asyncapis:
- description: AsyncAPI definition for the Copper CRM webhook surface. Copper webhooks are HTTP POST deliveries from Copper to a subscriber-defined `target` URL that was registered via the Copper Developer API (`POS
  name: Copper CRM Webhooks
  slug: copper-webhooks-asyncapi
collections:
- collection_type: postman
  name: Copper Developer Activities API
  slug: postman-copper-activities-api
- collection_type: postman
  name: Copper Developer Activities Companies API
  slug: postman-copper-companies-api
- collection_type: postman
  name: Copper Developer Activities Leads API
  slug: postman-copper-leads-api
- collection_type: postman
  name: Copper Developer Activities Opportunities API
  slug: postman-copper-opportunities-api
- collection_type: postman
  name: Copper Developer Activities People API
  slug: postman-copper-people-api
- collection_type: postman
  name: Copper Developer Activities Tasks API
  slug: postman-copper-tasks-api
- collection_type: postman
  name: Copper Developer Activities Webhooks API
  slug: postman-copper-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Copper Developer Activities API
  slug: open-copper-activities-api
- collection_type: open
  name: Copper Developer Activities Companies API
  slug: open-copper-companies-api
- collection_type: open
  name: Copper Developer API
  slug: open-copper-developer-api
- collection_type: open
  name: Copper Developer Activities Leads API
  slug: open-copper-leads-api
- collection_type: open
  name: Copper Developer Activities Opportunities API
  slug: open-copper-opportunities-api
- collection_type: open
  name: Copper Developer Activities People API
  slug: open-copper-people-api
- collection_type: open
  name: Copper Developer Activities Tasks API
  slug: open-copper-tasks-api
- collection_type: open
  name: Copper Developer Activities Webhooks API
  slug: open-copper-webhooks-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/copper/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/copper-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/copper-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/copper-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/copper-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ProsperWorks
- group: company
  title: ''
  type: Website
  url: https://www.copper.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.copper.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.copper.com/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.copper.com/introduction/requests.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.copper.com/introduction/quick-start.html
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.copper.com/introduction/requests.html
- group: design
  title: ''
  type: ErrorCodes
  url: https://developer.copper.com/introduction/responses.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.copper.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.copper.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.copper.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.copper.com/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.copper.com/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/copperinc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/copperinc/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/CopperCRM
created: '2025-01-07'
description: Copper is a CRM platform built natively for Google Workspace, designed to help teams cultivate enduring client relationships through purposeful collaboration. Copper offers a RESTful Developer API providing programmatic access to People, Companies, Leads, Opportunities, Projects, Tasks, Activities, Webhooks, and related resources for CRM integration and automation.
features:
- 'Starter $9/mo: 1K contacts, Google Workspace integration'
- 'Basic $23/mo: 2,500 contacts, pipelines, project management'
- 'Professional $59/mo: 15K contacts, workflow automation, bulk email'
- 'Business $99/mo: unlimited contacts, custom reports, multi-currency'
- Native Google Workspace integration (Gmail, Calendar, Drive, Docs)
- REST API at api.copper.com/developer_api/v1
- Default 600 req/min, 10 req/sec
- OAuth 2.0 + API keys
- Webhooks for record/activity events
- Pipelines and opportunity stages
- Lead scoring (Professional+)
- Workflow automation (Professional+)
- Bulk email (Professional+)
- Email templates and tracking
- Project Management module
- Mobile apps (iOS + Android)
finops:
- name: Copper Finops
  service_category: CRM
  slug: copper-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/copper.png
json_schemas:
- name: Activity
  property_count: 10
  slug: copper-activity
- name: Address
  property_count: 5
  slug: copper-address
- name: Company
  property_count: 14
  slug: copper-company
- name: CompanySearchRequest
  property_count: 6
  slug: copper-companysearchrequest
- name: CustomFieldValue
  property_count: 2
  slug: copper-customfieldvalue
- name: Error
  property_count: 2
  slug: copper-error
- name: Lead
  property_count: 16
  slug: copper-lead
- name: LeadSearchRequest
  property_count: 7
  slug: copper-leadsearchrequest
- name: Opportunity
  property_count: 18
  slug: copper-opportunity
- name: PeopleSearchRequest
  property_count: 8
  slug: copper-peoplesearchrequest
- name: Person
  property_count: 21
  slug: copper-person
- name: Task
  property_count: 12
  slug: copper-task
- name: Webhook
  property_count: 5
  slug: copper-webhook
json_structures:
- name: Copper Structure
  property_count: 0
  slug: copper-structure
jsonld:
- class_count: 44
  name: Copper Context
  property_count: 0
  slug: copper-context
layout: provider
modified: '2026-05-30'
name: Copper
nav: Providers
network: true
overview: 'Copper publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Companies API, Leads API, and 4 more. Tagged areas include Activities, Companies, Contact Relationship Management, Contacts, and CRM.


  The Copper catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Copper''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, YouTube channel, and 15 more developer resources.'
plans:
- name: Copper Plans Pricing
  plan_count: 4
  slug: copper-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 2
  name: Copper Rate Limits
  slug: copper-rate-limits
rules:
- name: Copper API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: copper-asyncapi-spectral-rules
- name: Copper API Rules
  rule_count: 14
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 7
  slug: copper-developer-api-rules
- name: Copper API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: copper-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.4
  delta: 0.0
  facets:
    commercial_clarity: 55.3
    contract_quality: 69.3
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 26.3
  previous_composite: 53.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/copper/refs/heads/main/screenshots/copper-2026-06-20T175018.png
security:
- kind: authentication
  name: Copper Authentication
  slug: copper-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Copper Domain Security
  slug: copper-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Copper Trust Center
  slug: copper-trust-center
  summary_line: HIPAA, FedRAMP, GDPR
slug: copper
tags:
- Activities
- Companies
- Contact Relationship Management
- Contacts
- CRM
- Customer Relationship Management
- Google Workspace
- Leads
- Opportunities
- People
- Projects
- Sales
- Tasks
website: https://www.copper.com
---
