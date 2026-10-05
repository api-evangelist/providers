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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API documentation not publicly machine‑readable; no OpenAPI/AsyncAPI/GraphQL spec found.
  name: Asato API
  slug: asato-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.asato.ai/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asato/refs/heads/main/conformance/asato-conformance.yml
  title: ''
  type: Conformance
  url: conformance/asato-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/asato/refs/heads/main/llms/asato-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asato-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/asato/refs/heads/main/well-known/asato-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/asato-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asato/refs/heads/main/hosts/asato-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asato-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asato/refs/heads/main/vendors/asato-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asato-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.asato.ai/newsroom
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asato/refs/heads/main/security/asato-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/asato-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asato/refs/heads/main/security/asato-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asato-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.asato.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.asato.ai/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.asato.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.asato.ai/talk-to-sales
- group: operate
  title: ''
  type: StatusPage
  url: https://status.asato.ai/status/url
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.asato.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.asato.ai/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://www.asato.ai/security
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, or GraphQL spec could be retrieved from known API hosts.
  evidence:
  - status: failed
    url: https://api.asato.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Asato is an AI‑powered IT asset optimization platform founded in 2023. It helps enterprises discover, reconcile, and optimize their entire IT asset landscape using autonomous AI agents that continuously aggregate data from SaaS, cloud, hardware, and contracts, turning fragmented records into decision‑grade insights for CIOs. The platform aims to reduce waste, improve spend visibility, and enable strategic resource allocation across software, cloud, and AI services.
image: https://cdn.prod.website-files.com/661f8627cdc522269a1a1906/67fd24f670f933e821190df8_Screenshot%202025-04-14%20at%208.38.32%E2%80%AFPM.avif
layout: provider
modified: '2026-09-26'
name: Asato
nav: Providers
network: true
overview: 'Asato publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, IT Asset Management, Software-as-a-Service, and Cloud.


  Asato''s developer surface includes documentation, engineering blog, support, and 14 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hitrust
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Asato Domain Security
  slug: asato-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Asato Trust Center
  slug: asato-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: asato
tags:
- Company
- Artificial Intelligence
- IT Asset Management
- Software-as-a-Service
- Cloud
website: https://www.asato.ai
---
