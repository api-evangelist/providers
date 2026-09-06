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
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 81
  human_in_the_loop: 1
  name: Zenduty Agentic Access
  operation_count: 140
  slug: zenduty-agentic-access
  summary_line: 140 operations · 81 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: 'Management REST API for incidents, services, teams, users, schedules, escalation policies, and integrations. Authenticated via "Authorization: Token <token>" header.'
  name: Zenduty REST API
  slug: rest-api
- description: Alert ingestion API for sending incident events from monitoring, observability, and custom systems into Zenduty.
  name: Zenduty Events API
  slug: events-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents a custom role of the account. Each custom role object has custom permissions, which the account admin can set from account level permissions and assign this custom role to a par
  name: Zenduty Account Custom Role API
  slug: zenduty-account-custom-role-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents a user of the account. Each account member object has a role, which can be owner, admin, or user. Each account has a single owner, but the admins and users can be multiple.
  name: Zenduty Account Member API
  slug: zenduty-account-member-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: Alert Rules in Zenduty are advanced conditions for incoming alerts. They dictate how Zenduty handles alerts and their incidents upon receipt, altering behavior and routing based on predefined rules an
  name: Zenduty Alert Rules API
  slug: zenduty-alert-rules-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: These endpoints provide incident analytics for your account. All analytics endpoints accept POST requests with optional filter parameters and return metrics such as incident counts, MTTA, and MTTR.
  name: Zenduty Analytics API
  slug: zenduty-analytics-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents one of the following communication channels(Email, SMS, Phone Call, Slack, Microsoft Team, Google Chat). A user can add multiple contacts methods.
  name: Zenduty Contact Methods API
  slug: zenduty-contact-methods-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the escalation policy of a team. You can checkout the escalation policy docs here https://docs.zenduty.com/docs/escalationpolicies
  name: Zenduty Escalation Policies API
  slug: zenduty-escalation-policies-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the events of an integration.
  name: Zenduty Events API
  slug: zenduty-events-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents a user's forwarding rules. A user can forward his notifications to the other account members in case an incident occurs.
  name: Zenduty Forwarding Rules API
  slug: zenduty-forwarding-rules-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the Global Router of the Account. You can checkout the global alert routing docs here https://docs.zenduty.com/docs/globalalertrouting
  name: Zenduty Global Router API
  slug: zenduty-global-router-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: The Rules of the Global Router in an Account are represented by this object. Visit this link to view the documentation for the global alert routing rules https://docs.zenduty.com/docs/globalalertrouti
  name: Zenduty Global Router Rules API
  slug: zenduty-global-router-rules-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the incident alerts of an incident.
  name: Zenduty Incident Alerts API
  slug: zenduty-incident-alerts-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the incident notes of an incident.
  name: Zenduty Incident Notes API
  slug: zenduty-incident-notes-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the incident responders of an incident.
  name: Zenduty Incident Responders API
  slug: zenduty-incident-responders-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the incident roles of an incident. You can checkout the incident role docs here https://docs.zenduty.com/docs/incidentroles
  name: Zenduty Incident Roles API
  slug: zenduty-incident-roles-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the incident tags of an incident.
  name: Zenduty Incident Tags API
  slug: zenduty-incident-tags-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the incidents of the account. You can checkout the incident docs here https://docs.zenduty.com/docs/incidents
  name: Zenduty Incidents API
  slug: zenduty-incidents-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the integrations associated with a service. You can checkout the integration docs here https://docs.zenduty.com/docs/integrations
  name: Zenduty Integrations API
  slug: zenduty-integrations-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents a user's notification rules. A user can have notification rules for high urgency and low urgency incidents.
  name: Zenduty Notification Rules API
  slug: zenduty-notification-rules-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the user who is oncall.
  name: Zenduty OnCall API
  slug: zenduty-oncall-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the postmortem of an incident. You can checkout the postmortem docs here https://docs.zenduty.com/docs/incidentpostmortem
  name: Zenduty Postmortem API
  slug: zenduty-postmortem-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the priority of an incident. You can checkout the priority docs here https://docs.zenduty.com/docs/incidentpriority
  name: Zenduty Priorities API
  slug: zenduty-priorities-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the Override of a Schedule. You can checkout the Schedule Override docs here https://docs.zenduty.com/docs/schedules/#schedule-override
  name: Zenduty Schedule Overrides API
  slug: zenduty-schedule-overrides-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the schedule of a team. You can checkout the schedule docs here https://docs.zenduty.com/docs/schedules
  name: Zenduty Schedules API
  slug: zenduty-schedules-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the services associated with a team. You can checkout the services docs here https://docs.zenduty.com/docs/services
  name: Zenduty Services API
  slug: zenduty-services-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the SLA of an incident. You can checkout the SLA docs here https://docs.zenduty.com/docs/incidentsla
  name: Zenduty SLA API
  slug: zenduty-sla-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the tags of an incident. You can checkout the tag docs here https://docs.zenduty.com/docs/incidenttags
  name: Zenduty Tags API
  slug: zenduty-tags-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the task templates of the team. You can checkout the task template docs here https://docs.zenduty.com/docs/tasktemplates
  name: Zenduty Task Templates API
  slug: zenduty-task-templates-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the maintenance mode of a team. You can checkout the team maintenance mode docs here https://docs.zenduty.com/docs/maintenancewindows
  name: Zenduty Team Maintenance Mode API
  slug: zenduty-team-maintenance-mode-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the users of a team. Each team member has a role which can be a manager or a user. You can checkout the team member docs here https://docs.zenduty.com/docs/users
  name: Zenduty Team Members API
  slug: zenduty-team-members-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents the permissions of a team. It lets you access the particular team elements that the team has given permissions to use.
  name: Zenduty Team Permissions API
  slug: zenduty-team-permissions-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents a team of the account. It lets you create different independent operational units in the account. You can check out the team docs here https://docs.zenduty.com/docs/teams.
  name: Zenduty Teams API
  slug: zenduty-teams-api
