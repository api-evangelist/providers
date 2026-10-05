---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/benga/refs/heads/main/llms/benga-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/benga-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/benga/refs/heads/main/hosts/benga-hosts.yml
  title: ''
  type: Hosts
  url: hosts/benga-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/benga/refs/heads/main/vendors/benga-vendors.yml
  title: ''
  type: Vendors
  url: vendors/benga-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/benga/refs/heads/main/security/benga-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/benga-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.benga.eu
coverage:
  checked: '2026-09-28'
  detail: The website https://www.benga.eu provides only marketing content and no developer documentation or API endpoints.
  evidence:
  - status: 200
    url: https://www.benga.eu
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Benga International GmbH is a diversified provider of specialized products and services, including medical supplies, military and police equipment, travel accessories, and custom branding solutions. Operating out of Cyprus with a global client base across Germany, Japan, and the USA, Benga leverages over 25 years of experience to deliver high‑quality, durable products tailored to government tenders and private sector needs. The company emphasizes innovative research, comprehensive engineering, and customer service, positioning itself as a world‑class supplier for discerning clients seeking reliable, customizable solutions.
layout: provider
modified: '2026-09-27'
name: Benga
nav: Providers
network: true
overview: Benga is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Supplies, Military Equipment, Travel Products, and Custom Branding.
random_paper: 3
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - global
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Benga Domain Security
  slug: benga-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: benga
tags:
- Company
- Medical Supplies
- Military Equipment
- Travel Products
- Custom Branding
- International
website: https://www.benga.eu
---
