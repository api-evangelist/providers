---
access_model:
  confidence: low
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: true
  try_now: false
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/aimech-app/plans/aimech-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aimech-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aimech-app/llms/aimech-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aimech-app-llms.txt
- group: other
  href: https://artifacts.apis.io/aimech-app/hosts/aimech-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aimech-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/aimech-app/vendors/aimech-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aimech-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aimech-app/security/aimech-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aimech-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aimech.app/
- group: docs
  title: ''
  type: Documentation
  url: https://aimech.app/about
- group: commercial
  title: ''
  type: Pricing
  url: https://aimech.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aimech.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aimech.app/privacy
- group: operate
  title: ''
  type: Support
  url: https://aimech.app/faq
coverage:
  checked: '2026-11-01'
  detail: Documentation pages exist but no OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 200
    url: https://aimech.app/guides/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AIMECH.APP provides an AI-powered car diagnostics platform that helps users identify vehicle issues through text, photo, or sound inputs. The service offers a free diagnosis with limited queries and paid plans for deeper analysis, including suggested parts and repair cost estimates. It aims to simplify automotive troubleshooting for both DIY owners and professionals, integrating AI insights with real-world repair data.
image: https://aimech.app/brand/09894ebb1_generated_image.png
layout: provider
modified: '2026-11-01'
name: AIMECH.APP
nav: Providers
network: true
overview: 'AIMECH.APP is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Car Diagnostics, Vehicle Maintenance, Digital Garage, and Repair Cost Estimates.


  AIMECH.APP''s developer surface includes documentation, pricing, support, and 8 more developer resources.'
plans:
- name: Aimech App Plans Pricing
  plan_count: 3
  slug: aimech-app-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 39.3
    operational_transparency: 0.0
  previous_composite: 19.2
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aimech App Domain Security
  slug: aimech-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aimech-app
tags:
- Car Diagnostics
- Vehicle Maintenance
- Digital Garage
- Repair Cost Estimates
website: https://aimech.app/
---
