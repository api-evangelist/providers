---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 164
  human_in_the_loop: 4
  name: Spotio Agentic Access
  operation_count: 295
  slug: spotio-agentic-access
  summary_line: 295 operations · 164 acting · 4 human-in-the-loop
api_count: 39
apis:
- description: The controller is responsible for handling the creation, updating, and retrieval of activities. Mainly the controller allow to manage activities (current and done)
  name: SPOTIO Activities V2 API
  slug: spotio-activitiesv2-api
- description: 'The controller is responsible for handling the creation, updating, deleting and retrieval of appointment. Mainly the controller allow to manage appointment (current and future). Every appointment has '
  name: SPOTIO Appointments V2 API
  slug: spotio-appointmentsv2-api
- description: The controller provides various endpoints for managing autoplays, which are automated workflows that can be triggered for dataObject in application. Allowed is adding / editing contacts and changing s
  name: SPOTIO Autoplays API
  slug: spotio-autoplays-api
- description: The Business Cards API allows managing business card and their related operations, such as fetching details, listing, creating, updating, cloning, sharing, previewing, downloading, and rendering busin
  name: SPOTIO Business Cards API
  slug: spotio-businesscards-api
- description: The controller is responsible for managing calendar settings. Setup for company users calendar.
  name: SPOTIO Calendar Settings API
  slug: spotio-calendarsettings-api
- description: API for communication activities. You can retrieve data about communication activities. You can also marks calls, emails, texts as seen/read.
  name: SPOTIO Communication API
  slug: spotio-communication-api
- description: The controller is responsible for managing company templates. Templates for text messages and emails. The controller allows creating new templates which can include information about dataObjects and c
  name: SPOTIO Communication Templates API
  slug: spotio-communicationtemplates-api
- description: The controller is responsible for managing company links (connectors). The controller allows creating new connectors which user can use them on web or mobile app. Connector can can include information
  name: SPOTIO Connectors API
  slug: spotio-connectors-api
- description: The controller is responsible for gets information about contracts templates and signed documents / files.
  name: SPOTIO Contracts API
  slug: spotio-contracts-api
- description: The controller is responsible for manages the data objects and their related operations like creating, retrieving, updating, and deleting data objects, as well as some bulk actions.
  name: SPOTIO Data Objects API
  slug: spotio-dataobjects-api
- description: 'Bulk operations on data objects. Flow: Create job -> Upload NDJSON data -> Start processing -> Poll progress -> Download results -> Cleanup.'
  name: SPOTIO Data Objects Bulk Jobs API
  slug: spotio-dataobjectsbulkjobs-api
- description: 'This controller is responsible for searching data objects. There are available endpoints for: * simple global searches - return only basic information about data objects * searching on lists - return '
  name: SPOTIO Data Objects Search API
  slug: spotio-dataobjectssearch-api
- description: The controller is responsible for handling the upload and retrieval of documents. Documents can be attached to data object, activity or be available company wide.
  name: SPOTIO Documents API
  slug: spotio-documents-api
- description: The controller is responsible for exporting data from the application, such as exporting dataObjects (leads) and activities. The result of the export is a CSV file.
  name: SPOTIO Exports API
  slug: spotio-exports-api
- description: The controller is responsible for handling operations on filter objects. Filter can be used throughout the system to filter data. It can be passed wherever filterId query parameter or property is avai
  name: SPOTIO Filters API
  slug: spotio-filters-api
- description: The controller is responsible for handling operations on filter objects. Filter can be used throughout the system to filter data. It can be passed wherever filterId query parameter or property is avai
  name: SPOTIO Filters V2 API
  slug: spotio-filtersv2-api
- description: The controller is responsible for content generating for text messages and emails.
  name: SPOTIO Generate Content API
  slug: spotio-generatecontent-api
- description: The Layouts API from SPOTIO — 8 operation(s) for layouts.
  name: SPOTIO Layouts API
  slug: spotio-layouts-api
- description: The controller is responsible for leaderboards.
  name: SPOTIO Leaderboards API
  slug: spotio-leaderboards-api
- description: 'The controller is responsible for handling operations related to MCP. It provides endpoints for generating, retrieving, deactivating, and regenerating MCP keys. These keys are used for authenticating '
  name: SPOTIO MCP API
  slug: spotio-mcp-api
