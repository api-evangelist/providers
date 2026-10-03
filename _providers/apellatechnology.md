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
    dynamic_client_registration: true
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
  score: 18.7
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apellatechnology/refs/heads/main/security/apellatechnology-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/apellatechnology-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apellatechnology/refs/heads/main/llms/apellatechnology-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apellatechnology-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apellatechnology/refs/heads/main/well-known/apellatechnology-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/apellatechnology-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apellatechnology/refs/heads/main/well-known/apellatechnology-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apellatechnology-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apellatechnology/refs/heads/main/hosts/apellatechnology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apellatechnology-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apellatechnology/refs/heads/main/vendors/apellatechnology-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apellatechnology-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.apella.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apella.io/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.apella.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apella.io/privacy
- group: company
  title: ''
  type: Blog
  url: https://apella.io/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apellatechnology/refs/heads/main/security/apellatechnology-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/apellatechnology-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apellatechnology/refs/heads/main/security/apellatechnology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apellatechnology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apella.io
coverage:
  checked: 2026-09-25
  detail: API spec at https://api.apella.io/openapi.json requires authentication (401)
  evidence:
  - status: 401
    url: https://api.apella.io/openapi.json
  reason: partner-login
  state: gated
created: '2026-09-25'
description: Apellatechnology, operating under the brand Apella, provides ambient AI solutions for operating rooms, optimizing surgical capacity, reducing delays, and improving turnover efficiency. Their platform integrates with EHR systems to deliver real-time analytics, predictive case duration, and resource optimization for hospitals and surgical teams.
image: https://apella.io/og?title=Apella+%7C+Ambient+AI+for+the+Operating+Room&subtitle=Transform+your+OR+with+Apella%E2%80%99s+AI-powered+surgical+operations+platform
layout: provider
modified: '2026-09-25'
name: Apellatechnology
nav: Providers
network: true
overview: 'Apellatechnology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, and Surgery.


  Apellatechnology''s developer surface includes engineering blog and 13 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 15.9
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
    developer_ergonomics: 2.4
    discoverability: 46.4
    operational_transparency: 26.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 22.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apellatechnology Domain Security
  slug: apellatechnology-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Apellatechnology Vulnerability Disclosure
  slug: apellatechnology-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apellatechnology
tags:
- Company
- Healthcare
- Artificial Intelligence
- Surgery
website: https://apella.io
---
