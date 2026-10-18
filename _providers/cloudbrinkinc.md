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
api_count: 0
artifact_total: 1
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cloudbrinkinc/refs/heads/main/changelog/cloudbrinkinc-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cloudbrinkinc-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudbrinkinc/refs/heads/main/llms/cloudbrinkinc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudbrinkinc-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudbrinkinc/refs/heads/main/well-known/cloudbrinkinc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudbrinkinc-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudbrinkinc/refs/heads/main/hosts/cloudbrinkinc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudbrinkinc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudbrinkinc/refs/heads/main/vendors/cloudbrinkinc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudbrinkinc-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloudbrink.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://cloudbrink.com/newsroom/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.cloudbrink.com/release-notes
- group: company
  title: ''
  type: Blog
  url: https://cloudbrink.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cloudbrink.com/configuration/first-time-onboarding
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudbrink.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudbrinkinc/refs/heads/main/security/cloudbrinkinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudbrinkinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudbrink.com
coverage:
  checked: '2026-10-09'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: error
    url: https://api.cloudbrink.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Cloudbrinkinc provides a modern, cloud‑native security platform delivering Zero Trust Network Access (ZTNA), Secure Access Service Edge (SASE), and personal SD‑WAN solutions. Their services enable secure remote access, hybrid worker connectivity, and multi‑cloud networking for enterprises, combining high‑performance VPN alternatives with automated moving‑target defense. The company emphasizes AI‑driven monitoring, compliance, and a seamless user experience across devices and locations.
image: https://cloudbrink.com/wp-content/uploads/2025/12/y9DpT.jpg
layout: provider
modified: '2026-10-09'
name: Cloudbrinkinc
nav: Providers
network: true
overview: 'Cloudbrinkinc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Networking, Cloud, Zero Trust, and Software-as-a-Service.


  Cloudbrinkinc''s developer surface includes changelog, engineering blog, getting-started guide, documentation, and 9 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 15.8
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
  name: Cloudbrinkinc Domain Security
  slug: cloudbrinkinc-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: cloudbrinkinc
tags:
- Security
- Networking
- Cloud
- Zero Trust
- Software-as-a-Service
website: https://cloudbrink.com
---
