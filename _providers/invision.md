---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - '{''url'': ''https://www.invisionapp.com'', ''status'': 301, ''note'': ''declared website redirects to https://miro.com:443/ — a different registrable domain (invisionapp.com -> miro.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The InVision Design System Manager (DSM) API allowed teams to programmatically retrieve design tokens (colors, text styles, fonts, spacing) and icons from their DSM design system. API keys were scoped
  name: InVision DSM Design Tokens API
  slug: invision-dsm-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/invision-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.invisionapp.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.invisionapp.com/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/InVisionApp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/invisionapp
- group: company
  title: ''
  type: Blog
  url: https://engineering.invisionapp.com
- group: commercial
  title: ''
  type: Pricing
  url: https://support.invisionapp.com/docs/plans-1
- group: operate
  title: ''
  type: StatusPage
  url: https://status.invisionapp.com
- group: other
  title: ''
  type: X
  url: https://x.com/InVisionApp
- group: commercial
  title: ''
  type: Plans
  url: plans/invision-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/invision-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/invision-finops.yml
created: '2026-06-13'
description: InVision was a digital product design platform used by teams to build the world's best customer experiences. It provided REST APIs for managing prototypes, design documents, boards, comments, workflows, and design system components including design tokens and icons via the Design System Manager (DSM). InVision shut down all services on January 1, 2025, with its domain now redirecting to Miro.
finops:
- name: Invision Finops
  service_category: ''
  slug: invision-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/invision.png
jsonld:
- class_count: 0
  name: Invision Context
  property_count: 0
  slug: invision
layout: provider
modified: '2026-06-13'
name: InVision
nav: Providers
network: true
overview: 'InVision publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Design, Prototyping, Design Systems, Collaboration, and Digital Product Design.


  The InVision catalog on APIs.io includes 1 JSON-LD context.


  InVision''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Invision Plans Pricing
  plan_count: 3
  slug: invision-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Invision Rate Limits
  slug: invision-rate-limits
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 57.0
    catalog_earned_first_party: 0.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 21.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/invision/refs/heads/main/screenshots/invision-2026-06-20T183609.png
security:
- kind: domain-security
  name: Invision Domain Security
  slug: invision-domain-security
  summary_line: TLSv1.3 · HSTS
slug: invision
tags:
- Design
- Prototyping
- Design Systems
- Collaboration
- Digital Product Design
- Deprecated
website: https://www.invisionapp.com
---
