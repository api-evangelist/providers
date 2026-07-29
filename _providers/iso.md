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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iso-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.iso.org
- group: other
  title: ''
  type: Standards
  url: https://www.iso.org/standards.html
- group: company
  title: ''
  type: About
  url: https://www.iso.org/about-us.html
created: '2025-01-01'
description: The International Organization for Standardization (ISO) develops and publishes international standards covering technology, manufacturing, food safety, and many other industries. ISO standards provide globally recognized frameworks that help organizations ensure quality, safety, interoperability, and consistency in their products and processes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iso.png
jsonld:
- class_count: 28
  name: Iso Context
  property_count: 6
  slug: iso-context
layout: provider
modified: '2026-04-28'
name: ISO
nav: Providers
network: true
overview: 'ISO is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Certification, International, Quality Management, and Standards.


  The ISO catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 11
rules:
- name: ISO API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: iso-rules
score:
  band: minimal
  composite: 8.5
  delta: -2.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 10.4
    operational_transparency: 0.0
  previous_composite: 10.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iso/refs/heads/main/screenshots/iso-2026-06-20T183617.png
security:
- kind: domain-security
  name: Iso Domain Security
  slug: iso-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iso
tags:
- Certification
- International
- Quality Management
- Standards
website: https://www.iso.org
---
