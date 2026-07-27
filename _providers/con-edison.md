---
access_model:
  confidence: high
  generated: '2026-07-27'
  label: Free · Registration, Data Security Agreement and supervised onboarding required
  method: manual
  onboarding: application-approval
  pricing: free
  public: false
  source:
  - documentation
  - authentication
  trial: false
  try_now: false
api_count: 2
artifact_total: 0
created: '2026-07-27'
description: 'Consolidated Edison Company of New York, Inc. (CECONY, trading as Con Edison) is the investor-owned electric, gas and steam utility that serves New York City and Westchester County, and together with its sibling Orange & Rockland Utilities (ORU) forms the regulated utility core of Consolidated Edison, Inc. It is a wires-and-pipes distribution utility rather than a competitive retailer: it owns and operates the distribution system, meters the customer and bills the customer, while wholesale energy markets are run by NYISO and competitive supply is sold by ESCOs. It is rate-regulated by the New York State Public Service Commission. Its API posture is the most interesting in the United States sample because both halves are real and they are gated completely differently. On the consumer side Con Edison runs a genuine, verified Green Button Connect My Data implementation — the NAESB REQ.21 ESPI standard, branded "Share My Data" — with a live production base URI at https://api.coned.com/gbc/espi/1_1
  that answers anonymously with HTTP 401 "Unauthorized. Access token is missing or invalid.", a publicly downloadable 37-path Swagger 2.0 definition ("DCX GBC API V2"), a public Postman collection titled "GBC Certification Third party V3.3", OAuth 2.0 authorization-code and client-credentials flows, ESPI functional-block scopes, batch and real-time interval endpoints, and a 35-page technical onboarding document last revised 2026-05-07. The United States has no federal energy consumer data right; Con Edison''s adoption sits under New York PSC supervision (the Joint Utilities DSIP proceeding, Case 16-M-0411, in which it committed to implement the first phase of GBC by end of 2017, the Data Access Framework in Case 20-M-0082, and a Customer Data Access Tariff) rather than under a statutory mandate like Australia''s Consumer Data Right or Ontario Regulation 633/21. That data is not self-serve: a third party must register, sign a Data Security Agreement, submit a technical onboarding form and
  pass 30 to 60 days of supervised testing before production credentials are issued, and Con Edison states plainly that it "is unable to support API development for third parties." On the market side, by contrast, Con Edison publishes distribution-grid data openly and anonymously: the Hosting Capacity Map documents REST API access, and its ArcGIS feature services for segmented and network hosting capacity, EV transformer capacity, 33kV feeders, non-wires-solutions networks and disadvantaged communities all answer unauthenticated. Open on the grid, accredited on the customer — that split is the finding.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-27'
name: Con Edison
nav: Providers
network: true
random_paper: 55
slug: con-edison
tags:
- Energy
- United States
- New York
- Utilities
- Electricity
- Gas
- Steam
- Smart Metering
- Green Button
- Energy Data
- Grid
- Distribution
- Hosting Capacity
- Distributed Energy Resources
- Solar
- EV Charging
- Demand Response
---
