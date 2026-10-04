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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.1
  scored_at: '2026-10-03'
api_count: 11
apis:
- description: 'JSON-based REST API for the Act! CRM database exposing contacts, companies, groups, opportunities, tasks, activity series, calendar, notes, history, documents, attachments, users, teams, preferences, '
  name: Act! Web API
  slug: web-api
- baseURL: https://apimta.act.com/act.web.api
  baseurl_source: declared
  description: The ActivitySeries API from Act! CRM — 2 operation(s) for activityseries.
  name: Act! CRM Activity Series API
  phrasing_intents:
  - id: ActivitySeries_GetDeprecated_1026BB09
    intent: Get an activity series (deprecated)
    question: How do I look up a repeating activity series on the legacy ActivitySeries endpoint?
  - id: ActivitySeries_PutDeprecated_CDA0E3CC
    intent: Replace an activity series (deprecated)
    question: Can I fully update a series activity on the old ActivitySeries route?
  - id: ActivitySeries_DeleteDeprecated_FBE2FFCB
    intent: Delete an activity series (deprecated)
    question: Does deleting a series activity also remove occurrences I rescheduled?
  - id: ActivitySeries_PatchDeprecated_70F1EE46
    intent: Partially update an activity series (deprecated)
    question: Can I patch just the location of a series activity on the legacy endpoint?
  - id: ActivitySeries_GetDeprecated_FE2F02D8
    intent: List activity series (deprecated)
    question: How do I list all repeating activity series on the old endpoint?
  - id: ActivitySeries_PostDeprecated_3028AEF2
    intent: Create an activity series (deprecated)
    question: Can I still create a repeating activity through the legacy ActivitySeries route?
  phrasing_ops: 6
  slug: act-activityseries-api
- baseURL: https://apimta.act.com/act.web.api
  baseurl_source: declared
  description: The HistoryTypes API from Act! CRM — 5 operation(s) for historytypes.
  name: Act! CRM History Types API
  phrasing_intents:
  - id: HistoryTypes_GetHistoryTypeById_4E0AF16E
    intent: Get a history type
    question: How do I look up one history type by its id?
  - id: HistoryTypes_GetDeprecatedHistoryTypeByName_3232927F
    intent: Get a history type by name (deprecated)
    question: Can I still look up a history type by name on the old historytypes path?
  - id: HistoryTypes_GetHistoryTypes_2691B741
    intent: List history types
    question: What kinds of history entries can be recorded?
  - id: HistoryTypes_GetDeprecatedHistoryTypes_76F493AB
    intent: List history types (deprecated route)
    question: Does the old /api/historytypes listing still work?
  - id: HistoryTypes_GetHistoryTypesByTaskTypeId_C004BADF
    intent: List history types for an activity type
    question: Which history types go with a given activity type, like a call or meeting?
  phrasing_ops: 5
  slug: act-historytypes-api
- baseURL: https://apimta.act.com/act.web.api
  baseurl_source: declared
  description: The MarketingAutomations API from Act! CRM — 3 operation(s) for marketingautomations.
  name: Act! CRM Marketing Automations API
  phrasing_intents:
  - id: MarketingAutomations_GetCampaignResults_2DD93C76
    intent: Get a contact's campaign results
    question: How did one contact engage with my email campaigns?
  - id: MarketingAutomations_GetCampaign_29DE6BDC
    intent: List campaigns a contact received
    question: Which campaigns has a given contact been sent?
  - id: MarketingAutomations_PostEmail_60DBC5D7
    intent: Record a marketing automation email
    question: Can I log a marketing email sent from an outside campaign tool?
  phrasing_ops: 3
  slug: act-marketingautomations-api
- baseURL: https://apimta.act.com/act.web.api
  baseurl_source: declared
  description: The MetadataInfo API from Act! CRM — 14 operation(s) for metadatainfo.
  name: Act! CRM Metadata Info API
  phrasing_intents:
  - id: MetadataInfo_GetDropDownList_E02B587D
    intent: Get a drop-down list
    question: What values are in one particular drop-down list?
  - id: MetadataInfo_PutDropDownList_235230B0
    intent: Update a drop-down list
    question: Can I rename a drop-down list or change its items?
  - id: MetadataInfo_DeleteDropDownList_796D9B2D
    intent: Delete a drop-down list
    question: Can I remove a drop-down list I no longer use?
  - id: MetadataInfo_GetField_43A47EF1
    intent: Get a field definition for a record type
    question: What are the settings of one field on contacts or opportunities?
  - id: MetadataInfo_PutField_E8FC57AB
    intent: Update a field definition
    question: Can I change a custom field's display name or default value?
  - id: MetadataInfo_DeleteField_96ACDBD0
    intent: Delete a field
    question: Can I remove a custom field from a record type?
  - id: MetadataInfo_GetAllowedDataTypes_C0BD5F64
    intent: List allowed field data types
    question: Which data types can a new field use in Act!?
  - id: MetadataInfo_GetDropDownLists_1C3E17D1
    intent: List all drop-down lists
    question: What drop-down lists are defined in my database?
  phrasing_ops: 22
  slug: act-metadatainfo-api
