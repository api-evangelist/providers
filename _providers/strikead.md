---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-12'
  detail: StrikeAd was acquired by Sizmek in May 2015 and the brand was retired; strikead.com is now a GoDaddy-parked domain whose catch-all responder returns the identical 114-byte /lander HTML for every path - including a nonsense negative-control path - so its 200s on /.well-known/ and /openapi.json are parking shells, not documents.
  evidence:
  - status: 200
    url: https://strikead.com/this-path-does-not-exist-12345
  - status: 200
    url: https://strikead.com/.well-known/agent-card.json
  - status: 200
    url: https://strikead.com/openapi.json
  - status: 0
    url: https://api.strikead.com/
  - status: 200
    url: https://api.github.com/orgs/strikead
  reason: defunct
  state: none
created: '2026-07-17'
description: StrikeAd was a mobile advertising technology company, founded in New York City in 2010 and backed by Uncork Capital, that built Fusion - one of the first demand-side platforms (DSPs) built specifically for mobile programmatic advertising. Sizmek Inc. completed its acquisition of StrikeAd for approximately $11.7 million in May 2015 and folded the platform into Sizmek MDX; Sizmek itself was subsequently broken up, with its ad server going to Amazon and its DSP and DMP to Zeta Global. The StrikeAd brand no longer operates. Its primary domain (strikead.com) is now a parked domain on GoDaddy nameservers that answers every request - homepage, /.well-known/ discovery paths, and common contract paths alike - with the same 114-byte HTML lander redirect to /lander, confirmed against a negative-control path. The api., docs. and developer. subdomains do not resolve, and the github.com/strikead organization is named "ex-StrikeAd" and has zero public repositories. No developer portal, API
  documentation, OpenAPI definition, or other machine-readable API surface exists.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/strikead.png
layout: provider
modified: '2026-08-12'
name: StrikeAd
nav: Providers
network: true
overview: StrikeAd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Mobile, AdTech, and Programmatic.
random_paper: 15
slug: strikead
tags:
- Company
- Advertising
- Mobile
- AdTech
- Programmatic
- DSP
---
