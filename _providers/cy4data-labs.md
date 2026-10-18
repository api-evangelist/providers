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
  href: https://raw.githubusercontent.com/api-evangelist/cy4data-labs/refs/heads/main/llms/cy4data-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cy4data-labs-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cy4data-labs/refs/heads/main/hosts/cy4data-labs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cy4data-labs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cy4data-labs/refs/heads/main/vendors/cy4data-labs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cy4data-labs-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cy4datalabs.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://www.cy4datalabs.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.cy4datalabs.com/status/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cy4datalabs.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.cy4datalabs.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cy4data-labs/refs/heads/main/security/cy4data-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cy4data-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cy4datalabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cy4datalabs.com/product/
- group: company
  title: ''
  type: About
  url: https://www.cy4datalabs.com/about/
- group: company
  title: ''
  type: Blog
  url: https://www.cy4datalabs.com/blog/
coverage:
  checked: '2026-10-12'
  detail: Access to documentation pages returns HTTP 403, indicating a sales or partner login gate.
  evidence:
  - status: 403
    url: https://www.cy4datalabs.com/contact/
  reason: sales-gate
  state: gated
created: '2026-10-12'
description: Cy4Data Labs provides atomic‑level encryption solutions, delivering quantum‑proof data security for enterprises, public sector, and telecoms. Founded by security veterans, the company focuses on protecting data itself, ensuring that even if attackers breach systems, the information remains unreadable. Their platform offers encryption, key management, and compliance tools, aiming to make data breaches effectively worthless.
image: https://cy4datalabs.com/assets/images/CY4%20Logo_Icon_Color.png
layout: provider
modified: '2026-10-12'
name: Cy4Data Labs
nav: Providers
network: true
overview: 'Cy4Data Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Encryption, Data Security, Quantum Proof, and Enterprise.


  Cy4Data Labs'' developer surface includes support, documentation, engineering blog, and 10 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 15.1
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
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: unknown
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
  name: Cy4Data Labs Domain Security
  slug: cy4data-labs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cy4data-labs
tags:
- Company
- Encryption
- Data Security
- Quantum Proof
- Enterprise
website: https://www.cy4datalabs.com/
---
