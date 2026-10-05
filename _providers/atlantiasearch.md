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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API for Atlantiasearch platform, providing market research data and insights.
  name: Atlantiasearch API
  slug: atlantiasearch-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atlantiasearch/refs/heads/main/llms/atlantiasearch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atlantiasearch-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atlantiasearch/refs/heads/main/hosts/atlantiasearch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlantiasearch-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atlantiasearch/refs/heads/main/vendors/atlantiasearch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atlantiasearch-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atlantia.ai/es/glossary/privacy_analytics
- group: commercial
  title: ''
  type: Pricing
  url: https://www.atlantia.ai/es/glossary/pricing_research
- group: docs
  title: ''
  type: Documentation
  url: https://www.atlantia.ai/es/guides
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlantiasearch/refs/heads/main/security/atlantiasearch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlantiasearch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atlantia.ai
coverage:
  checked: 2026-09-26
  detail: Guides page redirects and renders via JavaScript, preventing retrieval of a machine‑readable OpenAPI spec.
  evidence:
  - status: 307
    url: https://www.atlantia.ai/es/guides
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Atlantiasearch, operating under the brand Atlantia, provides an AI‑powered market research platform that automates consumer insights, product testing, and data analysis. The service helps brands make faster, data‑driven decisions by delivering automated studies, concept tests, and reporting in minutes rather than weeks. It serves teams across the Americas, offering tools for market research, shopper insights, and product innovation, with a focus on AI and large‑scale data processing.
image: https://www.atlantia.ai/assets/atlantia-vertical.png
layout: provider
modified: '2026-09-26'
name: Atlantiasearch
nav: Providers
network: true
overview: 'Atlantiasearch publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Market Research, Consumer Insights, Data Analytics, and Software-as-a-Service.


  Atlantiasearch''s developer surface includes pricing, documentation, and 6 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atlantiasearch Domain Security
  slug: atlantiasearch-domain-security
  summary_line: TLSv1.3 · HSTS
slug: atlantiasearch
tags:
- Artificial Intelligence
- Market Research
- Consumer Insights
- Data Analytics
- Software-as-a-Service
- Platform
website: https://www.atlantia.ai
---
