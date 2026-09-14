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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/landvault-domain-security.yml
created: '2026-07-17'
description: 'Landvault was surfaced as a portfolio company of Speedinvest and added to the API Evangelist network as a stub awaiting enrichment. Enrichment probing on 2026-07-19 found no operating company surface: the landvault.io domain of record resolves to a GoDaddy parking page rather than a website, serving a /lander redirect stub for every path, with no MX records and only a registrar-default DMARC record. The landvault.xyz variant redirects to a GoDaddy for-sale listing. No developer portal, documentation, API reference, OpenAPI definition, SDK, package-registry presence, or GitHub organization could be verified. This profile is retained as a dead lead with recorded probe evidence so the enrichment pipeline does not repeatedly re-attempt it.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/landvault.png
layout: provider
modified: '2026-07-19'
name: Landvault
nav: Providers
network: true
overview: Landvault is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Portfolio Lead, Speedinvest, No API Surface, and Parked Domain.
random_paper: 5
security:
- kind: domain-security
  name: Landvault Domain Security
  slug: landvault-domain-security
  summary_line: TLSv1.3 · DMARC
slug: landvault
tags:
- Company
- Portfolio Lead
- Speedinvest
- No API Surface
- Parked Domain
---
