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
- description: Online help portal for SEEBURGER Cloud services, providing documentation and guides.
  name: SEEBURGER Cloud Help
  slug: seeburger-cloud-help
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/seeburger/refs/heads/main/llms/seeburger-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/seeburger-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seeburger/refs/heads/main/hosts/seeburger-hosts.yml
  title: ''
  type: Hosts
  url: hosts/seeburger-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.seeburger.com/legal-notice
- group: commercial
  title: ''
  type: Pricing
  url: https://blog.seeburger.com/plans-are-being-discussed-to-introduce-a-b2b-e-invoicing-mandate-in-germany/
- group: company
  title: ''
  type: Blog
  url: https://blog.seeburger.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.cloud.seeburger.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seeburger/refs/heads/main/security/seeburger-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seeburger-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.seeburger.com
coverage:
  checked: '2026-10-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on api.seeburger.com or docs host.
  evidence:
  - status: 0
    url: https://api.seeburger.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: SEEBURGER provides a comprehensive Business Integration Suite (BIS) platform that enables enterprises to integrate applications, data, and processes across cloud, on‑premise, and hybrid environments. Their solutions include managed file transfer, B2B EDI, API integration, AI‑orchestrated workflows, and industry‑specific cloud services, helping customers automate and scale digital business operations.
image: https://www.seeburger.com/fileadmin/images/social-media/social-media-default-image.png
layout: provider
modified: '2026-10-03'
name: SEEBURGER
nav: Providers
network: true
overview: 'SEEBURGER publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, Cloud, and B2B.


  SEEBURGER''s developer surface includes pricing, engineering blog, documentation, and 5 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 5
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
    discoverability: 55.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Seeburger Domain Security
  slug: seeburger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: seeburger
tags:
- Company
- Integration
- Cloud
- B2B
website: https://www.seeburger.com
---
