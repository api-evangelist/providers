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
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/clearsense/refs/heads/main/plans/clearsense-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clearsense-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clearsense/refs/heads/main/conformance/clearsense-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clearsense-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clearsense/refs/heads/main/hosts/clearsense-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clearsense-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clearsense/refs/heads/main/vendors/clearsense-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clearsense-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://clearsense.com/resources/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clearsense/refs/heads/main/security/clearsense-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearsense-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clearsense.com
- group: docs
  title: ''
  type: Documentation
  url: https://clearsense.com/resources
- group: operate
  title: ''
  type: Support
  url: https://clearsense.com/contact
- group: company
  title: ''
  type: Blog
  url: https://clearsense.com/resources/blogs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clearsense.com/privacy-policy
coverage:
  checked: '2026-10-09'
  detail: Clearsense provides a public developer portal but no machine‑readable API specification (OpenAPI/GraphQL/AsyncAPI) is published.
  evidence:
  - status: 200
    url: https://clearsense.com/resources
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Clearsense provides an enterprise healthcare data platform that enables organizations to unify, archive, and manage large volumes of clinical and operational data. Their solutions include data archiving, managed services, and research acceleration tools, helping healthcare providers improve cost savings, revenue recovery, and data accessibility across multiple systems. The company serves hundreds of hospitals and health systems, offering cloud‑native, scalable platforms for data integration, analytics, and compliance.
image: https://clearsense.com/hubfs/clearsense_logo_t3.png
layout: provider
modified: '2026-10-08'
name: Clearsense
nav: Providers
network: true
overview: 'Clearsense is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Data Platform, Cloud, and Enterprise.


  Clearsense''s developer surface includes documentation, support, engineering blog, and 8 more developer resources.'
plans:
- name: Clearsense Plans Pricing
  plan_count: 1
  slug: clearsense-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hitrust
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clearsense Domain Security
  slug: clearsense-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clearsense
tags:
- Company
- Healthcare
- Data Platform
- Cloud
- Enterprise
website: https://clearsense.com
---
