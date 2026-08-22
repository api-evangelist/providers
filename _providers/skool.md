---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Skool's only official programmatic surface. This is a Zapier-mediated automation integration, not a public REST API. It is available on the paid Pro plan only (not Hobby) and is enabled via a per-grou
  name: Skool Zapier Integration
  slug: skool-zapier-integration
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skool-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/skool
- group: company
  title: ''
  type: Website
  url: https://www.skool.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.skool.com
- group: commercial
  title: ''
  type: Plans
  url: plans/skool-plans-pricing.yml
created: '2026-07-05'
description: 'Skool is an all-in-one community platform that combines discussion communities, online courses, live calls, and gamification in a single product, founded by Sam Ovens and popularized in partnership with Alex Hormozi. As of this review, Skool does NOT publish an official public or partner developer REST API. The only official programmatic surface is a Zapier integration, gated to the paid Pro plan, that exposes a small set of triggers and actions via a per-group API key used solely to link a Skool group to Zapier - it is not a general-purpose developer API. All broader "Skool API" offerings found in the wild (Apify actors, docs.skoolapi.com, reverse-engineered clients, Chrome extensions) are unofficial third-party tools built on Skool''s undocumented internal endpoints and are not endorsed or supported by Skool. This catalog entry is an honest gated stub: no public API surface is modeled because none is documented.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/skool.png
layout: provider
modified: '2026-07-05'
name: Skool
nav: Providers
network: true
overview: 'Skool publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Community, Courses, Online Learning, Membership, and Creator Economy.


  Skool''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Skool Plans Pricing
  plan_count: 2
  slug: skool-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 12.1
  delta: 0.2
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Skool Domain Security
  slug: skool-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: skool
tags:
- Community
- Courses
- Online Learning
- Membership
- Creator Economy
- No Public API
website: https://www.skool.com
---
