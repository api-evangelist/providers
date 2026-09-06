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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'The de facto standard programming interface for TCP/IP networking, defined in RFC 3493. Implemented nearly ubiquitously in modern operating systems and programming languages, the Sockets API provides '
  name: Berkeley Sockets API
  slug: sockets-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tcp-ip-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.rfc-editor.org/
- group: docs
  title: ''
  type: Documentation
  url: https://datatracker.ietf.org/
- group: docs
  title: ''
  type: Specification
  url: https://www.rfc-editor.org/rfc/rfc9293
- group: docs
  title: ''
  type: Specification
  url: https://www.rfc-editor.org/rfc/rfc791
- group: docs
  title: ''
  type: Specification
  url: https://www.rfc-editor.org/rfc/rfc768
- group: docs
  title: ''
  type: Specification
  url: https://www.rfc-editor.org/rfc/rfc1180
- group: docs
  title: ''
  type: Specification
  url: https://www.rfc-editor.org/rfc/rfc3493
- group: docs
  title: ''
  type: Specification
  url: https://www.rfc-editor.org/rfc/rfc4614
- group: company
  title: ''
  type: Website
  url: https://www.ietf.org/
created: '2025-01-01'
description: TCP/IP (Transmission Control Protocol/Internet Protocol) is the foundational communication protocol suite that powers the internet and most computer networks. It provides reliable, ordered delivery of data between applications across diverse network hardware through a layered architecture of protocols. The suite encompasses protocols at multiple layers including TCP, IP, UDP, HTTP, and many others, defined through IETF RFCs maintained at the RFC Editor.
finops:
- name: Tcp Ip Finops
  service_category: API
  slug: tcp-ip-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tcp-ip.png
layout: provider
modified: '2026-05-03'
name: TCP/IP
nav: Providers
network: true
overview: 'TCP/IP publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Networking, Protocol, Internet, Standards, and IETF.


  TCP/IP''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Tcp Ip Plans Pricing
  plan_count: 3
  slug: tcp-ip-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Tcp Ip Rate Limits
  slug: tcp-ip-rate-limits
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 12.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tcp-ip/refs/heads/main/screenshots/tcp-ip-2026-06-20T194943.png
security:
- kind: domain-security
  name: Tcp Ip Domain Security
  slug: tcp-ip-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: tcp-ip
tags:
- Networking
- Protocol
- Internet
- Standards
- IETF
- RFC
- TCP
- IP
website: https://www.ietf.org/
---