- baseURL: https://www.zenduty.com/api
  baseurl_source: declared
  description: This object represents a user's custom role. Each user can be assigned to only one custom role.
  name: Zenduty User Custom Role API
  slug: zenduty-user-custom-role-api
artifact_total: 72
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zenduty Account Custom Role API
  slug: open-zenduty-account-custom-role-api
- collection_type: open
  name: Zenduty Account Custom Role Account Member API
  slug: open-zenduty-account-member-api
- collection_type: open
  name: Zenduty Account Custom Role Alert Rules API
  slug: open-zenduty-alert-rules-api
- collection_type: open
  name: Zenduty Account Custom Role Analytics API
  slug: open-zenduty-analytics-api
- collection_type: open
  name: Zenduty Account Custom Role Contact Methods API
  slug: open-zenduty-contact-methods-api
- collection_type: open
  name: Zenduty Account Custom Role Escalation Policies API
  slug: open-zenduty-escalation-policies-api
- collection_type: open
  name: Zenduty Account Custom Role Events API
  slug: open-zenduty-events-api
- collection_type: open
  name: Zenduty Account Custom Role Forwarding Rules API
  slug: open-zenduty-forwarding-rules-api
- collection_type: open
  name: Zenduty Account Custom Role Global Router API
  slug: open-zenduty-global-router-api
- collection_type: open
  name: Zenduty Account Custom Role Global Router Rules API
  slug: open-zenduty-global-router-rules-api
- collection_type: open
  name: Zenduty Account Custom Role Incident Alerts API
  slug: open-zenduty-incident-alerts-api
- collection_type: open
  name: Zenduty Account Custom Role Incident Notes API
  slug: open-zenduty-incident-notes-api
- collection_type: open
  name: Zenduty Account Custom Role Incident Responders API
  slug: open-zenduty-incident-responders-api
- collection_type: open
  name: Zenduty Account Custom Role Incident Roles API
  slug: open-zenduty-incident-roles-api