- description: The controller is responsible for text messages management. Sending messages to customers
  name: SPOTIO Multi Channel Communication API
  slug: spotio-multichannelcommunication-api
- description: The controller is responsible for managing MyReports in a web application, creation, updating and rendering MyReports.
  name: SPOTIO My Reports API
  slug: spotio-myreports-api
- description: The controller is responsible for handling operations on notification objects. Notifications are created automatically when creating appointments with reminder property set. Push notifications are sup
  name: SPOTIO Notifications V2 API
  slug: spotio-notificationsv2-api
- description: Pins API handles searching and retrieving pins with details. It provides operations including fetching pins by viewport, getting pin details with data objects, searching for pins with specific criteri
  name: SPOTIO Pins V2 API
  slug: spotio-pinsv2-api
- description: The controller is responsible exporting data by selected report type.
  name: SPOTIO Reports API
  slug: spotio-reports-api
- description: API for routes. You can manage routes and calculate route based on stops list. You can also start a new trip based on the route.
  name: SPOTIO Routes V2 API
  slug: spotio-routesv2-api
- description: The controller is responsible for handling operations on teams creating, updating, deleting, and retrieving team data. The controller also handles adding users to teams, getting a list of all teams in
  name: SPOTIO Teams API
  slug: spotio-teams-api
- description: The controller is responsible for getting all territories for a company.
  name: SPOTIO Territories API
  slug: spotio-territories-api
- description: The controller is responsible for handling operations on trip objects. Trips are created from routes and record places that user visited during the trip. Some apis are exposed through Trips and some t
  name: SPOTIO Trips API
  slug: spotio-trips-api
- description: The controller is responsible for handling operations on trip objects. Trips are created from routes and record places that user visited during the trip. Some apis are exposed through Trips and some t
  name: SPOTIO Trips V2 API
  slug: spotio-tripsv2-api
- description: Handles file upload operations
  name: SPOTIO Upload Care API
  slug: spotio-uploadcare-api
- description: The controller is responsible for handling the creation, updating, deleting Spotio Users. This controller allow users to exchange of credentials for a token.
  name: SPOTIO Users API
  slug: spotio-users-api
- description: User tracking API. You can configure Spotio to track users which using the app. Using the following methods you can retrieve tracking data.
  name: SPOTIO User Tracking API
  slug: spotio-usertracking-api
- description: The controller is responsible for handling webhooks related operations. It provides methods for retrieving available webhook scopes, getting all webhooks for the current company, creating a new webhoo
  name: SPOTIO Webhooks API
  slug: spotio-webhooks-api
- description: Activity templates are used to define type of activities in the system. To create activity from the activity template refer to the ActivitiesController. Each activity template can have multiple activi
  name: SPOTIO Workflow Activity Templates API
  slug: spotio-workflowactivitytemplates-api
- description: This controller is responsible for managing data object definitions. Data object definition consists of field and stages definitions. To create records from the definition refer to DataObjectsControll
  name: SPOTIO Workflow Data Objects API
  slug: spotio-workflowdataobjects-api
- description: Api is responsible for the comprehensive management of fields associated with data objects within a workflow. This includes functionality for retrieving available and existing fields, creating new fie
  name: SPOTIO Workflow Fields API
  slug: spotio-workflowfields-api
- description: Workflow Settings API provides operations including fetching full workflow settings for company as well as retrieving and updating workflow company properties.
  name: SPOTIO Workflow Settings API
  slug: spotio-workflowsettings-api
- description: 'This controller is responsible for managing stages definitions. You can split stages in 3 groups, each group can have different set of stages. The available groups are: active, won and lost. Stages ca'
  name: SPOTIO Workflow Stages API
  slug: spotio-workflowstages-api
artifact_total: 87
asyncapis:
- description: ''
  name: Spotio Webhooks
  slug: spotio-webhooks
collections:
- collection_type: open
  name: Spotio 2.0 Activities V2 API
  slug: open-spotio-activitiesv2-api
- collection_type: open
  name: Spotio 2.0 Appointments V2 API
  slug: open-spotio-appointmentsv2-api
- collection_type: open
  name: Spotio 2.0 Autoplays API
  slug: open-spotio-autoplays-api
