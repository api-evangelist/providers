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
- acting_count: 16
  human_in_the_loop: 0
  name: Watchguard Agentic Access
  operation_count: 33
  slug: watchguard-agentic-access
  summary_line: 33 operations · 16 acting
api_count: 11
apis:
- description: Manage WatchGuard Cloud accounts and sub-accounts.
  name: WatchGuard Accounts API
  slug: watchguard-accounts-api
- description: Activate hardware devices and software licenses.
  name: WatchGuard Activations API
  slug: watchguard-activations-api
- description: Allocate and deallocate assets to managed accounts.
  name: WatchGuard Allocations API
  slug: watchguard-allocations-api
- description: Retrieve audience tokens for managed account API access.
  name: WatchGuard Authorization API
  slug: watchguard-authorization-api
- description: Manage endpoint security configurations.
  name: WatchGuard Configurations API
  slug: watchguard-configurations-api
- description: Perform actions on endpoint devices such as isolation and scanning.
  name: WatchGuard Device Actions API
  slug: watchguard-device-actions-api
- description: Manage and query endpoint devices.
  name: WatchGuard Devices API
  slug: watchguard-devices-api
- description: Retrieve endpoint security license information.
  name: WatchGuard Licenses API
  slug: watchguard-licenses-api
- description: Manage WatchGuard Cloud operator users.
  name: WatchGuard Operators API
  slug: watchguard-operators-api
- description: Retrieve risk assessment summaries and detected risks.
  name: WatchGuard Risk Assessment API
  slug: watchguard-risk-assessment-api
- description: Retrieve security event data and overviews.
  name: WatchGuard Security Events API
  slug: watchguard-security-events-api
artifact_total: 29
collections:
- collection_type: open
  name: WatchGuard Cloud Platform API
  slug: open-watchguard-cloud-platform
- collection_type: open
  name: WatchGuard Endpoint Security Management API
  slug: open-watchguard-endpoint-security
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/watchguard-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/watchguard-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/watchguard-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/watchguard-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WatchGuard
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/watchguard-technologies
- group: company
  title: ''
  type: Website
  url: https://www.watchguard.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.watchguard.com/help/docs/API/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cloud.watchguard.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.watchguard.com/help/docs/API/Content/en-US/api_get_started/get_started.html
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/watchguard-cloud-platform-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/watchguard-endpoint-security-openapi.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/watchguard-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/watchguard-device-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/watchguard-device-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/watchguard-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/watchguard-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.cloud.watchguard.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.watchguard.com/wgrd-news/blog/feed
created: '2025-02-17'
description: WatchGuard provides cloud-managed network and endpoint security solutions including Firebox next-generation firewalls, WatchGuard Endpoint Security (WES), AuthPoint multi-factor authentication, and WatchGuard Wi-Fi. WatchGuard Cloud is the unified management platform exposing RESTful APIs for account management, device activation, asset allocation, endpoint device management, security event monitoring, and operator administration.
examples:
- key_count: 3
  name: Watchguard Activatedevice Example
  slug: watchguard-activateDevice-example
- key_count: 3
  name: Watchguard Getaccount Example
  slug: watchguard-getAccount-example
- key_count: 3
  name: Watchguard Isolatedevices Example
  slug: watchguard-isolateDevices-example
- key_count: 3
  name: Watchguard Listdevices Example
  slug: watchguard-listDevices-example
finops:
- name: Watchguard Finops
  service_category: API
  slug: watchguard-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/watchguard.png
json_schemas:
- name: WatchGuard Endpoint Device
  property_count: 9
  slug: watchguard-device
json_structures:
- name: Watchguard Device Structure
  property_count: 0
  slug: watchguard-device-structure
jsonld:
- class_count: 9
  name: Watchguard Context
  property_count: 19
  slug: watchguard-context
layout: provider
modified: '2026-05-19'
name: WatchGuard
nav: Providers
network: true
overview: 'WatchGuard publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Activations API, Allocations API, and 8 more. Tagged areas include Cloud Security, Endpoint Security, Firewall, MFA, and Network Security.


  The WatchGuard catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  WatchGuard''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 15 more developer resources.'
plans:
- name: Watchguard Plans Pricing
  plan_count: 3
  slug: watchguard-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Watchguard Rate Limits
  slug: watchguard-rate-limits
rules:
- name: WatchGuard API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: watchguard-jsonschema-spectral-rules
- name: WatchGuard API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 0
    warning: 4
  slug: watchguard-rules
score:
  band: developing
  composite: 54.2
  delta: -3.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 71.2
    developer_ergonomics: 41.3
    discoverability: 72.2
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 57.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/watchguard/refs/heads/main/screenshots/watchguard-2026-06-20T201244.png
security:
- kind: authentication
  name: Watchguard Authentication
  slug: watchguard-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Watchguard Domain Security
  slug: watchguard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Watchguard Vulnerability Disclosure
  slug: watchguard-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: watchguard
tags:
- Cloud Security
- Endpoint Security
- Firewall
- MFA
- Network Security
- Zero Trust
website: https://www.watchguard.com
---
