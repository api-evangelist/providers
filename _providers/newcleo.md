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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.newcleo.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/newcleo-dev-team
- group: build
  title: ''
  type: Packages
  url: packages/newcleo-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/newcleo-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newcleo-domain-security.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/newcleo-stock
coverage:
  checked: '2026-08-04'
  detail: 'Newcleo builds physical lead-cooled fast reactors and MOX fuel, not software products: www.newcleo.com is a 354-byte React shell that returns HTTP 404 with the same empty body for every sub-path and pulls all content client-side from a private Azure API Management Contentful proxy, and the only APIM routes referenced in its JavaScript bundle are website form handlers (contact-us, investor, supply-chain, user-admin) gated behind an Ocp-Apim-Subscription-Key, with no developer portal, no docs host, and no published specification anywhere.'
  evidence:
  - status: 200
    url: https://www.newcleo.com/
  - status: 404
    url: https://www.newcleo.com/our-technology/
  - status: 404
    url: https://newcleo-web-apim-prod.azure-api.net/contentful
  - status: 404
    url: https://newcleo-web-apim-prod.azure-api.net/newcleo-func-production/contact-us
  - status: 404
    url: https://www.newcleo.com/.well-known/agent-card.json
  - status: 404
    url: https://www.newcleo.com/llms.txt
  - status: 200
    url: https://github.com/newcleo-dev-team
  reason: not-a-software-company
  state: none
created: '2026-08-04'
description: Newcleo is a nuclear energy company founded in September 2021 by Stefano Buono, Luciano Cinotti and Elisabeth Rizzotti, headquartered in Paris with operations across France, Italy, the United Kingdom, Switzerland, Belgium and Slovakia. It designs small modular lead-cooled fast reactors (LFR) fuelled with mixed oxide (MOX) fuel made from reprocessed spent nuclear fuel, with the aim of closing the nuclear fuel cycle and reducing long-lived waste. The group employs roughly 1,000 people, has raised over EUR 780 million, and has grown by acquisition (Hydromine Nuclear Energy, SRS-Fucina, Rutschi Group). Newcleo publishes no public developer API or developer program; its only public machine-consumable software is a small set of open-source scientific Python libraries released through its newcleo-dev-team GitHub organisation.
image: https://avatars.githubusercontent.com/u/113201176?v=4
layout: provider
modified: '2026-08-04'
name: Newcleo
nav: Providers
network: true
overview: Newcleo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Nuclear Energy, Clean Energy, and Reactors.
random_paper: 14
score:
  band: minimal
  composite: 3.6
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 3.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/newcleo/refs/heads/main/screenshots/newcleo-2026-08-07T185057.png
security:
- kind: domain-security
  name: Newcleo Domain Security
  slug: newcleo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: newcleo
tags:
- Company
- Energy
- Nuclear Energy
- Clean Energy
- Reactors
- Deep Tech
- Manufacturing
- Open-Source
- Scientific Computing
website: https://www.newcleo.com
---
