---
api_count: 3
artifact_total: 0
created: '2026-07-27'
description: 'AGL Energy Limited (ASX:AGL) is Australia''s oldest listed company — founded in Sydney in 1837 as the Australian Gas Light Company — and one of the country''s largest integrated energy businesses, retailing electricity, gas, broadband and mobile to roughly four million customer accounts while owning the nation''s largest electricity generation portfolio (Bayswater and Loy Yang A coal, gas peakers, hydro, wind, utility-scale solar and grid-scale batteries). It sits at both ends of the Australian value chain: generator and wholesale market participant in the NEM, and the retailer of record that holds the customer relationship, the billing account and the metering data. Its API posture is entirely a product of regulation, not of product strategy. AGL publishes no public developer portal and no self-serve API programme — apideveloper.agl.com.au resolves through Akamai but returns HTTP 403 to every anonymous client, and agl.com.au itself is bot-blocked at 403. What AGL does expose
  is the Consumer Data Right: it is a designated CDR energy data holder, listed on the CDR Register under brand "AGL" with public base URI https://public.cdr.agl.com.au, and that surface is real and verified — GET /cds-au/v1/discovery/status and /cds-au/v1/discovery/outages both return HTTP 200 with conformant Consumer Data Standards envelopes, and AGL''s own outage notices describe scheduled downtime of the "AGL CDR Consent flow". Its energy plan Product Reference Data is genuinely open and anonymous — 1,343 plans at https://cdr.energymadeeasy.gov.au/agl/cds-au/v1/energy/plans — but that endpoint is operated centrally by the Australian Energy Regulator, not by AGL, which is the structural difference from CDR banking where every bank serves its own PRD. Consumer usage, billing, service point, DER and account data is available only to Accredited Data Recipients, over mTLS, under a consumer authorisation, with the base URI distributed through the CDR Register rather than published. AGL is
  therefore open on product data, closed to everyone but accredited recipients on consumer data, and silent everywhere else — it publishes no open grid or market data of its own. It is also migrating around four million customer services onto the Kaluza platform under a A$150m, 20 percent stake taken in 2024, so the retail data layer behind these mandated endpoints is being rebuilt on a third-party energy operating system.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-27'
name: AGL Energy
nav: Providers
network: true
random_paper: 51
slug: agl-energy
tags:
- Energy
- Australia
- Utilities
- Electricity
- Gas
- Energy Retailer
- Consumer Data Right
- CDR
- Smart Metering
- Solar
- DER
- Renewables
- Energy Markets
---
