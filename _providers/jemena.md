---
api_count: 1
artifact_total: 0
created: '2026-07-27'
description: 'Jemena is an Australian energy infrastructure owner-operator, headquartered in Melbourne and owned by SGSP (Australia) Assets — 60% State Grid Corporation of China, 40% Singapore Power. It sits on the poles-and-pipes side of the value chain, not the retail side: it runs the Jemena Electricity Network distributing power to north and north-west Melbourne, the Jemena Gas Network distributing gas across New South Wales, the Eastern, Queensland and Northern Gas Pipelines, the Colongra storage facility, and holds 50% of ActewAGL''s ACT distribution networks. Its API posture is the inverse of what the Australian Consumer Data Right story would predict. Jemena is NOT a designated CDR energy data holder — the CDR energy designation covers retailers as primary data holders and AEMO as secondary data holder, and the live CDR Register energy brand list contains 84 brands, all of them retailers and none of them a distribution network. There is consequently no Jemena consumer usage or billing
  API, and the Electricity Outlook customer smart-meter portal no longer resolves in DNS. Jemena also publishes no open market or network data API; its outage map is CloudFront geo-restricted and its Daily Gas Data product is a paid annual email subscription. What Jemena does run is a real, live, standards-conformant machine-to-machine API for grid control: the JEN CSIP-AUS Utility Server, an IEEE 2030.5 / SEP2 implementation of the CSIP-AUS (SA TS 5573) profile, stood up to satisfy the Victorian Government''s emergency backstop mandate for remotely curtailable rooftop solar. It is fully documented in public PDF handbooks, has published staging and production base URIs, and is gated behind Jemena-issued mTLS PKI certificates, IP whitelisting and an OEM conformance-testing programme.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jemena.png
layout: provider
modified: '2026-07-27'
name: Jemena
nav: Providers
network: true
random_paper: 12
slug: jemena
tags:
- Energy
- Australia
- Utilities
- Electricity
- Gas
- Grid
- Network Distributor
- DER
- Solar
- Smart Metering
- Demand Response
- IEEE 2030.5
---
