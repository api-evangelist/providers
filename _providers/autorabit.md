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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.autorabit.com/trust-center/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/autorabit/refs/heads/main/llms/autorabit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autorabit-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/autorabit/refs/heads/main/well-known/autorabit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autorabit-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autorabit/refs/heads/main/hosts/autorabit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autorabit-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autorabit/refs/heads/main/vendors/autorabit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autorabit-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.autorabit.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.autorabit.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.autorabit.com/news/
- group: company
  title: ''
  type: Blog
  url: https://www.autorabit.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autorabit/refs/heads/main/security/autorabit-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/autorabit-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autorabit/refs/heads/main/security/autorabit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autorabit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.autorabit.com/
coverage:
  checked: 2026-09-26
  detail: Documentation pages return HTML shells and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://go.autorabit.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: AutoRABIT provides a Salesforce DevSecOps platform that secures and accelerates development, offering CI/CD, code quality, backup & recovery, and security posture management. It helps regulated enterprises ensure compliance, reduce risk, and deploy confidently with built‑in security features across its suite of products.
layout: provider
modified: '2026-09-26'
name: AutoRABIT
nav: Providers
network: true
overview: 'AutoRABIT is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Salesforce, DevSecOps, CI/CD, Compliance, and Automation.


  AutoRABIT''s developer surface includes support, engineering blog, and 10 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Autorabit Domain Security
  slug: autorabit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Autorabit Trust Center
  slug: autorabit-trust-center
  summary_line: FedRAMP
slug: autorabit
tags:
- Salesforce
- DevSecOps
- CI/CD
- Compliance
- Automation
website: https://www.autorabit.com/
---
