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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cuure4978/refs/heads/main/llms/cuure4978-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cuure4978-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cuure4978/refs/heads/main/well-known/cuure4978-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cuure4978-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cuure4978/refs/heads/main/hosts/cuure4978-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cuure4978-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cuure4978/refs/heads/main/vendors/cuure4978-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cuure4978-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cuure4978/refs/heads/main/security/cuure4978-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cuure4978-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cuure.com
- group: docs
  title: ''
  type: Documentation
  url: https://cuure.com/en/about/mission
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cuure.com/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cuure.com/en/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://cuure.com/en/help-contact/customer-support
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI or other machine‑readable contract found at typical endpoints on api.cuure.com.
  evidence:
  - status: 404
    url: https://api.cuure.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Cuure is a science‑backed supplement company founded in 2019 with the ambition to raise the standards of the supplement industry. It develops clinically validated, optimised dosage products through continuous innovation and a scientific committee, delivering measurable results for customers. The brand offers a range of vitamins and health solutions, emphasizing evidence‑based formulations and transparent, customer‑focused support.
image: https://content.cuure.com/images/home/og-all-ranges.jpg
layout: provider
modified: '2026-10-12'
name: Cuure4978
nav: Providers
network: true
overview: 'Cuure4978 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Food Supplements, Personalised Health, Biological Tests, Tracking Technologies, and Science‑Backed.


  Cuure4978''s developer surface includes documentation, support, and 8 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 13.1
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
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cuure4978 Domain Security
  slug: cuure4978-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cuure4978
tags:
- Food Supplements
- Personalised Health
- Biological Tests
- Tracking Technologies
- Science‑Backed
- French Lab
website: https://cuure.com
---
