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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/poste-italiane/llms/poste-italiane-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/poste-italiane-llms.txt
- group: auth
  href: https://artifacts.apis.io/poste-italiane/well-known/poste-italiane-aiutaciamigliorarecfm-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/poste-italiane-aiutaciamigliorarecfm-security.txt
- group: agent
  href: https://artifacts.apis.io/poste-italiane/well-known/poste-italiane-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/poste-italiane-well-known.yml
- group: other
  href: https://artifacts.apis.io/poste-italiane/hosts/poste-italiane-hosts.yml
  title: ''
  type: Hosts
  url: hosts/poste-italiane-hosts.yml
- group: other
  href: https://artifacts.apis.io/poste-italiane/vendors/poste-italiane-vendors.yml
  title: ''
  type: Vendors
  url: vendors/poste-italiane-vendors.yml
- group: auth
  href: https://artifacts.apis.io/poste-italiane/security/poste-italiane-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/poste-italiane-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.poste.it
- group: operate
  title: ''
  type: Support
  url: https://www.poste.it/assistenza
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.poste.it/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.mypostedeliverybusiness.it/offertaunica/
coverage:
  checked: '2026-10-13'
  detail: The Poste Delivery Business (Delivery Express) parcel API and its credentials are issued only to contracted business customers through the MyPDB portal at mypostedeliverybusiness.it; poste.it publishes an llms.txt but no developer portal, API reference or OpenAPI contract (api.poste.it and developer.poste.it do not resolve).
  evidence:
  - status: 200
    url: https://www.mypostedeliverybusiness.it/offertaunica/
  - status: 200
    url: https://www.poste.it/llms.txt
  - status: 404
    url: https://business.poste.it/business/it/api.html
  reason: customer-only-docs
  state: gated
created: '2026-10-13'
description: Poste Italiane (Gruppo Poste Italiane S.p.A.) is Italy's national postal operator and largest integrated omnichannel services platform, active in logistics, mail and parcels, financial services (BancoPosta), insurance (Poste Vita, Poste Assicura), payments and telecommunications. Its parcel carrier API for Poste Delivery Business (Delivery Express) is available only to contracted business customers via the MyPDB portal; no public developer documentation or machine-readable contract is published. Surfaced via the API Evangelist harvest backlog (market-gap:shipping-logistics).
image: https://www.media.poste.it/f2968aa3-8485-4882-a834-86c8555185ae/lg/webp/conceptbfoto-soggettolg-buonopremium_reveal@2x
layout: provider
modified: '2026-10-13'
name: Poste Italiane
nav: Providers
network: true
overview: 'Poste Italiane is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Shipping, Logistics, Postal Services, and Parcel.


  Poste Italiane''s developer surface includes support and 9 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Poste Italiane Domain Security
  slug: poste-italiane-domain-security
  summary_line: TLSv1.3 · DMARC
slug: poste-italiane
tags:
- Company
- Shipping
- Logistics
- Postal Services
- Parcel
- Italy
- Financial Services
website: https://www.poste.it
---
