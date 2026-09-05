---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 65
  human_in_the_loop: 0
  name: Supaglue Agentic Access
  operation_count: 139
  slug: supaglue-agentic-access
  summary_line: 139 operations · 65 acting
api_count: 9
apis:
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: The `Account` Common Object represents a "company" in CRMs.
  name: Supaglue Accounts API
  slug: supaglue-accounts-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: The Associations API from Supaglue — 1 operation(s) for associations.
  name: Supaglue Associations API
  slug: supaglue-associations-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: An `Association Schema` is an object describing an association between two entities.
  name: Supaglue AssociationSchemas API
  slug: supaglue-associationschemas-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: The Attachment object is used to represent an attachment for a ticket.
  name: Supaglue Attachments API
  slug: supaglue-attachments-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: The Collection object is used to represent collections of tickets. Collections may include other collections as sub collections.
  name: Supaglue Collections API
  slug: supaglue-collections-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: The Comment object is used to represent a comment on a ticket.
  name: Supaglue Comments API
  slug: supaglue-comments-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: A `Connection` represents a Customer's connection to a Provider.
  name: Supaglue Connections API
  slug: supaglue-connections-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: A `ConnectionSyncConfig` is a configuration for how to sync a specific Customer's data from a Provider to a Destination on a schedule.
  name: Supaglue ConnectionSyncConfigs API
  slug: supaglue-connectionsyncconfigs-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: The `Contact` Common Object represents a "contact" in CRMs.
  name: Supaglue Contacts API
  slug: supaglue-contacts-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: A `Customer` represents one of your customers.
  name: Supaglue Customers API
  slug: supaglue-customers-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: A `Custom Object` is an instance of a `Custom Object Schema`.
  name: Supaglue CustomObjects API
  slug: supaglue-customobjects-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: A `Custom Object Schema` is an object schema defined by the user.
  name: Supaglue CustomObjectSchemas API
  slug: supaglue-customobjectschemas-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: A `Destination` is a data store where we write data in your infrastructure.
  name: Supaglue Destinations API
  slug: supaglue-destinations-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: An [`Entity`](https://docs.supaglue.com/platform/entities/overview) allows you to represent your application data models in Supaglue so customers can map their different Provider objects and fields. S
  name: Supaglue Entities API
  slug: supaglue-entities-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: An [`Entity Mapping`](https://docs.supaglue.com/platform/entities/overview#entity-mapping) maps an [Entity](https://docs.supaglue.com/platform/entities/overview) to a customer's Provider object and fi
  name: Supaglue EntityMappings API
  slug: supaglue-entitymappings-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: The `Lead` Common Object represents a "potential customer" in CRMs.
  name: Supaglue Leads API
  slug: supaglue-leads-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: The `List` Object represents a collection of CRM records.
  name: Supaglue Lists API
  slug: supaglue-lists-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: A `Magic Link` is a secure URL that allows your customers to connect their accounts to Supaglue.
  name: Supaglue Magic Links API
  slug: supaglue-magic-links-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: The `Mailbox` Common Object is used to represent email mailbox, used within the application for sending and syncing emails.
  name: Supaglue Mailboxes API
  slug: supaglue-mailboxes-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: The `Opportunity` Common Object represents a "deal opportunity" in CRMs.
  name: Supaglue Opportunities API
  slug: supaglue-opportunities-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: A `Property` is a field in a Provider Object.
  name: Supaglue Properties API
  slug: supaglue-properties-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: A `Provider` is a third-party SaaS tool we can connect to (e.g. Salesforce).
  name: Supaglue Providers API
  slug: supaglue-providers-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: A `Schema Mapping` is a mapping between a [Schema](https://docs.supaglue.com/platform/objects/overview#schemas) field and fields in your customer's Provider object.
  name: Supaglue SchemaMappings API
  slug: supaglue-schemamappings-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: A [`Schema`](https://docs.supaglue.com/platform/objects/overview#schemas) allows you to normalize fields for customers across a single Provider object. Supaglue uses Schemas for Managed Syncs and Acti
  name: Supaglue Schemas API
  slug: supaglue-schemas-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: The `Sequence State` Common Object represents the state of a contact in a sequence, commonly known as a "sequence membership".
  name: Supaglue Sequence States API
  slug: supaglue-sequence-states-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: The `Sequence` Common Object represents a "sequence" in Engagements.
  name: Supaglue Sequences API
  slug: supaglue-sequences-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: The StandardObjects API from Supaglue — 2 operation(s) for standardobjects.
  name: Supaglue StandardObjects API
  slug: supaglue-standardobjects-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: A `Standard Object Schema` is an object schema of a standard object type supported by the provider.
  name: Supaglue StandardObjectSchemas API
  slug: supaglue-standardobjectschemas-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: A `SyncConfig` is a configuration for how to sync your Customers' data from a Provider to a Destination on a schedule.
  name: Supaglue SyncConfigs API
  slug: supaglue-syncconfigs-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: A `SyncRun` is a single execution of a Sync at a point in time.
  name: Supaglue SyncRuns API
  slug: supaglue-syncruns-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: A `Sync` is a way for a Customer to sync data from a Provider to a Destination on a schedule.
  name: Supaglue Syncs API
  slug: supaglue-syncs-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: The Tag object is used to represent a tag or label for a ticket.
  name: Supaglue Tags API
  slug: supaglue-tags-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: The Team object is used to represent a team within the company receiving the ticket.
  name: Supaglue Teams API
  slug: supaglue-teams-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: The Ticket object is used to represent a ticket or a task within a system.
  name: Supaglue Tickets API
  slug: supaglue-tickets-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: The `User` Common Object represents a "user" that can log in to CRMs.
  name: Supaglue Users API
  slug: supaglue-users-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: Endpoints for managing and submitting forms
  name: Supaglue Forms API
  slug: supaglue-forms-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: Hubspot is a CRM Provider.
  name: Supaglue Hubspot API
  slug: supaglue-hubspot-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: Passthrough operations to underlying providers.
  name: Supaglue Passthrough API
  slug: supaglue-passthrough-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: Relating to enrichment data that is derived from information about a Person. This may include demographic and firmographic data.
  name: Supaglue Persons API
  slug: supaglue-persons-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: Salesforce is a CRM Provider.
  name: Supaglue Salesforce API
  slug: supaglue-salesforce-api
- baseURL: https://api.supaglue.io/crm/v2
  baseurl_source: declared
  description: The Webhook Events API from Supaglue — 0 operation(s) for webhook events.
  name: Supaglue Webhook Events API
  slug: supaglue-webhook-events-api
artifact_total: 100
asyncapis:
- description: ''
  name: Supaglue Webhooks
  slug: supaglue-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Unified CRM Accounts API
  slug: open-supaglue-accounts-api
- collection_type: open
  name: Actions API
  slug: open-supaglue-actions-api
- collection_type: open
  name: Unified CRM Accounts Associations API
  slug: open-supaglue-associations-api
- collection_type: open
  name: Unified CRM Accounts AssociationSchemas API
  slug: open-supaglue-associationschemas-api
- collection_type: open
  name: Unified CRM Accounts Attachments API
  slug: open-supaglue-attachments-api
- collection_type: open
  name: Unified CRM Accounts Collections API
  slug: open-supaglue-collections-api
- collection_type: open
  name: Unified CRM Accounts Comments API
  slug: open-supaglue-comments-api
- collection_type: open
  name: Unified CRM Accounts Connections API
  slug: open-supaglue-connections-api
- collection_type: open
  name: Unified CRM Accounts ConnectionSyncConfigs API
  slug: open-supaglue-connectionsyncconfigs-api
- collection_type: open
  name: Unified CRM Accounts Contacts API
  slug: open-supaglue-contacts-api
- collection_type: open
  name: Unified CRM API
  slug: open-supaglue-crm-api
- collection_type: open
  name: Unified CRM Accounts Customers API
  slug: open-supaglue-customers-api
- collection_type: open
  name: Unified CRM Accounts CustomObjects API
  slug: open-supaglue-customobjects-api
- collection_type: open
  name: Unified CRM Accounts CustomObjectSchemas API
  slug: open-supaglue-customobjectschemas-api
- collection_type: open
  name: Data Listing API
  slug: open-supaglue-data-api
- collection_type: open
  name: Unified CRM Accounts Destinations API
  slug: open-supaglue-destinations-api
- collection_type: open
  name: Unified Engagement API
  slug: open-supaglue-engagement-api
- collection_type: open
  name: Unified Enrichment API
  slug: open-supaglue-enrichment-api
- collection_type: open
  name: Unified CRM Accounts Entities API
  slug: open-supaglue-entities-api
- collection_type: open
  name: Unified CRM Accounts EntityMappings API
  slug: open-supaglue-entitymappings-api
- collection_type: open
  name: Unified CRM Accounts Leads API
  slug: open-supaglue-leads-api
- collection_type: open
  name: Unified CRM Accounts Lists API
  slug: open-supaglue-lists-api
- collection_type: open
  name: Unified CRM Accounts Magic Links API
  slug: open-supaglue-magic-links-api
- collection_type: open
  name: Unified CRM Accounts Mailboxes API
  slug: open-supaglue-mailboxes-api
- collection_type: open
  name: Management API
  slug: open-supaglue-management-api
- collection_type: open
  name: Unified Enrichment API
  slug: open-supaglue-marketing-automation-api
- collection_type: open
  name: Metadata API
  slug: open-supaglue-metadata-api
- collection_type: open
  name: Unified CRM Accounts Opportunities API
  slug: open-supaglue-opportunities-api
- collection_type: open
  name: Unified CRM Accounts Properties API
  slug: open-supaglue-properties-api
- collection_type: open
  name: Unified CRM Accounts Providers API
  slug: open-supaglue-providers-api
- collection_type: open
  name: Unified CRM Accounts SchemaMappings API
  slug: open-supaglue-schemamappings-api
- collection_type: open
  name: Unified CRM Accounts Schemas API
  slug: open-supaglue-schemas-api
- collection_type: open
  name: Unified CRM Accounts Sequence States API
  slug: open-supaglue-sequence-states-api
- collection_type: open
  name: Unified CRM Accounts Sequences API
  slug: open-supaglue-sequences-api
- collection_type: open
  name: Unified CRM Accounts StandardObjects API
  slug: open-supaglue-standardobjects-api
- collection_type: open
  name: Unified CRM Accounts StandardObjectSchemas API
  slug: open-supaglue-standardobjectschemas-api
- collection_type: open
  name: Unified CRM Accounts SyncConfigs API
  slug: open-supaglue-syncconfigs-api
- collection_type: open
  name: Unified CRM Accounts SyncRuns API
  slug: open-supaglue-syncruns-api
- collection_type: open
  name: Unified CRM Accounts Syncs API
  slug: open-supaglue-syncs-api
- collection_type: open
  name: Unified CRM Accounts Tags API
  slug: open-supaglue-tags-api
- collection_type: open
  name: Unified CRM Accounts Teams API
  slug: open-supaglue-teams-api
- collection_type: open
  name: Unified Ticketing API (Preview)
  slug: open-supaglue-ticketing-api
- collection_type: open
  name: Unified CRM Accounts Tickets API
  slug: open-supaglue-tickets-api
- collection_type: open
  name: Unified CRM Accounts Users API
  slug: open-supaglue-users-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/supaglue-labs/supaglue/blob/main/LICENSE
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/supaglue-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/supaglue-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/supaglue-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/supaglue-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/supaglue-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/supaglue-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/supaglue-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/supaglue-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/supaglue-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://github.com/supaglue-labs/supaglue/blob/main/docs/docs/security_legal/security.md
- group: design
  title: ''
  type: Components
  url: components/supaglue-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/supaglue-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/supaglue-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/supaglue-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/supaglue-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/supaglue-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/supaglue-labs/supaglue/blob/main/SECURITY.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/supaglue-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/supaglue-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/supaglue-finops.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/supaglue-actions-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/supaglue-crm-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/supaglue-data-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/supaglue-engagement-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/supaglue-enrichment-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/supaglue-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/supaglue-marketing-automation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/supaglue-metadata-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/supaglue-ticketing-overlay.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/supaglue-labs/supaglue/tree/main/docs/docs
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/supaglue-labs/supaglue/tree/main/docs/docs/api/v2
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/supaglue-labs/supaglue/blob/main/docs/docs/quickstart.mdx
- group: other
  title: ''
  type: API Introduction
  url: https://github.com/supaglue-labs/supaglue/blob/main/docs/docs/api/introduction.mdx
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/supaglue-labs/supaglue
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/supaglue-labs
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/orgs/supaglue-labs/projects/4/views/1
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/supaglue-labs/supaglue/blob/main/docs/docs/security_legal/terms.md
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://github.com/supaglue-labs/supaglue/blob/main/docs/docs/security_legal/privacy.md
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/supaglue
- group: company
  title: ''
  type: X (Twitter)
  url: https://twitter.com/supaglue_labs
created: '2026-03-27'
description: 'Supaglue was an open-source unified API platform for B2B SaaS product integrations: a single contract for CRM, engagement, ticketing, enrichment and marketing-automation objects projected across 30+ third-party providers (Salesforce, HubSpot, Pipedrive, Outreach, Salesloft, Zendesk, Apollo and more), plus managed OAuth to those providers, managed syncs into the customer''s own warehouse (Postgres, BigQuery, Snowflake, Redshift, S3), a passthrough escape hatch to native provider APIs, and a Management API to configure customers, connections, schemas, entities and sync schedules. Nine first-party OpenAPI documents (v2, x-api-key auth) and nine typed webhook events were published. THE SERVICE IS RETIRED: the GitHub repository (github.com/supaglue-labs) was archived by its owner on 2024-03-10, api.supaglue.io and app.supaglue.io no longer resolve, and supaglue.com now redirects to a HugeDomains sale listing. The MIT-licensed code remains self-hostable, and the contract is preserved
  here as the historical record of a well-shaped unified API.'
examples:
- key_count: 4
  name: Supaglue List Contacts Example
  slug: supaglue-list-contacts-example
finops:
- name: Supaglue Finops
  service_category: Unified CRM API (Open Source)
  slug: supaglue-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/supaglue.png
json_schemas:
- name: Supaglue CRM Contact
  property_count: 15
  slug: supaglue-contact
json_structures:
- name: Supaglue Crm Structure
  property_count: 0
  slug: supaglue-crm-structure
jsonld:
- class_count: 0
  name: Supaglue Context
  property_count: 22
  slug: supaglue-context
layout: provider
modified: '2026-08-13'
name: Supaglue
nav: Providers
network: true
overview: 'Supaglue publishes 41 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Associations API, AssociationSchemas API, and 38 more. Tagged areas include CRM, HRIS, Unified-API, Open-Source, and Integration.


  The Supaglue catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Supaglue''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, and 37 more developer resources.'
plans:
- name: Supaglue Plans Pricing
  plan_count: 1
  slug: supaglue-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Supaglue Rate Limits
  slug: supaglue-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Supaglue API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: supaglue-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Supaglue API Rules
  rule_count: 10
  severity_counts:
    error: 0
    hint: 0
    info: 6
    warn: 4
  slug: supaglue-rules
score:
  band: developing
  composite: 53.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 63.5
    catalog_earned_first_party: 8.0
    catalog_gap: 51.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 31.8
    contract_quality: 68.2
    developer_ergonomics: 42.3
    discoverability: 74.1
    governance: 31.8
    operational_transparency: 42.1
  previous_composite: 53.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 41
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/supaglue/refs/heads/main/screenshots/supaglue-2026-08-17T083633.png
security:
- kind: authentication
  name: Supaglue Authentication
  slug: supaglue-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Supaglue Domain Security
  slug: supaglue-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Supaglue Vulnerability Disclosure
  slug: supaglue-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: supaglue
tags:
- CRM
- HRIS
- Unified-API
- Open-Source
- Integration
- Sales Engagement
- Ticketing
- Data Synchronization
- Marketing Automation
- Enrichment
- Webhook
- Archived
---
