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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: The Real-Time Streaming Protocol (RTSP) is a stateful protocol defined in RFC 2326 (1.0) and RFC 7826 (2.0). It defines methods including OPTIONS, DESCRIBE, SETUP, PLAY, PAUSE, RECORD, ANNOUNCE, GET_P
  name: RTSP Protocol
  slug: rtsp-protocol
- description: Common open-source RTSP server and client implementations used in production. MediaMTX (formerly rtsp-simple-server) is a ready-to-use media server supporting RTSP/RTMP/WebRTC with an HTTP API for man
  name: RTSP Implementations
  slug: rtsp-implementations
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rtsp-domain-security.yml
- group: docs
  title: ''
  type: Specification
  url: https://datatracker.ietf.org/doc/html/rfc7826
- group: docs
  title: ''
  type: Specification
  url: https://datatracker.ietf.org/doc/html/rfc2326
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Real-Time_Streaming_Protocol
created: '2025-01-01'
description: Real-Time Streaming Protocol (RTSP) is an application-level network protocol designed for controlling streaming media servers. Defined by IETF RFC 2326 (RTSP 1.0) and RFC 7826 (RTSP 2.0), it acts as a network remote control for multimedia servers, enabling on-demand delivery of real-time audio and video data. RTSP controls sessions between endpoints but relies on RTP (Real-time Transport Protocol) for actual media transport. It is widely used in IP cameras, DVR systems, media servers, and live streaming platforms.
finops:
- name: Rtsp Finops
  service_category: API
  slug: rtsp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rtsp.png
json_schemas:
- name: RTSP Session
  property_count: 8
  slug: rtsp-session
json_structures:
- name: Rtsp Session Structure
  property_count: 0
  slug: rtsp-session-structure
jsonld:
- class_count: 3
  name: Rtsp Context
  property_count: 8
  slug: rtsp-context
layout: provider
modified: '2026-05-02'
name: RTSP
nav: Providers
network: true
overview: 'RTSP publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Streaming, Video, Media, Protocol, and Real-Time.


  The RTSP catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Rtsp Plans Pricing
  plan_count: 3
  slug: rtsp-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 5
  name: Rtsp Rate Limits
  slug: rtsp-rate-limits
rules:
- name: RTSP API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rtsp-jsonschema-spectral-rules
score:
  band: emerging
  composite: 27.0
  delta: -4.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 8.1
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 31.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rtsp/refs/heads/main/screenshots/rtsp-2026-06-20T193241.png
security:
- kind: domain-security
  name: Rtsp Domain Security
  slug: rtsp-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: rtsp
tags:
- Streaming
- Video
- Media
- Protocol
- Real-Time
---
