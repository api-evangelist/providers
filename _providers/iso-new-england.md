---
access_model:
  confidence: high
  generated: '2026-07-27'
  label: Free - Self-serve ISO Express account required for the API
  method: observed
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - probe
  - documentation
  trial: false
  try_now: false
api_count: 1
artifact_total: 0
created: '2026-07-27'
description: ISO New England Inc. is the independent, nonprofit regional transmission organization authorized by the Federal Energy Regulatory Commission to operate the high-voltage power system, administer the wholesale electricity markets, and plan the power system for Connecticut, Rhode Island, Massachusetts, Vermont, New Hampshire, and most of Maine. Home market is the United States. It sits at the wholesale layer of the value chain, between generators, transmission owners, interconnections with New York and Canada, and the load-serving entities that resell power to retail customers - and it states on its own site that handling retail electricity is something it does not do. Its API posture is the sector's classic split, read from the wholesale end. Market and system data is genuinely open, so open that the ISO Express portal serves full nodal day-ahead LMP files as anonymous CSV and the public dashboards are backed by an anonymous JSON feed. Consumer data does not exist here at all,
  and cannot, because ISO New England holds no retail customer relationships and no Green Button, ESPI, or consumer data-portability mandate reaches it. The one documented programmatic contract, the Web Services API v1.1, is a real, richly documented RESTful surface of 477 path templates across 90 market and operations resources, but it answers 401 to anonymous callers - a developer must first create a free, self-serve ISO Express account, which the ISO says automatically grants access to the data feeds, and then authenticate with HTTP Basic over SSL.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-27'
name: ISO New England
nav: Providers
network: true
random_paper: 52
slug: iso-new-england
tags:
- Energy
- United States
- Electricity
- Energy Markets
- Grid
- Open Data
- Wholesale Markets
- Demand Response
- Renewables
- New England
---
