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
  name: Federal Communications Commission Agentic Access
  operation_count: 4
  slug: federal-communications-commission-agentic-access
  summary_line: 4 operations
api_count: 2
apis:
- baseURL: https://publicapi.fcc.gov/ecfs
  baseurl_source: declared
  description: Dataset catalog and resources
  name: Federal Communications Commission Datasets API
  slug: federal-communications-commission-datasets-api
- baseURL: https://publicapi.fcc.gov/ecfs
  baseurl_source: declared
  description: The Filings API from Federal Communications Commission — 1 operation(s) for filings.
  name: Federal Communications Commission Filings API
  slug: federal-communications-commission-filings-api
- baseURL: https://publicapi.fcc.gov/ecfs
  baseurl_source: declared
  description: Pirate Radio Broadcasting Database
  name: Federal Communications Commission Pirate Radio API
  slug: federal-communications-commission-pirate-radio-api
- baseURL: https://publicapi.fcc.gov/ecfs
  baseurl_source: declared
  description: The Proceedings API from Federal Communications Commission — 1 operation(s) for proceedings.
  name: Federal Communications Commission Proceedings API
  slug: federal-communications-commission-proceedings-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FCC ECFS API
  slug: open-ecfs
- collection_type: open
  name: FCC ECFS Datasets API
  slug: open-federal-communications-commission-datasets-api
- collection_type: open
  name: FCC ECFS Datasets Filings API
  slug: open-federal-communications-commission-filings-api
- collection_type: open
  name: FCC ECFS Datasets Pirate Radio API
  slug: open-federal-communications-commission-pirate-radio-api
- collection_type: open
  name: FCC ECFS Datasets Proceedings API
  slug: open-federal-communications-commission-proceedings-api
- collection_type: open
  name: FCC Open Data API
  slug: open-opendata
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/federal-communications-commission-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-communications-commission-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/federal-communications-commission-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fcc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/federal-communications-commission
- group: company
  title: ''
  type: Website
  url: https://www.fcc.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fcc.gov/reports-research/developers
created: '2024-12-03'
description: The Federal Communications Commission (FCC) regulates interstate and international communications by radio, television, wire, satellite, and cable in the United States. The FCC exposes public APIs including the Electronic Comment Filing System (ECFS) and the FCC Open Data portal.
finops:
- name: Federal Communications Commission Finops
  service_category: API
  slug: federal-communications-commission-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-communications-commission.png
layout: provider
modified: '2026-05-19'
name: Federal Communications Commission
nav: Providers
network: true
overview: 'Federal Communications Commission publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Datasets API, Filings API, Pirate Radio API, and 1 more. Tagged areas include Communications, Federal-Government, and Open Data.


  The Federal Communications Commission catalog on APIs.io includes 2 Spectral governance rulesets.


  Federal Communications Commission''s developer surface includes authentication, documentation, and 5 more developer resources.'
plans:
- name: Federal Communications Commission Plans Pricing
  plan_count: 3
  slug: federal-communications-commission-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Federal Communications Commission Rate Limits
  slug: federal-communications-commission-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Federal Communications Commission API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: ecfs-rules
- effective_rule_count: 0
  extends: []
  name: Federal Communications Commission API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: opendata-rules
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-communications-commission/refs/heads/main/screenshots/federal-communications-commission-2026-06-20T181114.png
security:
- kind: authentication
  name: Federal Communications Commission Authentication
  slug: federal-communications-commission-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Federal Communications Commission Domain Security
  slug: federal-communications-commission-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: federal-communications-commission
tags:
- Communications
- Federal-Government
- Open Data
website: https://www.fcc.gov/
---
