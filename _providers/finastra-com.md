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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/finastra-com/well-known/finastra-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/finastra-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/finastra-com/hosts/finastra-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/finastra-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.finastra.com/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://support.finastra.com/s/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.finastra.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/finastra-com/security/finastra-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/finastra-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://finastra.com/
created: '2026-10-20'
description: Finastra is a global financial software provider delivering a broad portfolio of banking, payments, lending and treasury solutions. Their platform enables banks and fintechs to innovate faster, improve customer experiences, and streamline operations across digital channels.
image: https://www.finastra.com/themes/custom/themekit/logo-v2.png
layout: provider
modified: '2026-10-20'
name: Finastra
nav: Providers
network: true
overview: 'Finastra is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Banking Software, Payments, and FinTech.


  Finastra''s developer surface includes support and 6 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Finastra Com Domain Security
  slug: finastra-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: finastra-com
tags:
- Company
- Financial Services
- Banking Software
- Payments
- FinTech
website: https://finastra.com/
---
