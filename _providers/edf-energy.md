---
api_count: 3
artifact_total: 0
created: '2026-07-27'
description: 'EDF Energy Ltd is the British integrated energy business wholly owned by Electricite de France (EDF), the French state-owned utility. Formed in 2002 from London Electricity, SWEB and SEEBOARD and enlarged by the 2009 acquisition of British Energy, it is one of the largest suppliers of electricity and gas in Great Britain with roughly five million customer accounts, and it is also Britain''s largest generator of zero-carbon electricity — it operates the country''s fleet of operating nuclear power stations (the advanced gas-cooled reactors at Hartlepool, Heysham 1, Heysham 2 and Torness, and the Sizewell B pressurised water reactor), is building Hinkley Point C, and owns wind, solar, battery (Pivot Power) and EV charging (Pod Point) businesses. It therefore sits at both ends of the GB value chain: a licensed generator and wholesale market participant, and the retailer of record holding the customer relationship, the billing account and the meter data. Its API posture is the opposite
  of the mandated-utility pattern. The United Kingdom has no consumer energy data-portability right — no Consumer Data Right, no Green Button obligation. Britain mandated infrastructure instead: the licensed Smart DCC monopoly carries smart-meter traffic under the Smart Energy Code, and EDF is bound by that as a licensed supplier, but it confers no third-party consumer data API. And yet EDF publishes one of the more substantial public API programmes of any European utility, because it does not run its own retail platform: in 2023 EDF licensed Kraken from Octopus Energy Group and completed the migration of 5.8 million customer accounts in fifteen months, so EDF''s API is Kraken''s API, branded for EDF GB at developer.edfgb-kraken.energy. That portal is fully public and was confirmed live at HTTP 200 on 2026-07-27. It publishes a first-party OpenAPI 3.0.3 document for a 27-path REST API, a second OpenAPI 3.0.3 document for a 16-path customer-migration API, and a GraphQL API whose schema —
  2,492 types, 246 queries, 417 mutations — was harvested by anonymous introspection with no key and no account. EDF''s retail tariff and product data is genuinely open: GET https://api.edfgb-kraken.energy/v1/products/ returned 21 live products at HTTP 200 anonymously, and the GraphQL energyProducts query returns real EDF tariffs with brand "EDF". Consumer usage and billing data is documented in the same contracts but requires an Authorization token issued to the account holder, or an OAuth application authorised against the OpenID Connect server at auth.edfgb-kraken.energy, whose anonymously served discovery document advertises 111 scopes including request:consumption-data and view:smartflex-data. Open market data is the gap: EDF discloses its REMIT generation unavailability on its own website as an HTML table, but the XML and CSV export links it publishes on that very page both return HTTP 404, and the machine-readable channel for those disclosures is Elexon''s BMRS platform, which EDF
  does not operate — 27 EDF REMIT messages under registration code 48X000000000022A were confirmed there in a single week. Open on tariffs, gated on consumer data, broken on its own market-data exports, and none of it compelled.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-27'
name: EDF Energy
nav: Providers
network: true
random_paper: 46
slug: edf-energy
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Gas
- Energy Retailer
- Energy Supplier
- Smart Metering
- Nuclear
- Renewables
- EV Charging
- Demand Response
- Tariffs
- Energy Markets
---
