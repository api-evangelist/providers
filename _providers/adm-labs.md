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
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://www.linkedin.com/company/admlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/admlabs
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/adm-labs_stock/
coverage:
  checked: '2026-09-07'
  detail: 'ADM Labs has no live first-party host of any kind: its original marketing domain adm-labs.com (a WordPress site with a Zoho Commerce storefront, last real content archived 2021) lapsed and was re-registered on 2022-07-20 through Spaceship with for-sale nameservers (DOMAIN-MAY-BE-FOR-SALE-AT.EDOMS.BIZ) and now returns an ad-monetized FingerprintJS parking redirect on every path, while hempcorpusa.com - the domain the company''s own LinkedIn page publishes under its successor brand "Hemp Corp", still registered to it at GoDaddy - answers every path, including a negative-control path that cannot exist, with the identical 114-byte GoDaddy parking lander, and no api./docs./developer./portal./app./store. subdomain of either domain resolves in DNS.'
  evidence:
  - status: 200
    url: https://hempcorpusa.com/
  - status: 200
    url: https://hempcorpusa.com/openapi.json
  - status: 200
    url: https://hempcorpusa.com/graphql
  - status: 200
    url: https://hempcorpusa.com/llms.txt
  - status: 200
    url: https://hempcorpusa.com/.well-known/agent-card.json
  - status: 200
    url: https://hempcorpusa.com/.well-known/adm-labs-negative-control-7f3ab91c.json
  - status: 200
    url: https://adm-labs.com/
  - status: 404
    url: https://adm-labs.com/openapi.json
  - status: 404
    url: https://adm-labs.com/apis.json
  - status: 404
    url: https://adm-labs.com/.well-known/agent-card.json
  - status: 200
    url: https://www.linkedin.com/company/admlabs
  - status: 403
    url: https://forgeglobal.com/adm-labs_stock/
  reason: defunct
  state: none
created: '2026-09-07'
description: 'ADM Labs is a Denver, Colorado hemp processor founded in 2017 by Arman Motiwalla as a subsidiary of ADM Group, running an extraction facility on Tejon Street that manufactured and wholesaled hemp-derived extracts - biomass, premium smokable, crude, distillate, isolate and water-soluble CBD, plus newer exotic cannabinoids - with white-label formulation for retail brands. It is a physical-goods manufacturer, not a software business, and never ran a developer program: its 2018-2021 site was a WordPress marketing site whose only transactional surface was a hosted Zoho Commerce storefront at store.adm-labs.com, with no API, SDK, webhook or developer link in its navigation. The company has since rebranded as Hemp Corp, which its original LinkedIn page still carries, and both adm-labs.com and the successor hempcorpusa.com now serve parking pages.'
layout: provider
modified: '2026-09-07'
name: ADM Labs
nav: Providers
network: true
overview: ADM Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hemp, CBD, Cannabinoids, and Extraction.
random_paper: 13
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.6
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: adm-labs
tags:
- Company
- Hemp
- CBD
- Cannabinoids
- Extraction
- Manufacturing
- Wholesale
- Consumer Packaged Goods
- Agriculture
website: https://www.linkedin.com/company/admlabs
---
