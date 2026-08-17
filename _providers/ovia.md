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
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.7
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://wepow.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://harver.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ovia-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ovia-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ovia-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ovia-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ovia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://wepow.com/.well-known/security.txt
created: '2026-07-17'
description: OVIA is listed via wepow.com, the domain of Wepow, a video-interviewing and candidate-assessment startup backed by 500 Global. Wepow is now part of Harver, a Talent Intelligence platform offering pre-employment assessments, automated interview scheduling, video interviewing, game-based assessments (pymetrics), and reference checking (Checkster). wepow.com 301-redirects to harver.com, and the served /.well-known documents and llms.txt are Harver's. This entry has no independent, self-service public API surface; enrichment captured the live security, well-known, and AI-governance signals published on the domain.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ovia.png
layout: provider
modified: '2026-07-20'
name: OVIA
nav: Providers
network: true
overview: OVIA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Recruiting, Talent Assessment, Video Interviewing, and Human Resources.
random_paper: 133
score:
  band: minimal
  composite: 9.2
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 9.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ovia/refs/heads/main/screenshots/ovia-2026-08-07T191144.png
security:
- kind: domain-security
  name: Ovia Domain Security
  slug: ovia-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Ovia Vulnerability Disclosure
  slug: ovia-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ovia
tags:
- Company
- Recruiting
- Talent Assessment
- Video Interviewing
- Human Resources
- Hiring
- HR Tech
website: https://wepow.com
---
