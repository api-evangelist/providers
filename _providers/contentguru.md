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
- description: API documented on website but no machine-readable spec found.
  name: Contentguru API
  slug: contentguru-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.contentguru.com/en-us/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contentguru/refs/heads/main/hosts/contentguru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contentguru-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contentguru/refs/heads/main/vendors/contentguru-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contentguru-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.contentguru.com/en-us/legal/terms/
- group: company
  title: ''
  type: Newsroom
  url: https://www.contentguru.com/en-us/resources/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contentguru/refs/heads/main/security/contentguru-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/contentguru-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contentguru/refs/heads/main/security/contentguru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contentguru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.contentguru.com
coverage:
  checked: '2026-10-10'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found on api.contentguru.com despite probing common spec endpoints.
  evidence:
  - status: 0
    url: https://api.contentguru.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Content Guru is a global provider of cloud‑based Customer Experience (CX) solutions, founded in 2005 and serving enterprises in over 60 countries. The company offers the Storm CX platform, AI‑driven conversational tools, and integration services that help organisations improve customer satisfaction, automate processes, and leverage generative AI. Content Guru’s portfolio includes the brain® AI suite and the Storm® CX cloud, supporting industries such as finance, healthcare, utilities, and public sector. The firm emphasizes compliance, data security, and scalable cloud communications.
image: https://www.contentguru.com/en-us/wp-content/uploads/sites/10/2026/06/Homepage-v2-20260610.png
layout: provider
modified: '2026-10-10'
name: Contentguru
nav: Providers
network: true
overview: Contentguru is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Experience, Cloud, Artificial Intelligence, and Communications.
random_paper: 4
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Contentguru Domain Security
  slug: contentguru-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Contentguru Trust Center
  slug: contentguru-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, FedRAMP
slug: contentguru
tags:
- Company
- Customer Experience
- Cloud
- Artificial Intelligence
- Communications
website: https://www.contentguru.com
---
