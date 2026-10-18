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
  href: https://raw.githubusercontent.com/api-evangelist/charm-security/refs/heads/main/hosts/charm-security-hosts.yml
  title: ''
  type: Hosts
  url: hosts/charm-security-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/charm-security/refs/heads/main/vendors/charm-security-vendors.yml
  title: ''
  type: Vendors
  url: vendors/charm-security-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.charmsecurity.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.charmsecurity.com/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.charmsecurity.com/docs/developer/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://docs.charmsecurity.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/charm-security/refs/heads/main/security/charm-security-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/charm-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.charmsecurity.com/
coverage:
  checked: '2026-10-08'
  detail: Docs site https://docs.charmsecurity.com returns a JavaScript shell with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://docs.charmsecurity.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-08'
description: Charm Security provides an agentic AI workforce that combats fraud and cybercrime in real time. Leveraging its proprietary Human Vulnerabilities and Exploits (HVE) model, the platform integrates behavioral science with advanced AI to detect, investigate, and prevent scams, social engineering, and financial fraud across banking, payments, and other financial services. Its solutions include fraud investigation agents, frontline assistance agents, and intelligence‑gathering agents that operate both within an organization and at the edge of the internet, delivering actionable insights and automated remediation to protect customers and institutions.
image: https://cdn.prod.website-files.com/67b4bbb8922794ecbcd77852/67c595ac698cb349eaa9643e_Charm%20Open%20Graph.avif
layout: provider
modified: '2026-10-08'
name: Charm Security
nav: Providers
network: true
overview: 'Charm Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fraud Prevention, Artificial Intelligence, Financial Services, Cybersecurity, and Customer Interaction.


  Charm Security''s developer surface includes getting-started guide, documentation, and 6 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Charm Security Domain Security
  slug: charm-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: charm-security
tags:
- Fraud Prevention
- Artificial Intelligence
- Financial Services
- Cybersecurity
- Customer Interaction
website: https://www.charmsecurity.com/
---
