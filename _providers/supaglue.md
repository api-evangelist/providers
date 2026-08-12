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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 69
  human_in_the_loop: 0
  name: Supaglue Agentic Access
  operation_count: 145
  slug: supaglue-agentic-access
  summary_line: 145 operations · 69 acting
api_count: 35
apis:
- description: The `Account` Common Object represents a "company" in CRMs.
  name: Supaglue Accounts API
  slug: supaglue-accounts-api
- description: The Associations API from Supaglue — 1 operation(s) for associations.
  name: Supaglue Associations API
  slug: supaglue-associations-api
- description: An `Association Schema` is an object describing an association between two entities.
  name: Supaglue AssociationSchemas API
  slug: supaglue-associationschemas-api
- description: The Attachment object is used to represent an attachment for a ticket.
  name: Supaglue Attachments API
  slug: supaglue-attachments-api
- description: The Collection object is used to represent collections of tickets. Collections may include other collections as sub collections.
  name: Supaglue Collections API
  slug: supaglue-collections-api
- description: The Comment object is used to represent a comment on a ticket.
  name: Supaglue Comments API
  slug: supaglue-comments-api
- description: A `Connection` represents a Customer's connection to a Provider.
  name: Supaglue Connections API
  slug: supaglue-connections-api
- description: A `ConnectionSyncConfig` is a configuration for how to sync a specific Customer's data from a Provider to a Destination on a schedule.
  name: Supaglue ConnectionSyncConfigs API
  slug: supaglue-connectionsyncconfigs-api
- description: The `Contact` Common Object represents a "contact" in CRMs.
  name: Supaglue Contacts API
  slug: supaglue-contacts-api
- description: A `Customer` represents one of your customers.
  name: Supaglue Customers API
  slug: supaglue-customers-api
- description: A `Custom Object` is an instance of a `Custom Object Schema`.
  name: Supaglue CustomObjects API
  slug: supaglue-customobjects-api
- description: A `Custom Object Schema` is an object schema defined by the user.
  name: Supaglue CustomObjectSchemas API
  slug: supaglue-customobjectschemas-api
- description: A `Destination` is a data store where we write data in your infrastructure.
  name: Supaglue Destinations API
  slug: supaglue-destinations-api
