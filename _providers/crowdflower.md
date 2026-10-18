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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crowdflower/refs/heads/main/well-known/crowdflower-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crowdflower-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crowdflower/refs/heads/main/hosts/crowdflower-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crowdflower-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crowdflower/refs/heads/main/vendors/crowdflower-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crowdflower-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.crowdgen.com/s/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.crowdgen.com/s/topic/0TOTR0000005U774AE/general-onboarding
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crowdflower/refs/heads/main/security/crowdflower-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crowdflower-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crowdgen.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.crowdgen.com/s/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crowdgen.com/terms-of-service
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://crowdgen.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: Crowdflower, now operating as CrowdGen under Appen, provides a platform connecting expert contributors with AI companies for data labeling, annotation, and specialized knowledge work. The service offers high‑pay freelance opportunities across domains such as accounting, healthcare, and finance, leveraging a global network of over 500,000 contributors. It supports AI model training, data quality assurance, and domain‑specific expertise for enterprise clients.
image: https://i0.wp.com/crowdgen.com/wp-content/uploads/2026/08/crowdgen-statement-A_specimen-block_centered.jpg?fit=1200%2C514&ssl=1
layout: provider
modified: '2026-10-11'
name: Crowdflower
nav: Providers
network: true
overview: 'Crowdflower is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Artificial Intelligence, Crowdsourcing, and Marketplace.


  Crowdflower''s developer surface includes support, getting-started guide, documentation, and 6 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crowdflower Domain Security
  slug: crowdflower-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crowdflower
tags:
- Company
- Data
- Artificial Intelligence
- Crowdsourcing
- Marketplace
website: https://crowdgen.com
---
