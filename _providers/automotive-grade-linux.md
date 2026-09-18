---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-09-17'
api_count: 2
apis:
- description: The AGL Application Framework provides APIs for managing applications on the AGL platform including installation, lifecycle management, permission enforcement, and inter-application communication. App
  name: AGL Application Framework API
  slug: agl-application-framework-api
- description: 'AGL uses SOME/IP (Scalable service-Oriented MiddlewarE over IP) via the vSomeIP library for vehicle service communication. This enables microservice communication between ECUs over Ethernet using the '
  name: AGL VSOMEIP Service API
  slug: vsomeip-service-api
- description: The AGL SoDeV (Software Defined Vehicle) reference platform provides APIs for software-defined vehicle architectures that decouple software from hardware. SoDeV builds on Zephyr RTOS and meta-AGL laye
  name: AGL SoDeV Software Defined Vehicle API
  slug: sodev-api
- description: The REST API of AGL's public LAVA (Linaro Automated Validation Architecture) continuous integration lab, where AGL images are booted and tested on real automotive hardware. Version v0.2 under /api/v0.
  name: AGL LAVA Test Lab API
  slug: agl-lava-api
- description: AGL runs its own Gerrit instance as the authoritative home of the AGL source tree - 263 projects including meta-agl, AGL-repo and the agl-service-* application-framework bindings. Its REST API is anon
  name: AGL Gerrit Code Review API
  slug: agl-gerrit-api
- description: The published interface specification between the Cluster UI in the HMI layer and the IC-Service in the service layer of an AGL instrument cluster. Revision 1.0, officially released 2026-02-04 after f
  name: AGL Instrument Cluster API
  slug: agl-instrument-cluster-api
- baseURL: https://www.automotivelinux.org/wp-json/tribe/events/v1
  baseurl_source: declared
  description: The Categories API from Automotive Grade Linux — 2 operation(s) for categories.
  name: Automotive Grade Linux Categories API
  slug: automotive-grade-linux-categories-api
- baseURL: https://www.automotivelinux.org/wp-json/tribe/events/v1
  baseurl_source: declared
  description: These operations are introduced by the Common library.
  name: Automotive Grade Linux Common API
  slug: automotive-grade-linux-common-api
- baseURL: https://www.automotivelinux.org/wp-json/tribe/events/v1
  baseurl_source: declared
  description: The Doc API from Automotive Grade Linux — 1 operation(s) for doc.
  name: Automotive Grade Linux Doc API
  slug: automotive-grade-linux-doc-api
- baseURL: https://www.automotivelinux.org/wp-json/tribe/events/v1
  baseurl_source: declared
  description: The Events API from Automotive Grade Linux — 7 operation(s) for events.
  name: Automotive Grade Linux Events API
  slug: automotive-grade-linux-events-api
- baseURL: https://www.automotivelinux.org/wp-json/tribe/events/v1
  baseurl_source: declared
  description: These operations are introduced by Events Pro.
  name: Automotive Grade Linux Events Pro API
  slug: automotive-grade-linux-events-pro-api
- baseURL: https://www.automotivelinux.org/wp-json/tribe/events/v1
  baseurl_source: declared
  description: The Organizers API from Automotive Grade Linux — 3 operation(s) for organizers.
  name: Automotive Grade Linux Organizers API
  slug: automotive-grade-linux-organizers-api
- baseURL: https://www.automotivelinux.org/wp-json/tribe/events/v1
  baseurl_source: declared
  description: The Tags API from Automotive Grade Linux — 2 operation(s) for tags.
  name: Automotive Grade Linux Tags API
  slug: automotive-grade-linux-tags-api
- baseURL: https://www.automotivelinux.org/wp-json/tribe/events/v1
  baseurl_source: declared
  description: The Venues API from Automotive Grade Linux — 3 operation(s) for venues.
  name: Automotive Grade Linux Venues API
  slug: automotive-grade-linux-venues-api
