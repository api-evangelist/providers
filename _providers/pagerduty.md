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
  band: agent-native
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 65.4
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 178
  human_in_the_loop: 2
  name: Pagerduty Agentic Access
  operation_count: 337
  slug: pagerduty-agentic-access
  summary_line: 337 operations · 178 acting · 2 human-in-the-loop
api_count: 38
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
artifact_total: 63
asyncapis:
- description: 'AsyncAPI description of PagerDuty''s event-driven surface. Two complementary channels are modelled: 1. Outbound V3 Webhooks — PagerDuty POSTs a JSON envelope to subscriber URLs whenever a configured in'
  name: PagerDuty Events
  slug: pagerduty-events-asyncapi
common:
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


  PagerDuty''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, engineering blog, support, and 13 more developer resources.'
plans:
- name: Pagerduty Plans Pricing
  plan_count: 4
  slug: pagerduty-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 3
  name: Pagerduty Rate Limits
  slug: pagerduty-rate-limits
rules:
- name: PagerDuty API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: pagerduty-asyncapi-spectral-rules
score:
  band: strong
  composite: 63.0
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 69.9
    developer_ergonomics: 54.3
    discoverability: 67.5
    governance: 52.6
    operational_transparency: 52.6
  previous_composite: 63.0
  schema_version: 0.5
  scored_at: '2026-07-27'
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