- baseURL: https://apimta.act.com/act.web.api
  baseurl_source: declared
  description: The SecondaryContacts API from Act! CRM — 3 operation(s) for secondarycontacts.
  name: Act! CRM Secondary Contacts API
  phrasing_intents:
  - id: SecondaryContacts_Get_5AE7C09D
    intent: Get a secondary contact
    question: How do I look up one secondary contact under a primary contact?
  - id: SecondaryContacts_Put_5975AAF3
    intent: Replace a secondary contact
    question: How do I overwrite an entire secondary contact record?
  - id: SecondaryContacts_Delete_33369209
    intent: Delete a secondary contact
    question: How do I remove an assistant or secondary contact from a primary contact?
  - id: SecondaryContacts_Patch_29CC2E85
    intent: Change a few fields on a secondary contact
    question: Can I update only a secondary contact's mobile number?
  - id: SecondaryContacts_Get_CD9BB980
    intent: List a contact's secondary contacts
    question: Who are the secondary contacts listed under a primary contact?
  - id: SecondaryContacts_Post_C7CBE102
    intent: Add a secondary contact
    question: How do I add an assistant as a secondary contact on someone's record?
  - id: SecondaryContacts_PutPromote_BAF24408
    intent: Promote a secondary contact to primary
    question: How do I turn a secondary contact into a full primary contact?
  phrasing_ops: 7
  slug: act-secondarycontacts-api
- baseURL: https://apimta.act.com/act.web.api
  baseurl_source: declared
  description: The SupplementalFiles API from Act! CRM — 8 operation(s) for supplementalfiles.
  name: Act! CRM Supplemental Files API
  phrasing_intents:
  - id: SupplementalFiles_GetByActivity_CF24B225
    intent: Get an activity's attachment
    question: How do I download the file attached to an activity?
  - id: SupplementalFiles_PostActivityAttachment_1E201089
    intent: Attach a file to an activity
    question: How do I attach a file to an activity?
  - id: SupplementalFiles_DeleteByActivity_6E842025
    intent: Delete an activity's attachment
    question: How do I remove an attachment from an activity?
  - id: SupplementalFiles_GetByDocument_969374C4
    intent: Get a document's attachment
    question: Where do I retrieve the file behind a document record?
  - id: SupplementalFiles_PostDocumentAttachments_32FDFB20
    intent: Attach a file to a document
    question: How do I upload a file to a document record?
  - id: SupplementalFiles_DeleteByDocument_D3D6EC90
    intent: Delete a document's attachment
    question: How do I remove the attachment from a document?
  - id: SupplementalFiles_GetByHistory_C6FD6D97
    intent: Get a history entry's attachment
    question: Can I download the file attached to a history entry?
  - id: SupplementalFiles_PostHistoryAttachments_B509AF9D
    intent: Attach a file to a history entry
    question: How do I attach a file to a history record?
  phrasing_ops: 16
  slug: act-supplementalfiles-api
- baseURL: https://apimta.act.com/act.web.api
  baseurl_source: declared
  description: The Custom Entities API from Act! CRM — 2 operation(s) for custom entities.
  name: Act! CRM Custom Entities API
  phrasing_intents:
  - id: CustomEntities_Get_E50407CC
    intent: Get a custom entity record
    question: How do I fetch one record of a custom entity type?
  - id: CustomEntities_Put_E2EE1D22
    intent: Save a custom entity record at a given ID
    question: Can I write a custom entity record under an ID I choose?
  - id: CustomEntities_Delete_B426AB4B
    intent: Delete a custom entity record
    question: How do I delete a record from a custom entity?
  - id: CustomEntities_Get_534E3316
    intent: List a custom entity's records
    question: Which records exist for one of my custom entities?
  - id: CustomEntities_Post_4BE499F1
    intent: Create a custom entity record
    question: How do I add a new record to a custom entity?
  phrasing_ops: 5
  slug: act-custom-entities-api