artifact_total: 34
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/overlays/automotive-grade-linux-events-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/automotive-grade-linux-events-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/overlays/automotive-grade-linux-events-tec-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/automotive-grade-linux-events-tec-v1-overlay.yaml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/packages/automotive-grade-linux-packages.yml
  title: ''
  type: Packages
  url: packages/automotive-grade-linux-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/packages/automotive-grade-linux-packages.yml
  title: ''
  type: SDKs
  url: packages/automotive-grade-linux-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/mcp/automotive-grade-linux-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/automotive-grade-linux-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/mcp/automotive-grade-linux-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/automotive-grade-linux-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/llms/automotive-grade-linux-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/automotive-grade-linux-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/well-known/automotive-grade-linux-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/automotive-grade-linux-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/well-known/automotive-grade-linux-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/automotive-grade-linux-api-catalog.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/conventions/automotive-grade-linux-conventions.yml
  title: ''
  type: Conventions
  url: conventions/automotive-grade-linux-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/lifecycle/automotive-grade-linux-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/automotive-grade-linux-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/changelog/automotive-grade-linux-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/automotive-grade-linux-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/errors/automotive-grade-linux-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/automotive-grade-linux-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/conformance/automotive-grade-linux-conformance.yml
  title: ''
  type: Conformance
  url: conformance/automotive-grade-linux-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/data-model/automotive-grade-linux-data-model.yml
  title: ''
  type: DataModel
  url: data-model/automotive-grade-linux-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/security/automotive-grade-linux-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/automotive-grade-linux-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/security/automotive-grade-linux-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/automotive-grade-linux-vulnerability-disclosure.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/plans/automotive-grade-linux-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/automotive-grade-linux-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/rate-limits/automotive-grade-linux-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/automotive-grade-linux-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/finops/automotive-grade-linux-finops.yml
  title: ''
  type: FinOps
  url: finops/automotive-grade-linux-finops.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.automotivelinux.org/en/master/05_APIs_and_Services/instrument-cluster/AGL-Instrument-Cluster-API-en/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.automotivelinux.org/software/download/get-started/
- group: operate
  title: ''
  type: Support
  url: https://lists.automotivelinux.org/g/agl-main
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/ZztCaVeQVG
- group: docs
  title: ''
  type: Documentation
  url: https://lf-automotivelinux.atlassian.net/wiki/spaces/HOME/
- group: build
  title: ''
  type: SourceCode
  url: https://gerrit.automotivelinux.org
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.linuxfoundation.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linuxfoundation.org/privacy
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UC1axavgir413w00rwBHPAtQ
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/authentication/automotive-grade-linux-authentication.yml
  title: ''
  type: Authentication
  url: authentication/automotive-grade-linux-authentication.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/COVESA/vsomeip/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/COVESA/vsomeip/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/COVESA/vsomeip/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/COVESA/vsomeip/blob/master/LICENSE
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/security/automotive-grade-linux-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/automotive-grade-linux-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.automotivelinux.org/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/automotive-grade-linux
- group: company
  title: ''
  type: Website
  url: https://www.automotivelinux.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.automotivelinux.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/automotive-grade-linux
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/automotive-grade-linux/meta-agl-monorepo
created: '2026-03-16'
description: Automotive Grade Linux (AGL) is a collaborative open source project under the Linux Foundation that develops a unified software platform for connected vehicles. AGL brings together automakers (Toyota, Honda, Mercedes-Benz), suppliers, and technology companies to build an open Linux-based software stack for in-vehicle infotainment, instrument clusters, telematics, and software-defined vehicle (SoDeV) architectures. The platform decouples software from hardware enabling rapid automotive application development.
features:
- description: AGL uses the Yocto Project and OpenEmbedded build framework with meta-AGL layers for creating customized embedded Linux distributions targeting automotive hardware platforms including Renesas R-Car and Raspberry Pi.
  name: Yocto-Based Build System
