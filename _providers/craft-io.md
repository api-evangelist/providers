---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Craft Io Agentic Access
  operation_count: 27
  slug: craft-io-agentic-access
  summary_line: 27 operations · 5 acting
api_count: 9
apis:
- description: REST API providing access to workspace data including work items, custom fields, terminology, initiatives, products, epics, features, and stories within Craft.io product workspaces.
  name: Craft.io Workspace API
  slug: craftio-workspace-api
- description: REST API providing access to portfolio data including portfolio items, portfolio custom fields, and terminology for enterprise product portfolio management.
  name: Craft.io Portfolio API
  slug: craftio-portfolio-api
- description: REST API for managing customer feedback portals, including listing portals and categories, retrieving feedback items, and submitting new feedback via POST requests.
  name: Craft.io Feedback Portal API
  slug: craftio-feedback-portal-api
- description: Feedback items are the main building blocks of your product’s feedback process.
  name: Craft.io Feedback items API
  slug: craft-io-feedback-items-api
- description: Feedback portals are the areas where various stakeholders submit their product related feedbacks
  name: Craft.io Feedback Portals API
  slug: craft-io-feedback-portals-api
- description: The Introspection API from Craft.io — 1 operation(s) for introspection.
  name: Craft.io Introspection API
  slug: craft-io-introspection-api
- description: The Portfolios API from Craft.io — 3 operation(s) for portfolios.
  name: Craft.io Portfolios API
  slug: craft-io-portfolios-api
- description: Work items are the main building blocks of your product’s roadmap, and include Products, Epics, Features and Sub Features.<br /> OKRs are the goal-setting framework of your product’s roadmap, and incl
  name: Craft.io Work Items and OKRs API
  slug: craft-io-work-items-and-okrs-api
- description: Workspaces are the areas where product teams are managing the full lifecycle of their products
  name: Craft.io Workspaces API
  slug: craft-io-workspaces-api
artifact_total: 69
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/craft-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/craft-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/craft-io-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://craft.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.craft.io/en/articles/8385550-craft-io-public-apis-for-workspace-portfolio-and-feedback-portal
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/io-craft-org
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/craft.io
- group: company
  title: ''
  type: Blog
  url: https://craft.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://craft.io/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://craftio.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://x.com/createwithcraft
- group: commercial
  title: ''
  type: Plans
  url: plans/craft-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/craft-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/craft-io-finops.yml
created: '2026-06-13'
description: Craft.io is a product management platform with a REST API for managing product backlog, specifications, OKRs, roadmaps, and customer feedback across product teams. The public API provides enterprise customers programmatic access to workspace, portfolio, and feedback portal data, enabling integration with BI tools and organizational communication channels.
examples:
- key_count: 43
  name: Craft Io Getitemflat 200 Example
  slug: craft-io-getitemflat-200-example
- key_count: 2
  name: Craft Io Getitemsflat 200 Example
  slug: craft-io-getitemsflat-200-example
- key_count: 3
  name: Craft Io Postidea 200 Example
  slug: craft-io-postidea-200-example
- key_count: 3
  name: Craft Io Postplainidea 200 Example
  slug: craft-io-postplainidea-200-example
finops:
- name: Craft Io Finops
  service_category: ''
  slug: craft-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/craft-io.png
json_schemas:
- name: ApiKeyIntrospection
  property_count: 5
  slug: craft-io-apikeyintrospection
- name: Assignee
  property_count: 3
  slug: craft-io-assignee
- name: BaseFeedbackItem
  property_count: 16
  slug: craft-io-basefeedbackitem
- name: Category
  property_count: 2
  slug: craft-io-category
- name: ConnectionUpdateRequest
  property_count: 5
  slug: craft-io-connectionupdaterequest
- name: CustomField
  property_count: 6
  slug: craft-io-customfield
- name: CustomFieldOption
  property_count: 4
  slug: craft-io-customfieldoption
- name: CustomFieldValue
  property_count: 5
  slug: craft-io-customfieldvalue
- name: Dependency
  property_count: 5
  slug: craft-io-dependency
- name: DevToolKeyList
  property_count: 6
  slug: craft-io-devtoolkeylist
- name: Entity
  property_count: 2
  slug: craft-io-entity
- name: EntityId
  property_count: 1
  slug: craft-io-entityid
- name: EntityParent
  property_count: 4
  slug: craft-io-entityparent
- name: EntityWithDates
  property_count: 4
  slug: craft-io-entitywithdates
- name: EntityWithTerminology
  property_count: 3
  slug: craft-io-entitywithterminology
- name: FeedbackItem
  property_count: 0
  slug: craft-io-feedbackitem
- name: FeedbackItemsPaginated_FeedbackItem_
  property_count: 2
  slug: craft-io-feedbackitemspaginated-feedbackitem-
