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
  href: https://raw.githubusercontent.com/api-evangelist/athena-security/refs/heads/main/well-known/athena-security-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/athena-security-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/athena-security/refs/heads/main/well-known/athena-security-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/athena-security-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/athena-security/refs/heads/main/llms/athena-security-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/athena-security-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/athena-security/refs/heads/main/hosts/athena-security-hosts.yml
  title: ''
  type: Hosts
  url: hosts/athena-security-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/athena-security/refs/heads/main/vendors/athena-security-vendors.yml
  title: ''
  type: Vendors
  url: vendors/athena-security-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.athena-security.com/terms-and-conditions/
- group: operate
  title: ''
  type: Support
  url: https://support.athena-security.com/support/home
- group: operate
  title: ''
  type: StatusPage
  url: https://status.athena-security.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.athena-security.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.athena-security.com/press/
- group: other
  title: ''
  type: Leadership
  url: https://www.athena-security.com/team/
- group: company
  title: ''
  type: Blog
  url: https://www.athena-security.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/athena-security/refs/heads/main/security/athena-security-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/athena-security-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/athena-security/refs/heads/main/security/athena-security-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/athena-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.athena-security.com/
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found on any discovered host.
  evidence:
  - status: 0
    url: https://api.athena-security.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Athena Security provides AI‑driven weapons detection systems for schools, hospitals, and public venues. Their platform combines advanced imaging, AI analytics, and real‑time alerts to help organizations prevent violent incidents. The company offers hardware, operator apps, compliance reporting, and integration services, aiming to enhance safety across critical infrastructure.
image: https://www.athena-security.com/wp-content/uploads/2026/02/Group-3-1.webp
layout: provider
modified: '2026-09-26'
name: Athena Security
nav: Providers
network: true
overview: 'Athena Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Artificial Intelligence, Weapons Detection, and Safety.


  Athena Security''s developer surface includes support, engineering blog, and 14 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 58.9
    operational_transparency: 26.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Athena Security Domain Security
  slug: athena-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Athena Security Vulnerability Disclosure
  slug: athena-security-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: athena-security
tags:
- Company
- Security
- Artificial Intelligence
- Weapons Detection
- Safety
website: https://www.athena-security.com/
---
