---
api_count: 2
artifact_total: 0
created: '2026-07-27'
description: Southern California Edison (SCE) is the regulated electric utility subsidiary of Edison International, delivering power to roughly 15 million people across a 50,000 square-mile service territory in central, coastal, and southern California. In the United States energy value chain SCE sits at the distribution and retail layer as an investor-owned utility (IOU) regulated by the California Public Utilities Commission, operating the meters, the distribution grid, and the customer of record relationship that every downstream energy-data platform, DER aggregator, demand response provider, and solar installer ultimately depends on. Its API posture splits cleanly in two. Consumer data is mandated but closed to the open web - SCE runs Green Button Connect My Data through its Customer Data Access platform under CPUC tariff Rule 26 (Advice 3087-E, Decision 14-05-016), and states publicly that third parties need OAuth 2.0 and bulk API capability consistent with the NAESB ESPI standard,
  but publishes no developer portal, no base URI, no OpenAPI, and no sandbox - a third party must register with a Taxpayer Identification Number, accept terms, and pass a machine-to-machine connectivity test before any endpoint is disclosed. Grid data is genuinely open - SCE's Distribution Resources Plan External Portal (DRPEP) serves Integration Capacity Analysis, distribution circuit, PSPS, fire map, and load growth layers over an anonymous, unauthenticated ArcGIS REST service catalog that any developer can query today without a key.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/southern-california-edison.png
layout: provider
modified: '2026-07-27'
name: Southern California Edison
nav: Providers
network: true
random_paper: 16
slug: southern-california-edison
tags:
- Energy
- United States
- Utilities
- Electricity
- Smart Metering
- Green Button
- Grid
- Demand Response
- Solar
- DER
- EV Charging
- California
---
