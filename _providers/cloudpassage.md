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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudpassage/refs/heads/main/llms/cloudpassage-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudpassage-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudpassage/refs/heads/main/hosts/cloudpassage-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudpassage-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudpassage/refs/heads/main/vendors/cloudpassage-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudpassage-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://fidelissecurity.com/trust-center/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fidelissecurity.com/terms-of-use/
- group: auth
  title: ''
  type: Security
  url: https://fidelissecurity.com/security/
- group: start
  title: ''
  type: Sandbox
  url: https://fidelissecurity.com/resource/datasheet/sandbox/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fidelissecurity.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://fidelissecurity.com/press/
- group: other
  title: ''
  type: Leadership
  url: https://fidelissecurity.com/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudpassage/refs/heads/main/security/cloudpassage-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudpassage-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fidelissecurity.com/
coverage:
  checked: '2026-10-09'
  detail: The developer portal is a JavaScript‑rendered site with no machine‑readable OpenAPI spec discovered.
  evidence:
  - status: 200
    url: https://fidelissecurity.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: CloudPassage, now operating as Fidelis Security, provides cloud security posture management, workload protection, and threat detection solutions. The company offers a unified XDR platform that integrates endpoint, network, cloud, and identity security, helping organizations detect, investigate, and respond to threats across their environments. Fidelis Security continues the CloudPassage legacy of delivering comprehensive cloud security services to enterprises worldwide.
image: https://fidelissecurity.com/wp-content/uploads/2026/04/Fidelis-Security-Open-Grapg.webp
layout: provider
modified: '2026-10-09'
name: CloudPassage
nav: Providers
network: true
overview: 'CloudPassage is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  CloudPassage''s developer surface includes sandbox and 11 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cloudpassage Domain Security
  slug: cloudpassage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cloudpassage
tags:
- Company
website: https://fidelissecurity.com/
---
