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
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kigen-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: well-known/kigen-security.txt
- group: company
  title: ''
  type: Website
  url: https://kigen.com/
- group: company
  title: ''
  type: About
  url: https://kigen.com/about/
- group: other
  title: ''
  type: Products
  url: https://kigen.com/products/
- group: company
  title: ''
  type: Blog
  url: https://kigen.com/blog/
- group: other
  title: ''
  type: Resources
  url: https://kigen.com/resources/
- group: operate
  title: ''
  type: Support
  url: https://kigen.com/contact/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/kigen-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kigen-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kigen-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kigen-domain-security.yml
created: '2026-07-17'
description: Kigen is a security-focused eSIM and iSIM technology company, spun out of Arm in 2020 and headquartered in Cambridge, UK, backed by SoftBank. Kigen builds GSMA-compliant SIM operating systems, integrated SIM (iSIM) and embedded SIM (eSIM) technology, remote SIM provisioning (RSP), and In-Factory Profile Provisioning (IFPP), together with lifecycle and over-the-air (OTA) management for connected and IoT devices. Its eUICC security, SIM OS, and provisioning platform serve mobile network operators, device manufacturers, OEMs and ODMs, IoT service providers, and enterprises building connected products, enabling secure cellular connectivity at scale across the device lifecycle. This profile was surfaced as a portfolio company of SoftBank Vision Fund and enriched by the API Evangelist pipeline from Kigen's public web surface.
image: https://kigen.com/wp-content/uploads/2021/03/kigen-logo.png
layout: provider
modified: '2026-07-19'
name: Kigen
nav: Providers
network: true
overview: 'Kigen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Frontier Tech, eSIM, iSIM, and SIM OS.


  Kigen''s developer surface includes engineering blog, support, and 10 more developer resources.'
random_paper: 46
score:
  band: minimal
  composite: 9.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 9.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kigen/refs/heads/main/screenshots/kigen-2026-07-25T223726.png
security:
- kind: domain-security
  name: Kigen Domain Security
  slug: kigen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kigen Vulnerability Disclosure
  slug: kigen-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kigen
tags:
- Company
- Frontier Tech
- eSIM
- iSIM
- SIM OS
- Remote SIM Provisioning
- IoT Connectivity
- eUICC Security
- GSMA
- Cellular Connectivity
website: https://kigen.com/
---
