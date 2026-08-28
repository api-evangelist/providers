---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    auth_clarity: negotiable
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
  score: 22.7
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Eaton Agentic Access
  operation_count: 15
  slug: eaton-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 19
apis:
- description: 'Subset of the Smart Breaker API surface scoped to Level-2 Green Motion EV charger devices (`hardwareType: ev-emcb`). Adds session-management, charge-control, and EV-specific telemetry on top of the sh'
  name: Eaton EV Smart Breaker Charger API
  slug: eaton-ev-smart-breaker-charger-api
- description: Healthcare-targeted subscription API that derives an "Activities of Daily Living" signal for residents of long-term care, assisted-living, and remote-care environments by applying proprietary ML/AI to
  name: Eaton Smart Ambient Monitoring API
  slug: eaton-smart-ambient-monitoring-api
- description: RESTful, HTTP-based API for utilities running Eaton Demand Response Management System (DRMS) programs. Exposes secure operations to interact with, schedule, and curtail Eaton Cellular and Wi-Fi load-c
  name: Brightlayer Demand Response Service API
  slug: brightlayer-demand-response-service-api
- description: Family of REST APIs that let partners and customers extend the monitoring capabilities of Eaton power infrastructure (UPS, PDU, transfer switches, breakers, meters) into their own applications via the
  name: Brightlayer Operations Insight APIs
  slug: brightlayer-operations-insight-apis
- description: RESTful API surface of Brightlayer 8.0 (on-premise platform) covering the unified Power, Distributed IT, DCIM, and EPMS product offerings. Documented in the "Brightlayer RESTful API User Guide, Releas
  name: Brightlayer RESTful API (On-Premise)
  slug: brightlayer-restful-api-on-premise
- description: RESTful API exposed by the Network Management Card (NMC) of Eaton's Rack PDU G4 (formerly Tripp Lite). Lets DCIM systems and IT operators provision outlets, query environmental sensors, schedule power
  name: Eaton Rack PDU G4 REST API
  slug: eaton-rack-pdu-g4-rest-api
- description: Critical Infrastructure Data (CI-Data) Open API listed on the Brightlayer Experience Hub from solution-partner WES. Provides a RESTful interface to Eaton's Electrical Power Monitoring System for real-
  name: CI-Data Open API (by WES)
  slug: ci-data-open-api-by-wes
- description: 'Eaton''s open-source design system and component library used to build Brightlayer applications. Ships themes, icons, progress icons, symbols, workflows, Storybook addons, and CLI templates for React, '
  name: Brightlayer UI (Design System)
  slug: brightlayer-ui-design-system
- description: JSON API on the Eaton easyE4 PLC / control relay that exposes I/O state, NET-IDs, markers, and configuration over HTTP for OT/IT integrations. Documented in the easyE4 JSON API user manual.
  name: Eaton easyE4 JSON API
  slug: eaton-easye4-json-api
- description: AI-powered digital energy twin co-developed with Autodesk that integrates Eaton's Brightlayer energy software with Autodesk Tandem to simulate, monitor, and optimize energy use, electrical system perf
  name: Brightlayer Digital Energy Twin (Autodesk)
  slug: brightlayer-digital-energy-twin-autodesk
- description: Eaton + NVIDIA reference architecture announced March 2026 for end-to-end AI-factory deployment on NVIDIA's Vera Rubin platform. Bundles supercapacitor-backed power, busbar power distribution, hot-ais
  name: Eaton Beam Rubin DSX Platform
  slug: eaton-beam-rubin-dsx-platform
- description: OAuth2 token issuance and user/service-account authentication.
  name: Eaton Authorization API
  slug: eaton-authorization-api
- description: Per-device and batch device-control commands.
  name: Eaton Device Commands API
  slug: eaton-device-commands-api
- description: Smart breakers and EV chargers (emcb, ev-emcb).
  name: Eaton Devices API
  slug: eaton-devices-api
- description: Real-time and historical energy telemetry.
  name: Eaton Energy Data API
  slug: eaton-energy-data-api
- description: Operations supported only by Eaton EV Smart Breaker Chargers.
  name: Eaton EV Only API
  slug: eaton-ev-only-api
- description: Device events, alarms, and notifications.
  name: Eaton Events API
  slug: eaton-events-api
- description: Sites, buildings, and panels grouping devices.
  name: Eaton Locations API
  slug: eaton-locations-api
- description: Tenant organizations that own devices and users.
  name: Eaton Organizations API
  slug: eaton-organizations-api
artifact_total: 49
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Eaton Smart Breaker Authorization API
  slug: open-eaton-authorization-api
- collection_type: open
  name: Eaton Smart Breaker Authorization Device Commands API
  slug: open-eaton-device-commands-api
- collection_type: open
  name: Eaton Smart Breaker Authorization Devices API
  slug: open-eaton-devices-api
- collection_type: open
  name: Eaton Smart Breaker Authorization Energy Data API
  slug: open-eaton-energy-data-api
- collection_type: open
  name: Eaton Smart Breaker Authorization EV Only API
  slug: open-eaton-ev-only-api
- collection_type: open
  name: Eaton Smart Breaker Authorization Events API
  slug: open-eaton-events-api
- collection_type: open
  name: Eaton Smart Breaker Authorization Locations API
  slug: open-eaton-locations-api
- collection_type: open
  name: Eaton Smart Breaker Authorization Organizations API
  slug: open-eaton-organizations-api
- collection_type: open
  name: Eaton Smart Breaker API
  slug: open-smart-breaker
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eaton-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eaton-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eaton-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/eaton-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://www.eaton.com/us/en-us/digital/brightlayer.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.eaton.com/get-started
- group: start
  title: ''
  type: DeveloperPortalAlt
  url: https://www.eaton.com/us/en-us/digital/for-developer-partners/developer_portal_get_started.html
