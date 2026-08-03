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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: API for the OCUDU Ecosystem Foundation, providing programmatic access to the open collaboration platform for Radio Access Network reference implementations and AI-based RAN algorithms.
  name: OCUDU Ecosystem Foundation API
  slug: ocudu-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ocudu-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ocudu-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.linuxfoundation.org/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ocudu
- group: company
  title: ''
  type: Blog
  url: https://ocudu.org/feed/
created: '2026-03-16'
description: The OCUDU Ecosystem Foundation is a Linux Foundation project announced at MWC Barcelona in March 2026. It is an open collaboration hub dedicated to building a foundational reference platform for Radio Access Networks including AI-based algorithms, with founding members AMD, AT&T, Ericsson, Nokia, NVIDIA, and Verizon.
finops:
- name: Ocudu Finops
  service_category: API
  slug: ocudu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ocudu.png
layout: provider
modified: '2026-07-25'
name: OCUDU Ecosystem Foundation
nav: Providers
network: true
overview: 'OCUDU Ecosystem Foundation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Linux Foundation, RAN, and Telecom.


  OCUDU Ecosystem Foundation''s developer surface includes documentation, engineering blog, and 3 more developer resources.'
plans:
- name: Ocudu Plans Pricing
  plan_count: 3
  slug: ocudu-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 5
  name: Ocudu Rate Limits
  slug: ocudu-rate-limits
score:
  band: emerging
  composite: 19.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 19.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ocudu/refs/heads/main/screenshots/ocudu-2026-06-20T190617.png
security:
- kind: domain-security
  name: Ocudu Domain Security
  slug: ocudu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ocudu Vulnerability Disclosure
  slug: ocudu-vulnerability-disclosure
  summary_line: disclosure policy published
slug: ocudu
tags:
- AI
- Linux Foundation
- RAN
- Telecom
---
