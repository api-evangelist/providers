---
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/menloinsurance/refs/heads/main/llms/menloinsurance-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/menloinsurance-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/menloinsurance/refs/heads/main/well-known/menloinsurance-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/menloinsurance-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/menloinsurance/refs/heads/main/hosts/menloinsurance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/menloinsurance-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/menloinsurance/refs/heads/main/vendors/menloinsurance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/menloinsurance-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.menloinsurance.com/support
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/menloinsurance/refs/heads/main/security/menloinsurance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/menloinsurance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.menloinsurance.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.menloinsurance.com/ai-assistants
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.menloinsurance.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.menloinsurance.com/privacy
coverage:
  checked: '2026-10-05'
  detail: MCP endpoint returns 405 indicating JSON-RPC requires POST, no public API.
  evidence:
  - status: 405
    url: https://www.menloinsurance.com/mcp
  reason: partner-login
  state: gated
created: '2026-10-05'
description: Menlo Insurance Services is an independent insurance brokerage offering a range of commercial and personal insurance products. They provide quote services for various coverages such as property, flood, workers' compensation, liability, and specialty lines, acting as a broker to compare carriers and find suitable policies for businesses and individuals.
layout: provider
modified: '2026-10-05'
name: Menlo Insurance Services
nav: Providers
network: true
overview: 'Menlo Insurance Services is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Brokerage, Commercial, Personal, and Quotes.


  Menlo Insurance Services'' developer surface includes support, documentation, and 8 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 17.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Menloinsurance Domain Security
  slug: menloinsurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: menloinsurance
tags:
- Insurance
- Brokerage
- Commercial
- Personal
- Quotes
website: https://www.menloinsurance.com
---
