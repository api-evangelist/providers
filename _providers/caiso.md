---
api_count: 2
artifact_total: 0
created: '2026-07-27'
description: 'The California Independent System Operator (CAISO) is the non-profit public benefit corporation that operates the high-voltage transmission grid serving roughly 80 percent of California plus a portion of Nevada, and runs the wholesale day-ahead and real-time electricity markets, the Western Energy Imbalance Market (WEIM), and the Extended Day-Ahead Market (EDAM). As a system and market operator in the United States it sits at the wholesale layer of the energy value chain — upstream of the investor-owned utilities that bill retail customers, and therefore it holds no retail customer accounts and publishes no consumer usage data. Its API posture is a clean split: market data is genuinely open and consumer data does not exist. The OASIS Download API at https://oasis.caiso.com/oasisapi serves locational marginal prices, demand and renewables forecasts, ancillary services, transmission and nodal reference data as zipped CSV or CIM XML to anonymous callers with no key, no account
  and no registration — CAISO states in writing that every system it operates except OASIS requires a company User Access Administrator to grant access. The Today''s Outlook telemetry feeds under https://www.caiso.com/outlook publish five-minute fuel mix, demand, net demand and CO2 as plain CSV, also anonymously. Everything else — market submission, dispatch, settlements and the participant portals — is behind PKI client certificates and UAA-sponsored accounts, and even the OASIS reference documentation on the developer site requires a signup reviewed against a corporate email domain and a written justification. No Green Button, ESPI, or Consumer Data Right surface exists here and none is expected to; the obligation CAISO answers to is FERC''s open-access transparency regime, not a consumer data right. No OpenAPI, AsyncAPI, or other machine-readable contract is published for any of it.'
image: https://www.caiso.com/apple-touch-icon.png
layout: provider
modified: '2026-07-27'
name: California ISO
nav: Providers
network: true
random_paper: 51
slug: caiso
tags:
- Energy
- United States
- Electricity
- Energy Markets
- Grid
- Renewables
- System Operator
- Market Data
- California
---
