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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Corsha provides an Industrial Identity Security Platform API documented at https://docs.corsha.com/.
  name: Corsha API
  slug: corsha-api
artifact_total: 2
common:
- group: docs
  title: ''
  type: Documentation
  url: https://docs.corsha.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/corsha/refs/heads/main/hosts/corsha-hosts.yml
  title: ''
  type: Hosts
  url: hosts/corsha-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/corsha/refs/heads/main/vendors/corsha-vendors.yml
  title: ''
  type: Vendors
  url: vendors/corsha-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://corsha.com/press-releases/tag/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/corsha/refs/heads/main/security/corsha-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/corsha-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://corsha.com
- group: company
  title: ''
  type: Blog
  url: https://corsha.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corsha.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corsha.com/privacy-policy
coverage:
  checked: '2026-10-11'
  detail: Docs at https://docs.corsha.com/ redirect to a JS challenge page for the OpenAPI spec, preventing machine-readable retrieval.
  evidence:
  - status: 200
    url: https://docs.corsha.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-11'
description: Corsha provides an Industrial Identity Security Platform that secures machine-to-machine connections in operational technology environments. It offers zero‑trust micro‑segmentation, continuous authentication, and real‑time threat detection for OT networks, helping enterprises modernize safely while maintaining compliance and visibility across factories, plants, and critical infrastructure.
layout: provider
modified: '2026-10-11'
name: Corsha
nav: Providers
network: true
overview: 'Corsha is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Industrial, Identity, and OT.


  Corsha''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 55.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Corsha Domain Security
  slug: corsha-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: corsha
tags:
- Company
- Security
- Industrial
- Identity
- OT
website: https://corsha.com
---
