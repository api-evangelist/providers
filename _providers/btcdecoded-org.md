---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for querying Bitcoin intelligence data and accessing MCP tools.
  name: BTCDecoded API
  slug: btcdecoded-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://btcdecoded.org/security/
- group: agent
  href: https://artifacts.apis.io/btcdecoded-org/llms/btcdecoded-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/btcdecoded-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/btcdecoded-org/well-known/btcdecoded-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/btcdecoded-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/btcdecoded-org/hosts/btcdecoded-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/btcdecoded-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/btcdecoded-org/vendors/btcdecoded-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/btcdecoded-org-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://btcdecoded.org/security/
- group: auth
  href: https://artifacts.apis.io/btcdecoded-org/security/btcdecoded-org-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/btcdecoded-org-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/btcdecoded-org/security/btcdecoded-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/btcdecoded-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://btcdecoded.org/
- group: docs
  title: ''
  type: Documentation
  url: https://btcdecoded.org/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://btcdecoded.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://btcdecoded.org/for-agents/
- group: operate
  title: ''
  type: Support
  url: https://btcdecoded.org/support/
- group: company
  title: ''
  type: Blog
  url: https://btccommons.substack.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BTCDecoded
- group: commercial
  title: ''
  type: Pricing
  url: https://btcdecoded.org/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://btcdecoded.org/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://btcdecoded.org/privacy/
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found on the provider’s API host.
  evidence:
  - status: 0
    url: https://api.btcdecoded.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: BTCDecoded provides an open, searchable intelligence platform for Bitcoin public coordination records. It aggregates data from IRC, mailing lists, GitHub, project repositories, core announcements, podcasts, and academic papers. Users can query the index, access documentation, and explore plans, with optional Lightning payment for premium access. The service emphasizes decentralization, no KYC, and offers tools via a Model Context Protocol (MCP) for developers.
image: https://btcdecoded.org/assets/og.jpg
layout: provider
modified: '2026-11-03'
name: BTCDecoded
nav: Providers
network: true
overview: 'BTCDecoded is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Bitcoin, Intelligence, Open Source, and Decentralization.


  BTCDecoded''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 12 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 57.1
    operational_transparency: 7.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Btcdecoded Org Domain Security
  slug: btcdecoded-org-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Btcdecoded Org Trust Center
  slug: btcdecoded-org-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: btcdecoded-org
tags:
- Bitcoin
- Intelligence
- Open Source
- Decentralization
website: https://btcdecoded.org/
---
