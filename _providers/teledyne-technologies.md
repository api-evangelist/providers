---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Teledyne Technologies Agentic Access
  operation_count: 7
  slug: teledyne-technologies-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: The Spinnaker SDK provides programmatic control of Teledyne FLIR and DALSA machine vision cameras over USB3, GigE, 5GigE, and 10GigE interfaces. Supports C++, C#, Python, and Java with a cross-platfor
  name: Teledyne FLIR Spinnaker SDK
  slug: flir-spinnaker-sdk
- description: The FLIR Mobile SDK enables iOS and Android developers to build mobile applications that integrate thermal imaging capabilities from Teledyne FLIR professional thermal cameras. Supports data collectio
  name: Teledyne FLIR Mobile SDK
  slug: flir-mobile-sdk
- description: ActiveDSO is Teledyne LeCroy's ActiveX/COM control enabling remote automation of MAUI-based oscilloscopes from Windows applications via SCPI commands, VISA drivers, Ethernet (ENET), GPIB, and USBTMC i
  name: Teledyne LeCroy ActiveDSO API
  slug: lecroy-activedso-api
- description: The Alarms API from Teledyne Technologies — 2 operation(s) for alarms.
  name: Teledyne Technologies Alarms API
  slug: teledyne-technologies-alarms-api
- description: The Images API from Teledyne Technologies — 1 operation(s) for images.
  name: Teledyne Technologies Images API
  slug: teledyne-technologies-images-api
- description: The Measurements API from Teledyne Technologies — 4 operation(s) for measurements.
  name: Teledyne Technologies Measurements API
  slug: teledyne-technologies-measurements-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Teledyne FLIR Camera REST API
  slug: open-teledyne-flir-camera-rest
- collection_type: open
  name: Teledyne FLIR Camera REST Alarms API
  slug: open-teledyne-technologies-alarms-api
- collection_type: open
  name: Teledyne FLIR Camera REST Alarms Images API
  slug: open-teledyne-technologies-images-api
- collection_type: open
  name: Teledyne FLIR Camera REST Alarms Measurements API
  slug: open-teledyne-technologies-measurements-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/teledyne-technologies-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teledyne-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.teledyne.com/en-us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.flir.com/developer/mobile-sdk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/FLIR
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Teledyne-MV
- group: company
  title: ''
  type: Website
  url: https://www.teledynelecroy.com/
- group: company
  title: ''
  type: Website
  url: https://www.teledyneimaging.com/
- group: company
  title: ''
  type: Website
  url: https://www.teledyne-api.com/en-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teledyne-technologies
created: '2026-03-24'
description: Teledyne Technologies Incorporated is a leading provider of sophisticated digital imaging products and software, instrumentation, aerospace and defense electronics, and engineered systems. Headquartered in Thousand Oaks, California, Teledyne serves the defense, commercial, and industrial markets. Key subsidiaries include Teledyne FLIR (thermal imaging cameras and systems), Teledyne LeCroy (oscilloscopes and protocol analyzers), Teledyne Imaging (scientific and industrial cameras), and Teledyne API (air quality monitoring instruments). Teledyne FLIR provides REST APIs and SDKs for thermal camera integration, while Teledyne LeCroy provides ActiveDSO and VISA-based automation APIs for test and measurement instruments.
examples:
- key_count: 2
  name: Teledyne Get All Alarms Example
  slug: teledyne-get-all-alarms-example
- key_count: 2
  name: Teledyne Get Box Measurement Example
  slug: teledyne-get-box-measurement-example
- key_count: 2
  name: Teledyne Get Spot Measurement Example
  slug: teledyne-get-spot-measurement-example
finops:
- name: Teledyne Technologies Finops
  service_category: Instrumentation / Defense Electronics
  slug: teledyne-technologies-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teledyne-technologies.png
json_schemas:
- name: Teledyne FLIR Camera Alarm
  property_count: 7
  slug: teledyne-flir-alarm
- name: Teledyne FLIR Temperature Measurement
  property_count: 0
  slug: teledyne-flir-measurement
json_structures:
- name: Teledyne Flir Measurement Structure
  property_count: 0
  slug: teledyne-flir-measurement-structure
jsonld:
- class_count: 26
  name: Teledyne Technologies Context
  property_count: 0
  slug: teledyne-technologies-context
layout: provider
modified: '2026-05-19'
name: Teledyne Technologies
nav: Providers
network: true
overview: 'Teledyne Technologies publishes 3 APIs on the [APIs.io](https://apis.io/) network: Alarms API, Images API, and Measurements API. Tagged areas include Aerospace, Defense, Digital Imaging, Instrumentation, and Thermal Imaging.


  The Teledyne Technologies catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Teledyne Technologies'' developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: Teledyne Technologies Plans Pricing
  plan_count: 1
  slug: teledyne-technologies-plans-pricing
press:
- date: '2026-05-25'
  title: Teledyne FLIR OEM Advances State of the Art in Infrared ...
  url: https://www.teledyne.com/en-us/news/Pages/teledyne-flir-oem-advances-state-of-the-art-in-infrared-imaging.aspx
- date: '2026-05-25'
  title: News - Teledyne FLIR OEM
  url: https://oem.flir.com/about/news/
- date: '2026-05-25'
  title: Innovation at every layer. Teledyne FLIR OEM delivers ...
  url: https://www.facebook.com/FLIR/posts/innovation-at-every-layerteledyne-flir-oem-delivers-industry-leading-ndaa-compli/1252638966900095/
- date: '2026-05-25'
  title: Test Solutions for Enhanced AI Performance
  url: https://www.teledynelecroy.com/serialdata/artificial_intelligence
- date: '2026-05-25'
  title: Teledyne to Hold Investor Meetings
  url: https://www.teledyne.com/en-us/news/Pages/teledyne-to-hold-investor-meetings-20250902.aspx
random_paper: 3
rate_limits:
- limit_count: 1
  name: Teledyne Technologies Rate Limits
  slug: teledyne-technologies-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Teledyne Technologies API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: teledyne-technologies-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Teledyne Technologies API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 6
  slug: teledyne-technologies-rules
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 17
    catalog_gap: 38.5
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 13.6
    contract_quality: 58.0
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 29.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/teledyne-technologies/refs/heads/main/screenshots/teledyne-technologies-2026-06-20T195024.png
security:
- kind: domain-security
  name: Teledyne Technologies Domain Security
  slug: teledyne-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: teledyne-technologies
tags:
- Aerospace
- Defense
- Digital Imaging
- Instrumentation
- Thermal Imaging
- Test and Measurement
- Fortune 500
website: https://www.teledyne.com/en-us
---
