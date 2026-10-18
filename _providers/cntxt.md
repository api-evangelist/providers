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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cntxt/refs/heads/main/llms/cntxt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cntxt-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cntxt/refs/heads/main/hosts/cntxt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cntxt-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cntxt/refs/heads/main/vendors/cntxt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cntxt-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.cntxt.tech/newsroom
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cntxt/refs/heads/main/security/cntxt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cntxt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cntxt.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cntxt.tech/
- group: company
  title: ''
  type: Blog
  url: https://www.cntxt.tech/insight-hub
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cntxt.tech/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cntxt.tech/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.cntxt.tech/contact
coverage:
  checked: '2026-10-16'
  detail: The provider's website https://cntxt.tech/ returns HTML but no machine‑readable API specification was found.
  evidence:
  - status: 200
    url: https://cntxt.tech/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: NBULA - AI As A Service, operating under the brand CNTXT AI, provides Arabic-first artificial intelligence and data solutions for enterprises and governments. Based in the UAE, the company offers data services to organize, label, and prepare datasets for AI, custom AI solutions tailored to complex needs, and an AI product lab developing domain-specific models. Their flagship speech‑to‑text model, Munsit, delivers highly accurate Arabic transcription across dialects. CNTXT emphasizes sovereign, in‑region hosting, compliance, and end‑to‑end AI readiness, targeting sectors such as finance, healthcare, and public services. The platform integrates data pipelines, model training, and deployment tools to accelerate AI adoption for Arabic‑language markets.
layout: provider
modified: '2026-10-16'
name: NBULA - AI As A Service
nav: Providers
network: true
overview: 'NBULA - AI As A Service is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Data, Arabic, and Enterprise.


  NBULA - AI As A Service''s developer surface includes documentation, engineering blog, support, and 8 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 12.6
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
    developer_ergonomics: 16.7
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cntxt Domain Security
  slug: cntxt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cntxt
tags:
- Company
- Artificial Intelligence
- Data
- Arabic
- Enterprise
website: https://cntxt.tech/
---
