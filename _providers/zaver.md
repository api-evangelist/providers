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
- description: Zaver provides a modern payments platform with APIs for accepting and managing payments.
  name: Zaver Payments API
  slug: zaver-payments-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zaver/refs/heads/main/llms/zaver-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zaver-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zaver/refs/heads/main/hosts/zaver-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zaver-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zaver/refs/heads/main/vendors/zaver-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zaver-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zaver.com/terms-and-conditions
- group: company
  title: ''
  type: Newsroom
  url: https://www.zaver.com/media
- group: start
  title: ''
  type: GettingStarted
  url: https://www.zaver.com/get-started
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zaver/refs/heads/main/security/zaver-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zaver-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zaver.com/
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on any discovered host.
  evidence:
  - status: 404
    url: https://api.zaver.com/openapi.json
  - status: 200
    url: https://app.zaver.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Zaver provides a modern payments platform that enables businesses to accept, process, and manage payments across multiple channels, including online, in‑store, and mobile. The company focuses on delivering secure, fast, and developer‑friendly APIs that integrate with existing e‑commerce and ERP systems. Zaver’s solutions include payment processing, fraud detection, recurring billing, and comprehensive reporting tools, helping merchants streamline financial operations and improve customer experience.
image: https://cdn.prod.website-files.com/667138c442ba9d555f0896e4/67041f708aa81acfb7c7bf4b_Open%20Graph%20-%20Image%201200x630.jpg
layout: provider
modified: '2026-10-15'
name: Zaver
nav: Providers
network: true
overview: 'Zaver is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Fintech, E-Commerce, Software-as-a-Service, and Company.


  Zaver''s developer surface includes getting-started guide and 7 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 8.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Zaver Domain Security
  slug: zaver-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: zaver
tags:
- Payments
- Fintech
- E-Commerce
- Software-as-a-Service
- Company
website: https://zaver.com/
---
