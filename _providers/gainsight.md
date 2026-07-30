---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
- acting_count: 55
  human_in_the_loop: 0
  name: Gainsight Agentic Access
  operation_count: 97
  slug: gainsight-agentic-access
  summary_line: 97 operations · 55 acting
api_count: 29
apis:
- description: Manage account records and attributes
  name: Gainsight Accounts API
  slug: gainsight-accounts-api
- description: Manage timeline activities
  name: Gainsight Activities API
  slug: gainsight-activities-api
- description: Retrieve activity type configurations
  name: Gainsight Activity Types API
  slug: gainsight-activity-types-api
- description: CRUD operations on company records
  name: Gainsight Companies API
  slug: gainsight-companies-api
- description: Manage company team records
  name: Gainsight Company Team API
  slug: gainsight-company-team-api
- description: Success plan configuration
  name: Gainsight Configuration API
  slug: gainsight-configuration-api
- description: Retrieve CTA type and reason configurations
  name: Gainsight CTA Configuration API
  slug: gainsight-cta-configuration-api
- description: Create and manage Calls to Action
  name: Gainsight CTAs API
  slug: gainsight-ctas-api
- description: Send custom events for tracking
  name: Gainsight Custom Events API
  slug: gainsight-custom-events-api
- description: CRUD operations on custom object records
  name: Gainsight Custom Objects API
  slug: gainsight-custom-objects-api
- description: Manage in-app engagements
  name: Gainsight Engagements API
  slug: gainsight-engagements-api
- description: Publish and manage events
  name: Gainsight Events API
  slug: gainsight-events-api
- description: Track feature usage and adoption
  name: Gainsight Feature Match API
  slug: gainsight-feature-match-api
- description: Retrieve field metadata
  name: Gainsight Fields API
  slug: gainsight-fields-api
- description: Manage customer goals
  name: Gainsight Goals API
  slug: gainsight-goals-api
- description: Manage bulk import jobs
  name: Gainsight Jobs API
  slug: gainsight-jobs-api
- description: Manage goal metrics
  name: Gainsight Metrics API
  slug: gainsight-metrics-api
- description: Manage success plan objectives
  name: Gainsight Objectives API
  slug: gainsight-objectives-api
- description: Retrieve object metadata
  name: Gainsight Objects API
  slug: gainsight-objects-api
- description: Manage opportunity records
  name: Gainsight Opportunities API
  slug: gainsight-opportunities-api
- description: Manage person records
  name: Gainsight People API
  slug: gainsight-people-api
- description: Retrieve playbook configurations
  name: Gainsight Playbooks API
  slug: gainsight-playbooks-api
- description: Run reports and retrieve analytics data
  name: Gainsight Reports API
  slug: gainsight-reports-api
- description: SCIM provisioning endpoints
  name: Gainsight SCIM API
  slug: gainsight-scim-api
- description: Manage event subscriptions
  name: Gainsight Subscription API
  slug: gainsight-subscription-api
- description: Manage success plans
  name: Gainsight Success Plans API
  slug: gainsight-success-plans-api
- description: Manage tasks
  name: Gainsight Tasks API
  slug: gainsight-tasks-api
- description: Manage goal templates
  name: Gainsight Templates API
  slug: gainsight-templates-api
- description: Manage Gainsight users
  name: Gainsight Users API
  slug: gainsight-users-api
artifact_total: 125
collections:
- collection_type: open
  name: Gainsight CS Bulk API
  slug: open-gainsight-cs-bulk-api
- collection_type: open
  name: Gainsight CS Company API
  slug: open-gainsight-cs-company-api
- collection_type: open
  name: Gainsight CS CTA API
  slug: open-gainsight-cs-cta-api
- collection_type: open
  name: Gainsight CS Custom Object API
  slug: open-gainsight-cs-custom-object-api
- collection_type: open
  name: Gainsight CS Customer Goals API
  slug: open-gainsight-cs-customer-goals-api
- collection_type: open
  name: Gainsight CS Data Management API
  slug: open-gainsight-cs-data-management-api
- collection_type: open
  name: Gainsight CS Events API
  slug: open-gainsight-cs-events-api
- collection_type: open
  name: Gainsight CS Person API
  slug: open-gainsight-cs-person-api
- collection_type: open
  name: Gainsight CS Renewal Center API
  slug: open-gainsight-cs-renewal-center-api
