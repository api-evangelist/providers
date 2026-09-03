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
  band: agent-aware
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: OASIS Standard publish/subscribe messaging protocol for IoT and M2M communication. MQTT v5.0 defines the wire format and behavior of CONNECT, PUBLISH, SUBSCRIBE, UNSUBSCRIBE, PINGREQ, DISCONNECT and o
  name: MQTT Version 5.0 Protocol
  slug: protocol-v5
- description: Previous OASIS Standard version of MQTT, still widely deployed across IoT brokers, devices, and cloud platforms. MQTT 3.1.1 defines the publish/subscribe messaging semantics, QoS levels 0/1/2, retaine
  name: MQTT Version 3.1.1 Protocol
  slug: protocol-v3-1-1
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mqtt-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mqtt
- group: company
  title: ''
  type: Website
  url: https://mqtt.org
- group: docs
  title: ''
  type: Specification
  url: https://mqtt.org/mqtt-specification/
- group: other
  title: ''
  type: OASIS Technical Committee
  url: https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=mqtt
- group: other
  title: ''
  type: Software Listings
  url: https://mqtt.org/software/
- group: company
  title: ''
  type: Blog
  url: https://www.oasis-open.org/feed/
created: '2026-05-11'
description: 'MQTT (Message Queuing Telemetry Transport) is an OASIS-standard, lightweight publish/subscribe messaging transport protocol designed for constrained devices and low-bandwidth, high-latency, or unreliable networks, making it the de-facto messaging protocol for IoT and machine-to-machine (M2M) communication. MQTT is a protocol specification rather than a hosted API: clients connect over TCP/TLS (typically port 1883 or 8883) or WebSocket (8080/8081) to an MQTT broker (such as Mosquitto, HiveMQ, EMQX, or AWS IoT Core) and exchange CONNECT, PUBLISH, SUBSCRIBE, and other control packets defined by the standard. The current standard is MQTT Version 5.0 (OASIS Standard, 7 March 2019); MQTT 3.1.1 remains widely deployed.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mqtt.png
layout: provider
modified: '2026-05-30'
name: MQTT
nav: Providers
network: true
overview: 'MQTT publishes 1 API on the [APIs.io](https://apis.io/) network: Version 5.0 Protocol. Tagged areas include MQTT, Messaging, Publish Subscribe, IoT, and M2M.


  MQTT''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 3
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 42.7
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 18.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mqtt/refs/heads/main/screenshots/mqtt-2026-06-20T185839.png
security:
- kind: domain-security
  name: Mqtt Domain Security
  slug: mqtt-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mqtt
tags:
- MQTT
- Messaging
- Publish Subscribe
- IoT
- M2M
- Protocol
- OASIS Standard
- Telemetry
website: https://mqtt.org
---
