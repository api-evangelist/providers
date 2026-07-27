---
api_count: 1
artifact_total: 0
created: '2026-07-27'
description: 'Hydro Ottawa Holding Inc. is a private corporation 100 percent owned by the City of Ottawa, and the parent of Hydro Ottawa Limited — the regulated local distribution company (LDC) that delivers electricity to roughly 372,000 customers in Ottawa and Casselman, Ontario — alongside Portage Power (Ontario''s largest municipally-owned renewable generator, with run-of-river hydroelectric plants at Chaudière Falls and elsewhere in Ontario, Quebec and New York plus solar installations across Ottawa), Envari (energy solutions) and Hiboo Networks (fibre). It sits at the wires-and-meter end of the Canadian value chain: it does not run the market — that is IESO — and it is not a competitive retailer, it is the monopoly distributor that owns the smart meter, the interval data and the billing relationship. Its API posture exists because Ontario legislated it. Ontario Regulation 633/21 (Energy Data) under the Electricity Act, 1998 compels roughly sixty electricity and natural gas utilities
  in the province to implement Green Button Download My Data and Green Button Connect My Data to the NAESB REQ.21 ESPI v3.3 standard and to have those implementations certified by the Green Button Alliance — a province-level, standard-specific consumer data mandate with no Canadian national equivalent. Hydro Ottawa states on its own site that it offers both services free of charge and that third parties must complete its onboarding process and certify with the GBA. Two live surfaces back that up: a customer Green Button authorization portal at https://hydroottawa.savagedata.com/Connect/Authorize (HTTP 200) and an anonymously reachable third-party developer registration application at https://ottawaonboarding.savagedata.com/ (HTTP 200), both operated by the North Bay vendor Savage Data Systems. What could NOT be verified is the thing the mandate actually requires: no ESPI base URI is published anywhere, the vendor host is a catch-all Blazor SPA that returns HTTP 200 with identical HTML for
  every path including invented ones, no OpenID Connect discovery document is served anonymously, and no public Green Button Alliance certificate register listing Hydro Ottawa by name could be found. The mandate is recorded here as claimed-and-plausibly- operating, not as verified. Everything else is closed: hydroottawa.com returns 404 for /developers, /api, /docs, /data, /openapi.json and /swagger.json; developers.hydroottawa.com does not resolve and developersdev.hydroottawa.com answers HTTP 530 through Cloudflare; api.hydroottawa.com exists but returns 403 at root and 404 on every path; the github.com/hydroottawa organization has existed since 2015 with zero public repositories; and the City of Ottawa open data portal carries 682 datasets, none of them Hydro Ottawa''s. The one genuinely open, anonymous, machine-readable feed carrying Hydro Ottawa data — live outage counts under the KUBRA StormCenter instance behind outages.hydroottawa.com — is undocumented vendor infrastructure that Hydro
  Ottawa does not publish as a product, and it is deliberately not listed as an API here. Hydro Ottawa is therefore a utility with a mandated consumer data API it does not document, and no open market data at all.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-27'
name: Hydro Ottawa
nav: Providers
network: true
random_paper: 27
slug: hydro-ottawa
tags:
- Energy
- Canada
- Ontario
- Utilities
- Electricity
- Electricity Distribution
- Smart Metering
- Green Button
- ESPI
- Municipal Utility
- Renewables
- Hydroelectric
- Solar
- Demand Response
- Grid
---
