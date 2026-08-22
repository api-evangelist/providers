---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-08-19'
api_count: 24
apis:
- description: The Mp1 reference point between MEC applications and the MEC platform, standardised in ETSI GS MEC 011. Covers MEC service registration, deregistration, discovery and event notification (MecServiceMgm
  name: ETSI MEC 011 Edge Platform Application Enablement API
  slug: mec-011-edge-platform-application-enablement
- description: The Radio Network Information Service (RNIS) defined in ETSI GS MEC 012, exposing up-to-date radio network conditions, measurement reports, cell change and carrier aggregation information from the RAN
  name: ETSI MEC 012 Radio Network Information API
  slug: mec-012-radio-network-information
- description: The MEC Location Service defined in ETSI GS MEC 013, providing network-derived location of user equipment and of radio nodes, zone and access-point occupancy, distance calculation, area and periodic l
  name: ETSI MEC 013 Location API
  slug: mec-013-location
- description: The UE Identity API from ETSI GS MEC 014, which lets a MEC application register a UE identity tag with the MEC platform so that traffic filtering rules can be applied to a specific device.
  name: ETSI MEC 014 UE Identity API
  slug: mec-014-ue-identity
- description: 'The two traffic-management APIs of ETSI GS MEC 015: Bandwidth Management, which lets applications register bandwidth requirements and priorities with the MEC platform, and Multi-access Traffic Steerin'
  name: ETSI MEC 015 Traffic Management APIs
  slug: mec-015-traffic-management
- description: The Mx2 reference point from ETSI GS MEC 016, used by a device-side application to discover which MEC applications are available in the system and to request instantiation or termination of a user app
  name: ETSI MEC 016 UE Application Interface API
  slug: mec-016-ue-application-interface
- description: ETSI GS MEC 010-2 Part 2 application package management, application lifecycle management and application grant APIs, used by an operations support system to onboard, instantiate, operate and terminat
  name: ETSI MEC 010-2 Application Package and Lifecycle Management APIs
  slug: mec-010-2-application-lifecycle-management
- description: The Application Mobility Service defined in ETSI GS MEC 021, which coordinates the relocation of a running application instance and its user context between MEC hosts as a device moves across the netw
  name: ETSI MEC 021 Application Mobility Service API
  slug: mec-021-application-mobility
- description: The WLAN Access Information Service from ETSI GS MEC 028, exposing access-point, station and measurement information from Wi-Fi networks to edge applications alongside the cellular information service
  name: ETSI MEC 028 WLAN Information API
  slug: mec-028-wlan-information
- description: The Fixed Access Information Service from ETSI GS MEC 029, extending MEC information exposure beyond mobile to fixed broadband access networks including PON and cable, so edge applications can read fi
  name: ETSI MEC 029 Fixed Access Information API
  slug: mec-029-fixed-access-information
- description: 'The V2X Information Service defined in ETSI GS MEC 030, providing predicted quality of service, provisioning information and multi-operator V2X message distribution for connected-vehicle applications '
  name: ETSI MEC 030 V2X Information Services API
  slug: mec-030-v2x-information-services
- description: 'The IoT API from ETSI GS MEC 033, defining how IoT device registration, IoT platform selection and device-to-platform association are managed by a MEC system so that IoT traffic can be terminated and '
  name: ETSI MEC 033 IoT API
  slug: mec-033-iot
- description: The MEC Federation enablement API from ETSI GS MEC 040, which lets edge systems operated by different providers discover one another, exchange availability zone and system information, and federate so
  name: ETSI MEC 040 MEC Federation Enablement API
  slug: mec-040-federation-enablement
- description: 'The RESTful protocols and data models of ETSI GS NFV-SOL 002 (Ve-Vnfm reference point, between a VNF and its VNF manager) and ETSI GS NFV-SOL 003 (Or-Vnfm reference point, between an NFV orchestrator '
  name: ETSI NFV SOL002 / SOL003 VNF Lifecycle, Fault, Performance and Package Management APIs
  slug: nfv-sol002-sol003
- description: The RESTful protocols and data models of ETSI GS NFV-SOL 005 on the Os-Ma-nfvo reference point, between an OSS/BSS and an NFV orchestrator. Covers network service descriptor management, network servic
  name: ETSI NFV SOL005 Os-Ma-nfvo Network Service Management APIs
  slug: nfv-sol005
- description: The RESTful protocols and data models of ETSI GS NFV-SOL 009 for managing the NFV management-and-orchestration functions themselves, covering NFV-MANO configuration and information management, fault m
  name: ETSI NFV SOL009 NFV-MANO Management APIs
  slug: nfv-sol009
- description: The RESTful protocols and data models of ETSI GS NFV-SOL 011 on the Or-Or reference point, used between NFV orchestrators in different administrative domains for nested network service descriptor mana
  name: ETSI NFV SOL011 Or-Or Multi-Administrative-Domain APIs
  slug: nfv-sol011
- description: The RESTful protocol and data model of ETSI GS NFV-SOL 012 for policy management across NFV management and orchestration, covering policy transfer, activation, deactivation, deletion and the associate
  name: ETSI NFV SOL012 Policy Management API
  slug: nfv-sol012
- description: The NGSI-LD API standardised by ETSI ISG CIM in GS CIM 009, a JSON-LD context information management API for entities, attributes, relationships, subscriptions, temporal queries, entity types, context
  name: ETSI NGSI-LD API (ISG CIM)
  slug: ngsi-ld
- description: The ETSI Software Development Group implementation of the 3GPP Common API Framework, TS 29.222. Harvested here are the API Invoker Management, API Provider Management, Access Control Policy and Auditi
  name: ETSI OpenCAPIF (3GPP CAPIF TS 29.222) APIs
  slug: opencapif
- description: A CAMARA Quality on Demand (QoD) Provisioning API implementation shipped as an add-on to ETSI OpenSlice. It wraps a running TM Forum service inventory entry so an operator can expose an existing 5G co
  name: ETSI OpenSlice CAMARA-as-a-Service QoD Provisioning API
  slug: openslice-camara-qod-provisioning
- description: The Open Exposure Gateway of the ETSI Operator Platform SDG, implementing the Open Exposure Gateway role defined by the GSMA Operator Platform Group. It exposes northbound CAMARA APIs to application p
  name: ETSI Operator Platform Open Exposure Gateway API
  slug: operator-platform-open-exposure-gateway
- description: ETSI SDG OpenSlice is an open-source service-based OSS delivering Network as a Service, and it exposes its catalog, ordering and inventory surface as TM Forum Open APIs. The documentation lists more t
  name: ETSI OpenSlice TM Forum Open APIs
  slug: openslice-tmforum-open-apis
- description: 'A hosted, free interactive environment where developers exercise live ETSI MEC service APIs against emulated 4G, 5G and Wi-Fi network scenarios with moving user equipment. It serves MEC 011, MEC 012, '
  name: ETSI MEC Sandbox / EdgeNative Connector
  slug: mec-sandbox-edgenative-connector
artifact_total: 30
asyncapis:
- description: ''
  name: Etsi Webhooks
  slug: etsi-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/etsi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.etsi.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.etsi.org/standards/get-standards
- group: other
  title: ''
  type: Standards
  url: https://www.etsi.org/deliver/
- group: start
  title: ''
  type: Portal
  url: https://portal.etsi.org/
- group: other
  title: ''
  type: Repository
  url: https://forge.etsi.org/rep/
- group: other
  title: ''
  type: Repository
  url: https://labs.etsi.org/rep/
- group: commercial
  title: ''
  type: License
  url: https://forge.etsi.org/legal-matters
- group: start
  title: ''
  type: Sandbox
  url: https://try-mec.etsi.org/
- group: other
  title: ''
  type: Wiki
  url: https://mecwiki.etsi.org/
- group: other
  title: ''
  type: OpenSource
  url: https://osl.etsi.org/
- group: other
  title: ''
  type: OpenSource
  url: https://ocf.etsi.org/
- group: other
  title: ''
  type: OpenSource
  url: https://tfs.etsi.org/
- group: other
  title: ''
  type: OpenSource
  url: https://osm.etsi.org/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.etsi.org/feed
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/etsi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/etsi-forge
- group: start
  title: ''
  type: DeveloperPortal
  url: https://forge.etsi.org/rep/
- group: docs
  title: ''
  type: APIReference
  url: https://www.etsi.org/standards/get-standards
- group: start
  title: ''
  type: GettingStarted
  url: https://www.etsi.org/standards/understanding-standards
- group: operate
  title: ''
  type: Support
  url: https://www.etsi.org/about/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.etsi.org/newsroom/
- group: operate
  title: ''
  type: Roadmap
  url: https://portal.etsi.org/webapp/WorkProgram/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.etsi.org/membership/contribution-classes
- group: start
  title: ''
  type: SignUp
  url: https://www.etsi.org/membership/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.etsi.org/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.etsi.org/privacy/
- group: company
  title: ''
  type: Newsletter
  url: https://www.etsi.org/subscribe-news/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/ETSIstandards
- group: other
  title: ''
  type: X
  url: https://x.com/ETSI_STANDARDS
- group: auth
  title: ''
  type: Security
  url: https://www.etsi.org/standards/coordinated-vulnerability-disclosure/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/etsi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/etsi-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/etsi-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/etsi-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/etsi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/etsi-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/etsi-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/etsi-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/etsi-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/etsi-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/etsi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/etsi-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/etsi-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/etsi-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/etsi-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/etsi-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/etsi-sandbox.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/etsi-mec-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/etsi-nfv-sol002-sol003-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/etsi-nfv-sol005-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/etsi-nfv-sol009-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/etsi-nfv-sol011-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/etsi-ngsi-ld-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/etsi-capif-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/etsi-camara-overlay.yaml
created: '2026-07-25'
description: 'ETSI, the European Telecommunications Standards Institute, is a not-for-profit standards development organisation headquartered in Sophia Antipolis, France, and one of only three bodies officially recognised by the European Union as a European Standards Organisation. With over 900 member organisations from more than 60 countries it standardises ICT across mobile, fixed, broadcast, IoT, security and emerging technologies, and it hosts the 3GPP Mobile Competence Centre. In the telecom value chain ETSI sits upstream of every operator and vendor: it does not run a network or sell connectivity, it writes the specifications that the network is built from. Its API posture is unusually open for a standards body. Every ETSI deliverable is downloadable free of charge without login from etsi.org/deliver, and the machine-readable API artefacts are published as BSD-3-Clause OpenAPI on two public GitLab instances, forge.etsi.org and labs.etsi.org, both of which serve an anonymous REST API.
  From those ETSI publishes the ISG MEC edge service APIs, the NFV SOL lifecycle and orchestration APIs, the ISG CIM NGSI-LD context information API, and open-source implementations including OpenCAPIF for 3GPP CAPIF, OpenSlice for TM Forum Open APIs, and an Operator Platform Open Exposure Gateway that exposes northbound CAMARA APIs. What is member-gated is participation, not publication: portal.etsi.org, working documents, drafting and voting sit behind ETSI membership, while the finished standards and their OpenAPI are open to anyone. ETSI itself is not a GSMA Open Gateway operator and not a CAMARA member organisation; it reaches CAMARA through liaison and through its own open-source code.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: etsi-mcp.yml
  slug: etsi-mcpyml
modified: '2026-07-25'
name: ETSI
nav: Providers
network: true
overview: 'ETSI publishes 23 APIs on the [APIs.io](https://apis.io/) network, including MEC 011 Edge Platform Application Enablement API, MEC 012 Radio Network Information API, MEC 013 Location API, and 20 more. Tagged areas include Telecommunications, France, Standards, Standards Body, and Network APIs.


  The ETSI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ETSI''s developer surface includes documentation, developer portal, sandbox, API reference, getting-started guide, support, engineering blog, and 50 more developer resources.'
random_paper: 17
scopes:
- name: Etsi Scopes
  scope_count: 13
  slug: etsi-scopes
  summary_line: 13 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 59.5
  delta: 4.9
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 16.7
    contract_quality: 51.3
    developer_ergonomics: 73.2
    discoverability: 77.8
    governance: 16.7
    operational_transparency: 42.1
  previous_composite: 54.6
  provenance:
    conformance: derived
    contracts:
      callable: 22.3
      derived: 0
      marker_coverage: 0.0
      total: 112
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 81.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/etsi/refs/heads/main/screenshots/etsi-2026-08-07T165027.png
security:
- kind: authentication
  name: Etsi Authentication
  slug: etsi-authentication
  summary_line: oauth2/openIdConnect/http · 4 schemes
- kind: domain-security
  name: Etsi Domain Security
  slug: etsi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Etsi Vulnerability Disclosure
  slug: etsi-vulnerability-disclosure
  summary_line: contact published
slug: etsi
tags:
- Telecommunications
- France
- Standards
- Standards Body
- Network APIs
- Edge Computing
- MEC
- NFV
- 5G
- CAMARA
- TM Forum
- 3GPP
- CAPIF
- NGSI-LD
- IoT
- Open Source
- Europe
- OpenAPI
- Network Slicing
- Broadband
website: https://www.etsi.org/
---