- description: An [`Entity`](https://docs.supaglue.com/platform/entities/overview) allows you to represent your application data models in Supaglue so customers can map their different Provider objects and fields. S
  name: Supaglue Entities API
  slug: supaglue-entities-api
- description: An [`Entity Mapping`](https://docs.supaglue.com/platform/entities/overview#entity-mapping) maps an [Entity](https://docs.supaglue.com/platform/entities/overview) to a customer's Provider object and fi
  name: Supaglue EntityMappings API
  slug: supaglue-entitymappings-api
- description: The `Lead` Common Object represents a "potential customer" in CRMs.
  name: Supaglue Leads API
  slug: supaglue-leads-api
- description: The `List` Object represents a collection of CRM records.
  name: Supaglue Lists API
  slug: supaglue-lists-api
- description: A `Magic Link` is a secure URL that allows your customers to connect their accounts to Supaglue.
  name: Supaglue Magic Links API
  slug: supaglue-magic-links-api
- description: The `Mailbox` Common Object is used to represent email mailbox, used within the application for sending and syncing emails.
  name: Supaglue Mailboxes API
  slug: supaglue-mailboxes-api
- description: The `Opportunity` Common Object represents a "deal opportunity" in CRMs.
  name: Supaglue Opportunities API
  slug: supaglue-opportunities-api
- description: A `Property` is a field in a Provider Object.
  name: Supaglue Properties API
  slug: supaglue-properties-api
- description: A `Provider` is a third-party SaaS tool we can connect to (e.g. Salesforce).
  name: Supaglue Providers API
  slug: supaglue-providers-api
- description: A `Schema Mapping` is a mapping between a [Schema](https://docs.supaglue.com/platform/objects/overview#schemas) field and fields in your customer's Provider object.
  name: Supaglue SchemaMappings API
  slug: supaglue-schemamappings-api
- description: A [`Schema`](https://docs.supaglue.com/platform/objects/overview#schemas) allows you to normalize fields for customers across a single Provider object. Supaglue uses Schemas for Managed Syncs and Acti
  name: Supaglue Schemas API
  slug: supaglue-schemas-api
- description: The `Sequence State` Common Object represents the state of a contact in a sequence, commonly known as a "sequence membership".
  name: Supaglue Sequence States API
  slug: supaglue-sequence-states-api
- description: The `Sequence` Common Object represents a "sequence" in Engagements.
  name: Supaglue Sequences API
  slug: supaglue-sequences-api
- description: The StandardObjects API from Supaglue — 2 operation(s) for standardobjects.
  name: Supaglue StandardObjects API
  slug: supaglue-standardobjects-api
- description: A `Standard Object Schema` is an object schema of a standard object type supported by the provider.
  name: Supaglue StandardObjectSchemas API
  slug: supaglue-standardobjectschemas-api
- description: A `SyncConfig` is a configuration for how to sync your Customers' data from a Provider to a Destination on a schedule.
  name: Supaglue SyncConfigs API
  slug: supaglue-syncconfigs-api
- description: A `SyncRun` is a single execution of a Sync at a point in time.
  name: Supaglue SyncRuns API
  slug: supaglue-syncruns-api
- description: A `Sync` is a way for a Customer to sync data from a Provider to a Destination on a schedule.
  name: Supaglue Syncs API
  slug: supaglue-syncs-api
- description: The Tag object is used to represent a tag or label for a ticket.
  name: Supaglue Tags API
  slug: supaglue-tags-api
- description: The Team object is used to represent a team within the company receiving the ticket.
  name: Supaglue Teams API
  slug: supaglue-teams-api
- description: The Ticket object is used to represent a ticket or a task within a system.
  name: Supaglue Tickets API
  slug: supaglue-tickets-api
- description: The `User` Common Object represents a "user" that can log in to CRMs.
  name: Supaglue Users API
  slug: supaglue-users-api
artifact_total: 51
collections:
- collection_type: open
  name: Unified CRM API
  slug: open-supaglue-crm-api
- collection_type: open
  name: Unified Engagement API
  slug: open-supaglue-engagement-api
- collection_type: open
  name: Management API
  slug: open-supaglue-management-api
- collection_type: open
  name: Unified Ticketing API (Preview)
  slug: open-supaglue-ticketing-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/supaglue-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/supaglue-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/supaglue-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/supaglue
- group: company
  title: ''
  type: Website
  url: https://www.supaglue.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.supaglue.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/supaglue-labs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.supaglue.com/getting-started
- group: other
  title: ''
  type: API Introduction
  url: https://docs.supaglue.com/api/introduction
created: '2026-03-27'
description: Supaglue is an open-source unified API platform that enables B2B SaaS developers to build product integrations with CRM, HRIS, sales engagement, ticketing, and other business applications. It provides a unified API layer that abstracts away provider-specific differences, managed OAuth authentication, data syncing to data warehouses (BigQuery, Snowflake, Redshift, Postgres), and a management API for configuring customers, connections, and sync configurations. Supported providers include Salesforce, HubSpot, Pipedrive, Zendesk, Slack, and 15+ others. The platform is available as a managed cloud service (api.supaglue.io) and as a self-hosted open-source deployment. The GitHub organization is github.com/supaglue-labs.
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
modified: '2026-05-19'
name: Supaglue
nav: Providers
network: true
overview: 'Supaglue publishes 35 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Associations API, AssociationSchemas API, and 32 more. Tagged areas include CRM, HRIS, Unified API, Open Source, and Integrations.


  The Supaglue catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Supaglue''s developer surface includes authentication, documentation, getting-started guide, and 6 more developer resources.'
plans:
- name: Supaglue Plans Pricing
  plan_count: 1
  slug: supaglue-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 1
  name: Supaglue Rate Limits
  slug: supaglue-rate-limits
rules:
- name: Supaglue API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: supaglue-jsonschema-spectral-rules
- name: Supaglue API Rules
  rule_count: 10
  severity_counts:
    error: 0
    hint: 0
    info: 6
    warn: 4
  slug: supaglue-rules
score:
  band: thin
  composite: 40.6
  delta: -4.9
  facets:
    commercial_clarity: 13.2
    contract_quality: 68.2
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 10.5
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 35
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/supaglue/refs/heads/main/screenshots/supaglue-2026-06-20T194702.png
security:
- kind: authentication
  name: Supaglue Authentication
  slug: supaglue-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Supaglue Domain Security
  slug: supaglue-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: supaglue
tags:
- CRM
- HRIS
- Unified API
- Open Source
- Integrations
- Sales Engagement
website: https://www.supaglue.com/
---
