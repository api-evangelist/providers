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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: documented
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 60.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 65
  human_in_the_loop: 0
  name: Cint Agentic Access
  operation_count: 158
  slug: cint-agentic-access
  summary_line: 158 operations · 65 acting
api_count: 25
apis:
- description: Endpoints for managing Accounts-related resources, such as users.
  name: Cint Accounts API
  slug: cint-accounts-api
- description: Create, update, delete and list global and account Allocation templates. Templates allow you to store and automate your policy towards suppliers on the Exchange.
  name: Cint Allocation Templates Admin API
  slug: cint-allocation-templates-admin-api
- description: Platform-wide definitions endpoints.
  name: Cint Definitions API
  slug: cint-definitions-api
- description: For more information, if you need functionality in this section, please contact your account manager
  name: Cint Exclusive Endpoints API
  slug: cint-exclusive-endpoints-api
- description: Understand the success of the Target Groups you want to run, have already saved or are in field by providing a Target Group ID or details.
  name: Cint Feasibility API
  slug: cint-feasibility-api
- description: Create, update and obtain Target Group Fielding runs and Fielding Assistant assignments. This is critical for launching, scheduling and completing Target Groups.
  name: Cint Fielding API
  slug: cint-fielding-api
- description: Get, update Target Group Fielding Assistant assignments. Fielding Assistant provides optional modules to automate common workflows and optimise your Target Group.
  name: Cint Fielding Assistant API
  slug: cint-fielding-assistant-api
- description: Asynchronously update Target Group Fielding Runs in batches.
  name: Cint Fielding (Batch) API
  slug: cint-fielding-batch-api
- description: ':::info Fulfillment endpoints are for S2S enabled clients only. ::: Endpoints for managing respondent statuses while a target group is fielding.'
  name: Cint Fulfillment API
  slug: cint-fulfillment-api
- description: Select the best times for launching your Target Groups. Use before feasibility to optimise fill and time in field.
  name: Cint Intelligent Calendar API
  slug: cint-intelligent-calendar-api
- description: Management of Target Group profiles after launch—including creating, updating, retrieving, and deleting profile configurations, along with their conditions, quotas, and interlock settings.
  name: Cint Manage Profiles for Launched Target Groups API
  slug: cint-manage-profiles-for-launched-target-groups-api
- description: Endpoints for managing your Notifications Webhooks.
  name: Cint Notifications Webhooks API
  slug: cint-notifications-webhooks-api
- description: Helps by generating different profile configurations, including interlocked profiles for draft.
  name: Cint Profiling Helper API
  slug: cint-profiling-helper-api
- description: List all profiling questions including account specific questions with translations and categories. Profiling questions allow you to target and filter respondents based on their characteristics.
  name: Cint Profiling Library API
  slug: cint-profiling-library-api
- description: Get the distribution of available respondents for Target Group profiles, including retrieving supplier distribution per quota.
  name: Cint Profiling Quotas By Supplier API
  slug: cint-profiling-quotas-by-supplier-api
- description: Create, manage and reuse audience descriptions and templates to allow for efficient and automated targeting workflows on the Cint Exchange.
  name: Cint Profiling Templates API
  slug: cint-profiling-templates-api
- description: Create, list and update projects. Projects are a flexible container for Target Groups and enable basic aggregation and automation.
  name: Cint Projects API
  slug: cint-projects-api
- description: Validate, Submit and check reconciliations for one or more target groups.
  name: Cint Reconciliations API
  slug: cint-reconciliations-api
- description: Create, update, list and delete recontacts for a target group. Recontacts allow only specific respondents to enter your survey and are part of a larger workflow that needs specific configurations acro
  name: Cint Recontacts API
  slug: cint-recontacts-api
- description: Aggregate reports that roll statistics up on an _Account_, _Business Unit_, _Project_ and _Target Group_ level.
  name: Cint Reports API
  slug: cint-reports-api
- description: The Respondent Exclusions API from Cint — 17 operation(s) for respondent exclusions.
  name: Cint Respondent Exclusions API
  slug: cint-respondent-exclusions-api
- description: Allows you to insert respondent unique code(s) into the survey URL for each respondent entering the session.
  name: Cint Respondent Unique Codes API
  slug: cint-respondent-unique-codes-api
- description: Create, update, list supplier allocations for a target group. Allocations allow filtering and limiting of the available suppliers on the Exchange.
  name: Cint Target Group Allocations API
  slug: cint-target-group-allocations-api
- description: Create, update, list and other operations on Target Groups. A Target Group is the main unit of work in the Exchange.
  name: Cint Target Groups API
  slug: cint-target-groups-api
- description: Asynchronously create, update and delete Target Groups in batches.
  name: Cint Target Groups (Batch) API
  slug: cint-target-groups-batch-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Create a project and target group, check feasibility, then launch a fielding run.
  name: Launch a Cint Exchange Target Group
  slug: cint-launch-target-group
artifact_total: 33
asyncapis:
- description: ''
  name: Cint Webhooks
  slug: cint-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cint.com/demand/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.cint.com/demand/docs/2025-12-18/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cint.com/demand/docs/2025-12-18/reference/demand-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.cint.com/demand/docs/2025-12-18/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://www.cint.com/start-integration/
- group: operate
  title: ''
  type: Support
  url: https://help.cint.com/
- group: company
  title: ''
  type: Blog
  url: https://www.cint.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cint.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.cint.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cint.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cint.com/
- group: auth
  title: ''
  type: Compliance
  url: security/cint-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cint-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cint-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cint-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cint-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/cint-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cint-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cint-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cint-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cint-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cint-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cint-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cint-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cint-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/cint-demand-overlay.yaml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cint-launch-target-group.yml
created: '2026-07-17'
description: 'Cint is the world''s largest global research marketplace, connecting researchers, brands, and agencies with millions of survey respondents across 130+ countries. The Cint Exchange Demand API is a REST API for buying market-research sample programmatically: create projects and target groups, run feasibility, launch and manage fielding runs, handle respondent exclusions and recontacts, reconcile completed interviews, and receive event notifications via webhooks. Cint also operates Lucid Measurement (ad-campaign brand lift) and Cint Engage (audience monetization). Surfaced as a Creandum portfolio company and enriched from Cint''s public developer portal.'
image: https://www.cint.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: cint-mcp.yml
  slug: cint-mcpyml
modified: '2026-07-18'
name: Cint
nav: Providers
network: true
overview: 'Cint publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Allocation Templates Admin API, Definitions API, and 22 more. Tagged areas include Company, Market Research, Survey Sample, Consumer Insights, and Data Collection.


  The Cint catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cint''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 21 more developer resources.'
random_paper: 30
score:
  band: developing
  composite: 53.7
  delta: -1.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.0
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 39.5
  previous_composite: 55.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cint/refs/heads/main/screenshots/cint-2026-07-25T205351.png
security:
- kind: authentication
  name: Cint Authentication
  slug: cint-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Cint Domain Security
  slug: cint-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Cint Trust Center
  slug: cint-trust-center
  summary_line: ISO 20252:2019, Cyber Essentials
slug: cint
tags:
- Company
- Market Research
- Survey Sample
- Consumer Insights
- Data Collection
- Ad Measurement
- Marketplace
- Panel
website: https://developer.cint.com/demand/
---
