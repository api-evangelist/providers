---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
api_count: 4
apis:
- description: Client-library operations for managing 128-byte double-entry accounts - create_accounts (establish immutable accounts on a ledger with debit/credit constraint flags), lookup_accounts (fetch accounts b
  name: TigerBeetle Accounts API
  slug: tigerbeetle-accounts-api
- description: Client-library operations for moving funds between accounts as immutable 128-byte double-entry transfers - create_transfers (single-phase, plus two-phase pending / post-pending / void-pending transfer
  name: TigerBeetle Transfers API
  slug: tigerbeetle-transfers-api
- description: The get_account_balances operation returns the historical balances of an account over time (for accounts created with the history flag), each a point-in-time AccountBalance record of pending and poste
  name: TigerBeetle Account Balances API
  slug: tigerbeetle-account-balances-api
- description: 'Query surface for retrieving the transfers and balances tied to a single account. The get_account_transfers operation takes an AccountFilter (account_id, timestamp range, limit, direction, and flags) '
  name: TigerBeetle Account Filter Queries API
  slug: tigerbeetle-account-filter-queries-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tigerbeetle-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tigerbeetle
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tigerbeetle
- group: company
  title: ''
  type: Website
  url: https://tigerbeetle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tigerbeetle.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/tigerbeetle-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tigerbeetle-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://tigerbeetle.com/blog/atom.xml
created: '2026-07-02'
description: TigerBeetle is an open-source (Apache 2.0) distributed financial accounting and transactions database, purpose-built for high-throughput, mission-critical double-entry bookkeeping and online transaction processing (OLTP). It is NOT an HTTP/REST API and ships no OpenAPI - the database is accessed over a custom binary wire protocol on TCP (default port 3000) via official client libraries for .NET, Go, Java, Node.js, Python, Ruby, and Rust. The "API" is the set of client operations - create_accounts, create_transfers, lookup_accounts, lookup_transfers, get_account_transfers, get_account_balances, query_accounts, and query_transfers - that use fixed-size, cache-line-aligned structs for zero-deserialization performance. TigerBeetle is self-hostable; a fully managed service is also offered to select enterprise partners via sales@tigerbeetle.com.
finops:
- name: Tigerbeetle Finops
  service_category: Databases
  slug: tigerbeetle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tigerbeetle.png
layout: provider
modified: '2026-07-02'
name: TigerBeetle
nav: Providers
network: true
overview: 'TigerBeetle publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial, Accounting, Transaction, Database, and Double-Entry.


  TigerBeetle''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Tigerbeetle Plans Pricing
  plan_count: 2
  slug: tigerbeetle-plans-pricing
random_paper: 9
screenshot: https://raw.githubusercontent.com/api-evangelist/tigerbeetle/refs/heads/main/screenshots/tigerbeetle-2026-09-02T163740.png
security:
- kind: domain-security
  name: Tigerbeetle Domain Security
  slug: tigerbeetle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tigerbeetle
tags:
- Financial
- Accounting
- Transaction
- Database
- Double-Entry
- Ledger
- OLTP
- Distributed
- Open-Source
- Binary Protocol
website: https://tigerbeetle.com/
---
