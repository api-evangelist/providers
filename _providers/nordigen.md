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
api_count: 1
apis:
- description: Connect to bank accounts using official bank APIs and get raw transaction data
  name: Nordigen
  slug: nordigen
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nordigen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nordigen.com/en/account_information_documenation/integration/quickstart_guide/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Connect to bank accounts using official bank APIs and get raw transaction data
graphqls:
- description: This is a conceptual GraphQL schema for the GoCardless Bank Account Data API (formerly Nordigen). It models the open banking REST API that enables access to EU bank account data under PSD2 regulation.
  name: GoCardless (Nordigen) GraphQL Schema
  slug: nordigen-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nordigen.png
layout: provider
modified: '2026-05-28'
name: Nordigen
nav: Providers
network: true
overview: Nordigen publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance and Public APIs.
random_paper: 14
security:
- kind: domain-security
  name: Nordigen Domain Security
  slug: nordigen-domain-security
  summary_line: DMARC
slug: nordigen
tags:
- Finance
- Public APIs
website: https://nordigen.com/en/account_information_documenation/integration/quickstart_guide/
---
