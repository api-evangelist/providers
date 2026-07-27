---
access_model:
  confidence: high
  generated: '2026-07-27'
  label: Open public market data · Member-gated participant APIs
  method: manual
  onboarding: none-published
  pricing: free
  public: true
  source:
  - probe
  - documentation
  trial: false
  try_now: true
api_count: 6
artifact_total: 0
created: '2026-07-27'
description: 'Southwest Power Pool (SPP) is a nonprofit Regional Transmission Organization regulated by the Federal Energy Regulatory Commission and headquartered in Little Rock, Arkansas. Founded in 1941 and approved as an RTO in 2004, SPP operates the Integrated Marketplace day-ahead and real-time balancing markets, the Western Energy Imbalance Service (WEIS) market, Western Reliability Coordination services, and is building the Markets+ day-ahead market for the West with a targeted 2027 go-live. SPP sits at the wholesale layer of the United States energy value chain: it dispatches generation, prices congestion, plans transmission, and settles the market for its member utilities — it has no retail customers, so no consumer energy-data mandate such as Green Button applies to it. Its API posture is a clean split. Market and grid data is genuinely open: locational marginal prices, market clearing prices, operating reserves, load, generation mix, VER curtailments and outage capacity are served
  anonymously as CSV from the SPP Portal file browser and from an anonymous public FTP site, with an Esri ArcGIS REST price-contour service alongside — no account, no key, no licence click-through. Everything a market participant actually transacts against is the opposite: the Integrated Marketplace SOAP web services, the Settlement Management System API, and the FERC Order 881 LEP/TROLIE ratings API are member-only, require an OATI webCARES x.509 digital certificate plus an SPP UAA role, and SPP publishes no base URL and no OpenAPI for them.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-27'
name: Southwest Power Pool
nav: Providers
network: true
random_paper: 67
slug: spp
tags:
- Energy
- United States
- Energy Markets
- Electricity
- Grid
- Utilities
- Renewables
- Market Data
- Transmission
- System Operator
---
