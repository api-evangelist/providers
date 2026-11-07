---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Travel guide API documented at the Guides page
  name: Destaire API
  slug: destaire-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/destaire-com/llms/destaune-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/destaune-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/destaire-com/llms/destaire-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/destaire-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/destaire-com/well-known/destaire-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/destaire-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/destaire-com/hosts/destaire-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/destaire-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/destaire-com/vendors/destaire-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/destaire-com-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://destaire.com/guides
- group: auth
  href: https://artifacts.apis.io/destaire-com/security/destaire-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/destaire-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://destaire.com/
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://destaire.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://destaire.com/privacy
created: '2026-11-05'
description: Déstaire is a curated guide to exceptional hotels and private stays, offering travel writing, paid city guides, and a selection of unique accommodations worldwide. The platform blends editorial content with curated listings to inspire discerning travelers.
image: https://cdn.sanity.io/images/tft23uem/production/4dbd1c5ec7e37a3d2b6ccb91fa042086e81b81a1-2500x1667.avif/la-bergerie-stone-house-lawn-pool-below-limestone-cliffs-les.avif?rect=0,177,2500,1312&w=1200&h=630&fit=crop&fm=jpg
layout: provider
modified: '2026-11-05'
name: Destaire
nav: Providers
network: true
overview: 'Destaire is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Hospitality, Curated Guides, Luxury, and Destination.


  Destaire''s developer surface includes documentation and 9 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Destaire Com Domain Security
  slug: destaire-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: destaire-com
tags:
- Travel
- Hospitality
- Curated Guides
- Luxury
- Destination
website: https://destaire.com/
---
