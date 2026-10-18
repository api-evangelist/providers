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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carlaf042/refs/heads/main/hosts/carlaf042-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carlaf042-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carlaf042/refs/heads/main/vendors/carlaf042-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carlaf042-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carla.com/terms
- group: operate
  title: ''
  type: Support
  url: https://carla.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carla.com/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carlaf042/refs/heads/main/security/carlaf042-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carlaf042-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carla.com
coverage:
  checked: '2026-10-07'
  detail: No machine‑readable API specification was found on carla.com or its API host.
  evidence:
  - status: 200
    url: https://carla.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Carla (carlaf042) is a next‑generation private travel platform offering seamless, transparent, and instant booking of private jets, yachts, and villas. It supports both fiat (Stripe) and cryptocurrency payments, provides 24/7 concierge service, and emphasizes privacy, security, and advanced data protection. The company operates from its website carla.com, presenting its services, pricing, terms, and privacy policies, and offers a loyalty program and partner opportunities for jet owners.
layout: provider
modified: '2026-10-07'
name: Carlaf042
nav: Providers
network: true
overview: 'Carlaf042 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Private-Jet, Luxury, and Payments.


  Carlaf042''s developer surface includes support and 6 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carlaf042 Domain Security
  slug: carlaf042-domain-security
  summary_line: TLSv1.3
slug: carlaf042
tags:
- Company
- Travel
- Private-Jet
- Luxury
- Payments
website: https://carla.com
---
