---
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
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/astrobotic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.astrobotic.com/
- group: company
  title: ''
  type: Blog
  url: https://www.astrobotic.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.astrobotic.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.astrobotic.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.astrobotic.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.astrobotic.com/lunar-delivery/send-to-the-moon/terms-and-conditions/
- group: company
  title: ''
  type: Careers
  url: https://www.astrobotic.com/company/careers/
- group: company
  title: ''
  type: PressKit
  url: https://www.astrobotic.com/press-kit/
coverage:
  checked: '2026-08-06'
  detail: Astrobotic sells lunar delivery missions, landers, rovers and surface power hardware; its entire public web presence is a 27-page WordPress marketing site with no developer, docs or API section, and every contract-discovery probe (well-known, openapi, llms.txt, api/docs/developer subdomains) missed on both www.astrobotic.com and astrobotic.com.
  evidence:
  - status: 200
    url: https://www.astrobotic.com/
  - status: 404
    url: https://www.astrobotic.com/developers
  - status: 404
    url: https://www.astrobotic.com/openapi.json
  - status: 404
    url: https://www.astrobotic.com/.well-known/agent-card.json
  - status: 404
    url: https://www.astrobotic.com/.well-known/security.txt
  - status: 404
    url: https://www.astrobotic.com/llms.txt
  - status: 0
    url: https://api.astrobotic.com/
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Astrobotic Technology is a Pittsburgh-based space robotics company building lunar landers, rovers, and lunar surface infrastructure for NASA and commercial customers. Its product lines include the Peregrine and Griffin lunar landers, the CubeRover and Polaris rover families, LunaGrid lunar surface power, the Xodiac reusable suborbital rocket lander test platform, and spacecraft navigation, machine vision and computing systems. The company sells payload delivery to the Moon under NASA''s Commercial Lunar Payload Services (CLPS) program, alongside the consumer MoonBox service. Voyager Technologies completed its acquisition of Astrobotic on 13 July 2026 and the business now operates as Voyager Lunar Systems from its Pittsburgh headquarters. Astrobotic sells missions and hardware, not software: it publishes no public API, developer portal, SDK, or machine-readable specification.'
image: https://www.astrobotic.com/wp-content/uploads/2021/01/logo.png
layout: provider
modified: '2026-08-06'
name: Astrobotic
nav: Providers
network: true
overview: 'Astrobotic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, Aerospace, Robotics, and Lunar Logistics.


  Astrobotic''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 38
score:
  band: minimal
  composite: 10.5
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/astrobotic/refs/heads/main/screenshots/astrobotic-2026-08-07T161817.png
security:
- kind: domain-security
  name: Astrobotic Domain Security
  slug: astrobotic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: astrobotic
tags:
- Company
- Space
- Aerospace
- Robotics
- Lunar Logistics
- Spacecraft
- Satellites
- Defense and Space
website: https://www.astrobotic.com/
---
