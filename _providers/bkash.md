---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: Merchant payment API for accepting bKash payments — create, execute, query and refund tokenized payments; grant/refresh token auth.
  name: bKash Tokenized Checkout API
  slug: bkash-tokenized-checkout-api
artifact_total: 7
asyncapis:
- description: ''
  name: Bkash Webhooks
  slug: bkash-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.bkash.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bka.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bka.sh/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bKash-developer
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bkash/refs/heads/main/llms/bkash-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bkash-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bkash/refs/heads/main/security/bkash-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bkash-domain-security.yml
created: '2026-09-16'
description: bKash is Bangladesh's leading mobile financial services (MFS) provider, offering send money, payments, cash-out and a tokenized checkout API for merchants to accept bKash payments. The Payment Gateway (PGW) exposes token management, checkout and tokenized checkout, refunds and B2C instant payout over a REST/JSON interface. Backed by BRAC Bank and Ant Group.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: Candidate MCP server tool surface derived from bKash Payment Gateway documented operations. bKash publishes no official hosted/remote MCP server; this is a starting point (not authoritative), one tool
  name: bKash MCP Server
  slug: bkash-mcp-server
modified: '2026-09-16'
name: bKash
nav: Providers
network: true
overview: 'bKash publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Mobile Financial Services, Fintech, Checkout, and Bangladesh.


  The bKash catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  bKash''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Bkash Plans Pricing
  plan_count: 0
  slug: bkash-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Bkash Rate Limits
  slug: bkash-rate-limits
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 32.1
    discoverability: 75.9
    operational_transparency: 47.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 32.7
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/bkash/refs/heads/main/screenshots/bkash-2026-07-25T203226.png
security:
- kind: authentication
  name: Bkash Authentication
  slug: bkash-authentication
  summary_line: token/apiKey · 2 schemes
- kind: domain-security
  name: Bkash Domain Security
  slug: bkash-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bkash
tags:
- Payments
- Mobile Financial Services
- Fintech
- Checkout
- Bangladesh
- Digital Wallet
- Payment Gateway
website: https://www.bkash.com
---
