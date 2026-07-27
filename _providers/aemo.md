---
api_count: 77
artifact_total: 0
created: '2026-07-27'
description: 'AEMO, the Australian Energy Market Operator, is the independent system and market operator for Australia''s electricity and gas systems — it dispatches and prices the National Electricity Market across Queensland, New South Wales, Victoria, South Australia and Tasmania every five minutes, runs the Wholesale Electricity Market and the Gas Bulletin Board in Western Australia, operates the Victorian gas declared wholesale market and the Gas Supply Hubs, maintains the MSATS metering registry and the national Distributed Energy Resources register, and publishes the Integrated System Plan. It sits at the centre of the value chain: it does not generate, network or retail energy, it clears the market and holds the settlement-grade metering data that every other participant depends on. Under the Consumer Data Right extended to energy, AEMO is the designated SECONDARY data holder and gateway — retailers are the primary data holders, and AEMO serves NMI standing data, distributed energy
  resource records and up to twenty-four months of interval meter data through mandated Consumer Data Standards endpoints. Its API posture splits cleanly in two, and the split is the whole story: the market-data half is genuinely, radically open — 103 live NEMWeb report directories plus 68 archive directories of dispatch, price, demand, bidding, constraint and settlement data downloadable by anyone with no key, no account and no licence, alongside anonymous JSON endpoints behind the public NEM dashboard; the participant and consumer half is completely closed — a public developer portal at dev.aemo.com.au catalogues 74 APIs and 771 operations that anyone may read, but every one of them requires registration as an AEMO market participant, a Participant ID, MSATS user rights and an AEMO-signed mutual-TLS client certificate, and the OpenAPI documents the portal exports publicly are empty shells that declare zero paths and point at internal hostnames.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aemo.png
layout: provider
modified: '2026-07-27'
name: AEMO
nav: Providers
network: true
random_paper: 10
slug: aemo
tags:
- Energy
- Australia
- Electricity
- Gas
- Energy Markets
- Grid
- Market Operator
- System Operator
- Open Energy Data
- Consumer Data Right
- CDR
- Smart Metering
- Distributed Energy Resources
- Renewables
- Utilities
---
