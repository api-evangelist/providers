---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Powerhq Agentic Access
  operation_count: 1
  slug: powerhq-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: GraphQL API providing retail electricity plan data and enrollment URLs.
  name: PowerHQ Plan Data API
  slug: powerhq-plan-data-api
artifact_total: 5
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/powerhq/refs/heads/main/agentic-access/powerhq-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/powerhq-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/powerhq/refs/heads/main/rules/powerhq-rules.yml
  title: ''
  type: Spectral
  url: rules/powerhq-rules.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/powerhq/refs/heads/main/sandbox/powerhq-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/powerhq-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/powerhq/refs/heads/main/authentication/powerhq-authentication.yml
  title: ''
  type: Authentication
  url: authentication/powerhq-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/powerhq/refs/heads/main/errors/powerhq-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/powerhq-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/powerhq/refs/heads/main/conformance/powerhq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/powerhq-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/powerhq/refs/heads/main/llms/powerhq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/powerhq-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/powerhq/refs/heads/main/a2a/powerhq-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/powerhq-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/powerhq/refs/heads/main/well-known/powerhq-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/powerhq-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/powerhq/refs/heads/main/hosts/powerhq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/powerhq-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/powerhq/refs/heads/main/vendors/powerhq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/powerhq-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.powerhq.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.powerhq.co/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.powerhq.co/concepts/pricing
- group: docs
  title: ''
  type: APIReference
  url: https://docs.powerhq.co/reference/types
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.powerhq.co/quickstart
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/powerhq/refs/heads/main/security/powerhq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/powerhq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.powerhq.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.powerhq.co
created: '2026-10-02'
description: PowerHQ provides infrastructure for retail electricity commerce, offering a marketplace, drop‑in storefront, and a standardized API that gives access to plan data, real‑time pricing, validation, and enrollment across deregulated markets. It serves energy providers, developers, partners, and brokers who want to list plans, integrate enrollment, or add energy shopping experiences to their sites with minimal IT effort.
layout: provider
modified: '2026-10-02'
name: PowerHQ
nav: Providers
network: true
overview: 'PowerHQ publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy Commerce, Retail Electricity, Marketplace, Energy Providers, and Developers.


  The PowerHQ catalog on APIs.io includes 1 Spectral governance ruleset.


  PowerHQ''s developer surface includes sandbox, authentication, pricing, API reference, getting-started guide, documentation, and 13 more developer resources.'
random_paper: 4
rules:
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: PowerHQ API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: powerhq-rules
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 69.6
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Powerhq Authentication
  slug: powerhq-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Powerhq Domain Security
  slug: powerhq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: powerhq
tags:
- Energy Commerce
- Retail Electricity
- Marketplace
- Energy Providers
- Developers
- Partners
- Brokers
website: https://www.powerhq.co
---
