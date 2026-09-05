---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 65
  human_in_the_loop: 0
  name: Cint Agentic Access
  operation_count: 158
  slug: cint-agentic-access
  summary_line: 158 operations · 65 acting
api_count: 1
apis:
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Endpoints for managing Accounts-related resources, such as users.
  name: Cint Accounts API
  slug: cint-accounts-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Create, update, delete and list global and account Allocation templates. Templates allow you to store and automate your policy towards suppliers on the Exchange.
  name: Cint Allocation Templates Admin API
  slug: cint-allocation-templates-admin-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Platform-wide definitions endpoints.
  name: Cint Definitions API
  slug: cint-definitions-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: For more information, if you need functionality in this section, please contact your account manager
  name: Cint Exclusive Endpoints API
  slug: cint-exclusive-endpoints-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Understand the success of the Target Groups you want to run, have already saved or are in field by providing a Target Group ID or details.
  name: Cint Feasibility API
  slug: cint-feasibility-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Create, update and obtain Target Group Fielding runs and Fielding Assistant assignments. This is critical for launching, scheduling and completing Target Groups.
  name: Cint Fielding API
  slug: cint-fielding-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Get, update Target Group Fielding Assistant assignments. Fielding Assistant provides optional modules to automate common workflows and optimise your Target Group.
  name: Cint Fielding Assistant API
  slug: cint-fielding-assistant-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Asynchronously update Target Group Fielding Runs in batches.
  name: Cint Fielding (Batch) API
  slug: cint-fielding-batch-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: ':::info Fulfillment endpoints are for S2S enabled clients only. ::: Endpoints for managing respondent statuses while a target group is fielding.'
  name: Cint Fulfillment API
  slug: cint-fulfillment-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Select the best times for launching your Target Groups. Use before feasibility to optimise fill and time in field.
  name: Cint Intelligent Calendar API
  slug: cint-intelligent-calendar-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Management of Target Group profiles after launch—including creating, updating, retrieving, and deleting profile configurations, along with their conditions, quotas, and interlock settings.
  name: Cint Manage Profiles for Launched Target Groups API
  slug: cint-manage-profiles-for-launched-target-groups-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Endpoints for managing your Notifications Webhooks.
  name: Cint Notifications Webhooks API
  slug: cint-notifications-webhooks-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Helps by generating different profile configurations, including interlocked profiles for draft.
  name: Cint Profiling Helper API
  slug: cint-profiling-helper-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: List all profiling questions including account specific questions with translations and categories. Profiling questions allow you to target and filter respondents based on their characteristics.
  name: Cint Profiling Library API
  slug: cint-profiling-library-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Get the distribution of available respondents for Target Group profiles, including retrieving supplier distribution per quota.
  name: Cint Profiling Quotas By Supplier API
  slug: cint-profiling-quotas-by-supplier-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Create, manage and reuse audience descriptions and templates to allow for efficient and automated targeting workflows on the Cint Exchange.
  name: Cint Profiling Templates API
  slug: cint-profiling-templates-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Create, list and update projects. Projects are a flexible container for Target Groups and enable basic aggregation and automation.
  name: Cint Projects API
  slug: cint-projects-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Validate, Submit and check reconciliations for one or more target groups.
  name: Cint Reconciliations API
  slug: cint-reconciliations-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Create, update, list and delete recontacts for a target group. Recontacts allow only specific respondents to enter your survey and are part of a larger workflow that needs specific configurations acro
  name: Cint Recontacts API
  slug: cint-recontacts-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Aggregate reports that roll statistics up on an _Account_, _Business Unit_, _Project_ and _Target Group_ level.
  name: Cint Reports API
  slug: cint-reports-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: The Respondent Exclusions API from Cint — 17 operation(s) for respondent exclusions.
  name: Cint Respondent Exclusions API
  slug: cint-respondent-exclusions-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Allows you to insert respondent unique code(s) into the survey URL for each respondent entering the session.
  name: Cint Respondent Unique Codes API
  slug: cint-respondent-unique-codes-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Create, update, list supplier allocations for a target group. Allocations allow filtering and limiting of the available suppliers on the Exchange.
  name: Cint Target Group Allocations API
  slug: cint-target-group-allocations-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Create, update, list and other operations on Target Groups. A Target Group is the main unit of work in the Exchange.
  name: Cint Target Groups API
  slug: cint-target-groups-api
