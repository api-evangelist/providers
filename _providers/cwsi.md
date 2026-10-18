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
  href: https://raw.githubusercontent.com/api-evangelist/cwsi/refs/heads/main/llms/cwsi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cwsi-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cwsi/refs/heads/main/hosts/cwsi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cwsi-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cwsi/refs/heads/main/vendors/cwsi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cwsi-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cwsisecurity.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cwsisecurity.com/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cwsi/refs/heads/main/security/cwsi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cwsi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cwsisecurity.com/
coverage:
  checked: '2026-10-12'
  detail: The provider's website and API hosts return 404 for common OpenAPI paths and no machine‑readable spec was found.
  evidence:
  - status: 404
    url: https://cwsisecurity.com/openapi.json
  - status: 404
    url: https://api.cwsisecurity.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: CWSI is a security and compliance partner helping organisations across the UK, Ireland, the Netherlands, Belgium and Luxembourg embrace new technologies with confidence. They provide services in secure AI, data, endpoints, identity and operations, offering assessments, workshops and managed security. Founded in Dublin in 2010, CWSI has grown into a leading Microsoft‑focused security partner.
image: https://cwsisecurity.com/wp-content/uploads/2026/03/cwsi-security-made-human-1.jpg
layout: provider
modified: '2026-10-12'
name: CWSI
nav: Providers
network: true
overview: CWSI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Compliance, Cybersecurity, Enterprise, and United Kingdom.
random_paper: 20
score:
  band: minimal
  composite: 9.6
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
    developer_ergonomics: 0.0
    discoverability: 55.4
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
  name: Cwsi Domain Security
  slug: cwsi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cwsi
tags:
- Security
- Compliance
- Cybersecurity
- Enterprise
- United Kingdom
website: https://cwsisecurity.com/
---
