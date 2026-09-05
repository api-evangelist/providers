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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 0
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/http2
- group: docs
  title: ''
  type: Reference
  url: https://httpwg.org/specs/rfc7540.html
- group: company
  title: ''
  type: Website
  url: https://http2.github.io/
- group: docs
  title: ''
  type: HPACK Specification
  url: https://httpwg.org/specs/rfc7541.html
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/HTTP/2
created: '2025'
description: HTTP/2 is the second major version of the Hypertext Transfer Protocol, defined by the IETF in RFC 7540 and standardized in 2015. It optimizes use of network resources and reduces perceived latency by introducing a binary framing layer over a single TCP connection, with full request and response multiplexing across independent bidirectional streams. HTTP/2 uses HPACK header compression to eliminate redundant header data, credit-based flow control via WINDOW_UPDATE frames, stream prioritization through dependencies and weights, and server push via PUSH_PROMISE frames to proactively deliver anticipated resources. Core frame types include DATA, HEADERS, PRIORITY, RST_STREAM, SETTINGS, PUSH_PROMISE, PING, and GOAWAY, with the protocol preserving the existing HTTP semantics of methods, status codes, and headers while transforming how they are transported on the wire.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/http-2.png
layout: provider
modified: '2026-04-28'
name: HTTP/2
nav: Providers
network: true
overview: HTTP/2 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Binary Framing, HPACK, HTTP, HTTP/2, and IETF.
random_paper: 18
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 1
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 6.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/http-2/refs/heads/main/screenshots/http-2-2026-06-20T182904.png
slug: http-2
tags:
- Binary Framing
- HPACK
- HTTP
- HTTP/2
- IETF
- Multiplexing
- Networking
- Performance
- Protocol
- RFC 7540
- Server Push
website: https://http2.github.io/
---
