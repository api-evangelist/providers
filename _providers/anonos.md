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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://anonos.com/privacy
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anonos/refs/heads/main/conformance/anonos-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anonos-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anonos/refs/heads/main/well-known/anonos-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anonos-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anonos/refs/heads/main/well-known/anonos-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anonos-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anonos/refs/heads/main/hosts/anonos-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anonos-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anonos/refs/heads/main/vendors/anonos-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anonos-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://anonos.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anonos.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://anonos.com/docs
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anonos/refs/heads/main/security/anonos-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/anonos-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anonos/refs/heads/main/security/anonos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anonos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anonos.com
coverage:
  checked: 2026-09-25
  detail: Documentation is HTML without a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://anonos.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-24'
description: Anonos is a data privacy and tokenization company that enables organizations to use sensitive data securely without compromising its value. Over a decade of innovation, Anonos provides advanced tokenization, policy‑controlled protection, and utility‑preserving data use across analytics, AI, and enterprise workflows, helping customers meet privacy, security, governance, and compliance requirements.
image: https://anonos.com/images/social-anonos.webp
layout: provider
modified: '2026-09-24'
name: Anonos
nav: Providers
network: true
overview: 'Anonos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Tokenization, Privacy, Data Security, Enterprise Data, and Analytics.


  Anonos'' developer surface includes support, documentation, and 10 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anonos Domain Security
  slug: anonos-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Anonos Vulnerability Disclosure
  slug: anonos-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: anonos
tags:
- Tokenization
- Privacy
- Data Security
- Enterprise Data
- Analytics
- Compliance
website: https://anonos.com
---
