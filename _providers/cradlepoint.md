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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Cradlepoint Agentic Access
  operation_count: 14
  slug: cradlepoint-agentic-access
  summary_line: 14 operations · 3 acting
api_count: 12
apis:
- description: The next-generation NetCloud Manager API. Documented with OpenAPI 3.0, authenticated with bearer tokens, designed for improved performance, stability, and usability over API v2. Coexists with v2 durin
  name: Cradlepoint NetCloud Manager API v3
  slug: netcloud-manager-api-v3
- description: Outbound HTTP destinations (alert_push_destinations) configured via the NCM API or UI to receive real-time JSON alert payloads when NCM alert rules fire (router offline, signal degradation, configurat
  name: Cradlepoint NetCloud Alert Webhooks
  slug: netcloud-webhooks
- description: On-router Python SDK and toolchain (the "SDK" / "Router SDK") for building and deploying custom applications onto Cradlepoint routers running NetCloud OS. Lets developers write Python apps that read r
  name: Cradlepoint NetCloud Router SDK
  slug: netcloud-router-sdk
- description: Account and subaccount management
  name: Cradlepoint Accounts API
  slug: cradlepoint-accounts-api
- description: Audit / activity logs across accounts
  name: Cradlepoint ActivityLogs API
  slug: cradlepoint-activitylogs-api
- description: Outbound webhook destinations for alert delivery
  name: Cradlepoint AlertPushDestinations API
  slug: cradlepoint-alertpushdestinations-api
- description: Alert monitoring rule configuration
  name: Cradlepoint AlertRules API
  slug: cradlepoint-alertrules-api
- description: Generated alerts
  name: Cradlepoint Alerts API
  slug: cradlepoint-alerts-api
- description: Logical device groupings
  name: Cradlepoint Groups API
  slug: cradlepoint-groups-api
- description: Current and historical router location
  name: Cradlepoint Locations API
  slug: cradlepoint-locations-api
- description: Modems, WAN devices, and network interfaces on routers
  name: Cradlepoint NetDevices API
  slug: cradlepoint-netdevices-api
- description: Router (edge device) management
  name: Cradlepoint Routers API
  slug: cradlepoint-routers-api
artifact_total: 37
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cradlepoint NetCloud Manager API v2 Accounts API
  slug: open-cradlepoint-accounts-api
- collection_type: open
  name: Cradlepoint NetCloud Manager API v2 Accounts ActivityLogs API
  slug: open-cradlepoint-activitylogs-api
- collection_type: open
  name: Cradlepoint NetCloud Manager API v2 Accounts AlertPushDestinations API
  slug: open-cradlepoint-alertpushdestinations-api
- collection_type: open
  name: Cradlepoint NetCloud Manager API v2 Accounts AlertRules API
  slug: open-cradlepoint-alertrules-api
- collection_type: open
  name: Cradlepoint NetCloud Manager API v2 Accounts Alerts API
  slug: open-cradlepoint-alerts-api
- collection_type: open
  name: Cradlepoint NetCloud Manager API v2 Accounts Groups API
  slug: open-cradlepoint-groups-api
- collection_type: open
  name: Cradlepoint NetCloud Manager API v2 Accounts Locations API
  slug: open-cradlepoint-locations-api
- collection_type: open
  name: Cradlepoint NetCloud Manager API v2
  slug: open-cradlepoint-netcloud-manager-api-v2
- collection_type: open
  name: Cradlepoint NetCloud Manager API v2 Accounts NetDevices API
  slug: open-cradlepoint-netdevices-api
- collection_type: open
  name: Cradlepoint NetCloud Manager API v2 Accounts Routers API
  slug: open-cradlepoint-routers-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cradlepoint-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cradlepoint-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cradlepoint-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cradlepoint-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://cradlepoint.com
- group: other
  title: ''
  type: Company
  url: https://cradlepoint.com/about-us/
- group: other
  title: ''
  type: Products
  url: https://cradlepoint.com/products/
- group: other
  title: ''
  type: NetCloud
  url: https://cradlepoint.com/products/netcloud-service/
- group: other
  title: ''
  type: NetCloudSASE
  url: https://cradlepoint.com/products/netcloud-sase/
- group: other
  title: ''
  type: Private5G
  url: https://cradlepoint.com/products/private-5g/
- group: other
  title: ''
  type: Developer
  url: https://developer.cradlepoint.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cradlepoint.com/
- group: operate
  title: ''
  type: Support
  url: https://customer.cradlepoint.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cradlepoint
- group: build
  title: ''
  type: APISamples
  url: https://github.com/cradlepoint/api-samples
- group: build
  title: ''
  type: SDKSamples
  url: https://github.com/cradlepoint/sdk-samples
- group: build
  title: ''
  type: ContainerSamples
  url: https://github.com/cradlepoint/container-samples
- group: company
  title: ''
  type: Blog
  url: https://cradlepoint.com/resources/blog/
- group: company
  title: ''
  type: News
  url: https://cradlepoint.com/news-events/
- group: commercial
  title: ''
  type: Pricing
  url: https://cradlepoint.com/lets-talk/
- group: company
  title: ''
  type: Careers
  url: https://cradlepoint.com/about-us/careers/
- group: operate
  title: ''
  type: Contact
  url: https://cradlepoint.com/lets-talk/
- group: other
  title: ''
  type: Ericsson
  url: https://www.ericsson.com/en/enterprise-wireless-solutions
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/cradlepoint
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cradlepoint
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Cradlepoint
- group: commercial
  title: ''
  type: Plans
  url: plans/cradlepoint-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cradlepoint-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cradlepoint-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cradlepoint-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/cradlepoint-rules.yml
created: '2026-05-25'
description: Cradlepoint is a Boise, Idaho-based provider of cloud-managed wireless edge routers, 5G adapters, branch-in-a-box appliances, and the NetCloud platform for enterprise wireless WAN (LTE/5G), in-vehicle networks, branch connectivity, and IoT. Ericsson acquired Cradlepoint in 2020 (closed November 2020 for approximately US$1.1B) and Cradlepoint now operates as the core of Ericsson Enterprise Wireless Solutions, working alongside Ericsson Private 5G and the Ericsson NetCloud SASE offering. Cradlepoint exposes its NetCloud Manager (NCM) platform through a documented RESTful API — NCM API v2 (Swagger 1.2, paired X-CP-API-ID/X-CP-API-KEY + X-ECM-API-ID/X-ECM-API-KEY headers, base https://www.cradlepointecm.com/api/v2/) and a newer NCM API v3 (OpenAPI 3.0, bearer-token authentication) — plus a NetCloud Router SDK for on-router Python applications and webhook destinations for alert delivery. The developer area (developer.cradlepoint.com), customer support article base (customer.cradlepoint.com),
  and Ericsson Enterprise Wireless docs portal (docs.cradlepoint.com) host the Getting Started guides, API reference, sample collections, and Postman bundles.
examples:
- key_count: 11
  name: Cradlepoint Alert Webhook Example
  slug: cradlepoint-alert-webhook-example
- key_count: 2
  name: Cradlepoint List Routers Example
  slug: cradlepoint-list-routers-example
finops:
- name: Cradlepoint Finops
  service_category: Networking
  slug: cradlepoint-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cradlepoint.png
json_schemas:
- name: Cradlepoint NCM Alert
  property_count: 11
  slug: cradlepoint-alert
- name: Cradlepoint Router
  property_count: 16
  slug: cradlepoint-router
jsonld:
- class_count: 0
  name: Cradlepoint Context
  property_count: 4
  slug: cradlepoint-context
layout: provider
modified: '2026-05-25'
name: Cradlepoint
nav: Providers
network: true
overview: 'Cradlepoint publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, ActivityLogs API, AlertPushDestinations API, and 6 more. Tagged areas include Wireless WAN, 5G, LTE, Edge, and Branch Networking.


  The Cradlepoint catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cradlepoint''s developer surface includes authentication, documentation, support, GitHub presence, engineering blog, product news, pricing, and 24 more developer resources.'
plans:
- name: Cradlepoint Plans Pricing
  plan_count: 5
  slug: cradlepoint-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Cradlepoint Rate Limits
  slug: cradlepoint-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Cradlepoint API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cradlepoint-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Cradlepoint API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 6
  slug: cradlepoint-rules
score:
  band: developing
  composite: 45.2
  delta: 4.8
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.8
    contract_quality: 64.6
    developer_ergonomics: 52.4
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 5.3
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cradlepoint/refs/heads/main/screenshots/cradlepoint-2026-06-20T175202.png
security:
- kind: authentication
  name: Cradlepoint Authentication
  slug: cradlepoint-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Cradlepoint Domain Security
  slug: cradlepoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cradlepoint Vulnerability Disclosure
  slug: cradlepoint-vulnerability-disclosure
  summary_line: disclosure policy published
slug: cradlepoint
tags:
- Wireless WAN
- 5G
- LTE
- Edge
- Branch Networking
- SD-WAN
- SASE
- Router
- In-Vehicle
- IoT
- Cellular
- Private 5G
- NetCloud
- Ericsson
website: https://cradlepoint.com
---
