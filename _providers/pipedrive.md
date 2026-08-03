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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 191
  human_in_the_loop: 0
  name: Pipedrive Agentic Access
  operation_count: 371
  slug: pipedrive-agentic-access
  summary_line: 371 operations · 191 acting
api_count: 48
apis:
- description: 'Activities are appointments/tasks/events on a calendar that can be associated with a deal, a lead, a person and an organization. Activities can be of different type (such as call, meeting, lunch or a '
  name: Pipedrive Activities API
  slug: pipedrive-activities-api
- description: Activity fields represent different fields that an activity has.
  name: Pipedrive ActivityFields API
  slug: pipedrive-activityfields-api
- description: Activity types represent different kinds of activities that can be stored. Each activity type is presented to the user with an icon and a name. Additionally, a color can be defined (not implemented in
  name: Pipedrive ActivityTypes API
  slug: pipedrive-activitytypes-api
- description: Beta endpoints are endpoints that may have changes without a regular 60-90 day notice period.
  name: Pipedrive Beta API
  slug: pipedrive-beta-api
- description: Billing is responsible for handling your subscriptions, payments, plans and add-ons.
  name: Pipedrive Billing API
  slug: pipedrive-billing-api
- description: Call logs describe the outcome of a phone call managed by an integrated provider. Since these logs are also considered activities, they can be associated with a deal or a lead, a person and/or an orga
  name: Pipedrive CallLogs API
  slug: pipedrive-calllogs-api
- description: Channels API allows you to integrate your existing messaging channels into Pipedrive through [Messaging app extension](https://pipedrive.readme.io/docs/messaging-app-extension). It enables you to mana
  name: Pipedrive Channels API
  slug: pipedrive-channels-api
- description: Supported currencies which can be used to represent the monetary value of a deal, or a value of any monetary type custom field. The `Currency.code` field must be used to point to a currency. `Currency
  name: Pipedrive Currencies API
  slug: pipedrive-currencies-api
- description: Deal fields represent the near-complete schema for a deal in the context of the company of the authorized user. Each company can have a different schema for their deals, with various custom fields. In
  name: Pipedrive DealFields API
  slug: pipedrive-dealfields-api
- description: Deal installments are scheduled payment entries attached to a deal, enabling split payment arrangements.
  name: Pipedrive DealInstallments API
  slug: pipedrive-dealinstallments-api
- description: Deal products are goods or services attached to a deal. Each deal product links a product to a deal with configurable quantity, pricing, and discounts, and contributes to the total value of the deal.
  name: Pipedrive DealProducts API
  slug: pipedrive-dealproducts-api
- description: Deals represent ongoing, lost or won sales to an organization or to a person. Each deal has a monetary value and must be placed in a stage. Deals can be owned by a user, and followed by one or many us
  name: Pipedrive Deals API
  slug: pipedrive-deals-api
- description: Files are documents of any kind (images, spreadsheets, text files, etc.) that are uploaded to Pipedrive, and usually associated with a particular deal, person, organization, product, note or activity.
  name: Pipedrive Files API
  slug: pipedrive-files-api
- description: Each filter is essentially a set of data validation conditions. A filter of the same kind can be applied when fetching a list of deals, leads, persons, organizations or products in the context of a pi
  name: Pipedrive Filters API
  slug: pipedrive-filters-api
- description: Goals help your team meet your sales targets. There are three types of goals - company, team and user.
  name: Pipedrive Goals API
  slug: pipedrive-goals-api
- description: Ordered reference objects, pointing to either deals, persons, organizations, leads, products, files or mail attachments.
  name: Pipedrive ItemSearch API
  slug: pipedrive-itemsearch-api
- description: Lead fields represent the near-complete schema for a lead in the context of the company of the authorized user. Each company can have a different schema for their leads, with various custom fields. In
  name: Pipedrive LeadFields API
  slug: pipedrive-leadfields-api
- description: 'Lead labels allow you to visually categorize your leads. There are three default lead labels: hot, cold, and warm, but you can add as many new custom labels as you want.'
  name: Pipedrive LeadLabels API
  slug: pipedrive-leadlabels-api
- description: 'Leads are potential deals stored in Leads Inbox before they are archived or converted to a deal. Each lead needs to be named (using the `title` field) and be linked to a person or an organization. In '
  name: Pipedrive Leads API
  slug: pipedrive-leads-api
- description: 'A lead source indicates where your lead came from. Currently, these are the possible lead sources: `Manually created`, `Deal`, `Web forms`, `Prospector`, `Leadbooster`, `Live chat`, `Import`, `Website'
  name: Pipedrive LeadSources API
  slug: pipedrive-leadsources-api
- description: Legacy teams allow you to form groups of users withing the organization for more efficient management. Previously Legacy Teams were called Teams and occupied the `v1/teams*` path. They're being deprec
  name: Pipedrive LegacyTeams API
  slug: pipedrive-legacyteams-api
- description: Mailbox was designed to be the email control hub inside Pipedrive. Pipedrive supports all major providers (including Gmail, Outlook and also custom IMAP/SMTP). There are 2 options for syncing user ema
  name: Pipedrive Mailbox API
  slug: pipedrive-mailbox-api
- description: Meetings API allows integrating video calling apps into Pipedrive through [Video Calling App extension](https://pipedrive.readme.io/docs/video-calling-app-extension). It enables you to manage and inte
  name: Pipedrive Meetings API
  slug: pipedrive-meetings-api
- description: Note fields represent different fields that a note has.
  name: Pipedrive NoteFields API
  slug: pipedrive-notefields-api
- description: 'Notes are pieces of textual (HTML-formatted) information that can be attached to deals, persons and organizations. Notes are usually displayed in the UI in chronological order – newest first – and in '
  name: Pipedrive Notes API
  slug: pipedrive-notes-api
- description: Using OAuth 2.0 is necessary for developing apps that are available in the Pipedrive Marketplace. Authorization via OAuth 2.0 is a well-known and stable way to get fine-grained access to an API. To re
  name: Pipedrive Oauth API
  slug: pipedrive-oauth-api
- description: 'Organization fields represent the near-complete schema for an organization in the context of the company of the authorized user. Each company can have a different schema for their organizations, with '
  name: Pipedrive OrganizationFields API
  slug: pipedrive-organizationfields-api
- description: Organization relationships represent how different organizations are related to each other. The relationship can be hierarchical (parent-child companies) or lateral as defined by the `type` field - ei
  name: Pipedrive OrganizationRelationships API
  slug: pipedrive-organizationrelationships-api
- description: Organizations are companies and other kinds of organizations you are making deals with. Persons can be associated with organizations so that each organization can contain one or more persons.
  name: Pipedrive Organizations API
  slug: pipedrive-organizations-api
- description: 'Permission sets define what users in the account can do: which actions they are allowed to perform and which features they can access. Permission sets are app-specific, where apps are large parts of f'
  name: Pipedrive PermissionSets API
  slug: pipedrive-permissionsets-api
- description: Person fields represent the near-complete schema for a person in the context of the company of the authorized user. Each company can have a different schema for their persons, with various custom fiel
  name: Pipedrive PersonFields API
  slug: pipedrive-personfields-api
- description: Persons are your contacts, the customers you are doing deals with. Each person can belong to an organization. Persons should not be confused with users.
  name: Pipedrive Persons API
  slug: pipedrive-persons-api
- description: Pipelines are essentially ordered collections of stages.
  name: Pipedrive Pipelines API
  slug: pipedrive-pipelines-api
- description: Product fields represent the near-complete schema for a product in the context of the company of the authorized user. Each company can have a different schema for their products, with various custom f
  name: Pipedrive ProductFields API
  slug: pipedrive-productfields-api
- description: Products are the goods or services you are dealing with. Each product can have N different price points - firstly, each product can have a price in N different currencies, and secondly, each product c
  name: Pipedrive Products API
  slug: pipedrive-products-api
- description: Project boards are used to organize projects into different phases. Each board contains phases that define the workflow for projects.
  name: Pipedrive ProjectBoards API
  slug: pipedrive-projectboards-api
- description: Project fields represent the schema for a project in the context of the company of the authorized user. Each company can have a different schema for their projects, with various custom fields.
  name: Pipedrive ProjectFields API
  slug: pipedrive-projectfields-api
- description: Project phases represent the stages within a project board. Each phase belongs to a board and defines a step in the project workflow.
  name: Pipedrive ProjectPhases API
  slug: pipedrive-projectphases-api
- description: Projects represent ongoing, completed or canceled projects attached to an organization, person or to deals. Each project has an owner and must be placed in a phase. Each project consists of standard d
  name: Pipedrive Projects API
  slug: pipedrive-projects-api
- description: Project templates allow you to have reusable and dynamic structure to simplify creation of a project. Project template can contain information about activities, tasks and groups that will be used when
  name: Pipedrive ProjectTemplates API
  slug: pipedrive-projecttemplates-api
- description: Recent changes across all item types in Pipedrive (deals, persons, etc).
  name: Pipedrive Recents API
  slug: pipedrive-recents-api
- description: Roles are a part of the Visibility groups’ feature that allow the admin user to categorize other users and dictate what items they will be allowed access to see.
  name: Pipedrive Roles API
  slug: pipedrive-roles-api
- description: 'Stage is a logical component of a pipeline, and essentially a bucket that can hold a number of deals. In the context of the pipeline a stage belongs to, it has an order number which defines the order '
  name: Pipedrive Stages API
  slug: pipedrive-stages-api
- description: Tasks represent actions that need to be completed and must be associated with a project. Tasks have an optional due date, can be assigned to a user and can have subtasks.
  name: Pipedrive Tasks API
  slug: pipedrive-tasks-api
- description: Manage user connections.
  name: Pipedrive UserConnections API
  slug: pipedrive-userconnections-api
- description: 'Users are people with access to your Pipedrive account. A user may belong to one or many Pipedrive accounts, so deleting a user from one Pipedrive account will not remove the user from the data store '
  name: Pipedrive Users API
  slug: pipedrive-users-api
- description: View user settings.
  name: Pipedrive UserSettings API
  slug: pipedrive-usersettings-api
- description: See <a href="https://pipedrive.readme.io/docs/guide-for-webhooks-v2?ref=api_reference" target="_blank" rel="noopener noreferrer">the guide for Webhooks</a> for more information.
  name: Pipedrive Webhooks API
  slug: pipedrive-webhooks-api
artifact_total: 118
asyncapis:
- description: 'AsyncAPI description of the Pipedrive Webhooks v2 surface. Pipedrive delivers webhook notifications as HTTP `POST` requests carrying a JSON body. A webhook subscription is identified by combining two '
  name: Pipedrive Webhooks v2
  slug: pipedrive-webhooks-v2-asyncapi
collections:
- collection_type: postman
  name: Pipedrive API v1 Activities API
  slug: postman-pipedrive-activities-api
- collection_type: postman
  name: Pipedrive API v1 Activities ActivityFields API
  slug: postman-pipedrive-activityfields-api
- collection_type: postman
  name: Pipedrive API v1 Activities ActivityTypes API
  slug: postman-pipedrive-activitytypes-api
- collection_type: postman
  name: Pipedrive API v1 Activities Beta API
  slug: postman-pipedrive-beta-api
- collection_type: postman
  name: Pipedrive API v1 Activities Billing API
  slug: postman-pipedrive-billing-api
- collection_type: postman
  name: Pipedrive API v1 Activities CallLogs API
  slug: postman-pipedrive-calllogs-api
- collection_type: postman
  name: Pipedrive API v1 Activities Channels API
  slug: postman-pipedrive-channels-api
- collection_type: postman
  name: Pipedrive API v1 Activities Currencies API
  slug: postman-pipedrive-currencies-api
- collection_type: postman
  name: Pipedrive API v1 Activities DealFields API
  slug: postman-pipedrive-dealfields-api
- collection_type: postman
  name: Pipedrive API v1 Activities DealInstallments API
  slug: postman-pipedrive-dealinstallments-api
- collection_type: postman
  name: Pipedrive API v1 Activities DealProducts API
  slug: postman-pipedrive-dealproducts-api
- collection_type: postman
  name: Pipedrive API v1 Activities Deals API
  slug: postman-pipedrive-deals-api
- collection_type: postman
  name: Pipedrive API v1 Activities Files API
  slug: postman-pipedrive-files-api
- collection_type: postman
  name: Pipedrive API v1 Activities Filters API
  slug: postman-pipedrive-filters-api
- collection_type: postman
  name: Pipedrive API v1 Activities Goals API
  slug: postman-pipedrive-goals-api
- collection_type: postman
  name: Pipedrive API v1 Activities ItemSearch API
  slug: postman-pipedrive-itemsearch-api
- collection_type: postman
  name: Pipedrive API v1 Activities LeadFields API
  slug: postman-pipedrive-leadfields-api
- collection_type: postman
  name: Pipedrive API v1 Activities LeadLabels API
  slug: postman-pipedrive-leadlabels-api
- collection_type: postman
  name: Pipedrive API v1 Activities Leads API
  slug: postman-pipedrive-leads-api
- collection_type: postman
  name: Pipedrive API v1 Activities LeadSources API
  slug: postman-pipedrive-leadsources-api
- collection_type: postman
  name: Pipedrive API v1 Activities LegacyTeams API
  slug: postman-pipedrive-legacyteams-api
- collection_type: postman
  name: Pipedrive API v1 Activities Mailbox API
  slug: postman-pipedrive-mailbox-api
- collection_type: postman
  name: Pipedrive API v1 Activities Meetings API
  slug: postman-pipedrive-meetings-api
- collection_type: postman
  name: Pipedrive API v1 Activities NoteFields API
  slug: postman-pipedrive-notefields-api
- collection_type: postman
  name: Pipedrive API v1 Activities Notes API
  slug: postman-pipedrive-notes-api
- collection_type: postman
  name: Pipedrive API v1 Activities Oauth API
  slug: postman-pipedrive-oauth-api
- collection_type: postman
  name: Pipedrive API v1 Activities OrganizationFields API
  slug: postman-pipedrive-organizationfields-api
- collection_type: postman
  name: Pipedrive API v1 Activities OrganizationRelationships API
  slug: postman-pipedrive-organizationrelationships-api
- collection_type: postman
  name: Pipedrive API v1 Activities Organizations API
  slug: postman-pipedrive-organizations-api
- collection_type: postman
  name: Pipedrive API v1 Activities PermissionSets API
  slug: postman-pipedrive-permissionsets-api
- collection_type: postman
  name: Pipedrive API v1 Activities PersonFields API
  slug: postman-pipedrive-personfields-api
- collection_type: postman
  name: Pipedrive API v1 Activities Persons API
  slug: postman-pipedrive-persons-api
- collection_type: postman
  name: Pipedrive API v1 Activities Pipelines API
  slug: postman-pipedrive-pipelines-api
- collection_type: postman
  name: Pipedrive API v1 Activities ProductFields API
  slug: postman-pipedrive-productfields-api
- collection_type: postman
  name: Pipedrive API v1 Activities Products API
  slug: postman-pipedrive-products-api
- collection_type: postman
  name: Pipedrive API v1 Activities ProjectBoards API
  slug: postman-pipedrive-projectboards-api
- collection_type: postman
  name: Pipedrive API v1 Activities ProjectFields API
  slug: postman-pipedrive-projectfields-api
- collection_type: postman
  name: Pipedrive API v1 Activities ProjectPhases API
  slug: postman-pipedrive-projectphases-api
- collection_type: postman
  name: Pipedrive API v1 Activities Projects API
  slug: postman-pipedrive-projects-api
- collection_type: postman
  name: Pipedrive API v1 Activities ProjectTemplates API
  slug: postman-pipedrive-projecttemplates-api
- collection_type: postman
  name: Pipedrive API v1 Activities Recents API
  slug: postman-pipedrive-recents-api
- collection_type: postman
  name: Pipedrive API v1 Activities Roles API
  slug: postman-pipedrive-roles-api
- collection_type: postman
  name: Pipedrive API v1 Activities Stages API
  slug: postman-pipedrive-stages-api
- collection_type: postman
  name: Pipedrive API v1 Activities Tasks API
  slug: postman-pipedrive-tasks-api
- collection_type: postman
  name: Pipedrive API v1 Activities UserConnections API
  slug: postman-pipedrive-userconnections-api
- collection_type: postman
  name: Pipedrive API v1 Activities Users API
  slug: postman-pipedrive-users-api
- collection_type: postman
  name: Pipedrive API v1 Activities UserSettings API
  slug: postman-pipedrive-usersettings-api
- collection_type: postman
  name: Pipedrive API v1 Activities Webhooks API
  slug: postman-pipedrive-webhooks-api
- collection_type: open
  name: Pipedrive API v1
  slug: open-pipedrive-v1
- collection_type: open
  name: Pipedrive API v2
  slug: open-pipedrive-v2
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/pipedrive/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pipedrive-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pipedrive-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pipedrive-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pipedrive-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pipedrive
- group: company
  title: ''
  type: Website
  url: https://www.pipedrive.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.pipedrive.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.pipedrive.com/docs/api/v1
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pipedrive.com/en/pricing
- group: start
  title: ''
  type: Login
  url: https://app.pipedrive.com/auth/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pipedrive.com/
- group: company
  title: ''
  type: Blog
  url: https://www.pipedrive.com/en/blog
- group: operate
  title: ''
  type: Support
  url: https://support.pipedrive.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pipedrive
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pipedrive.com/en/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pipedrive.com/en/terms-of-service
- group: auth
  title: ''
  type: Authentication
  url: https://pipedrive.readme.io/docs/core-api-concepts-authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://pipedrive.readme.io/docs/core-api-concepts-rate-limiting
- group: design
  title: ''
  type: Webhooks
  url: https://developers.pipedrive.com/docs/api/v1/Webhooks
- group: commercial
  title: ''
  type: Plans
  url: plans/pipedrive-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pipedrive-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pipedrive-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.pipedrive.com/llms.txt
created: '2026-05-08'
description: Pipedrive is a sales CRM and pipeline management tool focused on small and mid-market teams. The Pipedrive REST API exposes deals, persons, organizations, activities, leads, products, pipelines, stages, mail, calls, files, notes, users, permissions, filters, goals, subscriptions, and webhooks.
features:
- REST API at https://api.pipedrive.com/v1 (and v2 endpoints)
- OAuth 2.0 (Marketplace apps) and API token (custom integrations)
- Five plan tiers — Essential, Advanced, Professional, Power, Enterprise
- Token-based daily budget — 30,000 base tokens × plan multiplier × seats
- Plan multipliers from 1 (Lite) to 7 (Ultimate)
- Token costs - 2 (single GET), 20 (list GET), 10 (PUT), 40 (search)
- Burst per-user limits in 2-second windows
- 429 returned when daily budget is exhausted; resets at server midnight
- Add-ons - LeadBooster, Smart Docs, Web Visitors, Projects, Campaigns
- SDKs in Node.js, PHP, Python, .NET, Ruby
finops:
- name: Pipedrive Finops
  service_category: CRM
  slug: pipedrive-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Pipedrive CRM API. Pipedrive provides a REST API at `https://api.pipedrive.com/v1` (and v2 endpoints). This schema models the same domain as
  name: Pipedrive GraphQL Schema
  slug: pipedrive-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pipedrive.png
layout: provider
modified: '2026-05-30'
name: Pipedrive
nav: Providers
network: true
overview: 'Pipedrive publishes 48 APIs on the [APIs.io](https://apis.io/) network, including Activities API, ActivityFields API, ActivityTypes API, and 45 more. Tagged areas include CRM, Sales, Pipeline Management, SaaS, and Small Business.


  The Pipedrive catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Pipedrive''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, support, and 18 more developer resources.'
plans:
- name: Pipedrive Plans Pricing
  plan_count: 11
  slug: pipedrive-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 7
  name: Pipedrive Rate Limits
  slug: pipedrive-rate-limits
rules:
- name: Pipedrive API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: pipedrive-asyncapi-spectral-rules
scopes:
- name: Pipedrive Scopes
  scope_count: 28
  slug: pipedrive-scopes
  summary_line: 28 scopes · authorizationCode
score:
  band: strong
  composite: 60.6
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 73.8
    developer_ergonomics: 37.0
    discoverability: 50.0
    governance: 41.7
    operational_transparency: 60.5
  previous_composite: 60.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 48
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pipedrive/refs/heads/main/screenshots/pipedrive-2026-06-20T191725.png
security:
- kind: authentication
  name: Pipedrive Authentication
  slug: pipedrive-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Pipedrive Domain Security
  slug: pipedrive-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pipedrive
tags:
- CRM
- Sales
- Pipeline Management
- SaaS
- Small Business
website: https://www.pipedrive.com/
---
