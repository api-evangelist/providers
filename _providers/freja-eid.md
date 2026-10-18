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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Freja eID provides a digital identity platform with authentication and signing capabilities. The developer portal is at the developers section page.
  name: Freja eID API
  slug: freja-eid-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/freja-eid/refs/heads/main/llms/freja-eid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/freja-eid-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/freja-eid/refs/heads/main/well-known/freja-eid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/freja-eid-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/freja-eid/refs/heads/main/hosts/freja-eid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/freja-eid-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://frejaeid.com/en/support/
- group: start
  title: ''
  type: SignUp
  url: https://frejaeid.com/en/register-with-your-id-card/
- group: auth
  title: ''
  type: Security
  url: https://frejaeid.com/en/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://frejaeid.com/nl/privacybeleid/
- group: company
  title: ''
  type: Newsroom
  url: https://frejaeid.com/en/newsroom/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/freja-eid/refs/heads/main/security/freja-eid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/freja-eid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://frejaeid.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://org.frejaeid.com/en/developers-section/
- group: docs
  title: ''
  type: Documentation
  url: https://org.frejaeid.com/en/developers-section/
- group: docs
  title: ''
  type: APIReference
  url: https://org.frejaeid.com/en/developers-section/
coverage:
  checked: '2026-10-15'
  detail: The developer portal provides documentation but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract is publicly available.
  evidence:
  - status: 200
    url: https://org.frejaeid.com/en/developers-section/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Freja eID provides a digital identity platform enabling secure electronic identification, authentication, and signing for individuals and businesses across the EU/EEA. Users can register with national ID cards or passports, and integrate Freja eID into services for login, payments, and compliance. The service supports multilingual access, wide international coverage, and is approved by Swedish authorities and the EU.
image: https://frejaeid.com/wp-content/uploads/2022/09/ShareFrejaLink.jpg
layout: provider
modified: '2026-10-15'
name: Freja eID
nav: Providers
network: true
overview: 'Freja eID is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Identity, Authentication, DigitalSignature, EU, and EEA.


  Freja eID''s developer surface includes support, signup flow, documentation, API reference, and 9 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Freja Eid Domain Security
  slug: freja-eid-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: freja-eid
tags:
- Identity
- Authentication
- DigitalSignature
- EU
- EEA
website: https://frejaeid.com/
---
