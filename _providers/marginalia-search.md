---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Marginalia Search Agentic Access
  operation_count: 5
  slug: marginalia-search-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api2.marginalia-search.com
  baseurl_source: declared
  description: Manage named search filters (new API only).
  name: Marginalia Search Filters API
  slug: marginalia-search-filters-api
- baseURL: https://api2.marginalia-search.com
  baseurl_source: declared
  description: Search the Marginalia index.
  name: Marginalia Search Search API
  slug: marginalia-search-search-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Marginalia Search Filters API
  slug: open-marginalia-search-filters-api
- collection_type: open
  name: Marginalia Filters Search API
  slug: open-marginalia-search-search-api
- collection_type: open
  name: Marginalia Search API
  slug: open-marginalia-search
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/marginalia-search-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marginalia-search-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/marginalia-search-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://marginalia-search.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MarginaliaSearch
- group: operate
  title: ''
  type: Contact
  url: mailto:contact@marginalia-search.com
created: '2025-02-06'
description: Marginalia Search is an independent search engine focused on non-commercial content. Its API is accessible through api2.marginalia-search.com (current) and the legacy api.marginalia.nu / api.marginalia-search.com endpoints, and allows developers to perform web searches against the Marginalia index.
finops:
- name: Marginalia Search Finops
  service_category: API
  slug: marginalia-search-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/marginalia-search.png
layout: provider
modified: '2026-05-19'
name: Marginalia Search
nav: Providers
network: true
overview: 'Marginalia Search publishes 2 APIs on the [APIs.io](https://apis.io/) network: Filters API and Search API. Tagged areas include Open-Source, Search, and Web Search.


  Marginalia Search''s developer surface includes authentication and 5 more developer resources.'
plans:
- name: Marginalia Search Plans Pricing
  plan_count: 3
  slug: marginalia-search-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Marginalia Search Rate Limits
  slug: marginalia-search-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/marginalia-search/refs/heads/main/screenshots/marginalia-search-2026-06-20T184938.png
security:
- kind: authentication
  name: Marginalia Search Authentication
  slug: marginalia-search-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Marginalia Search Domain Security
  slug: marginalia-search-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: marginalia-search
tags:
- Open-Source
- Search
- Web Search
website: https://marginalia-search.com/
---
