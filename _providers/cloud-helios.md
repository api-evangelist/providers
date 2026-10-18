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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloud-helios/refs/heads/main/hosts/cloud-helios-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloud-helios-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloud-helios/refs/heads/main/vendors/cloud-helios-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloud-helios-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloud-helios/refs/heads/main/security/cloud-helios-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloud-helios-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloud.helios.id/
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.helios.id/blog/
- group: company
  title: ''
  type: Blog
  url: https://cloud.helios.id/blog/
- group: operate
  title: ''
  type: Support
  url: https://cloud.helios.id/get-in-touch/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://helios.id/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.helios.id/privacy-policy
coverage:
  checked: '2026-10-09'
  detail: The provider's website offers HTML documentation but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications were found.
  evidence:
  - status: 200
    url: https://cloud.helios.id/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Cloud Helios provides end‑to‑end cloud adoption services, hybrid cloud solutions, and managed security for enterprises across Southeast Asia. Founded in 2016, the company helps over 250 clients modernize their IT infrastructure with generative AI, automation, data analytics, and advanced security protection. Their portfolio includes cloud migration, HPC, serverless computing, and AI‑driven workloads, backed by Microsoft partnership and certifications. Cloud Helios also offers consulting, training, and ongoing operational support to ensure continuous optimization and compliance.
image: https://cloud.helios.id/wp-content/uploads/2024/02/assisted-100-customer.png
layout: provider
modified: '2026-10-09'
name: Cloud Helios
nav: Providers
network: true
overview: 'Cloud Helios is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Identity and Access Management, IT Security, Cloud Services, Cloud Infrastructure, and Business Continuity.


  Cloud Helios'' developer surface includes documentation, engineering blog, support, and 6 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 12.2
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
    developer_ergonomics: 16.7
    discoverability: 48.2
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
  name: Cloud Helios Domain Security
  slug: cloud-helios-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cloud-helios
tags:
- Identity and Access Management
- IT Security
- Cloud Services
- Cloud Infrastructure
- Business Continuity
website: https://cloud.helios.id/
---
