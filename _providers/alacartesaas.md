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
  href: https://raw.githubusercontent.com/api-evangelist/alacartesaas/refs/heads/main/hosts/alacartesaas-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alacartesaas-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alacartesaas/refs/heads/main/vendors/alacartesaas-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alacartesaas-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alacartesaas/refs/heads/main/security/alacartesaas-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alacartesaas-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alacartesaas.com/
- group: docs
  title: ''
  type: Documentation
  url: https://alacartesaas.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://alacartesaas.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://alacartesaas.com/login
coverage:
  checked: '2026-10-15'
  detail: The provider's website returns a JavaScript shell with no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://alacartesaas.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-15'
description: A La Carte SaaS provides a secure, AI‑powered financial comparison platform for utilities, mortgage, insurance and other financial products in Ireland. It offers real‑time data, consumer apps and broker tools to help advisors sell and retain customers, with a focus on transparency and streamlined decision‑making.
image: https://alacartesaas.com/lovable-uploads/ad9d4953-fc6b-46cc-9f5d-b2c21d601132.png
layout: provider
modified: '2026-10-15'
name: OneBill Utilities
nav: Providers
network: true
overview: 'OneBill Utilities is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Comparison, Software-as-a-Service, and Ireland.


  OneBill Utilities'' developer surface includes documentation, getting-started guide, signup flow, and 4 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Alacartesaas Domain Security
  slug: alacartesaas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alacartesaas
tags:
- Company
- Finance
- Comparison
- Software-as-a-Service
- Ireland
website: https://alacartesaas.com/
---
