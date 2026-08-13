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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: The Zylo Platform API is the successor to Cleanshelf. It exposes SaaS application discovery, inventory, license, contract, and spend data so enterprises can integrate Zylo with finance, procurement, a
  name: Zylo Platform API (successor)
  slug: zylo-api
- description: Legacy v1.0 endpoints retained from the original Cleanshelf product line. New integrations should use the modern Zylo Platform API.
  name: Zylo Legacy API (Cleanshelf-era)
  slug: zylo-legacy-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/cleanshelf-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cleanshelf-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cleanshelf
- group: company
  title: ''
  type: Website
  url: https://zylo.com/
- group: other
  title: ''
  type: Acquirer
  url: https://zylo.com/
- group: other
  title: ''
  type: Acquisition Announcement
  url: https://zylo.com/news/zylo-acquires-cleanshelf/
- group: other
  title: ''
  type: Application
  url: https://app.zylo.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.zylo.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zylo.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zylo.com/legal/
- group: operate
  title: ''
  type: Support
  url: https://help.zylo.com/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cleanshelf-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cleanshelf-rules.yml
created: '2026-03-27'
deprecated: true
deprecated_note: Cleanshelf has been acquired and is no longer offered independently. Retained for historical reference.
description: Cleanshelf was a SaaS management platform that helped enterprises discover and inventory their SaaS applications, optimize software licenses, track spend, and surface shadow IT. Cleanshelf was acquired by Zylo in 2021 and its capabilities have been folded into the Zylo enterprise SaaS spend optimization platform. The Cleanshelf product brand and standalone API are no longer maintained; equivalent programmatic capabilities are now exposed through the Zylo Developer Hub at developer.zylo.com.
finops:
- name: Cleanshelf Finops
  service_category: API
  slug: cleanshelf-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cleanshelf.png
jsonld:
- class_count: 13
  name: Cleanshelf Context
  property_count: 0
  slug: cleanshelf-context
layout: provider
modified: '2026-04-23'
name: Cleanshelf
nav: Providers
network: true
overview: 'Cleanshelf publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Acquired, License Management, SaaS Management, Shadow IT, and SMP.


  The Cleanshelf catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cleanshelf''s developer surface includes developer portal, support, and 11 more developer resources.'
plans:
- name: Cleanshelf Plans Pricing
  plan_count: 3
  slug: cleanshelf-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 5
  name: Cleanshelf Rate Limits
  slug: cleanshelf-rate-limits
rules:
- name: Cleanshelf API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: cleanshelf-rules
score:
  band: emerging
  composite: 24.2
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 12.9
    developer_ergonomics: 13.0
    discoverability: 59.3
    governance: 20.8
    operational_transparency: 7.9
  previous_composite: 24.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cleanshelf/refs/heads/main/screenshots/cleanshelf-2026-06-20T174453.png
security:
- kind: domain-security
  name: Cleanshelf Domain Security
  slug: cleanshelf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cleanshelf Trust Center
  slug: cleanshelf-trust-center
  summary_line: SOC 2, GDPR
slug: cleanshelf
tags:
- Acquired
- License Management
- SaaS Management
- Shadow IT
- SMP
- Software Asset Management
- Spend Optimization
website: https://zylo.com/
---
