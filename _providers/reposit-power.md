---
api_count: 2
artifact_total: 0
created: '2026-07-27'
description: 'Reposit Power is an Australian home-energy technology company founded in 2012 and headquartered in Canberra, ACT, that builds the Reposit Controller — a local control device and cloud platform that sits on top of a household''s solar, battery and meter and trades that stored energy into the National Electricity Market on the owner''s behalf, paying the household back as GridCredits and underwriting the result with its No Bill guarantee. It is not a retailer, a distributor or a meter provider; it sits one layer above them in the Australian energy value chain as a distributed-energy-resource aggregator and virtual power plant operator, selling through a national network of solar installers and partnering with retailers and network businesses who dispatch and curtail its fleet. Its API posture is the opposite of the retailer pattern and needs stating plainly. Reposit is NOT a designated Consumer Data Right energy data holder — it does not appear among the 84 energy data-holder
  brands on the ACCC CDR Register, and it is not an accredited data recipient — so the Australian statutory energy mandate simply does not reach it, and the company publishes no CDR page at all. What it does publish, entirely voluntarily and with no obligation compelling it, is two real, downloadable, anonymously readable OpenAPI contracts behind two live Swagger UI pages: a Customer API covering a household''s own solar, inverter, battery state-of-charge, house consumption, grid-meter power and earned GridCredits, and a much larger Market API used by Reposit Fleet that lets network and retailer organisations enumerate nodes, build power stations, pull fleet telemetry and issue export curtailments and dispatches against real homes. Every operational endpoint on both APIs returned 401 anonymously — the contracts are open, the data is not. There is no open market or grid data feed of any kind, no Green Button, no Consumer Data Standards conformance and no reference to IEEE 2030.5, CSIP-AUS,
  OpenADR or IEC CIM anywhere in either specification; the shape is proprietary, with the Australian National Meter Identifier as its only sector identifier.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reposit-power.png
layout: provider
modified: '2026-07-27'
name: Reposit Power
nav: Providers
network: true
random_paper: 16
slug: reposit-power
tags:
- Energy
- Australia
- Utilities
- Electricity
- Batteries
- DER
- Virtual Power Plant
- Demand Response
- Solar
- Grid
- Energy Markets
- Smart Metering
- Storage
- Flexibility
---
