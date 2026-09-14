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
- acting_count: 1
  human_in_the_loop: 0
  name: Govinfo Agentic Access
  operation_count: 11
  slug: govinfo-agentic-access
  summary_line: 11 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.govinfo.gov
  baseurl_source: declared
  description: Discover new and updated documents based on GovInfo lastModified date/time
  name: GovInfo Collections API
  slug: govinfo-collections-api
- baseURL: https://api.govinfo.gov
  baseurl_source: declared
  description: Return content and metadata for individual packages
  name: GovInfo Packages API
  slug: govinfo-packages-api
- baseURL: https://api.govinfo.gov
  baseurl_source: declared
  description: Discover documents on GovInfo based on official publication date
  name: GovInfo Published API
  slug: govinfo-published-api
- baseURL: https://api.govinfo.gov
  baseurl_source: declared
  description: Discover relationships between documents available on GovInfo
  name: GovInfo Related API
  slug: govinfo-related-api
- baseURL: https://api.govinfo.gov
  baseurl_source: declared
  description: Discover documents on GovInfo using search queries and field operators available in the GovInfo UI
  name: GovInfo Search API
  slug: govinfo-search-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GovInfo Collections API
  slug: open-govinfo-collections-api
- collection_type: open
  name: GovInfo Collections Packages API
  slug: open-govinfo-packages-api
- collection_type: open
  name: GovInfo Collections Published API
  slug: open-govinfo-published-api
- collection_type: open
  name: GovInfo Collections Related API
  slug: open-govinfo-related-api
- collection_type: open
  name: GovInfo Collections Search API
  slug: open-govinfo-search-api
- collection_type: open
  name: GovInfo API
  slug: open-openapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.govinfo.gov/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/govinfo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/govinfo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/govinfo-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.govinfo.gov
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.govinfo.gov/developers
- group: docs
  title: ''
  type: Documentation
  url: https://api.govinfo.gov/docs/
- group: start
  title: ''
  type: Signup
  url: https://www.govinfo.gov/api-signup
- group: build
  title: ''
  type: GitHub
  url: https://github.com/usgpo/api
- group: auth
  title: ''
  type: Authentication
  url: https://api.data.gov
- group: commercial
  title: ''
  type: License
  url: https://github.com/usgpo/api/blob/master/LICENSE.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.govinfo.gov/about/policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.govinfo.gov/privacy
created: '2024-11-14'
description: The GovInfo API, provided by the U.S. Government Publishing Office (GPO), provides services for developers and webmasters to access GovInfo content and metadata, including search, packages, granules, collections, related items, and published documents.
finops:
- name: Govinfo Finops
  service_category: API
  slug: govinfo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/govinfo.png
layout: provider
modified: '2026-05-19'
name: GovInfo
nav: Providers
network: true
overview: 'GovInfo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Packages API, Published API, and 2 more. Tagged areas include Federal-Government, Government Publishing, Documents, and Open Data.


  GovInfo''s developer surface includes authentication, developer portal, documentation, signup flow, GitHub presence, and 8 more developer resources.'
plans:
- name: Govinfo Plans Pricing
  plan_count: 3
  slug: govinfo-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Govinfo Rate Limits
  slug: govinfo-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/govinfo/refs/heads/main/screenshots/govinfo-2026-06-20T182303.png
security:
- kind: authentication
  name: Govinfo Authentication
  slug: govinfo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Govinfo Domain Security
  slug: govinfo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: govinfo
tags:
- Federal-Government
- Government Publishing
- Documents
- Open Data
website: https://www.govinfo.gov/
---
