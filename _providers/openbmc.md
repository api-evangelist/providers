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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
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
  description: The EventService API from OpenBMC — 1 operation(s) for eventservice.
  name: OpenBMC EventService API
  slug: openbmc-eventservice-api
- baseURL_template: https://{bmc}/redfish/v1
  baseurl_source: spec_template
  description: The Managers API from OpenBMC — 3 operation(s) for managers.
  name: OpenBMC Managers API
  slug: openbmc-managers-api
- baseURL_template: https://{bmc}/redfish/v1
  baseurl_source: spec_template
  description: The OpenBMC Redfish API API from OpenBMC — 1 operation(s) for openbmc redfish api.
  name: OpenBMC OpenBMC Redfish API API
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
  description: The UpdateService API from OpenBMC — 1 operation(s) for updateservice.
  name: OpenBMC UpdateService API
  slug: openbmc-updateservice-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/openbmc-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openbmc-agentic-access.yml
- group: auth
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
- name: Openbmc Finops
  service_category: API
  slug: openbmc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openbmc.png
layout: provider
modified: '2026-04-28'
name: OpenBMC
nav: Providers
network: true
overview: 'OpenBMC publishes 8 APIs on the [APIs.io](https://apis.io/) network, including AccountService API, Chassis API, EventService API, and 5 more. Tagged areas include Firmware, Hardware, Linux Foundation, and Server.


  OpenBMC''s developer surface includes authentication, documentation, and 3 more developer resources.'
plans:
- name: Openbmc Plans Pricing
  plan_count: 3
  slug: openbmc-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Openbmc Rate Limits
  slug: openbmc-rate-limits
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 48.5
    developer_ergonomics: 21.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 26.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openbmc/refs/heads/main/screenshots/openbmc-2026-06-20T190919.png
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
- Server
---
