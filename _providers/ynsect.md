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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-04'
  detail: Ÿnsect was placed in judicial liquidation on 1 December 2025 and its web origin has since been switched off — ynsect.com still resolves to 51.75.15.14 but refuses connections on ports 80 and 443, so all 100 probes against ynsect.com and www.ynsect.com failed at connect with no HTTP status, while ynsect.fr returns a blanket 301 to that same dead host on all 25 paths probed.
  evidence:
  - status: 0
    url: https://ynsect.com/
  - status: 0
    url: https://www.ynsect.com/
  - status: 0
    url: https://ynsect.com/openapi.json
  - status: 0
    url: https://ynsect.com/.well-known/agent-card.json
  - status: 301
    url: http://ynsect.fr/openapi.json
  - status: 404
    url: https://github.com/ynsect
  - status: 403
    url: https://forgeglobal.com/ynsect_stock/
  reason: defunct
  state: none
created: '2026-09-04'
description: 'Ÿnsect (Ÿnsect SAS) was a French agri-technology company, founded in Évry, Essonne on 4 October 2011 by Antoine Hubert, Jean-Gabriel Levon, Fabrice Berro and Alexis Angot, that farmed Tenebrio molitor mealworms and Alphitobius diaperinus buffalo larvae in automated vertical farms and processed them into high-protein ingredients for aquaculture and animal feed, the Spryng pet-food line, food-grade ingredients for human nutrition, and the Ynfrass organic fertiliser made from insect frass. It was for a time the best-funded insect-protein company in the world, raising roughly €600 million over fourteen years, including a €372 million Series C in 2020 and a further €160 million in early 2023, and it operated sites at Dole and Damparis in the Jura while building the Ynfarm vertical farm at Poulainville near Amiens. The economics never closed: Ÿnsect requested safeguard proceedings on 26 September 2024, was placed in judicial reorganisation on 3 March 2025, and — unable to fund a
  continuation plan within the observation period — was placed in judicial liquidation on 1 December 2025. The Damparis site was taken over in 2025 by Keprea, a separate company founded by Ÿnsect alumni, to make fertiliser from insect frass; Keprea is not a successor to Ÿnsect and its surfaces are not part of this profile. Ÿnsect was an industrial producer of physical goods and never operated a developer program, public API, SDK, webhook surface or machine-readable specification of any kind. Its host ynsect.com is still registered to the company but the web origin has been switched off — TCP 80 and 443 refuse connections — and ynsect.fr is a bare OVH redirect to that dead host, so no pointer to a live company website is wired. This profile is retained as a historical record; there is no API surface to enrich.'
layout: provider
modified: '2026-09-04'
name: Ynsect
nav: Providers
network: true
overview: Ynsect is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Agriculture, AgTech, and Food.
random_paper: 11
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
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
slug: ynsect
tags:
- Company
- Defunct
- Agriculture
- AgTech
- Food
- Insect-Protein
- Animal-Feed
- Fertilizer
- Biotechnology
- Manufacturing
- France
---
