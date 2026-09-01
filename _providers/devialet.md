---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 18
  human_in_the_loop: 6
  name: Devialet Agentic Access
  operation_count: 25
  slug: devialet-agentic-access
  summary_line: 25 operations · 18 acting · 6 human-in-the-loop
api_count: 1
apis:
- description: Equalizer and night-mode settings, hosted by the system leader.
  name: Devialet Audio Settings API
  slug: devialet-audio-settings-api
- description: Individual physical Devialet products on the local network, including accessories.
  name: Devialet Devices API
  slug: devialet-devices-api
- description: Sets of one or more systems playing the same content in the multi-room configuration.
  name: Devialet Groups API
  slug: devialet-groups-api
- description: Play, pause, mute, unmute, next, and previous on the group's current source.
  name: Devialet Playback API
  slug: devialet-playback-api
- description: Volume query and control at the system level.
  name: Devialet Sound Control API
  slug: devialet-sound-control-api
- description: Sets of one or more speakers that always share playback state (solo or stereo).
  name: Devialet Systems API
  slug: devialet-systems-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Devialet IP Control Audio Settings API
  slug: open-devialet-audio-settings-api
- collection_type: open
  name: Devialet IP Control Devices API
  slug: open-devialet-devices-api
- collection_type: open
  name: Devialet IP Control Groups API
  slug: open-devialet-groups-api
- collection_type: open
  name: Devialet IP Control Playback API
  slug: open-devialet-playback-api
- collection_type: open
  name: Devialet IP Control Sound Control API
  slug: open-devialet-sound-control-api
- collection_type: open
  name: Devialet IP Control Systems API
  slug: open-devialet-systems-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/devialet-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/devialet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.devialet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.devialet.com/hc/en-us/articles/4415207423378-Phantom-s-documentation-for-piloting-them-via-IP
- group: docs
  title: ''
  type: APIReference
  url: openapi/_original/devialet-ip-control-r1.pdf
- group: operate
  title: ''
  type: Support
  url: https://help.devialet.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/devialet
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.devialet.com/en-eu/legal/general-terms-of-sale/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.devialet.com/en-eu/legal/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.devialet.com/en-eu/legal/compliance/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/devialet-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/devialet-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/devialet-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/devialet-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/devialet-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/devialet-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/devialet-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/devialet-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/devialet-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/devialet-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/devialet-ip-control-examples.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/devialet-ip-control-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/devialet-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/devialet-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: HiiveListing
  url: https://www.hiive.com/securities/devialet-stock
created: '2026-08-04'
description: Devialet is a French high-end audio company founded and headquartered in Paris, known for the Phantom active loudspeaker range, the Dione soundbar, the Mania portable speaker, the Gemini earbuds, and the Expert Pro amplifier line, and for patented acoustic technologies including ADH (Analog Digital Hybrid), SAM (Speaker Active Matching), and the EVO embedded platform. Its developer-facing surface is the Devialet IP Control API — an unauthenticated HTTP API served by the speakers themselves on the local network under the /ipcontrol/v1 path, introduced with DOS 2.14 firmware and documented by Devialet as a PDF reference for system integrators. It exposes device, system, and group state plus playback, volume, equalizer, night mode, Bluetooth pairing, and power and factory-reset commands, with mDNS/DNS-SD discovery. Devialet also ships certified home-automation drivers for Crestron and Control4 alongside the raw API.
image: https://assets.devialet.com//media/dvl_media/Visual_Devialet_Phantom_Ultimate_98_dB_Stereo_LP_16_9.png?twic=v1/cover=1.91:1/resize=1200x630
layout: provider
mcp_servers:
- description: ''
  name: Devialet MCP Server
  slug: devialet-mcp-server
modified: '2026-08-04'
name: Devialet
nav: Providers
network: true
overview: 'Devialet publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Audio Settings API, Devices API, Groups API, and 3 more. Tagged areas include Audio, Consumer Electronics, Smart Speakers, Home Automation, and Custom Installation.


  Devialet''s developer surface includes documentation, API reference, support, authentication, changelog, code examples, and 20 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 15.4
    developer_ergonomics: 35.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 27.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/devialet/refs/heads/main/screenshots/devialet-2026-08-07T164327.png
security:
- kind: authentication
  name: Devialet Authentication
  slug: devialet-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Devialet Domain Security
  slug: devialet-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: devialet
tags:
- Audio
- Consumer Electronics
- Smart Speakers
- Home Automation
- Custom Installation
- Device Control
- Local Network API
- IoT
- Hardware
- Music
- France
website: https://www.devialet.com/
---