- collection_type: open
  name: Gainsight CS Success Plan API
  slug: open-gainsight-cs-success-plan-api
- collection_type: open
  name: Gainsight CS Task and Playbook API
  slug: open-gainsight-cs-task-and-playbook-api
- collection_type: open
  name: Gainsight CS Timeline API
  slug: open-gainsight-cs-timeline-api
- collection_type: open
  name: Gainsight CS User Management API
  slug: open-gainsight-cs-user-management-api
- collection_type: open
  name: Gainsight PX API
  slug: open-gainsight-px-api
- collection_type: open
  name: Gainsight REST API
  slug: open-gainsight-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gainsight-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gainsight-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gainsight-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gainsight-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gainsight-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gainsight
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gainsight
- group: start
  title: ''
  type: Portal
  url: https://support.gainsight.com
- group: start
  title: ''
  type: Login
  url: https://app.gainsight.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gainsight.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gainsight.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://trust.gainsight.com/
- group: docs
  title: ''
  type: developer-docs
  url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs
- group: auth
  title: ''
  type: Authentication
  url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Generate_REST_API/Generate_REST_API_Key
- group: auth
  title: ''
  type: oauth
  url: https://support.gainsight.com/gainsight_nxt/01Onboarding_and_Implementation/Onboarding_for_Gainsight_NXT/Login_and_Permissions/OAuth_for_Gainsight_APIs
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://support.gainsight.com/gainsight_nxt/Release_Notes
- group: operate
  title: ''
  type: Community
  url: https://communities.gainsight.com
- group: company
  title: ''
  type: Blog
  url: https://www.gainsight.com/blog/
- group: other
  title: ''
  type: education
  url: https://education.gainsight.com
- group: design
  title: ''
  type: JSONLD
  url: json-ld/gainsight-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/gainsight-company-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/gainsight-person-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/gainsight-cta-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/gainsight-opportunity-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/gainsight-timeline-activity-schema.json
created: '2024'
description: Gainsight is a customer success platform that helps companies retain and grow their customer base through data-driven insights, automation, and engagement tools.
features:
- 'Essentials: 10 full users, 100 customers per user (custom price)'
- 'Enterprise: 20 full users, 200 customers per user (custom price)'
- AI Insights and Automations
- Customer 360 unified profile
- Playbooks and Success Plans
- Health Scorecards
- Surveys (CSAT, NPS)
- Digital Journeys for in-app onboarding
- Renewal and Expansion Forecasting (Enterprise)
- Org Mapping and Sponsor Tracking (Enterprise)
- REST API at api.gainsight.com
- Default 100 req/min/tenant
- OAuth 2.0 + access tokens
- Webhooks for customer health events
- Salesforce-native (Gainsight CS) or standalone (NXT)
- Unlimited Viewer Licenses on both tiers
finops:
- name: Gainsight Finops
  service_category: Customer Success
  slug: gainsight-finops
graphqls:
- description: Gainsight is a customer success platform that enables companies to retain and grow their customer base through health scoring, playbooks, engagement tracking, and renewal management. This conceptual G
  name: Gainsight GraphQL Schema
  slug: gainsight-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gainsight.png
json_schemas:
- name: Account
  property_count: 10
  slug: gainsight-account
- name: AccountInput
  property_count: 6
  slug: gainsight-accountinput
- name: Activity
  property_count: 15
  slug: gainsight-activity
- name: ActivityInput
  property_count: 9
  slug: gainsight-activityinput
- name: ActivityType
  property_count: 4
  slug: gainsight-activitytype
- name: ApiResponse
  property_count: 4
  slug: gainsight-apiresponse
- name: BulkJob
  property_count: 11
  slug: gainsight-bulkjob
- name: BulkJobError
  property_count: 3
  slug: gainsight-bulkjoberror
- name: Gainsight Company
  property_count: 18
  slug: gainsight-company
- name: CompanyInput
  property_count: 7
  slug: gainsight-companyinput
- name: CompanyRecord
  property_count: 18
  slug: gainsight-companyrecord
- name: CompanyTeamRecord
  property_count: 5
  slug: gainsight-companyteamrecord
- name: Gainsight Call to Action (CTA)
  property_count: 20
  slug: gainsight-cta
- name: CTAInput
  property_count: 10
  slug: gainsight-ctainput
- name: CTAPriority
  property_count: 3
  slug: gainsight-ctapriority
- name: CTAReason
  property_count: 3
  slug: gainsight-ctareason
