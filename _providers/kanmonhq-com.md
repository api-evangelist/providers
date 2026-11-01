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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/kanmonhq-com/conformance/kanmonhq-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kanmonhq-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/kanmonhq-com/llms/kanmonhq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kanmonhq-com-llms.txt
- group: other
  href: https://artifacts.apis.io/kanmonhq-com/hosts/kanmonhq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kanmonhq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/kanmonhq-com/vendors/kanmonhq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kanmonhq-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kanmon.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kanmon.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/kanmonhq-com/security/kanmonhq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kanmonhq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kanmonhq.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.kanmonhq.com
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Kanmon provides embedded working capital financing that integrates via a single API into software platforms used by business customers. The service offers term loans, revolving lines, invoice financing, buyer financing, and revenue‑based financing, with underwriting, compliance, and servicing handled by Kanmon. Platform partners earn revenue share on each dollar originated, while their customers receive capital within the product they already use.
layout: provider
modified: '2026-10-22'
name: Kanmon
nav: Providers
network: true
overview: Kanmon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Embedded financing, Working capital, API integration, Business loans, and Invoice financing.
random_paper: 1
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kanmonhq Com Domain Security
  slug: kanmonhq-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kanmonhq-com
tags:
- Embedded financing
- Working capital
- API integration
- Business loans
- Invoice financing
- Revenue-based financing
- Marketplace financing
website: https://www.kanmonhq.com
---
