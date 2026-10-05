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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arya/refs/heads/main/hosts/arya-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arya-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arya/refs/heads/main/vendors/arya-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arya-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arya.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arya.ai/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://arya.ai/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arya/refs/heads/main/security/arya-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arya-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arya.ai/
coverage:
  checked: 2026-09-26
  detail: No OpenAPI or other machine‑readable spec found; all probe URLs on api.arya.ai returned 404.
  evidence:
  - status: 404
    url: https://api.arya.ai/openapi.json
  - status: 404
    url: https://api.arya.ai/openapi.yaml
  - status: 404
    url: https://api.arya.ai/swagger.json
  - status: 404
    url: https://api.arya.ai/v1/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Arya.ai provides enterprise‑grade AI solutions for banking, insurance and lending, offering an API platform (Apex), AI models, and tools for cash‑flow forecasting, document processing, and more. The company aims to democratize AI innovation, delivering scalable, secure APIs and an AI operating system to help businesses integrate advanced intelligence into their workflows.
image: https://cdn.prod.website-files.com/66f4fc38efdfb829fb67bd5c/68554f33b5c891a3ff03582f_HOMEPAGE.png
layout: provider
modified: '2026-09-26'
name: Arya
nav: Providers
network: true
overview: 'Arya is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Enterprise, Banking, Insurance, and Lending.


  Arya''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 8.7
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
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 11.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arya Domain Security
  slug: arya-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: arya
tags:
- Artificial Intelligence
- Enterprise
- Banking
- Insurance
- Lending
website: https://arya.ai/
---
