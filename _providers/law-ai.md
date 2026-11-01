---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Law.AI MCP Server provides tools for searching lawyers, retrieving profiles, practice areas, and jurisdictions via the MCP protocol.
  name: Law.AI MCP Server
  slug: law-ai-mcp
artifact_total: 8
common:
- group: auth
  title: ''
  type: Compliance
  url: https://law.ai/security
- group: agent
  href: https://artifacts.apis.io/law-ai/llms/law-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/law-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/law-ai/hosts/law-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/law-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/law-ai/vendors/law-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/law-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://law.ai/security
- group: auth
  href: https://artifacts.apis.io/law-ai/security/law-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/law-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/law-ai/security/law-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/law-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://law.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://law.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://law.ai/developers
- group: docs
  title: ''
  type: APIReference
  url: https://law.ai/api
- group: start
  title: ''
  type: GettingStarted
  url: https://law.ai/developers
- group: operate
  title: ''
  type: Support
  url: https://support.law.ai/support/home
- group: company
  title: ''
  type: Blog
  url: https://law.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://law.ai/lawyers/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://law.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://law.ai/privacy
created: '2026-10-30'
description: Law.AI is an AI-powered lawyer directory and matching platform that helps users find trusted, bar-verified attorneys across the United States. With over 838,000 verified lawyer profiles, the service lets users search by practice area, city, and state, and provides AI-driven matching to connect clients with the most suitable legal professionals. The platform is free to use and aims to expand access to justice.
image: https://law.ai/brand-v2/social-banner-1500x500.png
layout: provider
mcp_servers:
- description: Law.AI MCP Server — Verified lawyer and attorney search, discovery, and matching for AI
  name: law-ai MCP Server
  slug: law-ai
modified: '2026-10-30'
name: law-ai
nav: Providers
network: true
overview: 'law-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include LegalTech, AI, Law, Directory, and Marketplace.


  law-ai''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Law Ai Plans Pricing
  plan_count: 0
  slug: law-ai-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Law Ai Rate Limits
  slug: law-ai-rate-limits
scopes:
- name: Law Ai Scopes
  scope_count: 0
  slug: law-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Law Ai Authentication
  slug: law-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Law Ai Domain Security
  slug: law-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Law Ai Trust Center
  slug: law-ai-trust-center
  summary_line: SOC 2, GDPR
slug: law-ai
tags:
- LegalTech
- AI
- Law
- Directory
- Marketplace
website: https://law.ai/
---
