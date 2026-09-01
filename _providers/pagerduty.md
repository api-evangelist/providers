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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 178
  human_in_the_loop: 2
  name: Pagerduty Agentic Access
  operation_count: 337
  slug: pagerduty-agentic-access
  summary_line: 337 operations · 178 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The PagerDuty Events API is a system for triggering, acknowledging, and resolving alerts from monitoring tools and other data sources.
  name: PagerDuty Events API
  slug: pagerduty-events-api
- description: This describes your account's abilities by feature name. For example `"teams"`. An ability may be available to your account based on things like your pricing plan or account state.
  name: PagerDuty Abilities API
  slug: pagerduty-abilities-api
- description: Developers can write their own functionality to insert into PagerDuty's UI.
  name: PagerDuty Add-Ons API
  slug: pagerduty-add-ons-api
- description: Alert Grouping Settings allow you to configure how alerts in services are grouped together into incidents.
  name: PagerDuty Alert Grouping Settings API
  slug: pagerduty-alert-grouping-settings-api
- description: Provides enriched incident data.
  name: PagerDuty Analytics API
  slug: pagerduty-analytics-api
- description: Provides audit record data.
  name: PagerDuty Audit API
  slug: pagerduty-audit-api
- description: Automation Actions invoke jobs that are staged in Runbook Automation or Process Automation.
  name: PagerDuty Automation Actions API
  slug: pagerduty-automation-actions-api
- description: Business services model capabilities that span multiple technical services and that may be owned by several different teams.
  name: PagerDuty Business Services API
  slug: pagerduty-business-services-api
- description: Change Events enable you to send informational events about recent changes such as code deploys and system config changes from any system that can make an outbound HTTP connection. These events do not
  name: PagerDuty Change Events API
  slug: pagerduty-change-events-api
- description: The Change Tags API from PagerDuty — 1 operation(s) for change tags.
  name: PagerDuty Change Tags API
  slug: pagerduty-change-tags-api
- description: Custom fields allow you to enrich PagerDuty incidents with critical and helpful metadata throughout the incident lifecycle.
  name: PagerDuty Custom Fields API
  slug: pagerduty-custom-fields-api
- description: Escalation policies define which user should be alerted at which time.
  name: PagerDuty Escalation Policies API
  slug: pagerduty-escalation-policies-api
- description: Event Orchestrations allow you to route events to an endpoint and create collections of Event Orchestrations, which define sets of actions to take based on event content.
  name: PagerDuty Event Orchestrations API
  slug: pagerduty-event-orchestrations-api
- description: A PagerDuty extension vendor represents a specific type of outbound extension such as Generic Webhook, Slack, ServiceNow.
  name: PagerDuty Extension Schemas API
  slug: pagerduty-extension-schemas-api
- description: Extensions are representations of Extension Schema objects that are attached to Services.
  name: PagerDuty Extensions API
  slug: pagerduty-extensions-api
- description: An Incident Workflow is a sequence of configurable Steps and associated Triggers that can execute automated Actions for a given Incident.
  name: PagerDuty Incident Workflows API
  slug: pagerduty-incident-workflows-api
- description: An incident represents a problem or an issue that needs to be addressed and resolved. Incidents trigger on a service, which prompts notifications to go out to on-call responders per the service's esca
  name: PagerDuty Incidents API
  slug: pagerduty-incidents-api
- description: Licenses are allocated to Users to allow for per-User access to PagerDuty functionality within an Account.
  name: PagerDuty Licenses API
  slug: pagerduty-licenses-api
- description: A log of all the events that happen to an Incident, and these are exposed as Log Entries.
  name: PagerDuty Log Entries API
  slug: pagerduty-log-entries-api
- description: A Maintenance Window is used to temporarily disable one or more Services for a set period of time.
  name: PagerDuty Maintenance Windows API
  slug: pagerduty-maintenance-windows-api
- description: A Notification is created when an Incident is triggered or escalated.
  name: PagerDuty Notifications API
  slug: pagerduty-notifications-api
