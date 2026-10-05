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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Beato provides payment workflow automation APIs.
  name: Beato API
  slug: beato-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beato/refs/heads/main/hosts/beato-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beato-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beato/refs/heads/main/vendors/beato-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beato-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beato/refs/heads/main/security/beato-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beato-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/beato
coverage:
  checked: '2026-09-27'
  detail: beato.com returns a bot challenge page with no machine‑readable API spec.
  evidence:
  - status: 202
    url: https://beato.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Beato is a financial technology company that provides a platform for managing and automating payment workflows. The company focuses on simplifying transaction processing for businesses, offering tools for invoicing, recurring payments, and integration with various banking services. As a stub entry in the API Evangelist network, Beato’s profile is being expanded to include detailed API documentation and operational metadata as part of the enrichment pipeline.
layout: provider
modified: '2026-09-27'
name: Beato
nav: Providers
network: true
overview: Beato publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Automation, and Software-as-a-Service.
random_paper: 17
score:
  band: minimal
  composite: 3.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 5.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beato Domain Security
  slug: beato-domain-security
  summary_line: TLSv1.3 · DMARC
slug: beato
tags:
- Company
- Fintech
- Payments
- Automation
- Software-as-a-Service
website: https://equityzen.com/company/beato
---