- name: FeedbackLink
  property_count: 5
  slug: craft-io-feedbacklink
- name: FeedbackPortal
  property_count: 5
  slug: craft-io-feedbackportal
- name: FormCustomField
  property_count: 7
  slug: craft-io-formcustomfield
- name: GeneralErrorResponse
  property_count: 1
  slug: craft-io-generalerrorresponse
- name: IdeaRequest
  property_count: 8
  slug: craft-io-idearequest
- name: Initiative
  property_count: 0
  slug: craft-io-initiative
- name: Item
  property_count: 37
  slug: craft-io-item
- name: ItemCreate
  property_count: 25
  slug: craft-io-itemcreate
- name: ItemFlat
  property_count: 50
  slug: craft-io-itemflat
- name: ItemsPaginated_Initiative_
  property_count: 2
  slug: craft-io-itemspaginated-initiative-
- name: ItemsPaginated_Item_
  property_count: 2
  slug: craft-io-itemspaginated-item-
- name: ItemsPaginated_ItemFlat_
  property_count: 2
  slug: craft-io-itemspaginated-itemflat-
- name: ItemUpdate
  property_count: 24
  slug: craft-io-itemupdate
- name: LinkedItem
  property_count: 4
  slug: craft-io-linkeditem
- name: Omit_Item.workspaceId-or-initiativeId-or-sprint-or-quarter-or-assignee-or-storyPoints-or-estimatedHours-or-objective-or-keyResult-or-persona-or-personas-or-parent-or-labels-or-kano_
  property_count: 0
  slug: craft-io-omit-item.workspaceid-or-initiativeid-or-sprint-or-quarter-or-assignee-or-storypoints-or-estimatedhours-or-objective-or-keyresult-or-persona-or-personas-or-parent-or-labels-or-kano-
- name: OptionShape
  property_count: 0
  slug: craft-io-optionshape
- name: OutIn
  property_count: 2
  slug: craft-io-outin
- name: PaginationMetadata
  property_count: 4
  slug: craft-io-paginationmetadata
- name: Person
  property_count: 3
  slug: craft-io-person
- name: Persona
  property_count: 3
  slug: craft-io-persona
- name: Pick_Item.Exclude_keyofItem.workspaceId-or-initiativeId-or-sprint-or-quarter-or-assignee-or-storyPoints-or-estimatedHours-or-objective-or-keyResult-or-persona-or-personas-or-parent-or-labels-or-kano__
  property_count: 23
  slug: craft-io-pick-item.exclude-keyofitem.workspaceid-or-initiativeid-or-sprint-or-quarter-or-assignee-or-storypoints-or-estimatedhours-or-objective-or-keyresult-or-persona-or-personas-or-parent-or-labels-or-kano--
- name: PlainIdeaRequest
  property_count: 7
  slug: craft-io-plainidearequest
- name: PortalForm
  property_count: 4
  slug: craft-io-portalform
- name: PortalImportance
  property_count: 3
  slug: craft-io-portalimportance
- name: Portfolio
  property_count: 4
  slug: craft-io-portfolio
- name: SlackConnection
  property_count: 5
  slug: craft-io-slackconnection
- name: SlackPortal
  property_count: 4
  slug: craft-io-slackportal
- name: SlackTeamInfo
  property_count: 0
  slug: craft-io-slackteaminfo
- name: TeamInfo
  property_count: 2
  slug: craft-io-teaminfo
- name: Terminology
  property_count: 4
  slug: craft-io-terminology
- name: ValidateErrorJSON
  property_count: 2
  slug: craft-io-validateerrorjson
- name: Workspace
  property_count: 4
  slug: craft-io-workspace
jsonld:
- class_count: 42
  name: Craft Io Context
  property_count: 4
  slug: craft-io-context
layout: provider
modified: '2026-06-13'
name: Craft.io
nav: Providers
network: true
overview: 'Craft.io publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Workspace API, Portfolio API, Feedback Portal API, and 6 more. Tagged areas include Product Management, Roadmaps, OKRs, Backlog, and Feedback.


  The Craft.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Craft.io''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Craft Io Plans Pricing
  plan_count: 3
  slug: craft-io-plans-pricing
random_paper: 93
rules:
- name: Craft.io API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: craft-io-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.6
  delta: -0.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 47.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/craft-io/refs/heads/main/screenshots/craft-io-2026-06-20T175212.png
security:
- kind: authentication
  name: Craft Io Authentication
  slug: craft-io-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Craft Io Domain Security
  slug: craft-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: craft-io
tags:
- Product Management
- Roadmaps
- OKRs
- Backlog
- Feedback
- Portfolio
- Specifications
website: https://craft.io/
---
