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
api_count: 1
apis:
- description: Mimecast provides email security APIs, but no machine‑readable contract was discovered.
  name: Mimecast API
  slug: mimecast-api
artifact_total: 4
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mimecast/refs/heads/main/vendors/mimecast-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mimecast-vendors.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.mimecast.com/
- group: auth
  title: ''
  type: Security
  url: https://www.mimecast.com/responsible-disclosure/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mimecast/refs/heads/main/well-known/mimecast-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mimecast-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mimecast/refs/heads/main/well-known/mimecast-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mimecast-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mimecast/refs/heads/main/hosts/mimecast-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mimecast-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mimecast.com/legal/terms-of-use/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mimecast.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mimecast.com/company/mimecast-trust-center/privacy-statement/
- group: start
  title: ''
  type: Login
  url: https://www.mimecast.com/login/
- group: company
  title: ''
  type: Blog
  url: https://www.mimecast.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.services.mimecast.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mimecast
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mimecast/refs/heads/main/security/mimecast-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mimecast-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mimecast/refs/heads/main/security/mimecast-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mimecast-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mimecast/refs/heads/main/security/mimecast-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mimecast-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mimecast.com
coverage:
  checked: '2026-10-14'
  detail: Developer portal https://developer.services.mimecast.com returns 403, and no OpenAPI spec was found on api.mimecast.com.
  evidence:
  - status: 403
    url: https://developer.services.mimecast.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Mimecast provides cloud‑based email security, data loss prevention, and archiving solutions that protect organizations from phishing, malware, and targeted attacks. Their platform secures inbound, outbound, and internal communications, offering advanced threat protection, human risk management, and secure collaboration tools. Mimecast’s services help enterprises maintain compliance, ensure data continuity, and reduce the risk of cyber‑threats across email, web, and other digital channels.
image: https://assets.mimecast.com/api/public/content/fc3a222119bd49b3bfde7d2fae0f64ea?v=5a6d0fc5
layout: provider
modified: '2026-10-13'
name: Mimecast
nav: Providers
network: true
overview: 'Mimecast is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email Security, Cloud, Data Loss Prevention, Threat Protection, and Collaboration.


  Mimecast''s developer surface includes engineering blog, documentation, and 15 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 31.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mimecast Domain Security
  slug: mimecast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mimecast Vulnerability Disclosure
  slug: mimecast-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Mimecast Trust Center
  slug: mimecast-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: mimecast
tags:
- Email Security
- Cloud
- Data Loss Prevention
- Threat Protection
- Collaboration
- Company
website: https://www.mimecast.com
---
