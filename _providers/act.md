---
access_model:
  confidence: high
  label: Public docs, paid access
  onboarding: unknown
  pricing: paid
  public: true
  source:
  - https://www.act.com/developer/
  - https://apimta.act.com/act.web.api/
  - https://www.act.com/pricing/
  - https://www.act.com/trial/act/
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'JSON-based REST API for the Act! CRM database exposing contacts, companies, groups, opportunities, tasks, activity series, calendar, notes, history, documents, attachments, users, teams, preferences, '
  name: Act! Web API
  slug: web-api
artifact_total: 40
asyncapis:
- description: ''
  name: Act Webhooks
  slug: act-webhooks
collections:
- collection_type: open
  name: Act! Web API — ActivitySeries
  slug: open-act-activity-series-api
- collection_type: open
  name: Act! Web API — Analytics
  slug: open-act-analytics-api
- collection_type: open
  name: Act! Web API — Calendar
  slug: open-act-calendar-api
- collection_type: open
  name: Act! Web API — Companies
  slug: open-act-companies-api
- collection_type: open
  name: Act! Web API — Configurations
  slug: open-act-configurations-api
- collection_type: open
  name: Act! Web API — Contacts
  slug: open-act-contacts-api
- collection_type: open
  name: Act! Web API — Cors
  slug: open-act-cors-api
- collection_type: open
  name: Act! Web API — CustomEntities
  slug: open-act-custom-entities-api
- collection_type: open
  name: Act! Web API — Database
  slug: open-act-database-api
- collection_type: open
  name: Act! Web API — DocumentTypes
  slug: open-act-document-types-api
- collection_type: open
  name: Act! Web API — Documents
  slug: open-act-documents-api
- collection_type: open
  name: Act! Web API — Geographics
  slug: open-act-geographics-api
- collection_type: open
  name: Act! Web API — Groups
  slug: open-act-groups-api
- collection_type: open
  name: Act! Web API — History
  slug: open-act-history-api
- collection_type: open
  name: Act! Web API — HistoryTypes
  slug: open-act-history-types-api
- collection_type: open
  name: Act! Web API — Import
  slug: open-act-import-api
- collection_type: open
  name: Act! Web API — MarketingAutomations
  slug: open-act-marketing-automations-api
- collection_type: open
  name: Act! Web API — MetadataInfo
  slug: open-act-metadata-info-api
- collection_type: open
  name: Act! Web API — Notes
  slug: open-act-notes-api
- collection_type: open
  name: Act! Web API — Opportunities
  slug: open-act-opportunities-api
- collection_type: open
  name: Act! Web API — Preferences
  slug: open-act-preferences-api
- collection_type: open
  name: Act! Web API — Products
  slug: open-act-products-api
- collection_type: open
  name: Act! Web API — SecondaryContacts
  slug: open-act-secondary-contacts-api
- collection_type: open
  name: Act! Web API — SupplementalFiles
  slug: open-act-supplemental-files-api
- collection_type: open
  name: Act! Web API — SyncData
  slug: open-act-sync-data-api
- collection_type: open
  name: Act! Web API — System
  slug: open-act-system-api
- collection_type: open
  name: Act! Web API — TaskTypes
  slug: open-act-task-types-api
- collection_type: open
  name: Act! Web API — Tasks
  slug: open-act-tasks-api
- collection_type: open
  name: Act! Web API — Teams
  slug: open-act-teams-api
- collection_type: open
  name: Act! Web API — Users
  slug: open-act-users-api
- collection_type: open
  name: Act! Web API — Webhooks
  slug: open-act-webhooks-api
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/act-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/act-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/act-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/act-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/act-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/act-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/act-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/act-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.act.com/obsolescence-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.act.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/act-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/act-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/act-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/act-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/actsoftware
- group: company
  title: ''
  type: Website
  url: https://www.act.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.act.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://www.act.com/developer/
- group: docs
  title: ''
  type: APIReference
  url: https://apimta.act.com/act.web.api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.act.com/resources/getting-started/act-cloud/
- group: operate
  title: ''
  type: Support
  url: https://support.act.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.act.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Swiftpage
- group: commercial
  title: ''
  type: Pricing
  url: https://www.act.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.act.com/trial/act/
- group: start
  title: ''
  type: Login
  url: https://my.act.com/en-us/myact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.act.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.act.com/legal/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.act.com/blog/
created: '2026-05-11'
description: Act! is a CRM and marketing automation platform built for small and mid-sized businesses, providing contact and activity management, opportunity tracking, email marketing, and pipeline reporting in cloud (Act! Advantage) or on-premises (Act! Premium Desktop) editions. The Act! Web API is a JSON-based REST API that exposes contacts, companies, groups, opportunities, activities, tasks, notes, history, documents and tenant-defined custom entities across 410 operations, with OData v4 query options ($filter, $orderby, $top, $skip, $select, $expand) on collection reads, multipart batching at POST /api/$batch, a webhook registration API, and a published Swagger 2.0 specification. Authentication is a JWT bearer token minted at GET /authorize from HTTP Basic credentials plus an Act-Database-Name header. The API is deployed per database — either on Act! Premium Cloud or on the customer's own IIS server — so the base URL is per-tenant.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/act.png
layout: provider
mcp_servers:
- description: ''
  name: act-mcp.yml
  slug: act-mcpyml
modified: '2026-08-13'
name: Act! CRM
nav: Providers
network: true
overview: 'Act! CRM publishes 1 API on the [APIs.io](https://apis.io/) network: Act! Web API. Tagged areas include CRM, Customer Relationship Management, Marketing Automation, Contact Management, and Sales.


  The Act! CRM catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Act! CRM''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, pricing, and 23 more developer resources.'
plans:
- name: Act Plans Pricing
  plan_count: 4
  slug: act-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Act Rate Limits
  slug: act-rate-limits
score:
  band: strong
  composite: 63.1
  delta: 2.8
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 30.3
    contract_quality: 59.2
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 52.6
  previous_composite: 60.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/act/refs/heads/main/screenshots/act-2026-08-17T121405.png
security:
- kind: authentication
  name: Act Authentication
  slug: act-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Act Domain Security
  slug: act-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Act Vulnerability Disclosure
  slug: act-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Act Trust Center
  slug: act-trust-center
  summary_line: SOC 2, SOC 3, ISO 27001, PCI DSS, HIPAA, FedRAMP
slug: act
tags:
- CRM
- Customer Relationship Management
- Marketing Automation
- Contact Management
- Sales
- Opportunity Management
- OData
- Small Business
website: https://www.act.com
---
