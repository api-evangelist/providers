---
access_model:
  confidence: low
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - security
  trial: false
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/brode-io/plans/brode-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brode-io-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/brode-io/llms/brode-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brode-io-llms.txt
- group: other
  href: https://artifacts.apis.io/brode-io/hosts/brode-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brode-io-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brode.io/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brode.io/en/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://brode.io/en/pricing
- group: start
  title: ''
  type: Login
  url: https://brode.io/en/login
- group: company
  title: ''
  type: Blog
  url: https://brode.io/en/blog
- group: auth
  href: https://artifacts.apis.io/brode-io/security/brode-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brode-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brode.io/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://brode.io/api/mcp
  - status: 200
    url: https://brode.io/
  reason: partner-login
  state: gated
created: '2026-11-03'
description: Brode provides professional-quality vectorization and machine embroidery services, converting images (PNG, JPG, SVG, WebP, GIF, BMP, TIFF) into studio-quality vector files (SVG, PDF, EPS, DXF) and ready-to-stitch embroidery files (DST, PES, JEF, VP3, EXP, U01, XXX). Free plan available, no credit card required.
image: https://brode.io/opengraph-image
layout: provider
modified: '2026-11-03'
name: Brode
nav: Providers
network: true
overview: 'Brode is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Vectorization, Machine Embroidery, Design Tools, Fabrication, and CAD.


  Brode''s developer surface includes pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Brode Io Plans Pricing
  plan_count: 4
  slug: brode-io-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brode Io Domain Security
  slug: brode-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brode-io
tags:
- Vectorization
- Machine Embroidery
- Design Tools
- Fabrication
- CAD
- Branding
- Laser Cutting
- File Conversion
website: https://brode.io/
---
