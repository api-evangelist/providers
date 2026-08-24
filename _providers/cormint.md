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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cormint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cormint.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cormint.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cormint.com/terms/
- group: operate
  title: ''
  type: Contact
  url: https://www.cormint.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cormint-Data-Systems
- group: other
  title: ''
  type: Profile
  url: https://forgeglobal.com/cormint_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cormint-llms.txt
coverage:
  checked: '2026-08-11'
  detail: Cormint is a vertically integrated power and data-center infrastructure owner-operator — 130 MW energized at Fort Blocks in West Texas, a 58 MW second site under construction — whose entire public web presence is six static marketing pages listed in its own sitemap, with no developer section, no API, and no machine-readable artifact anywhere; the only non-marketing host, dashboard.cormint.com, redirects to a Google Workspace sign-in restricted to the cormint.com domain.
  evidence:
  - status: 200
    url: https://www.cormint.com/sitemap-0.xml
  - status: 404
    url: https://www.cormint.com/openapi.json
  - status: 404
    url: https://www.cormint.com/.well-known/api-catalog
  - status: 404
    url: https://www.cormint.com/.well-known/agent-card.json
  - status: 404
    url: https://www.cormint.com/llms.txt
  - status: 200
    url: https://api.github.com/orgs/Cormint-Data-Systems/repos
  reason: not-a-software-company
  state: none
created: '2026-08-11'
description: 'Cormint Data Systems, Inc. is a Texas-based, vertically integrated developer and operator of power infrastructure for large-scale data centers and compute. The company designs, manufactures, deploys and operates its own electrical and site infrastructure in-house — from PDU wiring and PLC controls through transformer integration and substation work — and runs 130 MW energized today at its Fort Blocks site near Fort Stockton in West Texas, with a second 58 MW site (Bobcat) under construction near Orange Grove in ERCOT Load Zone South and a stated pipeline of roughly 370 MW across 707 controlled acres. Cormint built the operating platform in bitcoin mining, where it reports power costs of 2.3–3.1 cents per kWh and a #1 peer ranking on cost efficiency, and is now positioning the same platform for AI and HPC workloads as a colocation and EPC-style infrastructure owner-operator. It is an energy and data-center infrastructure business rather than a software vendor: it publishes no
  developer portal, no API, and no machine-readable specification of any kind.'
image: https://www.cormint.com/media/social-card-cormint-v1.png
layout: provider
modified: '2026-08-11'
name: Cormint
nav: Providers
network: true
overview: Cormint is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Centers, Power Infrastructure, Energy, and Bitcoin Mining.
plans:
- name: Cormint Plans Pricing
  plan_count: 0
  slug: cormint-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Cormint Rate Limits
  slug: cormint-rate-limits
score:
  band: minimal
  composite: 10.2
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Cormint Domain Security
  slug: cormint-domain-security
  summary_line: TLSv1.3
slug: cormint
tags:
- Company
- Data Centers
- Power Infrastructure
- Energy
- Bitcoin Mining
- AI Infrastructure
- High Performance Computing
- Colocation
- Texas
website: https://www.cormint.com/
---