- description: An on-call represents a contiguous unit of time for which a User will be on call for a given Escalation Policy and Escalation Rules
  name: PagerDuty On-Calls API
  slug: pagerduty-on-calls-api
- description: Provides paused Incident reporting data on services and accounts that have paused Alerts.
  name: PagerDuty Paused Incident Reports API
  slug: pagerduty-paused-incident-reports-api
- description: A priority is a label representing the importance and impact of an incident. This feature is only available on Standard and Enterprise plans.
  name: PagerDuty Priorities API
  slug: pagerduty-priorities-api
- description: Response Plays are a package of Incident Actions that can be applied during an Incident's life cycle.
  name: PagerDuty Response Plays API
  slug: pagerduty-response-plays-api
- description: Rulesets allow you to route events to an endpoint and create collections of Event Rules, which define sets of actions to take based on event content.
  name: PagerDuty Rulesets API
  slug: pagerduty-rulesets-api
- description: A Schedule determines the time periods that users are On-Call.
  name: PagerDuty Schedules API
  slug: pagerduty-schedules-api
- description: Services are categorized into technical and business services. Dependencies can be created via any combination of these services.
  name: PagerDuty Service Dependencies API
  slug: pagerduty-service-dependencies-api
- description: The Services API from PagerDuty — 8 operation(s) for services.
  name: PagerDuty Services API
  slug: pagerduty-services-api
- description: Standards help provide a clear understanding of what a good service configuration looks like, allowing to share and enforce organization guidelines across services to ensure adherence to best practice
  name: PagerDuty Standards API
  slug: pagerduty-standards-api
