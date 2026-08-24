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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Terminal emulator and SSH client for Windows and Unix platforms.
  name: PuTTY
  slug: putty
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/putty-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.putty.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html
created: '2024-01-01'
description: PuTTY is a free and open-source terminal emulator, serial console and network file transfer application. It supports several network protocols, including SCP, SSH, Telnet, rlogin, and raw socket connection.
finops:
- name: Putty Finops
  service_category: API
  slug: putty-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/putty.png
layout: provider
modified: '2026-03-16'
name: PuTTY
nav: Providers
network: true
overview: 'PuTTY publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Network Tools, Open-Source, Remote Access, SSH, and Terminal.


  PuTTY''s developer surface includes documentation and 2 more developer resources.'
plans:
- name: Putty Plans Pricing
  plan_count: 3
  slug: putty-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Putty Rate Limits
  slug: putty-rate-limits
score:
  band: emerging
  composite: 12.0
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
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/putty/refs/heads/main/screenshots/putty-2026-06-20T192320.png
security:
- kind: domain-security
  name: Putty Domain Security
  slug: putty-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: putty
tags:
- Network Tools
- Open-Source
- Remote Access
- SSH
- Terminal
website: https://www.putty.org
---
