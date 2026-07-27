---
api_count: 15
artifact_total: 0
created: '2026-07-27'
description: 'The Alberta Electric System Operator (AESO) is the independent, not-for-profit system and market operator for Alberta''s electricity system — a statutory body created under Alberta''s Electric Utilities Act that dispatches generation and operates the Alberta Interconnected Electric System twenty-four hours a day for roughly five million Albertans, plans the transmission system, administers grid connections, and runs Alberta''s energy-only wholesale market including price settlement and market rules. It sits in the middle of the value chain: it does not own generation, wires or retail customers, it clears the pool, publishes the Pool Price, and holds the market-wide operational data every generator, retailer and trader in Alberta depends on. Its API posture is unusually clean for the sector and is the exact opposite of a compliance story — there is no mandate on AESO at all. Alberta has no Consumer Data Right, no Green Button regulation (that is Ontario''s, by regulation, and
  Nova Scotia''s), and no consumer energy-data obligation of any kind, and AESO holds no retail customer usage or billing data, so the consumer-data half of this sector simply does not exist here. What AESO publishes voluntarily is a genuinely open market-data surface in two layers: the legacy Energy Trading System report servlets at ets.aeso.ca, which return real CSV and HTML market reports — current supply and demand, pool price, system marginal price, daily averages, outages — anonymously with no key, no account and no licence click-through; and a modern Azure API Management gateway at apimgw.aeso.ca fronting fourteen documented JSON APIs whose full reference, operations, schemas and OpenAPI export can be read anonymously from the public developer portal, and whose keys are issued self-serve — email confirmation, subscribe to the single "AESO Public API" product, keys generated instantly, no approval step. Authentication is a single API-KEY request header (or a subscription-key query
  parameter). The one real friction is legal rather than technical: AESO''s site terms permit non-commercial, personal or educational use only, and any other use requires written permission.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aeso.png
layout: provider
modified: '2026-07-27'
name: AESO
nav: Providers
network: true
random_paper: 16
slug: aeso
tags:
- Energy
- Canada
- Alberta
- Electricity
- Energy Markets
- Grid
- System Operator
- Market Operator
- Open Energy Data
- Wholesale Power
- Demand Response
- Renewables
- Utilities
---