- collection_type: open
  name: Spotio 2.0 Business Cards API
  slug: open-spotio-businesscards-api
- collection_type: open
  name: Spotio 2.0 Calendar Settings API
  slug: open-spotio-calendarsettings-api
- collection_type: open
  name: Spotio 2.0 Communication API
  slug: open-spotio-communication-api
- collection_type: open
  name: Spotio 2.0 Communication Templates API
  slug: open-spotio-communicationtemplates-api
- collection_type: open
  name: Spotio 2.0 Connectors API
  slug: open-spotio-connectors-api
- collection_type: open
  name: Spotio 2.0 Contracts API
  slug: open-spotio-contracts-api
- collection_type: open
  name: Spotio 2.0 Data Objects API
  slug: open-spotio-dataobjects-api
- collection_type: open
  name: Spotio 2.0 Data Objects Bulk Jobs API
  slug: open-spotio-dataobjectsbulkjobs-api
- collection_type: open
  name: Spotio 2.0 Data Objects Search API
  slug: open-spotio-dataobjectssearch-api
- collection_type: open
  name: Spotio 2.0 Documents API
  slug: open-spotio-documents-api
- collection_type: open
  name: Spotio 2.0 Exports API
  slug: open-spotio-exports-api
- collection_type: open
  name: Spotio 2.0 Filters API
  slug: open-spotio-filters-api
- collection_type: open
  name: Spotio 2.0 Filters V2 API
  slug: open-spotio-filtersv2-api
- collection_type: open
  name: Spotio 2.0 Generate Content API
  slug: open-spotio-generatecontent-api
- collection_type: open
  name: Spotio 2.0 Layouts API
  slug: open-spotio-layouts-api
- collection_type: open
  name: Spotio 2.0 Leaderboards API
  slug: open-spotio-leaderboards-api
- collection_type: open
  name: Spotio 2.0 MCP API
  slug: open-spotio-mcp-api
- collection_type: open
  name: Spotio 2.0 Multi Channel Communication API
  slug: open-spotio-multichannelcommunication-api
- collection_type: open
  name: Spotio 2.0 My Reports API
  slug: open-spotio-myreports-api
- collection_type: open
  name: Spotio 2.0 Notifications V2 API
  slug: open-spotio-notificationsv2-api
- collection_type: open
  name: Spotio 2.0 Pins V2 API
  slug: open-spotio-pinsv2-api
- collection_type: open
  name: Spotio 2.0 Reports API
  slug: open-spotio-reports-api
- collection_type: open
  name: Spotio 2.0 Routes V2 API
  slug: open-spotio-routesv2-api
- collection_type: open
  name: Spotio 2.0 Teams API
  slug: open-spotio-teams-api
- collection_type: open
  name: Spotio 2.0 Territories API
  slug: open-spotio-territories-api
- collection_type: open
  name: Spotio 2.0 Trips API
  slug: open-spotio-trips-api
- collection_type: open
  name: Spotio 2.0 Trips V2 API
  slug: open-spotio-tripsv2-api
- collection_type: open
  name: Spotio 2.0 Upload Care API
  slug: open-spotio-uploadcare-api
- collection_type: open
  name: Spotio 2.0 Users API
  slug: open-spotio-users-api
- collection_type: open
  name: Spotio 2.0 User Tracking API
  slug: open-spotio-usertracking-api
- collection_type: open
  name: Spotio 2.0 Webhooks API
  slug: open-spotio-webhooks-api
- collection_type: open
  name: Spotio 2.0 Workflow Activity Templates API
  slug: open-spotio-workflowactivitytemplates-api
- collection_type: open
  name: Spotio 2.0 Workflow Data Objects API
  slug: open-spotio-workflowdataobjects-api
- collection_type: open
  name: Spotio 2.0 Workflow Fields API
  slug: open-spotio-workflowfields-api
- collection_type: open
  name: Spotio 2.0 Workflow Settings API
  slug: open-spotio-workflowsettings-api
- collection_type: open
  name: Spotio 2.0 Workflow Stages API
  slug: open-spotio-workflowstages-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spotio-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spotio-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/spotio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spotio-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spotio
