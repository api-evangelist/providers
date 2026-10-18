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
  href: https://raw.githubusercontent.com/api-evangelist/contextlogic2/refs/heads/main/hosts/contextlogic2-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contextlogic2-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contextlogic2/refs/heads/main/vendors/contextlogic2-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contextlogic2-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contextlogic2/refs/heads/main/security/contextlogic2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contextlogic2-domain-security.yml
created: '2026-10-10'
description: Contextlogic2 is a stub company entry originating from the API Evangelist secondary-market harvest. The company is associated with ContextLogic Holdings Inc., a publicly traded e‑commerce and technology firm that has undergone corporate reorganization and holds significant net operating loss assets. Public information indicates the firm operates a consumer-facing e‑commerce platform and maintains investor relations through its corporate website. Further details about its API offerings, documentation, and developer resources are not publicly accessible at this time.
layout: provider
modified: '2026-10-10'
name: Contextlogic2
nav: Providers
network: true
overview: Contextlogic2 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Technology, Publicly‑traded, and Investor‑relations.
random_paper: 7
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Contextlogic2 Domain Security
  slug: contextlogic2-domain-security
  summary_line: TLSv1.3 · DMARC
slug: contextlogic2
tags:
- Company
- E-Commerce
- Technology
- Publicly‑traded
- Investor‑relations
---
