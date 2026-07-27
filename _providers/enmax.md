---
access_model:
  confidence: high
  generated: '2026-07-27'
  label: Free · No published developer program; open ArcGIS grid services are anonymous
  method: manual
  onboarding: none-published
  pricing: free
  public: true
  source:
  - documentation
  - probing
  trial: false
  try_now: false
api_count: 1
artifact_total: 0
created: '2026-07-27'
description: 'ENMAX Corporation is the Calgary-based energy company owned outright by The City of Calgary, describing itself on its own about page as "a regulated wires company, a competitive power generator and an energy retailer" operating "across Alberta and Maine." It spans three tiers of the value chain at once: ENMAX Power owns and operates the regulated electricity distribution and transmission system inside Calgary, ENMAX Energy generates power and sells electricity and natural gas into Alberta''s deregulated retail market under the Easymax brand, and Versant Power — acquired from Emera in 2020 — is the transmission and distribution utility for northern and eastern Maine. Its API posture is the exact inverse of the Ontario utilities it is usually compared to, and the inversion is the finding. No consumer energy data mandate binds ENMAX anywhere it operates: Alberta has no Green Button regulation, Ontario''s O. Reg. 633/21 does not reach across the provincial border, Canada has no
  national equivalent, and Maine imposes no Green Button obligation on Versant Power. Unmandated, ENMAX built nothing — its own support documentation states plainly that the Energy Insights usage view inside a customer''s Easymax account "is view-only within your online account and can''t be exported at this time," which is a harder closure than most: not merely no API, but no CSV, no XML, and no Green Button either. There is no developer portal, no developer, api, docs or data subdomain, no OpenAPI, and no published third-party data path. What ENMAX does publish openly is grid data. Its Hosting Capacity, Load Capacity and Service Area maps, linked from enmax.com/system-resources, are ArcGIS Online web applications backed by ArcGIS REST feature services that answer anonymous machine-readable queries with no key, no signup and no terms — distribution-feeder DER hosting headroom and remaining load capacity for the Calgary service territory, the data a solar or storage developer actually needs.
  ENMAX never calls this an API and documents none of it, but it is real, it is open, and it is queryable. Wide open on grid data, completely shut on customer data.'
image: https://www.enmax.com/favicon.ico
layout: provider
modified: '2026-07-27'
name: ENMAX
nav: Providers
network: true
random_paper: 61
slug: enmax
tags:
- Energy
- Canada
- Utilities
- Electricity
- Natural Gas
- Grid
- Smart Metering
- Solar
- DER
- Geospatial
- Alberta
- Electricity Distribution
---
