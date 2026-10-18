---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 26
  human_in_the_loop: 2
  name: Pickedbyagents Agentic Access
  operation_count: 42
  slug: pickedbyagents-agentic-access
  summary_line: 42 operations · 26 acting · 2 human-in-the-loop
api_count: 2
apis:
- baseURL: https://pickedbyagents.com
  baseurl_source: spec
  description: The Research Api API from Picked by Agents — 19 operation(s) for research api.
  name: Picked by Agents Research API
  slug: pickedbyagents-research-api-api
artifact_total: 6
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pickedbyagents/refs/heads/main/agentic-access/pickedbyagents-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pickedbyagents-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/pickedbyagents/refs/heads/main/plans/pickedbyagents-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pickedbyagents-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pickedbyagents/refs/heads/main/rules/pickedbyagents-rules.yml
  title: ''
  type: Spectral
  url: rules/pickedbyagents-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pickedbyagents/refs/heads/main/conformance/pickedbyagents-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pickedbyagents-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pickedbyagents/refs/heads/main/llms/pickedbyagents-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pickedbyagents-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pickedbyagents/refs/heads/main/a2a/pickedbyagents-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/pickedbyagents-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pickedbyagents/refs/heads/main/well-known/pickedbyagents-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pickedbyagents-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pickedbyagents/refs/heads/main/hosts/pickedbyagents-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pickedbyagents-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pickedbyagents/refs/heads/main/vendors/pickedbyagents-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pickedbyagents-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/gregm711/pickedbyagents-mcp
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pickedbyagents/refs/heads/main/authentication/pickedbyagents-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pickedbyagents-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pickedbyagents/refs/heads/main/security/pickedbyagents-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pickedbyagents-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pickedbyagents.com
- group: docs
  title: ''
  type: Documentation
  url: https://pickedbyagents.com/join
- group: commercial
  title: ''
  type: Pricing
  url: https://pickedbyagents.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pickedbyagents.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pickedbyagents.com/privacy
created: '2026-10-08'
description: Picked by Agents provides AI visibility monitoring for local businesses, allowing them to track whether AI assistants recommend them, who they name, and why. The service offers optional white‑glove assistance for deeper insights and helps businesses understand and improve their AI‑driven reputation.
image: https://pickedbyagents.com/opengraph-image?7e9ef0f0f43f1c4c
layout: provider
modified: '2026-10-08'
name: Picked by Agents
nav: Providers
network: true
overview: 'Picked by Agents publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Research API. Tagged areas include Company, Artificial Intelligence, Monitoring, Visibility, and Local Business.


  The Picked by Agents catalog on APIs.io includes 1 Spectral governance ruleset.


  Picked by Agents'' developer surface includes getting-started guide, authentication, documentation, pricing, and 13 more developer resources.'
plans:
- name: Pickedbyagents Plans Pricing
  plan_count: 4
  slug: pickedbyagents-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Picked by Agents API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: pickedbyagents-rules
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 48.5
    catalog_earned_first_party: 12.0
    catalog_gap: 66.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 42.9
    developer_ergonomics: 33.3
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Pickedbyagents Authentication
  slug: pickedbyagents-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pickedbyagents Domain Security
  slug: pickedbyagents-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pickedbyagents
tags:
- Company
- Artificial Intelligence
- Monitoring
- Visibility
- Local Business
website: https://pickedbyagents.com
---
