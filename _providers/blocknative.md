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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blocknative/refs/heads/main/hosts/blocknative-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blocknative-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blocknative/refs/heads/main/vendors/blocknative-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blocknative-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blocknative.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blocknative.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blocknative
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blocknative/refs/heads/main/security/blocknative-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blocknative-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blocknative.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blocknative.com/
- group: company
  title: ''
  type: Blog
  url: https://www.blocknative.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.blocknative.com/pricing
coverage:
  checked: '2026-09-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found despite probing API and docs hosts.
  evidence:
  - status: error
    url: https://api.blocknative.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-29'
description: Blocknative provides real‑time blockchain transaction monitoring and gas fee prediction APIs. Founded in 2018, the company powers developers with mempool data, L2 decoding, and wallet onboarding tools, enabling more efficient and transparent blockchain operations. Their platform supports multiple EVM‑compatible chains, offering developers accurate gas estimates, transaction status updates, and analytics to improve user experience and reduce costs.
image: https://www.blocknative.com/hubfs/blocknative-deloitte%201%20(1)%201.png
layout: provider
modified: '2026-09-29'
name: Blocknative
nav: Providers
network: true
overview: 'Blocknative is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, GasFees, and Monitoring.


  Blocknative''s developer surface includes documentation, engineering blog, pricing, and 7 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 39.3
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blocknative Domain Security
  slug: blocknative-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blocknative
tags:
- Company
- Blockchain
- GasFees
- Monitoring
website: https://www.blocknative.com/
---