- group: company
  title: ''
  type: Website
  url: https://spotio.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.spotio2.com/
- group: design
  title: ''
  type: Webhooks
  url: https://support.spotio.com/hc/en-us/articles/360057063834-Webhooks
- group: commercial
  title: ''
  type: Plans
  url: plans/spotio-plans-pricing.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/spotio-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/spotio-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spotio-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spotio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spotio-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spotio-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spotio-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.spotio2.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/spotio-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.spotio.com/release-notes
- group: design
  title: ''
  type: Conformance
  url: conformance/spotio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://spotio.com/features/security-compliance/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/spotio-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/spotio-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spotio-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/spotio-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.spotio2.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.spotio2.com/docs/spotio2/c977e70019695-spotio-2-0
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.spotio2.com/docs/spotio2/a4cpj8d1knctg-quickstart-for-the-spotio-api
- group: operate
  title: ''
  type: Support
  url: https://support.spotio.com/
- group: company
  title: ''
  type: Blog
  url: https://spotio.com/resources/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Spotio
- group: commercial
  title: ''
  type: Pricing
  url: https://spotio.com/plans/
- group: start
  title: ''
  type: Login
  url: https://app.spotio2.com/
- group: start
  title: ''
  type: SignUp
  url: https://spotio.com/request-a-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://spotio.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spotio.com/privacy-policy/
created: '2026-07-04'
description: 'SPOTIO is a field sales engagement and territory management platform for outside sales teams - lead and prospect tracking, activity logging, territory mapping and assignment, route optimization, appointment setting, and pipeline visibility, delivered through a mobile-first field app and a web console. Behind that product is a substantial and genuinely public API: SPOTIO 2.0 is an OpenAPI 3.0.1 contract of 238 paths and 295 operations across 39 capabilities, published from SPOTIO''s own Stoplight project at developer.spotio2.com and exportable without authentication. Authentication is a bearer JWT minted from a clientId/secret pair; collections page on a scrollId cursor; and SPOTIO''s data model is polymorphic - there is no fixed Lead entity, only a tenant-defined DataObject whose types, stages and fields are read from a Workflow before anything can be written. SPOTIO also operates a first-party remote MCP server at app.spotio2.com/mcp, authenticated with a SPOTIO-MCP-KEY that
  the API itself mints, plus a signed outbound webhook system covering ten lead, activity and appointment events. It publishes no SDK in any language, no idempotency contract, no rate limits and no security.txt.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spotio.png
layout: provider
mcp_servers:
- description: ''
  name: spotio-mcp.yml
  slug: spotio-mcpyml
modified: '2026-08-13'
name: SPOTIO
nav: Providers
network: true
overview: 'SPOTIO publishes 39 APIs on the [APIs.io](https://apis.io/) network, including Activities V2 API, Appointments V2 API, Autoplays API, and 36 more. Tagged areas include Field Sales, Sales Engagement, Territory Management, CRM, and Lead Tracking.


  The SPOTIO catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SPOTIO''s developer surface includes authentication, documentation, changelog, sandbox, API reference, getting-started guide, support, and 30 more developer resources.'
plans:
- name: Spotio Plans Pricing
  plan_count: 3
  slug: spotio-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Spotio Rate Limits
  slug: spotio-rate-limits
score:
  band: strong
  composite: 62.1
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 30.3
    contract_quality: 62.6
    developer_ergonomics: 66.1
    discoverability: 57.4
    governance: 30.3
    operational_transparency: 42.1
  previous_composite: 62.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 39
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spotio/refs/heads/main/screenshots/spotio-2026-08-17T082034.png
security:
- kind: authentication
  name: Spotio Authentication
  slug: spotio-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Spotio Domain Security
  slug: spotio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spotio Vulnerability Disclosure
  slug: spotio-vulnerability-disclosure
  summary_line: Hackerone · security.txt
- kind: trust-center
  name: Spotio Trust Center
  slug: spotio-trust-center
  summary_line: SOC 2, GDPR
slug: spotio
tags:
- Field Sales
- Sales Engagement
- Territory Management
- CRM
- Lead Tracking
- Outside Sales
- Sales Enablement
- Route Optimization
- Geospatial
- Webhooks
- MCP
- Door to Door
website: https://spotio.com
---
