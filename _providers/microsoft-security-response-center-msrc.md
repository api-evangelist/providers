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
    consent_identity: false
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
  score: 0.0
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Programmatic interfaces to engage with the Microsoft Security Response Center (MSRC)
  name: Microsoft Security Response Center (MSRC)
  slug: microsoft-security-response-center-msrc
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-security-response-center-msrc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-security-response-center-msrc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://msrc.microsoft.com/report/developer
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Programmatic interfaces to engage with the Microsoft Security Response Center (MSRC)
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-security-response-center-msrc.png
layout: provider
modified: '2026-05-28'
name: Microsoft Security Response Center (MSRC)
nav: Providers
network: true
overview: Microsoft Security Response Center (MSRC) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security and Public APIs.
random_paper: 52
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-security-response-center-msrc/refs/heads/main/screenshots/microsoft-security-response-center-msrc-2026-06-20T185530.png
security:
- kind: domain-security
  name: Microsoft Security Response Center Msrc Domain Security
  slug: microsoft-security-response-center-msrc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Security Response Center Msrc Vulnerability Disclosure
  slug: microsoft-security-response-center-msrc-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-security-response-center-msrc
tags:
- Security
- Public APIs
website: https://msrc.microsoft.com/report/developer
---
