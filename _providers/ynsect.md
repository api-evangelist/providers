---
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
