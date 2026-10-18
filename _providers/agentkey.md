---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.7
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: Unified data API layer for AI agents, as described in the API Reference.
  name: AgentKey API
  slug: agentkey-api-2
- baseURL: https://agentkey.app
  baseurl_source: spec
  description: The Install API from AgentKey (Data API Layer) — 1 operation(s) for install.
  name: AgentKey (Data API Layer) Install API
  slug: agentkey-install-api
artifact_total: 5
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentkey/refs/heads/main/rules/agentkey-rules.yml
  title: ''
  type: Spectral
  url: rules/agentkey-rules.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentkey/refs/heads/main/authentication/agentkey-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentkey-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentkey/refs/heads/main/conformance/agentkey-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentkey-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentkey/refs/heads/main/llms/agentkey-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentkey-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agentkey/refs/heads/main/a2a/agentkey-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentkey-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentkey/refs/heads/main/well-known/agentkey-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentkey-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agentkey/refs/heads/main/hosts/agentkey-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentkey-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agentkey/refs/heads/main/vendors/agentkey-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentkey-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentkey/refs/heads/main/security/agentkey-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentkey-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentkey.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agentkey.app/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.agentkey.app/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agentkey.app/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://agentkey.app/pricing.html
- group: company
  title: ''
  type: Blog
  url: https://agentkey.app/blog
- group: operate
  title: ''
  type: Support
  url: https://docs.agentkey.app/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentkey.app/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentkey.app/privacy.html
coverage:
  checked: '2026-10-15'
  detail: The provider's documentation does not expose any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://docs.agentkey.app/api-reference/introduction
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: AgentKey (Data API Layer) provides a unified gateway that connects AI agents to a wide range of digital services, including social media, crypto, finance, e‑commerce, and more. It offers a single API key to discover, describe, and execute actions across supported agents, with built‑in capabilities like auto‑failover, subscription management, and extensive documentation. The platform aims to simplify integration for developers building intelligent agents that need to interact with diverse external systems.
image: https://agentkey.app/local-assets/site/og-cover-v3.png
layout: provider
modified: '2026-10-15'
name: AgentKey (Data API Layer)
nav: Providers
network: true
overview: 'AgentKey (Data API Layer) is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Install API, and 1 more. Tagged areas include Company, Data, Integration, Artificial Intelligence, and Automation.


  The AgentKey (Data API Layer) catalog on APIs.io includes 1 Spectral governance ruleset.


  AgentKey (Data API Layer)''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, support, and 11 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: AgentKey (Data API Layer) API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: agentkey-rules
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 12.9
    developer_ergonomics: 47.6
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Agentkey Authentication
  slug: agentkey-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentkey Domain Security
  slug: agentkey-domain-security
  summary_line: TLSv1.3
slug: agentkey
tags:
- Company
- Data
- Integration
- Artificial Intelligence
- Automation
website: https://agentkey.app/
---
