---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 14.4
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.blackpanda.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blackpanda/refs/heads/main/well-known/blackpanda-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blackpanda-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blackpanda/refs/heads/main/hosts/blackpanda-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blackpanda-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blackpanda/refs/heads/main/vendors/blackpanda-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blackpanda-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.blackpanda.com/plans
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.blackpanda.com/
- group: company
  title: ''
  type: Blog
  url: https://www.blackpanda.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blackpanda/refs/heads/main/security/blackpanda-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/blackpanda-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blackpanda/refs/heads/main/security/blackpanda-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blackpanda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blackpanda.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/blackpanda
  reason: no-developer-program
  state: none
created: '2026-09-29'
description: Blackpanda is Asia’s leading cyber emergency response firm, offering incident response, proactive readiness intelligence, and integrated cyber insurance services across the region. Founded in 2015, it provides end‑to‑end digital emergency support at a fraction of traditional costs, serving enterprises and governments with rapid, local expertise.
layout: provider
modified: '2026-09-29'
name: Blackpanda
nav: Providers
network: true
overview: 'Blackpanda is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity, Incident Response, Digital Forensics, Cyber Insurance, and Asia.


  Blackpanda''s developer surface includes pricing, engineering blog, and 8 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 14.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blackpanda Domain Security
  slug: blackpanda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Blackpanda Trust Center
  slug: blackpanda-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: blackpanda
tags:
- Cybersecurity
- Incident Response
- Digital Forensics
- Cyber Insurance
- Asia
website: https://www.blackpanda.com
---
