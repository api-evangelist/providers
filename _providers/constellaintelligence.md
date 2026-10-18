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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Identity Intelligence API provides access to verified breach records and identity risk data.
  name: Identity Intelligence API
  slug: identity-intelligence-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/constellaintelligence/refs/heads/main/llms/constellaintelligence-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/constellaintelligence-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/constellaintelligence/refs/heads/main/hosts/constellaintelligence-hosts.yml
  title: ''
  type: Hosts
  url: hosts/constellaintelligence-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://constella.ai/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/constellaintelligence/refs/heads/main/security/constellaintelligence-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/constellaintelligence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://constella.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://constella.ai/data/developer-portal/
- group: docs
  title: ''
  type: Documentation
  url: https://constella.ai/data/developer-portal/
- group: docs
  title: ''
  type: APIReference
  url: https://constella.ai/data/intelligence-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://constella.ai/data/use-cases-api/
- group: operate
  title: ''
  type: Support
  url: https://constella.ai/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://constella.ai/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://constella.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://constella.ai/blog/website-privacy-policy/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://constella.ai/mcp
  - status: 200
    url: https://constella.ai
  - status: 403
    url: https://equityzen.com/company/constellaintelligence
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Constella provides identity risk intelligence and dark web monitoring through high‑velocity APIs. It aggregates verified breach data, compromised credentials, and other identity signals from surface, deep, and dark web sources. The platform offers real‑time threat data via a secure API endpoint, enabling organizations to detect account takeover, session hijacking, ransomware precursors, and other identity‑based attacks. Constella serves enterprises, fintech, law‑enforcement, and security teams with curated, de‑duplicated data, extensive coverage of over 1 trillion records, and flexible integration options for risk modeling and investigative workflows.
image: https://constella.ai/wp-content/uploads/ConstellaNewSite.png
layout: provider
modified: '2026-10-10'
name: Constellaintelligence
nav: Providers
network: true
overview: 'Constellaintelligence is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, Data, and Security.


  Constellaintelligence''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 8 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Constellaintelligence Domain Security
  slug: constellaintelligence-domain-security
  summary_line: TLSv1.3 · DMARC
slug: constellaintelligence
tags:
- Company
- Identity
- Data
- Security
website: https://constella.ai
---
