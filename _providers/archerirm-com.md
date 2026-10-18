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
- description: Archer provides a regulatory change management platform with an API referenced on the pricing page.
  name: Archer API
  slug: archer-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/archerirm-com/refs/heads/main/llms/archerirm-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/archerirm-com-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/archerirm-com/refs/heads/main/hosts/archerirm-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/archerirm-com-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/archerirm-com/refs/heads/main/vendors/archerirm-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/archerirm-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.archerirm.com/company/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://community.archerirm.com/hc/en-us/p/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.archerirm.com/company/privacy-statement
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/archerirm-com/refs/heads/main/security/archerirm-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/archerirm-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.archerirm.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.archerirm.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.archerirm.com/blog
coverage:
  checked: '2026-10-14'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found at api.archerirm.com despite probing common spec endpoints.
  evidence:
  - status: no-response
    url: https://api.archerirm.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Archer provides a comprehensive regulatory change management platform, offering solutions for risk, compliance, ESG, and AI governance. Their suite includes Archer Evolv, Evolv Foundation, and RMIS AI, serving enterprises across financial services, healthcare, utilities, and more. The platform unifies policy management, audit, third‑party risk, and operational resilience, delivering real‑time insights and automated compliance workflows to help organizations mitigate risk and meet regulatory requirements.
image: https://live-archerirm-production.pantheonsite.io/wp-content/uploads/2026/08/archer-evolv-dashboard.webp
layout: provider
modified: '2026-10-13'
name: Archer
nav: Providers
network: true
overview: 'Archer is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Risk Management, Compliance, ESG, and AI Governance.


  Archer''s developer surface includes support, pricing, engineering blog, and 7 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 64.3
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
  name: Archerirm Com Domain Security
  slug: archerirm-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: archerirm-com
tags:
- Company
- Risk Management
- Compliance
- ESG
- AI Governance
- Enterprise
website: https://www.archerirm.com
---
