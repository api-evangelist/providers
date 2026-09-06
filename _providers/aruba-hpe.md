---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.3
  scored_at: '2026-09-05'
api_count: 10
apis:
- description: The HPE Aruba Networking Central REST API is the primary programmatic surface for the Aruba Central cloud network management platform. It exposes configuration, monitoring, AIOps, troubleshooting, App
  name: HPE Aruba Networking Central REST API
  slug: aruba-central-rest-api
- description: The Central Streaming API delivers real-time telemetry and event streams (location, presence, AppRF, audit, security, monitoring) over a long-lived connection. An official Python streaming client is p
  name: HPE Aruba Networking Central Streaming API
  slug: aruba-central-streaming-api
- description: 'Central Webhooks deliver alert and event notifications to external endpoints with HMAC-authenticated payloads. They are the integration path for ITSM, SIEM, SOAR, and operations tooling that needs to '
  name: HPE Aruba Networking Central Webhooks
  slug: aruba-central-webhooks
- description: 'The AOS-CX REST API runs on-box on every AOS-CX switch (CX 6000/8000/9000/10000 series) and exposes the full switch configuration and state surface — system, VRFs, VLANs, interfaces, LAGs, OSPF, BGP, '
  name: AOS-CX REST API
  slug: aos-cx-rest-api
- description: The ClearPass Policy Manager REST API exposes the network access control (NAC) surface of ClearPass — endpoints, devices, guests, onboarded users, sessions, policies, certificates, TACACS, and OnGuard
  name: HPE Aruba Networking ClearPass Policy Manager REST API
  slug: clearpass-rest-api
- description: The EdgeConnect Orchestrator API (formerly Silver Peak Orchestrator) manages EdgeConnect SD-WAN appliances, business intent overlays, tunnels, segments, application definitions, security policies, and
  name: HPE Aruba Networking EdgeConnect Orchestrator API
  slug: edgeconnect-orchestrator-api
- description: HPE Aruba Networking Fabric Composer (AFC) automates data-center fabric provisioning across AOS-CX leaf-spine, VSX, and EVPN-VXLAN deployments. The pyafc SDK and the hpeanfc-ansible-collection wrap it
  name: HPE Aruba Networking Fabric Composer API
  slug: fabric-composer-api
- description: The User Experience Insight (UXI, formerly Cape Networks) API exposes synthetic test results, sensor health, network and SaaS application performance scores, and incident data for UXI sensors deployed
  name: HPE Aruba Networking User Experience Insight API
  slug: uxi-cloud-api
- description: The HPE Aruba Networking SSE (Security Service Edge) API exposes the Axis Security / HPE SSE cloud-delivered ZTNA, SWG, and CASB surface for policy management, user/device enrollment, and event report
  name: HPE Aruba Networking SSE API
  slug: sse-api
- description: The Network Analytics Engine (NAE) is the on-box programmable telemetry and analytics framework that runs Python agents inside AOS-CX switches. The official nae-scripts repository contains analytics a
  name: AOS-CX Network Analytics Engine (NAE)
  slug: network-analytics-engine
artifact_total: 33
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aruba-hpe-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.arubanetworks.com
- group: docs
  title: ''
  type: Documentation
  url: https://devhub.arubanetworks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.arubanetworks.com
- group: docs
  title: ''
  type: Documentation
  url: https://devhub.arubanetworks.com/docs/aruba-central
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aruba
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aruba
- group: start
  title: ''
  type: Portal
  url: https://www.hpe.com/us/en/aruba-networking.html
- group: start
  title: ''
  type: Portal
  url: https://www.hpe.com
- group: operate
  title: ''
  type: Forums
  url: https://community.arubanetworks.com/
- group: operate
  title: ''
  type: Support
  url: https://www.arubanetworks.com/support-services/
- group: operate
  title: ''
  type: Support
  url: https://asp.arubanetworks.com/
- group: design
  title: ''
  type: Versioning
  url: https://www.arubanetworks.com/support-services/end-of-life/
- group: company
  title: ''
  type: Blog
  url: https://www.arubanetworks.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://www.arubanetworks.com/resource/
- group: docs
  title: ''
  type: Documentation
  url: https://www.arubanetworks.com/about-us/security-bulletins/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arubanetworks.com/legal/privacy-statement/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arubanetworks.com/legal/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://www.arubanetworks.com/contact-us/
- group: docs
  title: ''
  type: Documentation
  url: https://www.arubanetworks.com/company/about-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hpe-aruba-networking/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/HPE_Networking
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@HPENetworking
- group: build
  title: ''
  type: SDKs
  url: https://github.com/aruba/pycentral
- group: build
  title: ''
  type: SDKs
  url: https://github.com/aruba/pyaoscx
- group: build
  title: ''
  type: SDKs
  url: https://github.com/aruba/pyclearpass
- group: build
  title: ''
  type: SDKs
  url: https://github.com/aruba/pyedgeconnect
- group: build
  title: ''
  type: SDKs
  url: https://github.com/aruba/pyafc
- group: build
  title: ''
  type: SDKs
  url: https://github.com/aruba/pyhpeuxi
- group: build
  title: ''
  type: SDKs
  url: https://github.com/aruba/pyhpesse
- group: build
  title: ''
  type: SDKs
  url: https://github.com/aruba/pyarubaimc
- group: build
  title: ''
  type: SDKs
  url: https://github.com/aruba/aoscxgo
- group: build
  title: ''
  type: Tools
  url: https://github.com/aruba/aruba-central-ansible-collection
