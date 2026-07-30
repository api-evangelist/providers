---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Demandbase Agentic Access
  operation_count: 67
  slug: demandbase-agentic-access
  summary_line: 67 operations · 26 acting
api_count: 28
apis:
- description: Manage target account lists
  name: Demandbase Account Lists API
  slug: demandbase-account-lists-api
- description: Look up and retrieve account information
  name: Demandbase Accounts API
  slug: demandbase-accounts-api
- description: Activity streams and event tracking
  name: Demandbase Activities API
  slug: demandbase-activities-api
- description: Retrieve campaign performance metrics
  name: Demandbase Analytics API
  slug: demandbase-analytics-api
- description: API key set management
  name: Demandbase API Keys API
  slug: demandbase-api-keys-api
- description: Create and manage audience segments
  name: Demandbase Audiences API
  slug: demandbase-audiences-api
- description: Manage advertising campaigns
  name: Demandbase Campaigns API
  slug: demandbase-campaigns-api
- description: Search and discover companies
  name: Demandbase Company Search API
  slug: demandbase-company-search-api
- description: Contact discovery and lookup
  name: Demandbase Contacts API
  slug: demandbase-contacts-api
- description: Identify companies from cookies
  name: Demandbase Cookie Identification API
  slug: demandbase-cookie-identification-api
- description: Download exported data files
  name: Demandbase Downloads API
  slug: demandbase-downloads-api
- description: Account engagement scores and metrics
  name: Demandbase Engagement API
  slug: demandbase-engagement-api
- description: Enrich account and contact records with B2B data
  name: Demandbase Enrichment API
  slug: demandbase-enrichment-api
- description: Create and manage data export jobs
  name: Demandbase Export Jobs API
  slug: demandbase-export-jobs-api
- description: Access firmographic data for companies
  name: Demandbase Firmographics API
  slug: demandbase-firmographics-api
- description: Identify companies from various signals
  name: Demandbase Identification API
  slug: demandbase-identification-api
- description: Create and manage data import jobs
  name: Demandbase Import Jobs API
  slug: demandbase-import-jobs-api
- description: Intent signals and buying indicators
  name: Demandbase Intent API
  slug: demandbase-intent-api
- description: Identify companies from IP addresses
  name: Demandbase IP Identification API
  slug: demandbase-ip-identification-api
- description: Manage accounts within lists
  name: Demandbase List Members API
  slug: demandbase-list-members-api
- description: Field mapping configuration
  name: Demandbase Mappings API
  slug: demandbase-mappings-api
- description: Role and permission management
  name: Demandbase Roles API
  slug: demandbase-roles-api
- description: CRM synchronization operations
  name: Demandbase Sync API
  slug: demandbase-sync-api
- description: Technology usage data
  name: Demandbase Technographics API
  slug: demandbase-technographics-api
- description: Upload data files for import
  name: Demandbase Uploads API
  slug: demandbase-uploads-api
- description: User management operations
  name: Demandbase Users API
  slug: demandbase-users-api
- description: Visitor tracking and company resolution
  name: Demandbase Visitor Intelligence API
  slug: demandbase-visitor-intelligence-api
- description: Webhook subscription management
  name: Demandbase Webhooks API
  slug: demandbase-webhooks-api
artifact_total: 95
collections:
- collection_type: open
  name: Demandbase Account List API
  slug: open-demandbase-account-list
- collection_type: open
  name: Demandbase Admin API
  slug: open-demandbase-admin
- collection_type: open
  name: Demandbase Advertising API
  slug: open-demandbase-advertising
- collection_type: open
  name: Demandbase API
  slug: open-demandbase-api
- collection_type: open
  name: Demandbase B2B Data API
  slug: open-demandbase-b2b-data
- collection_type: open
  name: Demandbase Data Export API
  slug: open-demandbase-data-export
- collection_type: open
  name: Demandbase Data Import API
  slug: open-demandbase-data-import
- collection_type: open
  name: Demandbase Engagement API
  slug: open-demandbase-engagement
- collection_type: open
  name: Demandbase IP API
  slug: open-demandbase-ip
- collection_type: open
  name: Demandbase Real-Time Identification API
  slug: open-demandbase-real-time-identification
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/demandbase-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/demandbase-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/demandbase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/demandbase-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/demandbase
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.demandbase.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://docs.demandbase.com/docs/authentication
- group: operate
  title: ''
  type: StatusPage
  url: https://status.demandbase.com/
- group: operate
  title: ''
  type: Support
  url: https://support.demandbase.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.demandbase.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.demandbase.com/terms-of-service/
- group: company
  title: ''
  type: Blog
  url: https://www.demandbase.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.demandbase.com/feed/
- group: operate
  title: ''
  type: Contact
  url: https://www.demandbase.com/contact/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/demandbase/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Demandbase
- group: start
  title: ''
  type: Portal
  url: https://developer.demandbase.com
- group: other
  title: ''
  type: KnowledgeBase
  url: https://kb.demandbase.com/hc/en-us
- group: company
  title: ''
  type: Partners
  url: https://partners.demandbase.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.demandbase.com/terms-of-use/
- group: start
  title: ''
  type: Signup
  url: https://www.demandbase.com/products/data/api-integration/api-trial/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/demandbase-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/demandbase-account-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/demandbase-contact-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/demandbase-campaign-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/demandbase-engagement-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/demandbase-vocabulary.yml
created: '2024-01-20'
description: Demandbase is the leading Account-Based Marketing (ABM) platform that helps B2B companies identify, engage, and convert target accounts through intent data, advertising, personalization, and sales intelligence.
finops:
- name: Demandbase Finops
  service_category: B2B Marketing / Sales Intelligence
  slug: demandbase-finops
