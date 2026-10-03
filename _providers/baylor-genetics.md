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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/baylor-genetics/refs/heads/main/conformance/baylor-genetics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/baylor-genetics-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/baylor-genetics/refs/heads/main/hosts/baylor-genetics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/baylor-genetics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/baylor-genetics/refs/heads/main/vendors/baylor-genetics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/baylor-genetics-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.baylorgenetics.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.baylorgenetics.com/privacy-notice/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.baylorgenetics.com/plans/
- group: company
  title: ''
  type: Newsroom
  url: https://www.baylorgenetics.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/baylor-genetics/refs/heads/main/security/baylor-genetics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/baylor-genetics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.baylorgenetics.com
- group: company
  title: ''
  type: Blog
  url: https://www.baylorgenetics.com/blog
- group: company
  title: ''
  type: About
  url: https://www.baylorgenetics.com/about
coverage:
  checked: '2026-09-27'
  detail: The public website provides no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract despite extensive documentation pages.
  evidence:
  - status: 200
    url: https://www.baylorgenetics.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Baylor Genetics provides precision diagnostic testing and genomic sequencing services, leveraging nearly 50 years of experience in clinical genomics. The company offers whole genome, exome, RNA sequencing, and specialized assays, supporting clinicians with actionable insights and comprehensive reports. It serves healthcare providers, researchers, and patients worldwide, emphasizing innovation and data-driven care.
layout: provider
modified: '2026-09-27'
name: Baylor Genetics
nav: Providers
network: true
overview: 'Baylor Genetics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Genetic Testing, Whole Genome Sequencing, Precision Diagnostics, and Clinical Genomics.


  Baylor Genetics'' developer surface includes pricing, engineering blog, and 9 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 37.5
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Baylor Genetics Domain Security
  slug: baylor-genetics-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: baylor-genetics
tags:
- Genetic Testing
- Whole Genome Sequencing
- Precision Diagnostics
- Clinical Genomics
website: https://www.baylorgenetics.com
---
