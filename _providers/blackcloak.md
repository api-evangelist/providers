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
api_count: 1
apis:
- description: API for Blackcloak's digital executive protection platform
  name: Blackcloak API
  slug: blackcloak-api
artifact_total: 4
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blackcloak/refs/heads/main/well-known/blackcloak-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blackcloak-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blackcloak/refs/heads/main/well-known/blackcloak-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blackcloak-well-known.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.blackcloak.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blackcloak/refs/heads/main/security/blackcloak-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/blackcloak-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blackcloak/refs/heads/main/hosts/blackcloak-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blackcloak-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blackcloak/refs/heads/main/vendors/blackcloak-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blackcloak-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://blackcloak.io/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blackcloak/refs/heads/main/security/blackcloak-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/blackcloak-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blackcloak/refs/heads/main/security/blackcloak-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/blackcloak-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blackcloak/refs/heads/main/security/blackcloak-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blackcloak-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blackcloak.io
- group: docs
  title: ''
  type: Documentation
  url: https://blackcloak.io/resources/
- group: company
  title: ''
  type: Blog
  url: https://blackcloak.io/cybersecurity-blog/
- group: operate
  title: ''
  type: Support
  url: https://blackcloak.io/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blackcloak.io/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blackcloak.io/terms-conditions/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://my.blackcloak.io/
coverage:
  checked: '2026-09-29'
  detail: Documentation pages return JavaScript challenges, preventing machine‑readable spec discovery.
  evidence:
  - status: 429
    url: https://blackcloak.io/resources/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-29'
description: BlackCloak provides digital executive protection and personal cybersecurity services, safeguarding high‑profile individuals and enterprises from deepfake scams, impersonation, and cyber threats. Their platform offers monitoring, threat detection, and response tools tailored for executives, families, and high‑net‑worth individuals, combining technology and expert guidance to mitigate personal and corporate risk.
image: https://blackcloak.io/wp-content/uploads/2026/09/NEW-VID-THUMBNAIL.jpg
layout: provider
modified: '2026-09-29'
name: Blackcloak
nav: Providers
network: true
overview: 'Blackcloak publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Cybersecurity, Executive Protection, PersonalSafety, and Digital Identity.


  Blackcloak''s developer surface includes documentation, engineering blog, support, and 14 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 58.9
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blackcloak Domain Security
  slug: blackcloak-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Blackcloak Vulnerability Disclosure
  slug: blackcloak-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Blackcloak Trust Center
  slug: blackcloak-trust-center
  summary_line: SOC 2
slug: blackcloak
tags:
- Security
- Cybersecurity
- Executive Protection
- PersonalSafety
- Digital Identity
website: https://blackcloak.io
---