graphqls:
- description: This conceptual GraphQL schema represents the Demandbase ABM (Account-Based Marketing) and B2B intelligence platform. Demandbase provides account identification, intent data, advertising management, e
  name: Demandbase GraphQL Schema
  slug: demandbase-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/demandbase.png
json_schemas:
- name: Demandbase Account
  property_count: 29
  slug: demandbase-account
- name: AccountEngagement
  property_count: 9
  slug: demandbase-accountengagement
- name: AccountList
  property_count: 8
  slug: demandbase-accountlist
- name: AccountListMember
  property_count: 4
  slug: demandbase-accountlistmember
- name: Activity
  property_count: 8
  slug: demandbase-activity
- name: ApiKeySet
  property_count: 9
  slug: demandbase-apikeyset
- name: Audience
  property_count: 6
  slug: demandbase-audience
- name: Demandbase Campaign
  property_count: 16
  slug: demandbase-campaign
- name: CampaignAnalytics
  property_count: 10
  slug: demandbase-campaignanalytics
- name: Company
  property_count: 26
  slug: demandbase-company
- name: Demandbase Contact
  property_count: 12
  slug: demandbase-contact
- name: CreateAccountListRequest
  property_count: 3
  slug: demandbase-createaccountlistrequest
- name: CreateApiKeyRequest
  property_count: 2
  slug: demandbase-createapikeyrequest
- name: CreateAudienceRequest
  property_count: 3
  slug: demandbase-createaudiencerequest
- name: CreateCampaignRequest
  property_count: 6
  slug: demandbase-createcampaignrequest
- name: CreateExportJobRequest
  property_count: 4
  slug: demandbase-createexportjobrequest
- name: CreateImportJobRequest
  property_count: 4
  slug: demandbase-createimportjobrequest
- name: CreateUserRequest
  property_count: 4
  slug: demandbase-createuserrequest
- name: CreateWebhookRequest
  property_count: 2
  slug: demandbase-createwebhookrequest
- name: Demandbase Account Engagement
  property_count: 11
  slug: demandbase-engagement
- name: EnrichmentRequest
  property_count: 2
  slug: demandbase-enrichmentrequest
- name: Error
  property_count: 2
  slug: demandbase-error
- name: ExportableEntity
  property_count: 3
  slug: demandbase-exportableentity
- name: ExportJob
  property_count: 13
  slug: demandbase-exportjob
- name: FieldMapping
  property_count: 5
  slug: demandbase-fieldmapping
- name: Firmographics
  property_count: 13
  slug: demandbase-firmographics
- name: IdentificationResult
  property_count: 33
  slug: demandbase-identificationresult
- name: ImportError
  property_count: 5
  slug: demandbase-importerror
- name: ImportJob
  property_count: 14
  slug: demandbase-importjob
- name: IntentSignals
  property_count: 4
  slug: demandbase-intentsignals
- name: IpIdentificationResult
  property_count: 42
  slug: demandbase-ipidentificationresult
- name: Role
  property_count: 4
  slug: demandbase-role
- name: Technographics
  property_count: 2
  slug: demandbase-technographics
- name: UpdateUserRequest
  property_count: 4
  slug: demandbase-updateuserrequest
- name: User
  property_count: 9
  slug: demandbase-user
- name: Webhook
  property_count: 5
  slug: demandbase-webhook
json_structures:
- name: Demandbase Structure
  property_count: 0
  slug: demandbase-structure
jsonld:
- class_count: 0
  name: Demandbase Context
  property_count: 10
  slug: demandbase-context
layout: provider
modified: '2026-05-19'
name: Demandbase
nav: Providers
network: true
overview: 'Demandbase publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Account Lists API, Accounts API, Activities API, and 25 more. Tagged areas include Account-Based Marketing, Advertising, AI Agents, B2B Marketing, and Data Enrichment.


  The Demandbase catalog on APIs.io includes 1 JSON-LD context and 11 Spectral governance rulesets.


  Demandbase''s developer surface includes authentication, getting-started guide, support, engineering blog, developer portal, signup flow, and 21 more developer resources.'
plans:
- name: Demandbase Plans Pricing
  plan_count: 1
  slug: demandbase-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 1
  name: Demandbase Rate Limits
  slug: demandbase-rate-limits
rules:
- name: Demandbase API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 2
  slug: demandbase-account-list-api-rules
- name: Demandbase API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: demandbase-admin-api-rules
- name: Demandbase API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: demandbase-advertising-api-rules
- name: Demandbase API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: demandbase-api-rules
- name: Demandbase API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: demandbase-b2b-data-api-rules
- name: Demandbase API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: demandbase-data-export-api-rules
- name: Demandbase API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: demandbase-data-import-api-rules
- name: Demandbase API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: demandbase-engagement-api-rules
- name: Demandbase API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: demandbase-ip-api-rules
- name: Demandbase API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: demandbase-jsonschema-spectral-rules
- name: Demandbase API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: demandbase-real-time-identification-api-rules
score:
  band: developing
  composite: 55.9
  delta: -2.5
  facets:
    commercial_clarity: 57.9
    contract_quality: 80.3
    developer_ergonomics: 37.0
    discoverability: 68.5
    governance: 37.5
    operational_transparency: 42.1
  previous_composite: 58.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 28
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/demandbase/refs/heads/main/screenshots/demandbase-2026-06-20T175908.png
security:
- kind: authentication
  name: Demandbase Authentication
  slug: demandbase-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Demandbase Domain Security
  slug: demandbase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Demandbase Trust Center
  slug: demandbase-trust-center
  summary_line: SOC 2, ISO 27001
slug: demandbase
tags:
- Account-Based Marketing
- Advertising
- AI Agents
- B2B Marketing
- Data Enrichment
- Intent Data
- Personalization
- Sales Intelligence
website: https://developer.demandbase.com
---
