---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.4
  scored_at: '2026-09-20'
api_count: 1
apis:
- description: 'Pay-per-search web agent (version 0.1.0-alpha) served from a2a-browser.digiant.nz: a JSON-RPC 2.0 POST endpoint at the host root, an A2A agent card at the legacy /.well-known/agent.json path (the cano'
  name: a2a-browser A2A Agent
  slug: a2a-browser-agent
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://digiant.nz/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/digiantnz
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/digiant-nz/refs/heads/main/well-known/digiant-nz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/digiant-nz-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/digiant-nz/refs/heads/main/llms/digiant-nz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/digiant-nz-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/digiant-nz/refs/heads/main/packages/digiant-nz-packages.yml
  title: ''
  type: Packages
  url: packages/digiant-nz-packages.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/digiant-nz/refs/heads/main/regulatory/digiant-nz-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/digiant-nz-regulatory-posture.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/digiant-nz/refs/heads/main/security/digiant-nz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digiant-nz-domain-security.yml
created: '2026-09-19'
description: digiantnz is a Christchurch, New Zealand operator that runs a2a-browser, a self-hosted, account-less, pay-per-query web retrieval agent published as an A2A 0.3 agent card at a2a-browser.digiant.nz. The agent exposes two skills over a JSON-RPC 2.0 endpoint — Web Search (SERP query with LLM synthesis and entity extraction) and Page Fetch (Playwright-rendered fetch with a 50k-character cap) — identifies callers by an Ed25519 public key instead of a signup, runs a free FIFO tier at 10 requests/hour, and quotes a paid tier live in satoshis (10 per search, 20 per fetch, 1,000 minimum, Lightning) that the card still marks alpha. No OpenAPI, documentation site, MCP server or SDK is published; the registrable domain digiant.nz redirects to a Web3 name (digiant.crypto) that public DNS does not resolve.
layout: provider
modified: '2026-09-19'
name: digiantnz
nav: Providers
network: true
overview: digiantnz publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, A2A, Agents, Web Search, and Web Scraping.
plans:
- name: Digiant Nz Plans Pricing
  plan_count: 2
  slug: digiant-nz-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Digiant Nz Rate Limits
  slug: digiant-nz-rate-limits
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 51.0
    catalog_earned_first_party: 16.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 18.0
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    operational_transparency: 26.3
  previous_composite: 2.8
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Digiant Nz Authentication
  slug: digiant-nz-authentication
  summary_line: public-key-identity · 2 schemes
- kind: domain-security
  name: Digiant Nz Domain Security
  slug: digiant-nz-domain-security
  summary_line: TLSv1.3
slug: digiant-nz
tags:
- Company
- A2A
- Agents
- Web Search
- Web Scraping
- Search
- Micropayments
- Lightning
- New Zealand
website: https://digiant.nz/
---
