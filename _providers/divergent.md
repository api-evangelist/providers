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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/divergent-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.divergent.us/
- group: operate
  title: ''
  type: Support
  url: https://www.divergent.us/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.divergent.us/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.divergent.us/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/divergent3d
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/divergent-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/divergent-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/divergent-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/divergent-rate-limits.yml
coverage:
  checked: '2026-08-12'
  detail: Divergent sells manufactured metal structures and DAPS production capacity under negotiated contracts — its whole public web presence is a five-URL marketing site whose own robots.txt disallows /api, with api., developer., docs. and portal. subdomains all NXDOMAIN and every /.well-known/ and OpenAPI path returning 404.
  evidence:
  - status: 404
    url: https://www.divergent.us/openapi.json
  - status: 404
    url: https://www.divergent.us/.well-known/agent-card.json
  - status: 200
    url: https://www.divergent.us/sitemap.xml
  - status: 404
    url: https://www.divergent.us/docs
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: 'Divergent Technologies, Inc. is a Torrance and Long Beach, California manufacturer that built the Divergent Adaptive Production System (DAPS), an end-to-end software-hardware production system for industrial digital manufacturing. DAPS pairs AI-driven generative design software with in-house metal additive manufacturing — the Monolith One printer, compatible with aluminum, nickel, steel and titanium alloys — and automated fixtureless robotic assembly, so complex multi-part structures can be engineered, printed and assembled without fixed tooling. Founded in 2013 by Kevin and Lukas Czinger, the company is a Tier 1 supplier to global automotive OEMs and has expanded into aerospace and defense, including selection under the US Air Force Eglin Wide Agile Acquisition Contract. Divergent sells manufactured structures and production capacity, not software: it publishes no developer portal, no public API, and no machine-readable contract of any kind.'
image: https://ihglvckx7z2732pf.public.blob.vercel-storage.com/daps_desaturated.png
layout: provider
modified: '2026-08-12'
name: Divergent
nav: Providers
network: true
overview: 'Divergent is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Additive Manufacturing, 3D Printing, and Industrial.


  Divergent''s developer surface includes support and 9 more developer resources.'
plans:
- name: Divergent Plans Pricing
  plan_count: 0
  slug: divergent-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Divergent Rate Limits
  slug: divergent-rate-limits
score:
  band: minimal
  composite: 11.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: domain-security
  name: Divergent Domain Security
  slug: divergent-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: divergent
tags:
- Company
- Manufacturing
- Additive Manufacturing
- 3D Printing
- Industrial
- Aerospace
- Defense
- Automotive
- Robotics
- Generative Design
website: https://www.divergent.us/
---
