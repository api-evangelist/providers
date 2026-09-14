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
  name: Open Fec Agentic Access
  operation_count: 15
  slug: open-fec-agentic-access
  summary_line: 15 operations
api_count: 1
apis:
- baseURL: https://api.open.fec.gov/v1
  baseurl_source: declared
  description: The Candidate API from OpenFEC — 3 operation(s) for candidate.
  name: OpenFEC Candidate API
  slug: open-fec-candidate-api
- baseURL: https://api.open.fec.gov/v1
  baseurl_source: declared
  description: The Candidates API from OpenFEC — 2 operation(s) for candidates.
  name: OpenFEC Candidates API
  slug: open-fec-candidates-api
- baseURL: https://api.open.fec.gov/v1
  baseurl_source: declared
  description: The Committee API from OpenFEC — 2 operation(s) for committee.
  name: OpenFEC Committee API
  slug: open-fec-committee-api
- baseURL: https://api.open.fec.gov/v1
  baseurl_source: declared
  description: The Committees API from OpenFEC — 1 operation(s) for committees.
  name: OpenFEC Committees API
  slug: open-fec-committees-api
- baseURL: https://api.open.fec.gov/v1
  baseurl_source: declared
  description: The Elections API from OpenFEC — 1 operation(s) for elections.
  name: OpenFEC Elections API
  slug: open-fec-elections-api
- baseURL: https://api.open.fec.gov/v1
  baseurl_source: declared
  description: The Filings API from OpenFEC — 1 operation(s) for filings.
  name: OpenFEC Filings API
  slug: open-fec-filings-api
- baseURL: https://api.open.fec.gov/v1
  baseurl_source: declared
  description: The Names API from OpenFEC — 2 operation(s) for names.
  name: OpenFEC Names API
  slug: open-fec-names-api
- baseURL: https://api.open.fec.gov/v1
  baseurl_source: declared
  description: The Schedules API from OpenFEC — 3 operation(s) for schedules.
  name: OpenFEC Schedules API
  slug: open-fec-schedules-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenFEC Candidate API
  slug: open-open-fec-candidate-api
- collection_type: open
  name: OpenFEC Candidate Candidates API
  slug: open-open-fec-candidates-api
- collection_type: open
  name: OpenFEC Candidate Committee API
  slug: open-open-fec-committee-api
- collection_type: open
  name: OpenFEC Candidate Committees API
  slug: open-open-fec-committees-api
- collection_type: open
  name: OpenFEC Candidate Elections API
  slug: open-open-fec-elections-api
- collection_type: open
  name: OpenFEC Candidate Filings API
  slug: open-open-fec-filings-api
- collection_type: open
  name: OpenFEC Candidate Names API
  slug: open-open-fec-names-api
- collection_type: open
  name: OpenFEC Candidate Schedules API
  slug: open-open-fec-schedules-api
- collection_type: open
  name: OpenFEC API
  slug: open-open-fec
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/open-fec-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/open-fec-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-fec-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/open-fec-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fecgov
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/federal-election-commission
- group: company
  title: ''
  type: Website
  url: https://www.fec.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://api.open.fec.gov/developers/
created: '2024-03-30'
description: The Federal Election Commission (FEC) API is a RESTful web service supporting full-text and field-specific searches on FEC data. Bulk downloads are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data are updated nightly.
finops:
- name: Open Fec Finops
  service_category: API
  slug: open-fec-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-fec.png
layout: provider
modified: '2026-05-19'
name: OpenFEC
nav: Providers
network: true
overview: 'OpenFEC publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Candidate API, Candidates API, Committee API, and 5 more. Tagged areas include Campaign Finance, Elections, FEC, Federal, and Government.


  OpenFEC''s developer surface includes authentication, documentation, and 6 more developer resources.'
plans:
- name: Open Fec Plans Pricing
  plan_count: 3
  slug: open-fec-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Open Fec Rate Limits
  slug: open-fec-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/open-fec/refs/heads/main/screenshots/open-fec-2026-06-20T190743.png
security:
- kind: authentication
  name: Open Fec Authentication
  slug: open-fec-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Open Fec Domain Security
  slug: open-fec-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: open-fec
tags:
- Campaign Finance
- Elections
- FEC
- Federal
- Government
website: https://www.fec.gov/
---