- baseURL: https://api.cint.com/v1
  baseurl_source: declared
  description: Asynchronously create, update and delete Target Groups in batches.
  name: Cint Target Groups (Batch) API
  slug: cint-target-groups-batch-api
arazzos:
- description: Create a project and target group, check feasibility, then launch a fielding run.
  name: Launch a Cint Exchange Target Group
  slug: cint-launch-target-group
artifact_total: 57
asyncapis:
- description: ''
  name: Cint Webhooks
  slug: cint-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Demand Accounts API
  slug: open-cint-accounts-api
- collection_type: open
  name: Demand Accounts Allocation Templates Admin API
  slug: open-cint-allocation-templates-admin-api
- collection_type: open
  name: Demand Accounts Definitions API
  slug: open-cint-definitions-api
- collection_type: open
  name: Demand Accounts Exclusive Endpoints API
  slug: open-cint-exclusive-endpoints-api
- collection_type: open
  name: Demand Accounts Feasibility API
  slug: open-cint-feasibility-api
- collection_type: open
  name: Demand Accounts Fielding API
  slug: open-cint-fielding-api
- collection_type: open
  name: Demand Accounts Fielding Assistant API
  slug: open-cint-fielding-assistant-api
- collection_type: open
  name: Demand Accounts Fielding (Batch) API
  slug: open-cint-fielding-batch-api
- collection_type: open
  name: Demand Accounts Fulfillment API
  slug: open-cint-fulfillment-api
- collection_type: open
  name: Demand Accounts Intelligent Calendar API
  slug: open-cint-intelligent-calendar-api
- collection_type: open
  name: Demand Accounts Manage Profiles for Launched Target Groups API
  slug: open-cint-manage-profiles-for-launched-target-groups-api
- collection_type: open
  name: Demand Accounts Notifications Webhooks API
  slug: open-cint-notifications-webhooks-api
- collection_type: open
  name: Demand Accounts Profiling Helper API
  slug: open-cint-profiling-helper-api
- collection_type: open
  name: Demand Accounts Profiling Library API
  slug: open-cint-profiling-library-api
- collection_type: open
  name: Demand Accounts Profiling Quotas By Supplier API
  slug: open-cint-profiling-quotas-by-supplier-api
- collection_type: open
  name: Demand Accounts Profiling Templates API
  slug: open-cint-profiling-templates-api
- collection_type: open
  name: Demand Accounts Projects API
  slug: open-cint-projects-api
- collection_type: open
  name: Demand Accounts Reconciliations API
  slug: open-cint-reconciliations-api
- collection_type: open
  name: Demand Accounts Recontacts API
  slug: open-cint-recontacts-api
- collection_type: open
  name: Demand Accounts Reports API
  slug: open-cint-reports-api
- collection_type: open
  name: Demand Accounts Respondent Exclusions API
  slug: open-cint-respondent-exclusions-api
- collection_type: open
  name: Demand Accounts Respondent Unique Codes API
  slug: open-cint-respondent-unique-codes-api
- collection_type: open
  name: Demand Accounts Target Group Allocations API
  slug: open-cint-target-group-allocations-api
- collection_type: open
  name: Demand Accounts Target Groups API
  slug: open-cint-target-groups-api
- collection_type: open
  name: Demand Accounts Target Groups (Batch) API
  slug: open-cint-target-groups-batch-api
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
  type: X-MCPServerCandidate
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
modified: '2026-07-18'
name: Cint
nav: Providers
network: true
overview: 'Cint publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Allocation Templates Admin API, Definitions API, and 22 more. Tagged areas include Company, Market Research, Survey Sample, Consumer Insights, and Data Collection.


  The Cint catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cint''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 21 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 51.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 63.8
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 51.0
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
