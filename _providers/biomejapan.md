---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API providing access to ecological data and analytics services.
  name: Biome API
  slug: biome-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/biomejapan/refs/heads/main/well-known/biomejapan-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/biomejapan-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biomejapan/refs/heads/main/hosts/biomejapan-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biomejapan-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biomejapan/refs/heads/main/security/biomejapan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biomejapan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biome.co.jp
- group: docs
  title: ''
  type: Documentation
  url: https://biome.co.jp/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://biome.co.jp/appmessage/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://biome.co.jp/privacy-policy/
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://biome.co.jp/security-policy/
coverage:
  checked: '2026-09-28'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://biome.co.jp/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: Biomejapan, operating under the brand Biome Inc., provides comprehensive nature data platforms and ecological analytics solutions for corporations and governments in Japan. Leveraging the country’s largest real‑time biological distribution dataset, the company offers APIs and services that enable monitoring, protection, and enrichment of natural environments, supporting sustainability initiatives and regulatory compliance.
image: https://biome.co.jp/wp/wp-content/uploads/2023/02/service-biome2x.png
layout: provider
modified: '2026-09-28'
name: Biomejapan
nav: Providers
network: true
overview: 'Biomejapan publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Ecology, Sustainability, and Japan.


  Biomejapan''s developer surface includes documentation and 7 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 5
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
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biomejapan Domain Security
  slug: biomejapan-domain-security
  summary_line: TLSv1.3 · DMARC
slug: biomejapan
tags:
- Company
- Data
- Ecology
- Sustainability
- Japan
website: https://biome.co.jp
---
