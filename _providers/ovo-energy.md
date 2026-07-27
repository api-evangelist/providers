---
api_count: 0
artifact_total: 0
created: '2026-07-27'
description: 'OVO Energy is a United Kingdom household electricity and gas supplier founded in Bristol in 2009 by Stephen Fitzpatrick, and — after absorbing SSE''s household energy business in January 2020 — the third-largest domestic supplier in Great Britain with roughly four million home energy customers. It sits at the retail end of the GB energy value chain: buying wholesale, holding an Ofgem supply licence, settling through Elexon, reading SMETS2 smart meters over the licensed Smart DCC network, and billing the customer, alongside solar, home battery, heat pump, EV smart-charging (Charge Anytime) and demand-flexibility (Power Move) propositions. Its parent OVO Group also owns Kaluza, an API-first energy intelligence platform licensed to utilities worldwide — the direct British analogue to Octopus Energy''s Kraken — but that platform is a separate brand on a separate domain, and none of its API surface is published under OVO Energy. OVO Energy''s own API posture is closed: no developer
  portal, no API documentation, no machine-readable contract, and no third-party route to a customer''s usage or billing data. developer.ovoenergy.com, developers.ovoenergy.com, docs.ovoenergy.com and data.ovoenergy.com do not resolve; /developers, /api, /docs, /openapi.json and /.well-known/openid-configuration all return 404; api.ovoenergy.com resolves and is live but answers every path with a bare text/plain 404 ("No context-path matches the request URI"). The only consumer data surface found is undocumented and unsupported — smartpaymapi.ovoenergy.com/usage/api/half-hourly returns HTTP 401 JSON to an anonymous caller and serves half-hourly smart-meter consumption only to a signed-in OVO customer session. Britain mandated the metering INFRASTRUCTURE, not a data right: OVO is bound by the Smart Energy Code and the DCC, which is live and implemented, but no consumer data-portability mandate equivalent to Australia''s Consumer Data Right or Ontario''s Green Button applies to it. The Australian
  namesake, OVO Energy Pty Ltd, IS a designated CDR energy data holder — but it was acquired outright by AGL Energy in April 2024 and is no longer part of this organization, so that obligation does not attach here. Consumer data is closed, open market data is published by other GB parties (NESO, Elexon, the DNOs), and on 11 May 2026 OVO agreed the sale of this retail business to E.ON, with Kaluza explicitly excluded from the deal.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-27'
name: OVO Energy
nav: Providers
network: true
random_paper: 15
slug: ovo-energy
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Gas
- Smart Metering
- Energy Retail
- Solar
- EV Charging
- Demand Response
---