- group: build
  title: ''
  type: Tools
  url: https://github.com/aruba/aoscx-ansible-collection
- group: build
  title: ''
  type: Tools
  url: https://github.com/aruba/aos-switch-ansible-collection
- group: build
  title: ''
  type: Tools
  url: https://github.com/aruba/hpeanfc-ansible-collection
- group: build
  title: ''
  type: Tools
  url: https://github.com/aruba/terraform-provider-aoscx
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/aruba/central-python-workflows
- group: build
  title: ''
  type: Tools
  url: https://github.com/aruba/central-automation-studio
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/aruba/nae-scripts
- group: docs
  title: ''
  type: Schema
  url: https://github.com/aruba/aoscx-yang
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/aruba/clearpass-exchange-snippets
- group: build
  title: ''
  type: Tools
  url: https://github.com/aruba/clearpass-csv2api
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/aruba/sdwan-edgeconnect-performance-monitoring
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/aruba/aoscx-ansible-workflows
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/aruba/aoscx-ansible-dcn-workflows
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/aruba/central-integration-snippets
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/aruba/central-large-public-venue-monitoring-dashboard
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/aruba/aruba-iotops-example-ble
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/aruba/openlocate-ble-beacons
created: '2026-05-25T00:00:00.000Z'
description: HPE Aruba Networking is the networking business unit of Hewlett Packard Enterprise (NYSE HPE), born of Aruba Networks (founded 2002, acquired by HPE in 2015) and reinforced by the acquisitions of Silver Peak (SD-WAN, 2020), Axis Security (SSE, 2023), and Pensando (data processing units / smart switches, 2022). Its portfolio covers campus and branch Wi-Fi, AOS-CX and AOS-Switch data-center and campus switching, the Aruba Central cloud management plane, ClearPass network access control, EdgeConnect SD-WAN, the HPE Aruba Networking SSE cloud security service, the User Experience Insight synthetic-monitoring sensors, and the HPE Aruba Networking Fabric Composer data-center fabric controller. Aruba is one of the most API-first vendors in enterprise networking — its developer hub publishes REST, streaming, and webhook documentation; its GitHub org carries 50+ public repositories including Python SDKs (pycentral, pyaoscx, pyclearpass, pyedgeconnect, pyafc, pyhpeuxi, pyhpesse), a Go
  SDK (aoscxgo), Ansible collections, a Terraform provider, the Network Analytics Engine script library, and the YANG models that back AOS-CX.
features:
- Aruba Central — single-pane-of-glass cloud network management for AP, switch, gateway, and SD-WAN fleets
- AOS-CX — modern data-center / campus switch operating system with full on-box REST API and YANG models
- AOS-Switch — classic Aruba (HPE ProCurve lineage) switching with REST and CLI automation paths
- ClearPass Policy Manager — RADIUS / TACACS / 802.1X NAC with REST API and ClearPass Exchange ecosystem
- EdgeConnect SD-WAN (Silver Peak) — Orchestrator and on-box APIs with business intent overlays
- HPE Aruba Networking Fabric Composer — automated EVPN-VXLAN leaf-spine fabric provisioning
- User Experience Insight (UXI) — synthetic sensor monitoring for Wi-Fi, wired, and SaaS application health
- HPE Aruba Networking SSE — cloud SASE / ZTNA / SWG / CASB built on the Axis Security acquisition
- Network Analytics Engine (NAE) — on-box Python analytics agents inside AOS-CX
- Aruba IoT Operations — BLE/Zigbee/USB IoT gateway services on Aruba access points
- Aruba User Experience Insight, AirWave, and Aruba Sensor portfolio
- Aruba Central API Gateway with OAuth 2.0 and per-customer API tokens
- Webhooks with HMAC-signed delivery for Central alerts and events
- Streaming API for real-time monitoring, location, presence, and AppRF telemetry
- Official Python SDKs — pycentral, pyaoscx, pyclearpass, pyedgeconnect, pyafc, pyhpeuxi, pyhpesse, pyarubaimc
- Go SDK — aoscxgo
- Ansible — aruba-central, aoscx, aos-switch, and hpeanfc collections
- Terraform — terraform-provider-aoscx for declarative AOS-CX configuration
- Central Automation Studio — graphical front-end for chaining Central API workflows
- HPE Aruba Networking Developer Hub (devhub.arubanetworks.com) — public docs, code exchange, and tutorials
- Airheads Community — large active forum across networking, security, and automation
- Backed by Hewlett Packard Enterprise — public NYSE company, Fortune 500
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aruba-hpe.png
layout: provider
modified: '2026-05-25'
name: HPE Aruba Networking
nav: Providers
network: true
overview: 'HPE Aruba Networking publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Networking, Switching, Wi-Fi, SD-WAN, and NAC.


  HPE Aruba Networking''s developer surface includes developer portal, documentation, support, engineering blog, YouTube channel, tooling, code examples, and 43 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 3
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 42.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 23.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aruba-hpe/refs/heads/main/screenshots/aruba-hpe-2026-06-20T172448.png
security:
- kind: domain-security
  name: Aruba Hpe Domain Security
  slug: aruba-hpe-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aruba-hpe
tags:
- Networking
- Switching
- Wi-Fi
- SD-WAN
- NAC
- Network Access Control
- Cloud Networking
- AIOps
- Data-Center
- Campus
- Branch
- Edge
- SSE
- SASE
- HPE
website: https://www.arubanetworks.com
---
