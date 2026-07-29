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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Multifamily Database is a Ginnie Mae database that contains information about Ginnie Maes multifamily mortgage-backed securities at the security and loan level.
  name: Ginnie Mae
  slug: ginnie-mae
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ginnie-mae-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ginnie-mae
- group: company
  title: ''
  type: Website
  url: https://www.ginniemae.gov/
created: '2024-12-03'
description: The Government National Mortgage Association (Ginnie Mae) is a government corporation within the U.S. Department of Housing and Urban Development (HUD), established in 1968 following the privatization of Fannie Mae. Its mission is to expand mortgage funding insured or guaranteed by federal agencies. By providing a full-faith-and-credit guarantee on securities backed by these mortgages, Ginnie Mae reduces investor risk and broadens the market for mortgage-backed securities.
finops:
- name: Ginnie Mae Finops
  service_category: API
  slug: ginnie-mae-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ginnie-mae.png
layout: provider
modified: '2026-04-28'
name: Ginnie Mae
nav: Providers
network: true
overview: Ginnie Mae publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Federal Government, Housing, and Mortgages.
plans:
- name: Ginnie Mae Plans Pricing
  plan_count: 3
  slug: ginnie-mae-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 5
  name: Ginnie Mae Rate Limits
  slug: ginnie-mae-rate-limits
score:
  band: emerging
  composite: 17.0
  delta: -1.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 18.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ginnie-mae/refs/heads/main/screenshots/ginnie-mae-2026-06-20T181827.png
security:
- kind: domain-security
  name: Ginnie Mae Domain Security
  slug: ginnie-mae-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ginnie-mae
tags:
- Federal Government
- Housing
- Mortgages
website: https://www.ginniemae.gov/
---
