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
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/avathon-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/avathon-llms.txt
- group: company
  title: ''
  type: Website
  url: https://avathon.com/
- group: other
  title: ''
  type: Platform
  url: https://avathon.com/platform-2/
- group: company
  title: ''
  type: Blog
  url: https://avathon.com/blogs/
- group: operate
  title: ''
  type: Support
  url: https://support.avathon.com/help
- group: operate
  title: ''
  type: ContactUs
  url: https://avathon.com/contact-us-2/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://avathon.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avathon.com/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://avathon.com/cookie-policy/
- group: other
  title: ''
  type: Resources
  url: https://avathon.com/resources/
- group: other
  title: ''
  type: CaseStudies
  url: https://avathon.com/case-studies/
- group: other
  title: ''
  type: Glossary
  url: https://avathon.com/ai-glossary/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/avathonai/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/avathon-stock
coverage:
  checked: '2026-08-06'
  detail: Avathon's entire documentation surface is the HubSpot-hosted help centre at support.avathon.com/help, which 307-redirects to /_hcms/mem/login — there is no docs., developer. or api. host in DNS at all, and the Industrial AI Platform's "application development SDK and APIs" are named only in marketing copy.
  evidence:
  - status: 307
    url: https://support.avathon.com/help
  - status: 404
    url: https://avathon.com/openapi.json
  - status: 404
    url: https://avathon.com/.well-known/agent-card.json
  - status: 0
    url: https://docs.avathon.com/
  reason: customer-only-docs
  state: gated
created: '2026-08-06'
description: Avathon — formerly SparkCognition, rebranded in November 2024 — is an industrial AI company whose Industrial AI Platform combines a data platform, industrial digital twin, AI modeling and application development layers to bring predictive maintenance, asset performance management, visual intelligence and autonomy to physical operations. Its solutions span renewables, oil and gas, power and utilities, manufacturing, mining, aerospace and defense, maritime, rail, aviation, logistics, warehousing and retail, with named offerings including Asset Performance Management, Visual AI / Visual Intelligence, Autonomy for Health, Safety and Environment, the Digital Maintenance Advisor and the Multidomain Awareness Advisor. The platform is sold and delivered as an enterprise engagement — marketing material references an application development SDK and APIs, but no public developer portal, API reference or machine-readable specification is published; the only documentation surface, support.avathon.com/help,
  redirects to a HubSpot member login. Avathon is backed by investors including Temasek, Verizon Ventures and Boeing, and is headquartered in Silicon Valley after relocating from Austin, Texas.
image: https://avathon.com/wp-content/uploads/2024/10/avathon-logo-1100.png
layout: provider
modified: '2026-08-06'
name: Avathon
nav: Providers
network: true
overview: 'Avathon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Industrial AI, Predictive Maintenance, and Asset Performance Management.


  Avathon''s developer surface includes engineering blog, support, and 13 more developer resources.'
random_paper: 57
score:
  band: minimal
  composite: 12.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/avathon/refs/heads/main/screenshots/avathon-2026-08-07T162012.png
security:
- kind: domain-security
  name: Avathon Domain Security
  slug: avathon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: avathon
tags:
- Company
- Artificial Intelligence
- Industrial AI
- Predictive Maintenance
- Asset Performance Management
- Computer Vision
- Digital Twin
- Renewable Energy
- Oil and Gas
- Manufacturing
- Aerospace and Defense
- Logistics
website: https://avathon.com/
---