- description: Status Dashboards represent user-defined views for the Status Dashboard product that are limited to specific Business Services rather than the whole set of top-level Business Services (those with no d
  name: PagerDuty Status Dashboards API
  slug: pagerduty-status-dashboards-api
- description: Status Pages can be public or private read-only pages, that display the status of some predefined set of services, to be shared with customers or internal stakeholders.
  name: PagerDuty Status Pages API
  slug: pagerduty-status-pages-api
- description: The Tags API from PagerDuty — 4 operation(s) for tags.
  name: PagerDuty Tags API
  slug: pagerduty-tags-api
- description: A team is a collection of Users and Escalation Policies that represent a group of people within an organization.
  name: PagerDuty Teams API
  slug: pagerduty-teams-api
- description: Templates is a new feature which will allow customers to create message templates to be leveraged by (but not limited to) status updates. The API will be secured to customers with the status updates e
  name: PagerDuty Templates API
  slug: pagerduty-templates-api
- description: Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.
  name: PagerDuty Users API
  slug: pagerduty-users-api
- description: A PagerDuty Vendor represents a specific type of integration. AWS Cloudwatch, Splunk, Datadog are all examples of vendors
  name: PagerDuty Vendors API
  slug: pagerduty-vendors-api
- description: A webhook is a way to receive events that occur on the PagerDuty platform via an HTTP POST request. V3 webhooks are set up by creating a webhook subscription.
  name: PagerDuty Webhooks API
  slug: pagerduty-webhooks-api
artifact_total: 138
asyncapis:
- description: 'AsyncAPI description of PagerDuty''s event-driven surface. Two complementary channels are modelled: 1. Outbound V3 Webhooks — PagerDuty POSTs a JSON envelope to subscriber URLs whenever a configured in'
  name: PagerDuty Events
  slug: pagerduty-events-asyncapi
collections:
- collection_type: postman
  name: PagerDuty Abilities API
  slug: postman-pagerduty-abilities-api
- collection_type: postman
  name: PagerDuty Abilities Add-Ons API
  slug: postman-pagerduty-add-ons-api
- collection_type: postman
  name: PagerDuty Abilities Alert Grouping Settings API
  slug: postman-pagerduty-alert-grouping-settings-api
- collection_type: postman
  name: PagerDuty Abilities Analytics API
  slug: postman-pagerduty-analytics-api
- collection_type: postman
  name: PagerDuty Abilities Audit API
  slug: postman-pagerduty-audit-api
- collection_type: postman
  name: PagerDuty Abilities Automation Actions API
  slug: postman-pagerduty-automation-actions-api
- collection_type: postman
  name: PagerDuty Abilities Business Services API
  slug: postman-pagerduty-business-services-api
- collection_type: postman
  name: PagerDuty Abilities Change Events API
  slug: postman-pagerduty-change-events-api
- collection_type: postman
  name: PagerDuty Abilities Change Tags API
  slug: postman-pagerduty-change-tags-api
- collection_type: postman
  name: PagerDuty Abilities Custom Fields API
  slug: postman-pagerduty-custom-fields-api
- collection_type: postman
  name: PagerDuty Abilities Escalation Policies API
  slug: postman-pagerduty-escalation-policies-api
- collection_type: postman
  name: PagerDuty Abilities Event Orchestrations API
  slug: postman-pagerduty-event-orchestrations-api
- collection_type: postman
  name: PagerDuty Abilities Extension Schemas API
  slug: postman-pagerduty-extension-schemas-api
- collection_type: postman
  name: PagerDuty Abilities Extensions API
  slug: postman-pagerduty-extensions-api
- collection_type: postman
  name: PagerDuty Abilities Incident Workflows API
  slug: postman-pagerduty-incident-workflows-api
- collection_type: postman
  name: PagerDuty Abilities Incidents API
  slug: postman-pagerduty-incidents-api
- collection_type: postman
  name: PagerDuty Abilities Licenses API
  slug: postman-pagerduty-licenses-api
- collection_type: postman
  name: PagerDuty Abilities Log Entries API
  slug: postman-pagerduty-log-entries-api
- collection_type: postman
  name: PagerDuty Abilities Maintenance Windows API
  slug: postman-pagerduty-maintenance-windows-api
- collection_type: postman
  name: PagerDuty Abilities Notifications API
  slug: postman-pagerduty-notifications-api
- collection_type: postman
  name: PagerDuty Abilities On-Calls API
  slug: postman-pagerduty-on-calls-api
- collection_type: postman
  name: PagerDuty Abilities Paused Incident Reports API
  slug: postman-pagerduty-paused-incident-reports-api
- collection_type: postman
  name: PagerDuty Abilities Priorities API
  slug: postman-pagerduty-priorities-api
- collection_type: postman
  name: PagerDuty Abilities Response Plays API
  slug: postman-pagerduty-response-plays-api
- collection_type: postman
  name: PagerDuty Abilities Rulesets API
  slug: postman-pagerduty-rulesets-api
- collection_type: postman
  name: PagerDuty Abilities Schedules API
  slug: postman-pagerduty-schedules-api
- collection_type: postman
  name: PagerDuty Abilities Service Dependencies API
  slug: postman-pagerduty-service-dependencies-api
- collection_type: postman
  name: PagerDuty Abilities Services API
  slug: postman-pagerduty-services-api
- collection_type: postman
  name: PagerDuty Abilities Standards API
  slug: postman-pagerduty-standards-api
- collection_type: postman
  name: PagerDuty Abilities Status Dashboards API
  slug: postman-pagerduty-status-dashboards-api
- collection_type: postman
  name: PagerDuty Abilities Status Pages API
  slug: postman-pagerduty-status-pages-api
- collection_type: postman
  name: PagerDuty Abilities Tags API
  slug: postman-pagerduty-tags-api
- collection_type: postman
  name: PagerDuty Abilities Teams API
  slug: postman-pagerduty-teams-api
- collection_type: postman
  name: PagerDuty Abilities Templates API
  slug: postman-pagerduty-templates-api
- collection_type: postman
  name: PagerDuty Abilities Users API
  slug: postman-pagerduty-users-api
- collection_type: postman
  name: PagerDuty Abilities Vendors API
  slug: postman-pagerduty-vendors-api
- collection_type: postman
  name: PagerDuty Abilities Webhooks API
  slug: postman-pagerduty-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PagerDuty Abilities API
  slug: open-pagerduty-abilities-api
- collection_type: open
  name: PagerDuty Abilities Add-Ons API
  slug: open-pagerduty-add-ons-api
- collection_type: open
  name: PagerDuty Abilities Alert Grouping Settings API
  slug: open-pagerduty-alert-grouping-settings-api
- collection_type: open
  name: PagerDuty Abilities Analytics API
  slug: open-pagerduty-analytics-api
- collection_type: open
  name: PagerDuty Abilities Audit API
  slug: open-pagerduty-audit-api
- collection_type: open
  name: PagerDuty Abilities Automation Actions API
  slug: open-pagerduty-automation-actions-api
- collection_type: open
  name: PagerDuty Abilities Business Services API
  slug: open-pagerduty-business-services-api
- collection_type: open
  name: PagerDuty Abilities Change Events API
  slug: open-pagerduty-change-events-api
- collection_type: open
  name: PagerDuty Abilities Change Tags API
  slug: open-pagerduty-change-tags-api
- collection_type: open
  name: PagerDuty Abilities Custom Fields API
  slug: open-pagerduty-custom-fields-api
- collection_type: open
  name: PagerDuty Abilities Escalation Policies API
  slug: open-pagerduty-escalation-policies-api
- collection_type: open
  name: PagerDuty Abilities Event Orchestrations API
  slug: open-pagerduty-event-orchestrations-api
- collection_type: open
  name: PagerDuty Abilities Extension Schemas API
  slug: open-pagerduty-extension-schemas-api
- collection_type: open
  name: PagerDuty Abilities Extensions API
  slug: open-pagerduty-extensions-api
- collection_type: open
  name: PagerDuty Abilities Incident Workflows API
  slug: open-pagerduty-incident-workflows-api
- collection_type: open
  name: PagerDuty Abilities Incidents API
  slug: open-pagerduty-incidents-api
- collection_type: open
  name: PagerDuty Abilities Licenses API
  slug: open-pagerduty-licenses-api
- collection_type: open
  name: PagerDuty Abilities Log Entries API
  slug: open-pagerduty-log-entries-api
- collection_type: open
  name: PagerDuty Abilities Maintenance Windows API
  slug: open-pagerduty-maintenance-windows-api
- collection_type: open
  name: PagerDuty Abilities Notifications API
  slug: open-pagerduty-notifications-api
- collection_type: open
  name: PagerDuty Abilities On-Calls API
  slug: open-pagerduty-on-calls-api
- collection_type: open
  name: PagerDuty Abilities Paused Incident Reports API
  slug: open-pagerduty-paused-incident-reports-api
- collection_type: open
  name: PagerDuty Abilities Priorities API
  slug: open-pagerduty-priorities-api
- collection_type: open
  name: PagerDuty Abilities Response Plays API
  slug: open-pagerduty-response-plays-api
- collection_type: open
  name: PagerDuty Abilities Rulesets API
  slug: open-pagerduty-rulesets-api
- collection_type: open
  name: PagerDuty Abilities Schedules API
  slug: open-pagerduty-schedules-api
- collection_type: open
  name: PagerDuty Abilities Service Dependencies API
  slug: open-pagerduty-service-dependencies-api
- collection_type: open
  name: PagerDuty Abilities Services API
  slug: open-pagerduty-services-api
- collection_type: open
  name: PagerDuty Abilities Standards API
  slug: open-pagerduty-standards-api
- collection_type: open
  name: PagerDuty Abilities Status Dashboards API
  slug: open-pagerduty-status-dashboards-api
- collection_type: open
  name: PagerDuty Abilities Status Pages API
  slug: open-pagerduty-status-pages-api
- collection_type: open
  name: PagerDuty Abilities Tags API
  slug: open-pagerduty-tags-api
- collection_type: open
  name: PagerDuty Abilities Teams API
  slug: open-pagerduty-teams-api
- collection_type: open
  name: PagerDuty Abilities Templates API
  slug: open-pagerduty-templates-api
- collection_type: open
  name: PagerDuty Abilities Users API
  slug: open-pagerduty-users-api
- collection_type: open
  name: PagerDuty Abilities Vendors API
  slug: open-pagerduty-vendors-api
- collection_type: open
  name: PagerDuty Abilities Webhooks API
  slug: open-pagerduty-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/pagerduty-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/pagerduty/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pagerduty-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pagerduty-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pagerduty-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pagerduty
- group: start
  title: ''
  type: Portal
  url: https://developer.pagerduty.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.pagerduty.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.pagerduty.com/docs/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.pagerduty.com/docs/authentication
- group: start
  title: ''
  type: Signup
  url: https://www.pagerduty.com/sign-up-free/
- group: start
  title: ''
  type: Login
  url: https://identity.pagerduty.com/sign_in
- group: company
  title: ''
  type: Blog
  url: https://www.pagerduty.com/blog/
- group: operate
  title: ''
  type: Community
  url: https://community.pagerduty.com/
- group: operate
  title: ''
  type: Support
  url: https://support.pagerduty.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pagerduty.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pagerduty.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pagerduty.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PagerDuty
- group: company
  title: ''
  type: Website
  url: https://www.pagerduty.com/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/PagerDuty/pagerduty-mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.pagerduty.com/llms.txt
created: '2026-03-16'
description: PagerDuty is a digital operations management platform that helps teams detect problems and resolve incidents with automated alerting, on-call management, and incident response workflows.
features:
- REST API for incidents, services, escalations, and on-call schedules
- Events API v2 for inbound alert ingestion (480 events/min/integration_key)
- Webhooks v3 with HMAC signing
- 750+ integrations with monitoring, ticketing, and chat tools
- Free tier up to 5 users with 1 schedule and 1 escalation policy
- Professional plan at $21/user/month with chat and Major Incident Workflow
- Business plan at $41/user/month with custom incident types and ITSM integrations
- Enterprise plan with incident workflows, post-incident reviews, ServiceNow sync
- PagerDuty Advance AI credits (1k/5k/20k by tier)
- Rundeck Automation (separate licensing)
- Status Pages (external up to 250/500 subscribers by tier)
- Internal Status Pages (Business+)
- REST API default rate of 960 req/min/token
- Analytics API rate-limited to 5 req/min/token
- Single Sign-On (Pro+) and SCIM provisioning
finops:
- name: Pagerduty Finops
  service_category: Incident Response
  slug: pagerduty-finops
graphqls:
- description: PagerDuty is a digital operations management platform providing incident management, on-call scheduling, and automated alerting for engineering and operations teams. This conceptual GraphQL schema rep
  name: PagerDuty GraphQL Schema
  slug: pagerduty-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pagerduty.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-30'
name: PagerDuty
nav: Providers
network: true
overview: 'PagerDuty publishes 38 APIs on the [APIs.io](https://apis.io/) network, including Events API, Abilities API, Add-Ons API, and 35 more. Tagged areas include Alerting, DevOps, Incident Management, and On-Call Management.


  The PagerDuty catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  PagerDuty''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, engineering blog, support, and 15 more developer resources.'
plans:
- name: Pagerduty Plans Pricing
  plan_count: 4
  slug: pagerduty-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Pagerduty Rate Limits
  slug: pagerduty-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: PagerDuty API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: pagerduty-asyncapi-spectral-rules
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 11.4
    contract_quality: 73.3
    developer_ergonomics: 19.0
    discoverability: 51.9
    governance: 11.4
    operational_transparency: 10.5
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 37
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pagerduty/refs/heads/main/screenshots/pagerduty-2026-06-20T191325.png
security:
- kind: authentication
  name: Pagerduty Authentication
  slug: pagerduty-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pagerduty Domain Security
  slug: pagerduty-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pagerduty
tags:
- Alerting
- DevOps
- Incident Management
- On-Call Management
website: https://www.pagerduty.com/
---