- group: docs
  title: ''
  type: APISpecificationCatalog
  url: https://www.eaton.com/us/en-us/digital/for-developer-partners/API_Specification_Catalog.html
- group: other
  title: ''
  type: Marketplace
  url: https://eaton.byappdirect.com/
- group: other
  title: ''
  type: MarketplaceCatalog
  url: https://www.eaton.com/us/en-us/digital/brightlayer-experience-hub.html
- group: other
  title: ''
  type: Hub
  url: https://www.eaton.com/us/en-us/digital/brightlayer-experience-hub.html
- group: start
  title: ''
  type: Signup
  url: https://www.eaton.com/us/en-us/digital/for-developer-partners/developer_portal_get_started.html
- group: operate
  title: ''
  type: FAQ
  url: https://www.eaton.com/us/en-us/digital/for-developer-partners/developer_portal_FAQ.html
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://knowledgehub.eaton.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eaton.com/us/en-us/company/policies-and-statements/brightlayer-experience-hub-terms-and-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eaton.com/us/en-us/company/policies-and-statements/privacy-policy.html
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.eaton.com/us/en-us/company/policies-and-statements.html
- group: company
  title: ''
  type: Blog
  url: https://www.eaton.com/us/en-us/company/news-insights.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.eaton.com/us/en-us/company/news-insights/blog/brightlayer-8-0-release-whatsnew.html
- group: operate
  title: ''
  type: NewsReleases
  url: https://www.eaton.com/us/en-us/company/news-insights/news-releases.html
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@eatonvideos
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eaton
- group: other
  title: ''
  type: X
  url: https://x.com/ETN_Electrical
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brightlayer-ui
- group: operate
  title: ''
  type: Support
  url: https://www.eaton.com/us/en-us/support.html
- group: operate
  title: ''
  type: Contact
  url: https://www.eaton.com/us/en-us/company/contact-us.html
- group: other
  title: ''
  type: ProfessionalServices
  url: https://www.eaton.com/us/en-us/services.html
- group: other
  title: ''
  type: Branding
  url: https://www.eaton.com/us/en-us/company/about-us/our-brand.html
- group: commercial
  title: ''
  type: Pricing
  url: https://eaton.byappdirect.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/eaton-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eaton-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/eaton-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/eaton-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/eaton-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.eaton.com/llms.txt
created: '2026-05-23'
description: 'Eaton Corporation plc (NYSE: ETN) is a global intelligent-power-management company with operations across electrical, aerospace, vehicle, and eMobility segments. Its digital surface centers on Brightlayer — a software portfolio for data centers, utilities, industrial, buildings, and mobility — together with a developer program that exposes REST APIs for smart breakers, EV chargers, ambient monitoring, demand response, PDUs, and Brightlayer Operations Insight. Eaton is a strategic partner to NVIDIA on the Beam Rubin DSX 800 VDC AI-factory platform and to Autodesk on the Brightlayer Digital Energy Twin.'
examples:
- key_count: 2
  name: Smart Breaker Energy Telemetry Example
  slug: smart-breaker-energy-telemetry-example
- key_count: 2
  name: Smart Breaker List Devices Example
  slug: smart-breaker-list-devices-example
- key_count: 2
  name: Smart Breaker List Sessions Example
  slug: smart-breaker-list-sessions-example
- key_count: 2
  name: Smart Breaker Oauth Token Example
  slug: smart-breaker-oauth-token-example
- key_count: 2
  name: Smart Breaker Send Command Example
  slug: smart-breaker-send-command-example
finops:
- name: Eaton Finops
  service_category: ''
  slug: eaton-finops
image: https://www.eaton.com/etc.clientlibs/settings/wcm/designs/eaton/clientlibs/clientlib-base/resources/images/eaton-logo.svg
json_schemas:
- name: ChargingSession
  property_count: 7
  slug: smart-breaker-charging-session
- name: DeviceEvent
  property_count: 6
  slug: smart-breaker-device-event
- name: Device
  property_count: 8
  slug: smart-breaker-device
- name: EnergyReading
  property_count: 6
  slug: smart-breaker-energy-reading
json_structures:
- name: Smart Breaker Device Structure
  property_count: 0
  slug: smart-breaker-device-structure
jsonld:
- class_count: 40
  name: Eaton Context
  property_count: 3
  slug: eaton-context
layout: provider
modified: '2026-05-23'
name: Eaton
nav: Providers
network: true
overview: 'Eaton publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Device Commands API, Devices API, and 5 more. Tagged areas include Power Management, Electrical, Smart Breaker, EV Charging, and Demand Response.


  The Eaton catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Eaton''s developer surface includes authentication, developer portal, signup flow, FAQ, engineering blog, release notes, YouTube channel, and 28 more developer resources.'
plans:
- name: Eaton Plans Pricing
  plan_count: 9
  slug: eaton-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Eaton Rate Limits
  slug: eaton-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Eaton API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: eaton-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Eaton API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: smart-breaker-rules
scopes:
- name: Eaton Scopes
  scope_count: 0
  slug: eaton-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.5
  delta: 5.3
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 28.8
    contract_quality: 16.7
    developer_ergonomics: 35.7
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 18.4
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 54.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/eaton/refs/heads/main/screenshots/eaton-2026-06-20T180408.png
security:
- kind: authentication
  name: Eaton Authentication
  slug: eaton-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Eaton Domain Security
  slug: eaton-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eaton
tags:
- Power Management
- Electrical
- Smart Breaker
- EV Charging
- Demand Response
- Data-Center
- DCIM
- PDU
- UPS
- Utility
- Industrial
- Building
- Mobility
- AI Factory
- Energy
- IoT
- Sustainability
website: https://developer.eaton.com/get-started
---
