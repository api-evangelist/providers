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
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 3
  name: Openbmc Agentic Access
  operation_count: 13
  slug: openbmc-agentic-access
  summary_line: 13 operations · 6 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: API for interacting with OpenBMC baseboard management controller firmware, providing programmatic access to server hardware management and monitoring capabilities.
  name: OpenBMC API
  slug: openbmc-api
- baseURL_template: https://{bmc}/redfish/v1
  baseurl_source: spec_template
  description: The AccountService API from OpenBMC — 1 operation(s) for accountservice.
  name: OpenBMC AccountService API
  slug: openbmc-accountservice-api
- baseURL_template: https://{bmc}/redfish/v1
  baseurl_source: spec_template
  description: The Chassis API from OpenBMC — 1 operation(s) for chassis.
  name: OpenBMC Chassis API
  slug: openbmc-chassis-api
- baseURL_template: https://{bmc}/redfish/v1
  baseurl_source: spec_template
  description: The Managers API from OpenBMC — 3 operation(s) for managers.
  name: OpenBMC Managers API
  slug: openbmc-managers-api
- baseURL_template: https://{bmc}/redfish/v1
  baseurl_source: spec_template
  description: The OpenBMC Redfish API API from OpenBMC — 1 operation(s) for openbmc redfish api.
  name: OpenBMC Redfish API
  slug: openbmc-openbmc-redfish-api-api
- baseURL_template: https://{bmc}/redfish/v1
  baseurl_source: spec_template
  description: The SessionService API from OpenBMC — 1 operation(s) for sessionservice.
  name: OpenBMC SessionService API
  slug: openbmc-sessionservice-api
- baseURL_template: https://{bmc}/redfish/v1
  baseurl_source: spec_template
  description: The Systems API from OpenBMC — 3 operation(s) for systems.
  name: OpenBMC Systems API
  slug: openbmc-systems-api
- baseURL_template: https://{bmc}/redfish/v1
  baseurl_source: spec_template
  description: The Event Service API from OpenBMC — 1 operation(s) for event service.
  name: OpenBMC Event Service API
  slug: openbmc-event-service-api
- baseURL_template: https://{bmc}/redfish/v1
  baseurl_source: spec_template
  description: The Update Service API from OpenBMC — 1 operation(s) for update service.
  name: OpenBMC Update Service API
  slug: openbmc-update-service-api
artifact_total: 24
collections:
- collection_type: open
  name: OpenBMC Redfish AccountService API
  slug: open-openbmc-accountservice-api
- collection_type: open
  name: OpenBMC Redfish AccountService Chassis API
  slug: open-openbmc-chassis-api
- collection_type: open
  name: OpenBMC Redfish AccountService EventService API
  slug: open-openbmc-eventservice-api
- collection_type: open
  name: OpenBMC Redfish AccountService Managers API
  slug: open-openbmc-managers-api
- collection_type: open
  name: OpenBMC Redfish AccountService OpenBMC Redfish API API
  slug: open-openbmc-openbmc-redfish-api-api
- collection_type: open
  name: OpenBMC Redfish AccountService SessionService API
  slug: open-openbmc-sessionservice-api
- collection_type: open
  name: OpenBMC Redfish AccountService Systems API
  slug: open-openbmc-systems-api
- collection_type: open
  name: OpenBMC Redfish AccountService UpdateService API
  slug: open-openbmc-updateservice-api
- collection_type: open
  name: OpenBMC Redfish API
  slug: open-openbmc
common:
- group: commercial
  href: https://artifacts.apis.io/openbmc/plans/openbmc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/openbmc-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/openbmc/rate-limits/openbmc-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/openbmc-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/openbmc/finops/openbmc-finops.yml
  title: ''
  type: FinOps
  url: finops/openbmc-finops.yml
- group: other
  href: https://artifacts.apis.io/openbmc/capabilities/openbmc-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/openbmc-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/openbmc/agentic-access/openbmc-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/openbmc-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/openbmc/authentication/openbmc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/openbmc-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/openbmc/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/openbmc
created: '2026-03-16'
description: OpenBMC is a Linux Foundation project producing an open source implementation of baseboard management controller firmware. Founded by Microsoft, Intel, IBM, Google, and Facebook, it provides a Linux-based firmware stack for managing and monitoring server hardware systems.
finops:
- has_sources: false
  method: generated
  name: Openbmc Finops
  primary_unit: request
  service_category: API
  slug: openbmc-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openbmc.png
layout: provider
modified: '2026-09-16'
name: OpenBMC
nav: Providers
network: true
overview: 'OpenBMC publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including AccountService API, Chassis API, Managers API, and 6 more. Tagged areas include Firmware, Hardware, Linux Foundation, and Servers.


  The OpenBMC catalog on APIs.io includes 1 Spectral governance ruleset.


  OpenBMC''s developer surface includes authentication, documentation, and 6 more developer resources.'
plans:
- name: Openbmc Plans Pricing
  plan_count: 3
  slug: openbmc-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Openbmc Rate Limits
  slug: openbmc-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: OpenBMC API Rules
  rule_count: 48
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 1
  slug: openbmc-rules
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.5
    catalog_earned_first_party: 0.0
    catalog_gap: 77.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 43.6
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 13.2
  previous_composite: 22.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/openbmc/openbmc-2026-06-20T190919.png
security:
- kind: authentication
  name: Openbmc Authentication
  slug: openbmc-authentication
  summary_line: apiKey · 1 scheme
slug: openbmc
tags:
- Firmware
- Hardware
- Linux Foundation
- Servers
---
