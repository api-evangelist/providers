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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.centari.com/security
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/centari/refs/heads/main/well-known/centari-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/centari-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/centari/refs/heads/main/hosts/centari-hosts.yml
  title: ''
  type: Hosts
  url: hosts/centari-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/centari/refs/heads/main/vendors/centari-vendors.yml
  title: ''
  type: Vendors
  url: vendors/centari-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.centari.com/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centari/refs/heads/main/security/centari-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/centari-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centari/refs/heads/main/security/centari-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centari-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://centari.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.centari.com/
- group: company
  title: ''
  type: Blog
  url: https://www.centari.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.centari.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.centari.com/terms-of-use
coverage:
  checked: '2026-10-16'
  detail: The public website provides no machine‑readable API specification and no developer documentation link was found.
  evidence:
  - status: 200
    url: https://www.centari.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: Centari provides AI‑powered deal intelligence for law firms and investment funds, transforming complex transaction documents into structured, actionable data. Their platform offers insights, negotiation context, and risk indicators, supporting both legal and finance professionals to win deals with precision and efficiency. Centari’s solutions include document analysis, data extraction, and a proprietary deal database, all delivered via a secure, cloud‑based service.
image: https://cdn.prod.website-files.com/69c2738f5707e91ebaae20c2/69d6803221afc95d1f04d6d2_6ebe03d5b94f44f047652910690c1678_logo-light%202.jpg
layout: provider
modified: '2026-10-16'
name: Centari
nav: Providers
network: true
overview: 'Centari is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Deal-Intelligence, Legal-Tech, and Finance.


  Centari''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Centari Domain Security
  slug: centari-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Centari Trust Center
  slug: centari-trust-center
  summary_line: SOC 2, ISO 27001
slug: centari
tags:
- Company
- Artificial Intelligence
- Deal-Intelligence
- Legal-Tech
- Finance
website: https://centari.com/
---
