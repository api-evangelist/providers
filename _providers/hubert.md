---
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Hubert provides an AI‑powered recruiting platform; the API reference page lists endpoints but no machine‑readable spec was found.
  name: Hubert API
  slug: hubert-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hubert/refs/heads/main/conformance/hubert-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hubert-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hubert/refs/heads/main/llms/hubert-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hubert-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hubert/refs/heads/main/well-known/hubert-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hubert-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hubert/refs/heads/main/hosts/hubert-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hubert-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hubert/refs/heads/main/vendors/hubert-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hubert-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.hubert.ai/hubert-candidate-support
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.hubert.ai/release-notes
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hubert/refs/heads/main/security/hubert-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hubert-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hubert.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.hubert.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.hubert.ai/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hubert.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hubert.ai/privacy-policy
coverage:
  checked: '2026-10-15'
  detail: API reference page exists but no OpenAPI/AsyncAPI/GraphQL spec was found after probing common spec locations.
  evidence:
  - status: 404
    url: https://api.hubert.ai/openapi.json
  - status: 404
    url: https://api.hubert.ai/openapi.yaml
  - status: 404
    url: https://api.hubert.ai/swagger.json
  - status: 404
    url: https://api.hubert.ai/v1/openapi.json
  - status: 404
    url: https://api.hubert.ai/api-docs
  - status: 404
    url: https://api.hubert.ai/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Hubert provides an AI‑powered platform that streamlines high‑volume hiring by automating candidate shortlisting, interview scheduling, and assessment. Their solution helps recruiters and hiring teams quickly identify top talent, reduce manual screening time, and improve candidate experience across industries such as social care, retail, and logistics. The platform offers integrations, pricing plans, and a candidate pledge to ensure transparent hiring practices.
image: https://res.cloudinary.com/dwa03c1lk/image/upload/v1663761850/Logos/hubert_symbol_bright_1_fi9lpu.png
layout: provider
modified: '2026-10-15'
name: Hubert
nav: Providers
network: true
overview: 'Hubert is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Hiring, Recruiting, and Automation.


  Hubert''s developer surface includes support, changelog, documentation, getting-started guide, pricing, and 8 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 64.3
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Hubert Domain Security
  slug: hubert-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hubert
tags:
- Company
- Artificial Intelligence
- Hiring
- Recruiting
- Automation
- Software-as-a-Service
website: https://hubert.ai/
---