- description: Service-oriented in-vehicle communication using the SOME/IP protocol via vSomeIP for microservice architectures across ECUs over automotive Ethernet networks.
  name: SOME/IP Vehicle Services
- description: AGL SoDeV reference platform for decoupling software from hardware, enabling flexible, updatable in-vehicle software architectures using Zephyr RTOS and container-based application isolation.
  name: Software Defined Vehicle (SoDeV)
- description: OTA update framework for delivering software updates to AGL-based in-vehicle systems without physical access, supporting fleet-wide update management.
  name: Over-The-Air Updates
- description: Wayland/Weston-based display framework for in-vehicle infotainment and digital instrument cluster applications with automotive-grade display requirements.
  name: IVI and Instrument Cluster Support
finops:
- name: Automotive Grade Linux Finops
  service_category: API
  slug: automotive-grade-linux-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/automotive-grade-linux.png
integrations:
- description: Integration with the COVESA Vehicle Signal Specification (VSS) for standardized access to vehicle sensor and actuator data.
  name: COVESA Vehicle Signal Specification
- description: Integration with Eclipse KUKSA for vehicle signal API abstraction enabling portable in-vehicle application development.
  name: Eclipse KUKSA
- description: AGL SoDeV integrates Zephyr RTOS for safety-critical microcontroller domains within software-defined vehicle architectures.
  name: Zephyr RTOS
- description: Primary hardware reference platform support for Renesas R-Car SoCs used in production automotive IVI and cluster systems.
  name: Renesas R-Car Platforms
layout: provider
mcp_servers:
- description: ''
  name: Automotive Grade Linux MCP Server
  slug: automotive-grade-linux-mcp-server
modified: '2026-09-14'
name: Automotive Grade Linux
nav: Providers
network: true
overview: 'Automotive Grade Linux publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Common API, Doc API, and 5 more. Tagged areas include Automotive, Connected Vehicles, Embedded Linux, In-Vehicle Infotainment, and IoT.


  Automotive Grade Linux''s developer surface includes changelog, API reference, getting-started guide, support, documentation, YouTube channel, authentication, and 35 more developer resources.'
plans:
- name: Automotive Grade Linux Plans Pricing
  plan_count: 0
  slug: automotive-grade-linux-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Automotive Grade Linux Rate Limits
  slug: automotive-grade-linux-rate-limits
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 50.7
    developer_ergonomics: 61.9
    discoverability: 66.7
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 50.0
  previous_composite: 43.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/screenshots/automotive-grade-linux-2026-06-20T172702.png
security:
- kind: authentication
  name: Automotive Grade Linux Authentication
  slug: automotive-grade-linux-authentication
  summary_line: http/token · 2 schemes
- kind: domain-security
  name: Automotive Grade Linux Domain Security
  slug: automotive-grade-linux-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Automotive Grade Linux Vulnerability Disclosure
  slug: automotive-grade-linux-vulnerability-disclosure
  summary_line: Hackerone
slug: automotive-grade-linux
tags:
- Automotive
- Connected Vehicles
- Embedded Linux
- In-Vehicle Infotainment
- IoT
- Linux Foundation
- Open-Source
- Software Defined Vehicles
use_cases:
- description: Develop navigation, media, and connectivity applications for automotive head units using AGL application framework APIs and the Wayland display system.
  name: In-Vehicle Infotainment Development
- description: Build telematics, V2X communication, and cloud connectivity capabilities on AGL-based vehicle computing platforms.
  name: Connected Car Platform
- description: Design vehicle software architectures that decouple application software from hardware using AGL SoDeV as the foundation platform.
  name: Software Defined Vehicle Architecture
- description: Create digital instrument cluster applications for speedometers, tachometers, and ADAS status displays using AGL display APIs.
  name: Instrument Cluster Applications
website: https://www.automotivelinux.org
---
