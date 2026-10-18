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
  href: https://raw.githubusercontent.com/api-evangelist/sphera/refs/heads/main/llms/sphera-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sphera-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sphera/refs/heads/main/hosts/sphera-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sphera-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sphera/refs/heads/main/vendors/sphera-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sphera-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sphera.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sphera.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://sphera.com/company/news/
- group: other
  title: ''
  type: Leadership
  url: https://sphera.com/company/leadership/
- group: company
  title: ''
  type: Blog
  url: https://sphera.com/resources/blog/psa-for-csrd-and-portfolio-strategy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sphera/refs/heads/main/security/sphera-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sphera-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sphera.com
- group: docs
  title: ''
  type: Documentation
  url: https://sphera.com/resources
- group: other
  title: ''
  type: Image
  url: https://sphera.com/wp-content/uploads/2023/11/Logo-2.png
coverage:
  checked: '2026-10-13'
  detail: Sphera's developer documentation is not publicly available; attempts to locate OpenAPI specs on api.sphera.com returned no response.
  evidence:
  - status: no-response
    url: https://api.sphera.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Sphera is a leading provider of integrated sustainability, safety, and risk management solutions. The company offers software, data, and consulting services focused on Environment, Health, Safety & Sustainability (EHS&S), Process Safety, and Product Stewardship. Its platform unifies risk, safety, and sustainability insights to help enterprises turn uncertainty into opportunity, supporting regulatory compliance, operational risk management, and sustainability reporting across multiple industries.
image: https://sphera.com/wp-content/uploads/2024/03/132-A-Quick-Guide-to-Spheras-2023.1-LCA-Databases-Update_1440.webp
layout: provider
modified: '2026-10-13'
name: Sphera
nav: Providers
network: true
overview: 'Sphera is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sustainability, Risk Management, Software, and Consulting.


  Sphera''s developer surface includes engineering blog, documentation, and 10 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 58.9
    operational_transparency: 0.0
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
  name: Sphera Domain Security
  slug: sphera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sphera
tags:
- Company
- Sustainability
- Risk Management
- Software
- Consulting
website: https://sphera.com
---