- baseURL: https://apimta.act.com/act.web.api
  baseurl_source: declared
  description: The Document Types API from Act! CRM — 4 operation(s) for document types.
  name: Act! CRM Document Types API
  phrasing_intents:
  - id: DocumentTypes_GetHistoryTypesByDocumentTypes_9824C3CA
    intent: List document history types
    question: What history types can documents be logged under?
  - id: DocumentTypes_GetLibraryDocumentHistoryTypes_51035BB4
    intent: List document history types (deprecated)
    question: Is the old historytypes endpoint for documents still available?
  - id: DocumentTypes_GetHistoryTypesByDocumentType_82E4F41A
    intent: Get a document history type by name
    question: Can I look up one document history type by its name?
  - id: DocumentTypes_GetLibraryDocumentHistoryTypeByName_59C45724
    intent: Get a document history type by name (deprecated)
    question: Does the deprecated historytypes-by-name lookup still work?
  phrasing_ops: 4
  slug: act-document-types-api
- baseURL: https://apimta.act.com/act.web.api
  baseurl_source: declared
  description: The Sync Data API from Act! CRM — 4 operation(s) for sync data.
  name: Act! CRM Sync Data API
  phrasing_intents:
  - id: SyncData_PostSearchContactsByBusinessEmail_094FD90D
    intent: Find contact IDs by business email
    question: Can I look up contact IDs from a list of business emails?
  - id: SyncData_PostSearchSyncedExternalId_8F2C702D
    intent: Find already-synced external IDs
    question: Which external IDs have already been synced?
  - id: SyncData_PostSearchSyncedCalendarUids_AC7119F4
    intent: Find synced calendar UIDs
    question: Which calendar UIDs are already synced, and what external IDs map to them?
  - id: SyncData_PostRefreshEmailIntegarionCache_480299E9
    intent: Refresh my email integration cache
    question: How do I refresh the email integration cache for my user?
  phrasing_ops: 4
  slug: act-sync-data-api
- baseURL: https://apimta.act.com/act.web.api
  baseurl_source: declared
  description: The Task Types API from Act! CRM — 4 operation(s) for task types.
  name: Act! CRM Task Types API
  phrasing_intents:
  - id: TaskTypes_GetRegardingDropdownList_9668D3E9
    intent: Get a task type's regarding options
    question: What regarding options are offered for a given task type?
  - id: TaskTypes_Get_CA70DD31
    intent: List task types
    question: What task types are available?
  - id: TaskTypes_Post_49D8FCA6
    intent: Create a custom task type
    question: How do I add a custom task type?
  - id: TaskTypes_GetById_82B0E217
    intent: Get a task type
    question: How do I look up one task type by ID?
  - id: TaskTypes_Put_85CD258C
    intent: Replace a custom task type
    question: How do I fully update a custom task type?
  - id: TaskTypes_Delete_AA10E002
    intent: Delete a custom task type
    question: How do I delete a custom task type?
  - id: TaskTypes_Patch_C3E0417B
    intent: Partially update a custom task type
    question: Can I deactivate a custom task type without changing anything else?
  - id: TaskTypes_PatchUpdateBatchOfActivityTasks_DE61FFCD
    intent: Update several task types at once
    question: Can I partially update a batch of task types in one call?
  phrasing_ops: 8
  slug: act-task-types-api
artifact_total: 49
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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/act/refs/heads/main/capabilities/act-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/act-capability-edges.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/act/refs/heads/main/authentication/act-authentication.yml
  title: ''
  type: Authentication
  url: authentication/act-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/act/refs/heads/main/security/act-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/act-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/act/refs/heads/main/security/act-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/act-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/act/refs/heads/main/security/act-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/act-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/act/refs/heads/main/security/act-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/act-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/act/refs/heads/main/security/act-trust-center.yml
  title: ''
  type: Compliance
  url: security/act-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/act/refs/heads/main/conformance/act-conformance.yml
  title: ''
  type: Conformance
  url: conformance/act-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/act/refs/heads/main/lifecycle/act-lifecycle.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/act/refs/heads/main/changelog/act-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/act-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/act/refs/heads/main/plans/act-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/act-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/act/refs/heads/main/packages/act-packages.yml
  title: ''
  type: Packages
  url: packages/act-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/act/refs/heads/main/llms/act-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/act-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/act/refs/heads/main/skills/_index.yml
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
modified: '2026-08-13'
name: Act! CRM
nav: Providers
network: true
overview: 'Act! CRM publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Act! Web API, Activity Series API, History Types API, and 8 more. Tagged areas include CRM, Marketing Automation, Contact Management, Sales, and Opportunity Management.


  The Act! CRM catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Act! CRM''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, pricing, and 24 more developer resources.'
plans:
- name: Act Plans Pricing
  plan_count: 4
  slug: act-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Act Rate Limits
  slug: act-rate-limits
score:
  band: exemplar
  composite: 69.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 55.3
    developer_ergonomics: 66.1
    discoverability: 71.4
    operational_transparency: 60.5
  previous_composite: 69.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 50.0
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
- Marketing Automation
- Contact Management
- Sales
- Opportunity Management
- OData
- Small Business
website: https://www.act.com
---
