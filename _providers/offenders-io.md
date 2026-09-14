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
- acting_count: 0
  human_in_the_loop: 0
  name: Offenders Io Agentic Access
  operation_count: 1
  slug: offenders-io-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.offenders.io
  baseurl_source: declared
  description: The Search API from Offenders.io — 1 operation(s) for search.
  name: Offenders.io Search API
  slug: offenders-io-search-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Offenders.io Search API
  slug: open-offenders-io-search-api
- collection_type: open
  name: Offenders.io API
  slug: open-offenders-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/offenders-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/offenders-io-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/offenders-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/offenders-io-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://offenders.io/
- group: agent
  title: ''
  type: LlmsText
  url: https://offenders.io/llms.txt
created: '2024-11-13'
description: Offenders.io is a technology company that specializes in providing innovative solutions for managing and monitoring offender populations. Their platform utilizes advanced data analytics and artificial intelligence to track and analyze the behavior of individuals who have been convicted of crimes. Offenders.io operates an industry-leading database of National Registered Sex Offenders for the United States, offering criteria-based search, facial recognition, and batch processing.
finops:
- name: Offenders Io Finops
  service_category: API
  slug: offenders-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/offenders-io.png
layout: provider
modified: '2026-05-19'
name: Offenders.io
nav: Providers
network: true
overview: 'Offenders.io publishes 1 API on the [APIs.io](https://apis.io/) network: Search API. Tagged areas include Sex Offenders, Public Safety, and Criminal Records.


  Offenders.io''s developer surface includes authentication and 5 more developer resources.'
plans:
- name: Offenders Io Plans Pricing
  plan_count: 3
  slug: offenders-io-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Offenders Io Rate Limits
  slug: offenders-io-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/offenders-io/refs/heads/main/screenshots/offenders-io-2026-06-20T190627.png
security:
- kind: authentication
  name: Offenders Io Authentication
  slug: offenders-io-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Offenders Io Domain Security
  slug: offenders-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Offenders Io Trust Center
  slug: offenders-io-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP, GDPR
slug: offenders-io
tags:
- Sex Offenders
- Public Safety
- Criminal Records
website: https://offenders.io/
---
