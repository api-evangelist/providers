---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Cisco Control Hub Agentic Access
  operation_count: 17
  slug: cisco-control-hub-agentic-access
  summary_line: 17 operations · 6 acting
api_count: 1
apis:
- baseURL: https://webexapis.com/v1
  baseurl_source: declared
  description: The Devices API from Cisco Control Hub — 1 operation(s) for devices.
  name: Cisco Control Hub Devices API
  slug: cisco-control-hub-devices-api
- baseURL: https://webexapis.com/v1
  baseurl_source: declared
  description: The Licenses API from Cisco Control Hub — 2 operation(s) for licenses.
  name: Cisco Control Hub Licenses API
  slug: cisco-control-hub-licenses-api
- baseURL: https://webexapis.com/v1
  baseurl_source: declared
  description: The Locations API from Cisco Control Hub — 2 operation(s) for locations.
  name: Cisco Control Hub Locations API
  slug: cisco-control-hub-locations-api
- baseURL: https://webexapis.com/v1
  baseurl_source: declared
  description: The Organizations API from Cisco Control Hub — 2 operation(s) for organizations.
  name: Cisco Control Hub Organizations API
  slug: cisco-control-hub-organizations-api
- baseURL: https://webexapis.com/v1
  baseurl_source: declared
  description: The People API from Cisco Control Hub — 2 operation(s) for people.
  name: Cisco Control Hub People API
  slug: cisco-control-hub-people-api
- baseURL: https://webexapis.com/v1
  baseurl_source: declared
  description: The Workspaces API from Cisco Control Hub — 1 operation(s) for workspaces.
  name: Cisco Control Hub Workspaces API
  slug: cisco-control-hub-workspaces-api
- baseURL: https://webexapis.com/v1
  baseurl_source: declared
  description: The Admin Audit Events API from Cisco Control Hub — 1 operation(s) for admin audit events.
  name: Cisco Control Hub Admin Audit Events API
  slug: cisco-control-hub-admin-audit-events-api
artifact_total: 23
collections:
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
- group: commercial
  href: https://artifacts.apis.io/cisco-control-hub/plans/cisco-control-hub-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cisco-control-hub-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cisco-control-hub/rate-limits/cisco-control-hub-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cisco-control-hub-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cisco-control-hub/finops/cisco-control-hub-finops.yml
  title: ''
  type: FinOps
  url: finops/cisco-control-hub-finops.yml
- group: other
  href: https://artifacts.apis.io/cisco-control-hub/capabilities/cisco-control-hub-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cisco-control-hub-capability-edges.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/webex/
- group: agent
  href: https://artifacts.apis.io/cisco-control-hub/agentic-access/cisco-control-hub-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cisco-control-hub-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cisco-control-hub/security/cisco-control-hub-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cisco-control-hub-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cisco-control-hub/authentication/cisco-control-hub-authentication.yml
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
- has_sources: false
  method: generated
  name: Cisco Control Hub Finops
  primary_unit: request
  service_category: API
  slug: cisco-control-hub-finops
  template: true
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
overview: 'Cisco Control Hub publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Devices API, Licenses API, Locations API, and 4 more. Tagged areas include Administration, Calling, Collaboration, Communications, and Device Management.


  The Cisco Control Hub catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cisco Control Hub''s developer surface includes authentication, engineering blog, and 7 more developer resources.'
plans:
- name: Cisco Control Hub Plans Pricing
  plan_count: 3
  slug: cisco-control-hub-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Cisco Control Hub Rate Limits
  slug: cisco-control-hub-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 49
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
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 52.5
    catalog_earned_first_party: 0.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 52.1
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 28.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cisco-control-hub/cisco-control-hub-2026-06-20T174357.png
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
- Identity and Access Management
- Licenses
- Reporting
- Webex
---
