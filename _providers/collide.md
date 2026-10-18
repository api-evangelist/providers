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
- description: Collide provides AI software for oil & gas; documentation at https://collide.io/guides/ai-in-oil-and-gas
  name: Collide API
  slug: collide-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/collide/refs/heads/main/llms/collide-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/collide-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/collide/refs/heads/main/hosts/collide-hosts.yml
  title: ''
  type: Hosts
  url: hosts/collide-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.collide.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://collide.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://collide.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://collide.io/podcasts/bde/price-on-natural-gas-ev-battery-shortage-elon-musk-twitter-bde-april-19th-2022
- group: docs
  title: ''
  type: Documentation
  url: https://collide.io/guides/ai-in-oil-and-gas
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/collide/refs/heads/main/security/collide-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/collide-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://collide.io/
coverage:
  checked: '2026-10-09'
  detail: API documentation pages return HTML shells and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://dashboard.collide.io/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: Collide provides an AI‑native operations system for the oil and gas sector. The platform connects structured data, documents, legacy applications and institutional knowledge to enable operators, midstream companies and oilfield service providers to find answers, make decisions and automate critical workflows such as regulatory filings and well‑status reporting. It is built for energy professionals who need to extract and use information from PDFs, spreadsheets and other unstructured sources.
image: https://collide.io/og-image.png
layout: provider
modified: '2026-10-09'
name: Collide
nav: Providers
network: true
overview: 'Collide is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Oil and Gas, Energy Software, AI Operations, and Regulatory Filings.


  Collide''s developer surface includes pricing, documentation, and 7 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 15.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Collide Domain Security
  slug: collide-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: collide
tags:
- Oil and Gas
- Energy Software
- AI Operations
- Regulatory Filings
website: https://collide.io/
---
