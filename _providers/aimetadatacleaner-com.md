---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API to remove hidden metadata from images, videos, PDFs and RAW files.
  name: Metadata Removal API
  slug: metadata-removal-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/aimetadatacleaner-com/plans/aimetadatacleaner-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aimetadatacleaner-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aimetadatacleaner-com/well-known/aimetadatacleaner-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aimetadatacleaner-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aimetadatacleaner-com/hosts/aimetadatacleaner-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aimetadatacleaner-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aimetadatacleaner-com/vendors/aimetadatacleaner-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aimetadatacleaner-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aimetadatacleaner-com/security/aimetadatacleaner-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aimetadatacleaner-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aimetadatacleaner.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aimetadatacleaner.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://aimetadatacleaner.com/subscription
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aimetadatacleaner.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aimetadatacleaner.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://aimetadatacleaner.com/blog
coverage:
  checked: '2026-11-01'
  detail: Developer documentation page is rendered via Cloudflare protection and requires JavaScript to view full spec, no machine‑readable OpenAPI found.
  evidence:
  - status: 200
    url: https://aimetadatacleaner.com/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AI Metadata Cleaner provides a free online tool and API to strip hidden metadata, including EXIF, GPS, C2PA, and AI generation tags, from images, videos, PDFs and RAW files. It aims to protect privacy for creators, professionals and everyday users by ensuring no unintended data is shared.
image: https://aimetadatacleaner.com/og-image.jpg
layout: provider
modified: '2026-11-01'
name: AI Metadata Cleaner
nav: Providers
network: true
overview: 'AI Metadata Cleaner is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Metadata Removal, Privacy, Image Processing, and AI Generated Content.


  AI Metadata Cleaner''s developer surface includes documentation, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Aimetadatacleaner Com Plans Pricing
  plan_count: 3
  slug: aimetadatacleaner-com-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 19.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aimetadatacleaner Com Domain Security
  slug: aimetadatacleaner-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aimetadatacleaner-com
tags:
- Metadata Removal
- Privacy
- Image Processing
- AI Generated Content
website: https://aimetadatacleaner.com/
---
