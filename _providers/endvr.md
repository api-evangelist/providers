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
- description: ENDVR offers a developer API documented at the guides page.
  name: ENDVR API
  slug: endvr-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/endvr/refs/heads/main/plans/endvr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/endvr-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/endvr/refs/heads/main/llms/endvr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/endvr-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/endvr/refs/heads/main/hosts/endvr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/endvr-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/endvr/refs/heads/main/vendors/endvr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/endvr-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://endvr.io/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://endvr.io/legal/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/endvr/refs/heads/main/security/endvr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/endvr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.endvr.io/
- group: docs
  title: ''
  type: Documentation
  url: https://endvr.io/resources
- group: commercial
  title: ''
  type: Pricing
  url: https://endvr.io/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://endvr.io/
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the API host.
  evidence:
  - status: 404
    url: https://api.endvr.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: ENDVR provides a sell‑through enablement platform that connects brands, retailers, and frontline teams. The network powers real‑time product availability insights, digital education, sales incentives, consumer cashback, and display maintenance tools. Brands can activate stores for free, access pricing calculators, and integrate with mobile apps on iOS and Android. ENDVR aims to boost sell‑through in every door by offering data‑driven insights and collaborative tools for brand and retail teams.
layout: provider
modified: '2026-10-12'
name: ENDVR
nav: Providers
network: true
overview: 'ENDVR is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Software-as-a-Service, Sales Enablement, and Data Platform.


  ENDVR''s developer surface includes documentation, pricing, getting-started guide, and 8 more developer resources.'
plans:
- name: Endvr Plans Pricing
  plan_count: 3
  slug: endvr-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 60.7
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
  name: Endvr Domain Security
  slug: endvr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: endvr
tags:
- Company
- Retail
- Software-as-a-Service
- Sales Enablement
- Data Platform
website: https://www.endvr.io/
---
