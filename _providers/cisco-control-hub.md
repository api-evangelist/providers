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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Cisco Control Hub Agentic Access
  operation_count: 17
  slug: cisco-control-hub-agentic-access
  summary_line: 17 operations · 6 acting
api_count: 7
apis:
- description: The AdminAuditEvents API from Cisco Control Hub — 1 operation(s) for adminauditevents.
  name: Cisco Control Hub AdminAuditEvents API
  slug: cisco-control-hub-adminauditevents-api
- description: The Devices API from Cisco Control Hub — 1 operation(s) for devices.
  name: Cisco Control Hub Devices API
  slug: cisco-control-hub-devices-api
- description: The Licenses API from Cisco Control Hub — 2 operation(s) for licenses.
  name: Cisco Control Hub Licenses API
  slug: cisco-control-hub-licenses-api
- description: The Locations API from Cisco Control Hub — 2 operation(s) for locations.
  name: Cisco Control Hub Locations API
  slug: cisco-control-hub-locations-api
- description: The Organizations API from Cisco Control Hub — 2 operation(s) for organizations.
  name: Cisco Control Hub Organizations API
  slug: cisco-control-hub-organizations-api
- description: The People API from Cisco Control Hub — 2 operation(s) for people.
  name: Cisco Control Hub People API
  slug: cisco-control-hub-people-api
- description: The Workspaces API from Cisco Control Hub — 1 operation(s) for workspaces.
  name: Cisco Control Hub Workspaces API
  slug: cisco-control-hub-workspaces-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cisco Webex Control Hub Admin AdminAuditEvents API
  slug: open-cisco-control-hub-adminauditevents-api
- collection_type: open
  name: Cisco Webex Control Hub Admin AdminAuditEvents Devices API
  slug: open-cisco-control-hub-devices-api
- collection_type: open
  name: Cisco Webex Control Hub Admin AdminAuditEvents Licenses API
  slug: open-cisco-control-hub-licenses-api
- collection_type: open
  name: Cisco Webex Control Hub Admin AdminAuditEvents Locations API
  slug: open-cisco-control-hub-locations-api
- collection_type: open
  name: Cisco Webex Control Hub Admin AdminAuditEvents Organizations API
  slug: open-cisco-control-hub-organizations-api
- collection_type: open
  name: Cisco Webex Control Hub Admin AdminAuditEvents People API
  slug: open-cisco-control-hub-people-api
- collection_type: open
  name: Cisco Webex Control Hub Admin AdminAuditEvents Workspaces API
  slug: open-cisco-control-hub-workspaces-api
- collection_type: open
  name: Cisco Webex Control Hub Admin API
  slug: open-cisco-control-hub
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/webex/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cisco-control-hub-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cisco-control-hub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cisco-control-hub-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.webex.com/feed/
created: '2024-01-01'
description: Cisco Control Hub is the administration console for Webex services. Programmatic access is delivered through the Webex Admin and adjacent REST APIs at webexapis.com — covering people, organizations, locations, workspaces, devices, licenses, calling configuration, audit events, and analytics reports. Authentication uses OAuth 2.0 access tokens or service-app tokens scoped to the organization.
finops:
- name: Cisco Control Hub Finops
  service_category: API
  slug: cisco-control-hub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cisco-control-hub.png
jsonld:
- class_count: 0
  name: Cisco Control Hub Context
  property_count: 7
  slug: cisco-control-hub-context
layout: provider
modified: '2026-08-19'
name: Cisco Control Hub
nav: Providers
network: true
overview: 'Cisco Control Hub publishes 7 APIs on the [APIs.io](https://apis.io/) network, including AdminAuditEvents API, Devices API, Licenses API, and 4 more. Tagged areas include Administration, Calling, Collaboration, Communications, and Device Management.


  The Cisco Control Hub catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cisco Control Hub''s developer surface includes authentication, engineering blog, and 3 more developer resources.'
plans:
- name: Cisco Control Hub Plans Pricing
  plan_count: 3
  slug: cisco-control-hub-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 5
  name: Cisco Control Hub Rate Limits
  slug: cisco-control-hub-rate-limits
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Cisco Control Hub API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: cisco-control-hub-rules
score:
  band: emerging
  composite: 26.0
  delta: -6.2
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 54.5
    contract_quality: 19.9
    developer_ergonomics: 14.3
    discoverability: 74.1
    governance: 54.5
    operational_transparency: 7.9
  previous_composite: 32.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/cisco-control-hub/refs/heads/main/screenshots/cisco-control-hub-2026-06-20T174357.png
security:
- kind: authentication
  name: Cisco Control Hub Authentication
  slug: cisco-control-hub-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cisco Control Hub Domain Security
  slug: cisco-control-hub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cisco-control-hub
tags:
- Administration
- Calling
- Collaboration
- Communications
- Device Management
- Identity Management
- Licenses
- Reporting
- Webex
---
