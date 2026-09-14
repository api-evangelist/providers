---
api_count: 1
apis:
- description: Find missing values, invalid types, out-of-range values, duplicate identifiers and CSV formula risks in one HTTP request. Results include record and column references and optional valid rows.
  name: RowGuard CSV Validation API
  slug: rowguard-csv-validation-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rowguard-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rowguard-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rowguard-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://rowguard-api.rowguard-api.workers.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://documenter.getpostman.com/view/58184962/2sBYAytUGg
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/dark-shadow-744867/rowguard-csv-validation-api/overview
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Frere527/rowguard-api-examples
- group: commercial
  title: ''
  type: Pricing
  url: https://rapidapi.com/Frere527/api/rowguard-csv-validation1
- group: operate
  title: ''
  type: RateLimits
  url: https://rapidapi.com/Frere527/api/rowguard-csv-validation1
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rapidapi.com/terms
- group: auth
  title: ''
  type: Security
  url: https://rowguard-api.rowguard-api.workers.dev/security
- group: start
  title: ''
  type: APIOnboarding
  url: https://rowguard-api.rowguard-api.workers.dev/.well-known/api-onboarding
- group: other
  title: ''
  type: APICatalog
  url: https://rowguard-api.rowguard-api.workers.dev/.well-known/api-catalog
- group: agent
  title: ''
  type: LLMsTxt
  url: https://rowguard-api.rowguard-api.workers.dev/llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rowguard-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/rowguard-security.txt
created: '2026-09-12'
description: RowGuard validates UTF-8 CSV data against a caller-supplied column schema before it is imported into a database or automation workflow. In one HTTP request it reports missing values, type and format errors, out-of-range numbers, disallowed values, duplicate identifiers, and spreadsheet-formula (CSV injection) risks, returning record- and column-level references and optionally the rows that passed. It stores no files and calls no AI model, and is distributed through the RapidAPI marketplace.
layout: provider
mcp_servers:
- description: ''
  name: RowGuard API Catalog MCP Server
  slug: rowguard-api-catalog-mcp-server
modified: '2026-09-13'
name: RowGuard API Catalog
nav: Providers
network: true
overview: 'RowGuard API Catalog publishes 1 API on the [APIs.io](https://apis.io/) network: RowGuard CSV Validation API. Tagged areas include CSV, validation, data quality, imports, and automation.


  RowGuard API Catalog''s developer surface includes authentication, documentation, pricing, and 13 more developer resources.'
plans:
- name: Rowguard Plans Pricing
  plan_count: 4
  slug: rowguard-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 9
  name: Rowguard Rate Limits
  slug: rowguard-rate-limits
security:
- kind: authentication
  name: Rowguard Authentication
  slug: rowguard-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rowguard Domain Security
  slug: rowguard-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Rowguard Vulnerability Disclosure
  slug: rowguard-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: rowguard
tags:
- CSV
- validation
- data quality
- imports
- automation
website: https://rowguard-api.rowguard-api.workers.dev/
---
