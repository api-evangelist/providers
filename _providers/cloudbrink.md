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
- description: Cloudbrink provides edge‑native Personal SASE solutions with APIs documented in the Cloudbrink documentation.
  name: Cloudbrink API
  slug: cloudbrink-api
artifact_total: 2
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cloudbrink/refs/heads/main/changelog/cloudbrink-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cloudbrink-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudbrink/refs/heads/main/llms/cloudbrink-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudbrink-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudbrink/refs/heads/main/well-known/cloudbrink-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudbrink-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudbrink/refs/heads/main/hosts/cloudbrink-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudbrink-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudbrink/refs/heads/main/vendors/cloudbrink-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudbrink-vendors.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/cloudbrink/refs/heads/main/security/cloudbrink-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudbrink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudbrink.com/
coverage:
  checked: '2026-10-09'
  detail: Documentation is provided as markdown pages without any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://docs.cloudbrink.com/cloudbrink-overview.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Cloudbrink provides edge‑native Personal SASE solutions, delivering high‑performance zero‑trust network access (ZTNA) and personal SD‑WAN for hybrid workforces. Founded in 2019, the Sunnyvale‑based company leverages AI/ML to accelerate cloud, SaaS, and data‑center connectivity, offering secure, low‑latency networking for remote and on‑premise users.
image: https://cloudbrink.com/wp-content/uploads/2025/12/y9DpT.jpg
layout: provider
modified: '2026-10-09'
name: Cloudbrink
nav: Providers
network: true
overview: 'Cloudbrink is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Networking, Cloud, and Software-as-a-Service.


  Cloudbrink''s developer surface includes changelog, engineering blog, getting-started guide, documentation, and 9 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    mcp: derived
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
  name: Cloudbrink Domain Security
  slug: cloudbrink-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: cloudbrink
tags:
- Company
- Security
- Networking
- Cloud
- Software-as-a-Service
website: https://cloudbrink.com/
---
