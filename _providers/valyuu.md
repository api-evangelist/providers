---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
api_count: 1
apis:
- description: Partner-facing trade-in API behind Valyuu's embedded recommerce platform. Version 1 exposes device catalog lookups (categories, brands, series, models, and model condition/attribute questions), FAQ co
  name: Valyuu Partner API
  slug: valyuu-partner-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/valyuu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://valyuu.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Valyuu
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://15q6umhquujjvdoy.public.blob.vercel-storage.com/privacy-policy/(EN)%20Privacy%20policy-SCHnPlBo0ZIC7CyGhWHgpLjRIeEVLE.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://15q6umhquujjvdoy.public.blob.vercel-storage.com/selling-t%26c/(EN)%20Selling%20Terms%20and%20Conditions_Valyuu%20-LdMQiilaDa887YNj0BWw2XEGmYgLmK.pdf
- group: agent
  title: ''
  type: WellKnown
  url: well-known/valyuu-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/valyuu-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/valyuu-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/valyuu-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/valyuu-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/valyuu-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/valyuu-sandbox.yml
created: '2026-07-17'
description: Valyuu is an Amsterdam-founded embedded recommerce service provider offering a plug-and-play trade-in platform that businesses integrate to buy back, resell, and recycle used consumer electronics such as smartphones, tablets, and smartwatches across Dutch, German, and English-language markets. Its partner-facing Trade-In API powers embedded trade-in flows covering device catalogs, condition questions, offers, payments, and shipping. Valyuu is a Techstars portfolio company; as of mid-2026 valyuu.com redirects to prioont.com, whose storefront is currently unreachable.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/valyuu.png
layout: provider
modified: '2026-07-21'
name: Valyuu
nav: Providers
network: true
overview: 'Valyuu publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Recommerce, Trade-In, Circular Economy, and Consumer Electronics.


  Valyuu''s developer surface includes authentication, sandbox, and 10 more developer resources.'
random_paper: 6
security:
- kind: authentication
  name: Valyuu Authentication
  slug: valyuu-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Valyuu Domain Security
  slug: valyuu-domain-security
  summary_line: TLSv1.3 · DMARC
slug: valyuu
tags:
- Company
- Recommerce
- Trade-In
- Circular Economy
- Consumer Electronics
- Sustainability
- E-Commerce
website: https://valyuu.com/
---
