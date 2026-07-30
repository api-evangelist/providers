---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 55
  human_in_the_loop: 0
  name: Reonic Agentic Access
  operation_count: 111
  slug: reonic-agentic-access
  summary_line: 111 operations · 55 acting
api_count: 29
apis:
- description: Timeline of events on a project — automatic activity records and manually logged calls and meetings.
  name: Reonic Activities API
  slug: reonic-activities-api
- description: Appointments on Reonic-hosted calendars only. External calendars (Google, Microsoft) cannot be read or written through the API.
  name: Reonic Appointments API
  slug: reonic-appointments-api
- description: Groupings used to organize [**Calendars**](#tag/calendars).
  name: Reonic Calendar Categories API
  slug: reonic-calendar-categories-api
- description: Reonic-hosted calendars only. External calendar integrations (Google, Microsoft) are visible inside the Reonic Portal but are not exposed through the public API.
  name: Reonic Calendars API
  slug: reonic-calendars-api
- description: Reusable checklists. Apply one to a residential project to populate its [**Checklists**](#tag/checklists). > [!warning] > **Beta:** These endpoints are in beta and may change as the service evolves. P
  name: Reonic Checklist Templates API
  slug: reonic-checklist-templates-api
- description: The active checklist for a residential project. > [!warning] > **Beta:** These endpoints are in beta and may change as the service evolves. Please report issues or unexpected behavior to our team.
  name: Reonic Checklists API
  slug: reonic-checklists-api
- description: Commercial customer projects across the request, offer, and installation lifecycle stages. > [!warning] > **Beta:** These endpoints are in beta and may change as the service evolves. Please report iss
  name: Reonic Commercial Projects API
  slug: reonic-commercial-projects-api
- description: Catalog of solar, storage, EV charger, and heat-pump products available to your workspace.
  name: Reonic Components API
  slug: reonic-components-api
- description: External people you interact with, such as customers or leads. Not to be confused with [**Users**](#tag/users), which represent members of your workspace.
  name: Reonic Contacts API
  slug: reonic-contacts-api
- description: Folders that organize [**Files**](#tag/files) within a project or contact. > [!note] > Personal and template folders are not exposed via the API.
  name: Reonic File Folders API
  slug: reonic-file-folders-api
- description: Files attached to a project or contact. File responses include a download URL valid for 24 hours; refetch the file to obtain a fresh URL after it expires.
  name: Reonic Files API
  slug: reonic-files-api
- description: Kanban boards used to group project columns within a lifecycle stage such as request, offer, or installation.
  name: Reonic Kanban Boards API
  slug: reonic-kanban-boards-api
- description: Kanban columns projects move through on a [**Kanban Boards**](#tag/kanban-boards).
  name: Reonic Kanban Columns API
  slug: reonic-kanban-columns-api
- description: Channels that brought a customer/contact to your workspace, such as referrals, ad campaigns, or partner integrations. Used to attribute projects to their origin.
  name: Reonic Lead Sources API
  slug: reonic-lead-sources-api
- description: Resolve a resource into a URL where it can be viewed in the Reonic web app.
  name: Reonic Links API
  slug: reonic-links-api
- description: Free-text notes attached to a project or contact.
  name: Reonic Notes API
  slug: reonic-notes-api
- description: 'Pre-configured combinations of planning packages used to quickly populate package categories when creating an offer. > [!warning] > **Beta:** These endpoints are in beta and may change as the service '
  name: Reonic Offer Templates API
  slug: reonic-offer-templates-api
- description: '3D reconstruction jobs built from uploaded site imagery. > [!warning] > **Beta:** These endpoints are in beta and may change as the service evolves. Please report issues or unexpected behavior to our '
  name: Reonic Photogrammetry API
  slug: reonic-photogrammetry-api
- description: Standard offer packages for PV, storage, heat pumps, and EV chargers, built from common [**Components**](#tag/components) and service combinations.
  name: Reonic Planning Packages API
  slug: reonic-planning-packages-api
- description: Small groups of [**Components**](#tag/components) that can be added to targeted planning sections when a project type or requirement calls for extra components.
  name: Reonic Planning Templates API
  slug: reonic-planning-templates-api
- description: Residential customer projects across the request, offer, and installation lifecycle stages.
  name: Reonic Residential Projects API
  slug: reonic-residential-projects-api
- description: Requests sent to a customer to sign a residential project's offer. Each carries the offer PDF for every variant the customer can choose between, available even before signing, plus the signed document
  name: Reonic Signature Requests API
  slug: reonic-signature-requests-api
- description: Reusable labels for categorizing and filtering projects, contacts, and other entities.
  name: Reonic Tags API
  slug: reonic-tags-api
- description: To-do items attached to a project or contact, with due dates, assignees, and completion state. > [!warning] > **Beta:** These endpoints are in beta and may change as the service evolves. Please report
  name: Reonic Tasks API
  slug: reonic-tasks-api
- description: Groups of users. Teams can be assigned to projects and nested under one another.
  name: Reonic Teams API
  slug: reonic-teams-api
- description: Time entries logged against projects. > [!warning] > **Beta:** These endpoints are in beta and may change as the service evolves. Please report issues or unexpected behavior to our team.
  name: Reonic Time Tracking API
  slug: reonic-time-tracking-api
- description: Two-step uploads for endpoints that accept user-provided file content. Call `POST /uploads/create` to obtain an `uploadUrl` and an `uploadId`. `PUT` the raw file body to `uploadUrl` within 1 hour, wit
  name: Reonic Upload API
  slug: reonic-upload-api
- description: Members of your workspace, such as employees. Not to be confused with [**Contacts**](#tag/contacts), which represent external people like customers or leads.
  name: Reonic Users API
  slug: reonic-users-api
- description: Your company's shared knowledge base — pages and folders. > [!warning] > **Beta:** These endpoints are in beta and may change as the service evolves. Please report issues or unexpected behavior to our
  name: Reonic Wiki API
  slug: reonic-wiki-api
artifact_total: 35
asyncapis:
- description: Event surface for the Reonic REST API v3. Reonic POSTs a signed JSON body (HMAC SHA-256, X-Reonic-Signature) to your configured HTTPS endpoint when a selected event occurs. Payloads are thin (ids only
  name: Reonic Webhooks
  slug: reonic-webhooks-asyncapi
- description: ''
  name: Reonic Webhooks
  slug: reonic-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.reonic.de/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.reonic.de/docs/category/integrationen/
- group: docs
  title: ''
  type: APIReference
  url: https://api.reonic.de/rest/v3/docs
- group: company
  title: ''
  type: Blog
  url: https://reonic.com/de-de/blog/
- group: operate
  title: ''
  type: Support
  url: mailto:support@reonic.de
- group: start
  title: ''
  type: SignUp
  url: https://portal.reonic.de
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reonic.com/de-de/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reonic.com/de-de/legal/dataprotection/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reonic
- group: auth
  title: ''
  type: Authentication
  url: authentication/reonic-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/reonic-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/reonic-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reonic-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/reonic-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/reonic-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reonic-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/reonic-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/reonic-well-known.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/reonic-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/reonic-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/reonic-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reonic-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reonic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reonic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://reonic.de
created: '2026-07-17'
description: Reonic is a German climate-tech company (founded 2021, Augsburg) building an AI-powered operating system for renewable-energy installers. Its platform covers the full workflow for selling and installing photovoltaic systems, heat pumps, EV chargers, and battery storage — CRM and lead management, 3D roof planning and shading simulation, instant pricing, proposal generation with digital signature, project and installation tracking, and documentation. The Reonic REST API v3 exposes 111 endpoints across 33 resource areas (contacts, residential and commercial projects, tasks, files, components, planning templates, time tracking, wiki, photogrammetry, and more), authenticated with rnc_v3_ API keys, plus a 17-event signed webhook surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reonic.png
layout: provider
mcp_servers:
- description: ''
  name: reonic-mcp.yml
  slug: reonic-mcpyml
modified: '2026-07-20'
name: Reonic
nav: Providers
network: true
overview: 'Reonic publishes 29 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Appointments API, Calendar Categories API, and 26 more. Tagged areas include Company, Climate Energy, Solar, Renewable Energy, and Photovoltaic.


  The Reonic catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Reonic''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, changelog, and 19 more developer resources.'
random_paper: 66
score:
  band: developing
  composite: 46.8
  delta: -2.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 61.9
    developer_ergonomics: 45.1
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 29
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Reonic Authentication
  slug: reonic-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Reonic Domain Security
  slug: reonic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: reonic
tags:
- Company
- Climate Energy
- Solar
- Renewable Energy
- Photovoltaic
- Heat Pumps
- Installer Software
- SaaS
- CRM
- Project Management
website: https://reonic.de
---