- name: CTAStatus
  property_count: 3
  slug: gainsight-ctastatus
- name: CTAType
  property_count: 3
  slug: gainsight-ctatype
- name: CustomEvent
  property_count: 7
  slug: gainsight-customevent
- name: Engagement
  property_count: 5
  slug: gainsight-engagement
- name: EventInput
  property_count: 7
  slug: gainsight-eventinput
- name: EventType
  property_count: 4
  slug: gainsight-eventtype
- name: Feature
  property_count: 6
  slug: gainsight-feature
- name: FieldMetadata
  property_count: 10
  slug: gainsight-fieldmetadata
- name: GainsightUser
  property_count: 11
  slug: gainsight-gainsightuser
- name: GainsightUserInput
  property_count: 6
  slug: gainsight-gainsightuserinput
- name: Goal
  property_count: 13
  slug: gainsight-goal
- name: GoalInput
  property_count: 7
  slug: gainsight-goalinput
- name: GoalMetric
  property_count: 7
  slug: gainsight-goalmetric
- name: GoalMetricInput
  property_count: 4
  slug: gainsight-goalmetricinput
- name: GoalTemplate
  property_count: 5
  slug: gainsight-goaltemplate
- name: Objective
  property_count: 10
  slug: gainsight-objective
- name: ObjectiveInput
  property_count: 5
  slug: gainsight-objectiveinput
- name: ObjectMetadata
  property_count: 9
  slug: gainsight-objectmetadata
- name: Gainsight Opportunity
  property_count: 20
  slug: gainsight-opportunity
- name: OpportunityRecord
  property_count: 20
  slug: gainsight-opportunityrecord
- name: Gainsight Person
  property_count: 18
  slug: gainsight-person
- name: PersonRecord
  property_count: 19
  slug: gainsight-personrecord
- name: Playbook
  property_count: 8
  slug: gainsight-playbook
- name: ScimUser
  property_count: 7
  slug: gainsight-scimuser
- name: ScimUserInput
  property_count: 5
  slug: gainsight-scimuserinput
- name: SearchRequest
  property_count: 5
  slug: gainsight-searchrequest
- name: SearchResponse
  property_count: 2
  slug: gainsight-searchresponse
- name: Subscription
  property_count: 5
  slug: gainsight-subscription
- name: SubscriptionInput
  property_count: 3
  slug: gainsight-subscriptioninput
- name: SuccessPlan
  property_count: 14
  slug: gainsight-successplan
- name: SuccessPlanInput
  property_count: 8
  slug: gainsight-successplaninput
- name: Task
  property_count: 16
  slug: gainsight-task
- name: TaskInput
  property_count: 7
  slug: gainsight-taskinput
- name: Gainsight Timeline Activity
  property_count: 15
  slug: gainsight-timeline-activity
- name: User
  property_count: 17
  slug: gainsight-user
- name: UserInput
  property_count: 10
  slug: gainsight-userinput
- name: WriteResponse
  property_count: 2
  slug: gainsight-writeresponse
json_structures:
- name: Gainsight Structure
  property_count: 0
  slug: gainsight-structure
jsonld:
- class_count: 0
  name: Gainsight Context
  property_count: 11
  slug: gainsight-context
layout: provider
modified: '2026-05-19'
name: Gainsight
nav: Providers
network: true
overview: 'Gainsight publishes 29 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Activities API, Activity Types API, and 26 more.


  The Gainsight catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Gainsight''s developer surface includes authentication, developer portal, release notes, engineering blog, and 21 more developer resources.'
plans:
- name: Gainsight Plans Pricing
  plan_count: 2
  slug: gainsight-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 2
  name: Gainsight Rate Limits
  slug: gainsight-rate-limits
rules:
- name: Gainsight API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: gainsight-jsonschema-spectral-rules
score:
  band: strong
  composite: 57.9
  delta: -1.4
  facets:
    commercial_clarity: 71.1
    contract_quality: 72.8
    developer_ergonomics: 26.1
    discoverability: 57.4
    governance: 58.3
    operational_transparency: 57.9
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 29
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/screenshots/gainsight-2026-07-25T215357.png
security:
- kind: authentication
  name: Gainsight Authentication
  slug: gainsight-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Gainsight Domain Security
  slug: gainsight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gainsight Vulnerability Disclosure
  slug: gainsight-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Gainsight Trust Center
  slug: gainsight-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: gainsight
website: https://support.gainsight.com
---
