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
- acting_count: 48
  human_in_the_loop: 0
  name: Incident Io Agentic Access
  operation_count: 99
  slug: incident-io-agentic-access
  summary_line: 99 operations · 48 acting
api_count: 25
apis:
- description: The Actions API from Incident.io — 2 operation(s) for actions.
  name: Incident.io Actions API
  slug: incident-io-actions-api
- description: The Alert Attributes API from Incident.io — 2 operation(s) for alert attributes.
  name: Incident.io Alert Attributes API
  slug: incident-io-alert-attributes-api
- description: The Alert Routes API from Incident.io — 2 operation(s) for alert routes.
  name: Incident.io Alert Routes API
  slug: incident-io-alert-routes-api
- description: The Alert Sources API from Incident.io — 2 operation(s) for alert sources.
  name: Incident.io Alert Sources API
  slug: incident-io-alert-sources-api
- description: The Alerts API from Incident.io — 3 operation(s) for alerts.
  name: Incident.io Alerts API
  slug: incident-io-alerts-api
- description: The API Keys API from Incident.io — 3 operation(s) for api keys.
  name: Incident.io API Keys API
  slug: incident-io-api-keys-api
- description: The Catalog Entries API from Incident.io — 2 operation(s) for catalog entries.
  name: Incident.io Catalog Entries API
  slug: incident-io-catalog-entries-api
- description: The Catalog Types API from Incident.io — 2 operation(s) for catalog types.
  name: Incident.io Catalog Types API
  slug: incident-io-catalog-types-api
- description: The Custom Fields API from Incident.io — 2 operation(s) for custom fields.
  name: Incident.io Custom Fields API
  slug: incident-io-custom-fields-api
- description: The Escalation Paths API from Incident.io — 2 operation(s) for escalation paths.
  name: Incident.io Escalation Paths API
  slug: incident-io-escalation-paths-api
- description: The Escalations API from Incident.io — 2 operation(s) for escalations.
  name: Incident.io Escalations API
  slug: incident-io-escalations-api
- description: The Follow-ups API from Incident.io — 2 operation(s) for follow-ups.
  name: Incident.io Follow-ups API
  slug: incident-io-follow-ups-api
- description: The Incident Roles API from Incident.io — 2 operation(s) for incident roles.
  name: Incident.io Incident Roles API
  slug: incident-io-incident-roles-api
- description: The Incident Statuses API from Incident.io — 2 operation(s) for incident statuses.
  name: Incident.io Incident Statuses API
  slug: incident-io-incident-statuses-api
- description: The Incident Types API from Incident.io — 2 operation(s) for incident types.
  name: Incident.io Incident Types API
  slug: incident-io-incident-types-api
- description: The Incidents API from Incident.io — 2 operation(s) for incidents.
  name: Incident.io Incidents API
  slug: incident-io-incidents-api
- description: The Maintenance Windows API from Incident.io — 2 operation(s) for maintenance windows.
  name: Incident.io Maintenance Windows API
  slug: incident-io-maintenance-windows-api
- description: The Postmortem Documents API from Incident.io — 2 operation(s) for postmortem documents.
  name: Incident.io Postmortem Documents API
  slug: incident-io-postmortem-documents-api
- description: The Schedules API from Incident.io — 2 operation(s) for schedules.
  name: Incident.io Schedules API
  slug: incident-io-schedules-api
- description: The Severities API from Incident.io — 2 operation(s) for severities.
  name: Incident.io Severities API
  slug: incident-io-severities-api
- description: The Status Pages API from Incident.io — 2 operation(s) for status pages.
  name: Incident.io Status Pages API
  slug: incident-io-status-pages-api
- description: The Teams API from Incident.io — 2 operation(s) for teams.
  name: Incident.io Teams API
  slug: incident-io-teams-api
- description: The Users API from Incident.io — 2 operation(s) for users.
  name: Incident.io Users API
  slug: incident-io-users-api
- description: The Utilities API from Incident.io — 3 operation(s) for utilities.
  name: Incident.io Utilities API
  slug: incident-io-utilities-api
- description: The Workflows API from Incident.io — 2 operation(s) for workflows.
  name: Incident.io Workflows API
  slug: incident-io-workflows-api
artifact_total: 55
collections:
- collection_type: open
  name: Incident.io API
  slug: open-incident-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/incident-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/incident-io-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/incident-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/incident-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/incident-io-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/incident-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/incident-io
- group: company
  title: ''
  type: Website
  url: https://incident.io
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.incident.io
- group: agent
  title: ''
  type: LlmsText
  url: https://incident.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://incident.io/blog
created: '2026-03-27'
description: incident.io is an incident management platform that helps teams declare, manage, and learn from incidents.
features:
- 'Basic: free Slack/MS Teams native incident response'
- 'Team: $15/user/mo annual + $10/user for on-call'
- 'Pro: $25/user/mo + $20/user for on-call; AI Scribe, SSO/SAML'
- 'Enterprise: custom; Slack Enterprise Grid, Sandbox, CSM'
- 'On-Call only: $20/user/mo standalone alerting'
- Slack-native and MS Teams-native flow
- AI suggestions for incident triage
- AI Scribe for post-mortem writing (Pro+)
- Status pages (public + internal)
- Workflows for automation
- Heartbeats for synthetic monitoring
- REST API at api.incident.io
- Default 600 req/min/org
- Webhook delivery + Catalog API
- OAuth 2.0 + Bearer tokens
- Live call routing for paged engineers
finops:
- name: Incident Io Finops
  service_category: Incident Response
  slug: incident-io-finops
graphqls:
- description: This directory contains a conceptual GraphQL schema for the [incident.io](https://incident.io) incident management platform. The schema is derived from the public REST API documented at [https://api-d
  name: incident.io GraphQL Schema
  slug: incident-io-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/incident-io.png
json_schemas:
- name: ListResponse
  property_count: 2
  slug: incident-io-listresponse
- name: Resource
  property_count: 0
  slug: incident-io-resource
json_structures:
- name: Incident Io Structure
  property_count: 0
  slug: incident-io-structure
layout: provider
modified: '2026-05-19'
name: Incident.io
nav: Providers
network: true
overview: 'Incident.io publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Alert Attributes API, Alert Routes API, and 22 more. Tagged areas include AIOps and Incident Management.


  The Incident.io catalog on APIs.io includes 1 Spectral governance ruleset.


  Incident.io''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Incident Io Plans Pricing
  plan_count: 5
  slug: incident-io-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 3
  name: Incident Io Rate Limits
  slug: incident-io-rate-limits
rules:
- name: Incident.io API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: incident-io-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.4
  delta: -1.2
  facets:
    commercial_clarity: 47.4
    contract_quality: 56.7
    developer_ergonomics: 21.7
    discoverability: 46.3
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/incident-io/refs/heads/main/screenshots/incident-io-2026-06-20T183308.png
security:
- kind: authentication
  name: Incident Io Authentication
  slug: incident-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Incident Io Domain Security
  slug: incident-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Incident Io Vulnerability Disclosure
  slug: incident-io-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Incident Io Trust Center
  slug: incident-io-trust-center
  summary_line: SOC 2
slug: incident-io
tags:
- AIOps
- Incident Management
website: https://incident.io
---
