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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advancecomposite-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://advance-composite.co.jp/
- group: company
  title: ''
  type: Blog
  url: https://advance-composite.co.jp/en/post/
- group: company
  title: ''
  type: BlogRSS
  url: https://advance-composite.co.jp/en/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://advance-composite.co.jp/en/privacy-policy/
coverage:
  checked: '2026-09-07'
  detail: Advance Composite manufactures physical metal-matrix-composite parts by squeeze casting molten aluminium into graphite and ceramic reinforcement, and its entire web presence is a 37-page WordPress marketing site whose own sitemap lists no developer, API, partner or pricing page — /openapi.json, /llms.txt, /graphql, /developers and every /.well-known/ path return a WordPress 404, and the only machine-readable route on the host, the WordPress core /wp-json/ index, is itself 403-blocked at the origin and is platform plumbing rather than a product API.
  evidence:
  - status: 200
    url: https://advance-composite.co.jp/
  - status: 200
    url: https://advance-composite.co.jp/wp-sitemap.xml
  - status: 404
    url: https://advance-composite.co.jp/openapi.json
  - status: 404
    url: https://advance-composite.co.jp/.well-known/agent-card.json
  - status: 403
    url: https://advance-composite.co.jp/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-09-07'
description: 'Advance Composite Corporation (アドバンスコンポジット株式会社) is a Japanese advanced-materials manufacturer founded on 22 July 2015 and headquartered at 2259-9 Oobuchi, Fuji City, Shizuoka Prefecture, with a Tokyo branch in Otemachi, Chiyoda-ku. The company develops, manufactures and sells metal matrix composite (MMC) materials and joined products using a proprietary squeeze-casting / molten-metal forging process that impregnates reinforcement materials such as graphite, alumina and other ceramics with molten aluminium under high pressure, producing parts with few internal voids. Its published material families include the ACM-H series (New ACM-H1/H2/H3 aluminium-graphite composites), AC-Alox (aluminium/alumina) and AC-Albolon, marketed on high thermal conductivity, low thermal expansion, low density and high stiffness for semiconductor manufacturing equipment, data centres, air conditioning, medical devices, mobility and rail. It is ISO 9001:2015 certified (Intertek registration 15556,
  UKAS accredited, first issued 2023-11-08), won the IVS2025 LAUNCHPAD, and raised a Series B from Kyoto iCAP in 2026. Advance Composite is a physical-materials manufacturer, not a software vendor: it publishes no developer program, public API, SDK, or machine-readable API contract of any kind.'
image: https://advance-composite.co.jp/wp/wp-content/uploads/2021/12/favicon.png
layout: provider
modified: '2026-09-07'
name: Advance Composite
nav: Providers
network: true
overview: 'Advance Composite is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Materials Science, Advanced Materials, and Metal Matrix Composites.


  Advance Composite''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 7.6
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Advancecomposite Domain Security
  slug: advancecomposite-domain-security
  summary_line: TLSv1.3 · DMARC
slug: advancecomposite
tags:
- Company
- Manufacturing
- Materials Science
- Advanced Materials
- Metal Matrix Composites
- Thermal Management
- Semiconductors
- Aluminum
- Japan
website: https://advance-composite.co.jp/
---
