---
access_model:
  confidence: high
  generated: '2026-07-27'
  label: Free · Own-account customer login required
  method: manual
  onboarding: customer-account-required
  pricing: free
  public: false
  source:
  - documentation
  - authentication
  trial: false
  try_now: false
api_count: 0
artifact_total: 0
created: '2026-07-27'
description: 'British Columbia Hydro and Power Authority (BC Hydro) is a provincial Crown corporation whose sole shareholder is the Province of British Columbia, and which states that it generates and delivers electricity to "95% of the population of B.C." and serves "over five million people." It is the vertically integrated end of the value chain in a market with no retail competition: BC Hydro owns the generation fleet (predominantly large hydroelectric), owns and operates the provincial transmission and distribution system, and is the monopoly retailer that bills the customer — all under rate regulation by the B.C. Utilities Commission (BCUC), not under any consumer data right. That regulatory fact drives the entire API posture. Ontario Regulation 633/21 compels Ontario distributors to implement Green Button Download My Data and Connect My Data; British Columbia has no equivalent, and no Canadian federal energy data mandate exists. BC Hydro has nonetheless adopted Green Button voluntarily
  — but only the file half of it. BC Hydro''s own MyHydro billing pages state that a customer can "Download a CSV or Green Button XML file with your metered electricity use," available through the previous day and up to three years back. There is no Connect My Data, no OAuth authorization surface, no third-party vendor onboarding, and no published resource base URI: a third party cannot obtain a customer''s usage data through any documented API, only the account holder can, by logging in and downloading a file. On the market-data side the picture is just as closed. There is no developer.bchydro.com, api.bchydro.com, data.bchydro.com or docs.bchydro.com (all DNS failures), no /developers, /api or /data path, no OpenAPI or Swagger definition anywhere, and no open data portal. Wholesale transmission information is posted to an OATI-hosted OASIS node that only registered transmission customers may use, and the BCUC-ordered transaction-data postings are documents rather than feeds. The single
  deliberate open-data artifact is one 2013 mapping layer published to the provincial BC Data Catalogue under the org "bc-hydro-and-power-authority." The finding is a utility that is closed on both axes: consumer data exists in a real standard but only as a human-initiated download behind a customer login, and grid/market data is either registration-gated or absent.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-27'
name: BC Hydro
nav: Providers
network: true
random_paper: 44
slug: bc-hydro
tags:
- Energy
- Canada
- Utilities
- Electricity
- Crown Corporation
- Hydroelectric
- Renewables
- Grid
- Transmission
- Distribution
- Smart Metering
- Green Button
- Energy Data
- EV Charging
---
