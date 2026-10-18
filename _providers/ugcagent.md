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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The Messages API from UGC Agent — 1 operation(s) for messages.
  name: UGC Agent Messages API
  slug: ugcagent-messages-api
artifact_total: 4
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ugcagent/refs/heads/main/plans/ugcagent-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ugcagent-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ugcagent/refs/heads/main/rules/ugcagent-rules.yml
  title: ''
  type: Spectral
  url: rules/ugcagent-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ugcagent/refs/heads/main/conformance/ugcagent-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ugcagent-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ugcagent/refs/heads/main/llms/ugcagent-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ugcagent-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ugcagent/refs/heads/main/hosts/ugcagent-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ugcagent-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ugcagent/refs/heads/main/vendors/ugcagent-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ugcagent-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ugcagent.app/developers/api/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ugcagent/refs/heads/main/security/ugcagent-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ugcagent-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ugcagent.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ugcagent.app/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ugcagent.app/
- group: commercial
  title: ''
  type: Pricing
  url: https://ugcagent.app/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ugcagent.app/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ugcagent.app/privacy/
- group: company
  title: ''
  type: Blog
  url: https://ugcagent.app/blog/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://ugcagent.app/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: UGC Agent provides a data hub for user‑generated content (UGC) marketing, offering a searchable database of over 28,000 creators with contact details, tools for creator tracking, automated sourcing, and integration with AI agents. Brands can discover, engage, and manage creators across industries, leveraging features like super‑search, CRM, and payout tracking, all via a developer API for programmatic access.
image: https://ugcagent.app/og-image.png
layout: provider
modified: '2026-10-12'
name: UGC Agent
nav: Providers
network: true
overview: 'UGC Agent is listed with 1 API on the [APIs.io](https://apis.io/) network: Messages API. Tagged areas include Company, UGC, Marketing, Data, and Creators.


  The UGC Agent catalog on APIs.io includes 1 Spectral governance ruleset.


  UGC Agent''s developer surface includes documentation, API reference, pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Ugcagent Plans Pricing
  plan_count: 4
  slug: ugcagent-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: UGC Agent API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: ugcagent-rules
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 48.5
    catalog_earned_first_party: 12.0
    catalog_gap: 66.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 9.4
    developer_ergonomics: 28.6
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Ugcagent Domain Security
  slug: ugcagent-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ugcagent
tags:
- Company
- UGC
- Marketing
- Data
- Creators
website: https://ugcagent.app/
---
