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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Xmatters Agentic Access
  operation_count: 36
  slug: xmatters-agentic-access
  summary_line: 36 operations · 17 acting
api_count: 11
apis:
- description: REST API for managing people, groups, devices, on-call schedules, events, conferences, scenarios, sites, and integrations in xMatters. The base URL identifies the customer instance and uses the path /
  name: xMatters REST API
  slug: rest-api
- description: The Devices API from xMatters — 2 operation(s) for devices.
  name: xMatters Devices API
  slug: xmatters-devices-api
- description: The Events API from xMatters — 3 operation(s) for events.
  name: xMatters Events API
  slug: xmatters-events-api
- description: The Groups API from xMatters — 3 operation(s) for groups.
  name: xMatters Groups API
  slug: xmatters-groups-api
- description: The Integrations API from xMatters — 1 operation(s) for integrations.
  name: xMatters Integrations API
  slug: xmatters-integrations-api
- description: The OnCall API from xMatters — 1 operation(s) for oncall.
  name: xMatters OnCall API
  slug: xmatters-oncall-api
- description: The People API from xMatters — 4 operation(s) for people.
  name: xMatters People API
  slug: xmatters-people-api
- description: The Plans API from xMatters — 2 operation(s) for plans.
  name: xMatters Plans API
  slug: xmatters-plans-api
- description: The Scenarios API from xMatters — 1 operation(s) for scenarios.
  name: xMatters Scenarios API
  slug: xmatters-scenarios-api
- description: The Services API from xMatters — 1 operation(s) for services.
  name: xMatters Services API
  slug: xmatters-services-api
- description: The Shifts API from xMatters — 1 operation(s) for shifts.
  name: xMatters Shifts API
  slug: xmatters-shifts-api
artifact_total: 17
collections:
- collection_type: open
  name: xMatters REST API
  slug: open-xmatters
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/xmatters-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/xmatters-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xmatters-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xmatters-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/xmatters-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xmatters
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xmatters-inc
- group: company
  title: ''
  type: Website
  url: https://www.xmatters.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.xmatters.com/ondemand/
- group: docs
  title: ''
  type: API Documentation
  url: https://help.xmatters.com/xmapi/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.xmatters.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.xmatters.com/signup-free-trial
- group: operate
  title: ''
  type: Support
  url: https://support.xmatters.com/
- group: other
  title: ''
  type: Terraform Provider
  url: https://registry.terraform.io/providers/xmatters/xmatters/latest/docs
- group: agent
  title: ''
  type: LlmsText
  url: https://xmatters.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.xmatters.com/blog/feed/
created: '2026-05-11'
description: xMatters is a service reliability platform that orchestrates intelligent communication, on-call management, and incident response workflows for IT operations, DevOps, and major incident teams. The platform routes signals from monitoring tools to the right people via multiple channels (voice, SMS, push, email, chat) and triggers automated remediation workflows via its integration builder and Flow Designer. The xMatters REST API provides full programmatic control over people, groups, on-call schedules, events, scenarios, and integrations using Basic auth, API keys, or OAuth 2.0.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xmatters.png
layout: provider
modified: '2026-05-11'
name: xMatters
nav: Providers
network: true
overview: 'xMatters publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Devices API, Events API, Groups API, and 7 more. Tagged areas include Incident Management, On-Call, Alerting, Service Reliability, and DevOps.


  xMatters'' developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 10 more developer resources.'
random_paper: 97
scopes:
- name: Xmatters Scopes
  scope_count: 0
  slug: xmatters-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.1
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 51.2
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 31.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xmatters/refs/heads/main/screenshots/xmatters-2026-06-20T201707.png
security:
- kind: authentication
  name: Xmatters Authentication
  slug: xmatters-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Xmatters Domain Security
  slug: xmatters-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Xmatters Trust Center
  slug: xmatters-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, FedRAMP, GDPR
slug: xmatters
tags:
- Incident Management
- On-Call
- Alerting
- Service Reliability
- DevOps
- Communication
- Workflow Automation
website: https://www.xmatters.com
---
