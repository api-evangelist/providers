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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/evenly/llms/evenly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/evenly-llms.txt
- group: agent
  href: https://artifacts.apis.io/evenly/well-known/evenly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/evenly-well-known.yml
- group: other
  href: https://artifacts.apis.io/evenly/hosts/evenly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/evenly-hosts.yml
- group: auth
  href: https://artifacts.apis.io/evenly/security/evenly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/evenly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.evenly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.evenly.com/dentists/why-evenly/
- group: operate
  title: ''
  type: Support
  url: https://www.evenly.com/dentists/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.evenly.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.evenly.com/privacy-policy/
created: '2026-10-22'
description: Evenly provides a cloud‑based platform for dental practices to manage Invisalign and other clear‑aligner treatments. By combining tele‑orthodontic expertise with a SaaS workflow, Evenly helps dentists increase revenue, streamline case management, and deliver remote patient monitoring. The service includes treatment planning, specialist consultations, and a patient portal, enabling practices to keep cases in‑house while offering high‑tech, high‑touch care.
image: https://www.evenly.com/wp-content/uploads/Evenly_Logo_Blue-1024x343.png
layout: provider
modified: '2026-10-22'
name: Evenly
nav: Providers
network: true
overview: 'Evenly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Dental, Orthodontics, SaaS, and Healthcare.


  Evenly''s developer surface includes documentation, support, and 7 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 12.4
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
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Evenly Domain Security
  slug: evenly-domain-security
  summary_line: TLSv1.3 · DMARC
slug: evenly
tags:
- Company
- Dental
- Orthodontics
- SaaS
- Healthcare
website: https://www.evenly.com/
---
