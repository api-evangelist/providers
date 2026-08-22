---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'An anonymous, read-oriented Model Context Protocol endpoint served from Field Medical''s own corporate domain. It is provided by the Wix website platform (Wix Site MCP), not authored by Field Medical, '
  name: Field Medical Site MCP
  slug: field-medical-site-mcp
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/field-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fieldmedicalinc.com/
- group: company
  title: ''
  type: Blog
  url: https://www.fieldmedicalinc.com/news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.fieldmedicalinc.com/blog-feed.xml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/field-medical/
- group: company
  title: ''
  type: Careers
  url: https://www.fieldmedicalinc.com/careers
- group: company
  title: ''
  type: Investors
  url: https://www.fieldmedicalinc.com/investors
- group: agent
  title: ''
  type: MCPServer
  url: mcp/field-medical-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/field-medical-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/field-medical-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/field-medical-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/field-medical-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/field-medical-plans-pricing.yml
created: '2026-08-12'
description: 'Field Medical, Inc. is a Carlsbad, California clinical-stage cardiac electrophysiology company founded in 2022 by Dr. Steven Mickelsen to build a second-generation pulsed field ablation (PFA) platform. Its FieldForce Ablation System pairs a focal catheter design with proprietary FieldBending energy and is positioned as the first PFA system purpose-built for ventricular arrhythmia ablation, with atrial fibrillation applications in development. The company holds FDA Breakthrough Device Designation and a place in the FDA TAP Pilot Program for its VT indication, has published first-in-human VCAS data in Circulation, and has raised roughly $75M across Series A and Series B. Field Medical is a medical device manufacturer, not a software vendor: it publishes no developer portal, no public REST/GraphQL API and no SDKs. Its only machine-readable public surface is the llms.txt and anonymous site MCP endpoint that its Wix-hosted corporate website serves.'
image: https://static.wixstatic.com/media/8a66b7_1cc006a6bfe247ada2ee91171488f369%7Emv2.png/v1/fill/w_192%2Ch_192%2Clg_1%2Cusm_0.66_1.00_0.01/8a66b7_1cc006a6bfe247ada2ee91171488f369%7Emv2.png
layout: provider
mcp_servers:
- description: ''
  name: field-medical-mcp.yml
  slug: field-medical-mcpyml
modified: '2026-08-12'
name: Field Medical
nav: Providers
network: true
overview: 'Field Medical publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Cardiology, and Medical Technology.


  Field Medical''s developer surface includes engineering blog, authentication, and 11 more developer resources.'
plans:
- name: Field Medical Plans Pricing
  plan_count: 0
  slug: field-medical-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Field Medical Rate Limits
  slug: field-medical-rate-limits
score:
  band: emerging
  composite: 13.0
  delta: -1.6
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 14.6
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Field Medical Authentication
  slug: field-medical-authentication
  summary_line: none/bearer-visitor-token · 2 schemes
- kind: domain-security
  name: Field Medical Domain Security
  slug: field-medical-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: field-medical
tags:
- Company
- Medical Devices
- Healthcare
- Cardiology
- Medical Technology
- Clinical Research
- Model Context Protocol
website: https://www.fieldmedicalinc.com/
---