- collection_type: open
  name: Zenduty Account Custom Role Incident Tags API
  slug: open-zenduty-incident-tags-api
- collection_type: open
  name: Zenduty Account Custom Role Incidents API
  slug: open-zenduty-incidents-api
- collection_type: open
  name: Zenduty Account Custom Role Integrations API
  slug: open-zenduty-integrations-api
- collection_type: open
  name: Zenduty Account Custom Role Notification Rules API
  slug: open-zenduty-notification-rules-api
- collection_type: open
  name: Zenduty Account Custom Role OnCall API
  slug: open-zenduty-oncall-api
- collection_type: open
  name: Zenduty Account Custom Role Postmortem API
  slug: open-zenduty-postmortem-api
- collection_type: open
  name: Zenduty Account Custom Role Priorities API
  slug: open-zenduty-priorities-api
- collection_type: open
  name: Zenduty Account Custom Role Schedule Overrides API
  slug: open-zenduty-schedule-overrides-api
- collection_type: open
  name: Zenduty Account Custom Role Schedules API
  slug: open-zenduty-schedules-api
- collection_type: open
  name: Zenduty Account Custom Role Services API
  slug: open-zenduty-services-api
- collection_type: open
  name: Zenduty Account Custom Role SLA API
  slug: open-zenduty-sla-api
- collection_type: open
  name: Zenduty Account Custom Role Tags API
  slug: open-zenduty-tags-api
- collection_type: open
  name: Zenduty Account Custom Role Task Templates API
  slug: open-zenduty-task-templates-api
- collection_type: open
  name: Zenduty Account Custom Role Team Maintenance Mode API
  slug: open-zenduty-team-maintenance-mode-api
- collection_type: open
  name: Zenduty Account Custom Role Team Members API
  slug: open-zenduty-team-members-api
- collection_type: open
  name: Zenduty Account Custom Role Team Permissions API
  slug: open-zenduty-team-permissions-api
- collection_type: open
  name: Zenduty Account Custom Role Teams API
  slug: open-zenduty-teams-api
- collection_type: open
  name: Zenduty Account Custom Role User Custom Role API
  slug: open-zenduty-user-custom-role-api
- collection_type: open
  name: Zenduty
  slug: open-zenduty
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/zenduty-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zenduty-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zenduty-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zenduty-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zenduty-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zenduty
- group: company
  title: ''
  type: Website
  url: https://www.zenduty.com
- group: docs
  title: ''
  type: Documentation
  url: https://zenduty.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zenduty.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.zenduty.com/signup
- group: build
  title: ''
  type: GitHub SDK
  url: https://github.com/Zenduty/zenduty-python-sdk
- group: company
  title: ''
  type: Blog
  url: https://zenduty.com/blog/rss.xml
created: '2026-05-11'
description: Zenduty is an incident management and on-call platform that orchestrates alert routing, escalation policies, on-call schedules, and incident response workflows for SRE and DevOps teams. The platform integrates with observability tools, ticketing systems, and chat platforms to centralize incident triage. Zenduty exposes a REST API for managing incidents, services, teams, schedules, and escalation policies, plus an Events API for ingesting alerts, all secured with Token authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zenduty.png
layout: provider
modified: '2026-05-11'
name: Zenduty
nav: Providers
network: true
overview: 'Zenduty publishes 32 APIs on the [APIs.io](https://apis.io/) network, including Account Custom Role API, Account Member API, Alert Rules API, and 29 more. Tagged areas include Incident Management, On-Call, Alerting, SRE, and DevOps.


  Zenduty''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 7 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 58.9
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 32.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 32
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zenduty/refs/heads/main/screenshots/zenduty-2026-06-20T201810.png
security:
- kind: authentication
  name: Zenduty Authentication
  slug: zenduty-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zenduty Domain Security
  slug: zenduty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Zenduty Trust Center
  slug: zenduty-trust-center
  summary_line: SOC 2, ISO 27001
slug: zenduty
tags:
- Incident Management
- On-Call
- Alerting
- SRE
- DevOps
- Observability
website: https://www.zenduty.com
---
