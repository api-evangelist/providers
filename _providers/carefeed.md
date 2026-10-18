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
  href: https://raw.githubusercontent.com/api-evangelist/carefeed/refs/heads/main/vendors/carefeed-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carefeed-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carefeed/refs/heads/main/well-known/carefeed-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/carefeed-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/carefeed/refs/heads/main/well-known/carefeed-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carefeed-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carefeed/refs/heads/main/hosts/carefeed-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carefeed-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.carefeed.com/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carefeed.com/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.carefeed.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.carefeed.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Carefeed
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carefeed/refs/heads/main/security/carefeed-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carefeed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carefeed.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.carefeed.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Carefeed provides a unified platform for senior living communities, integrating admissions, AI‑assisted referrals, employee enablement, resident and family experience, e‑billing, and payments. The SaaS solution connects with existing EHR and HR systems, offering HIPAA‑compliant messaging, automated reminders, and analytics to streamline operations, improve care quality, and reduce administrative overhead. Built for skilled‑nursing and long‑term care facilities, Carefeed aims to replace fragmented software tools with a single, secure system.
layout: provider
modified: '2026-10-07'
name: Carefeed
nav: Providers
network: true
overview: 'Carefeed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include senior‑living, Software-as-a-Service, Healthcare, admissions, and Artificial Intelligence.


  Carefeed''s developer surface includes support, documentation, and 9 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carefeed Domain Security
  slug: carefeed-domain-security
  summary_line: TLSv1.3 · DMARC
slug: carefeed
tags:
- senior‑living
- Software-as-a-Service
- Healthcare
- admissions
- Artificial Intelligence
website: https://www.carefeed.com/
---
