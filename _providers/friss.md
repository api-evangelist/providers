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
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/friss/refs/heads/main/integrations/friss-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/friss-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/friss/refs/heads/main/hosts/friss-hosts.yml
  title: ''
  type: Hosts
  url: hosts/friss-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/friss/refs/heads/main/security/friss-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/friss-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.friss.com
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/friss/refs/heads/main/llms/friss-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/friss-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.friss.com/blog/insurance-in-2025
- group: company
  title: ''
  type: Newsroom
  url: https://www.friss.com/press/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.friss.com/privacy-policy
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.friss.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: FRISS builds AI-powered fraud detection and risk assessment software (Trust Automation Platform) for property and casualty insurers, scoring policies, claims and renewals in real time. No public API documentation or machine-readable API contract was found on its public surface.
image: https://framerusercontent.com/assets/kxedfQ3PQPThZsXvooP43EZxHA.png
layout: provider
modified: '2026-10-13'
name: FRISS
nav: Providers
network: true
overview: 'FRISS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Fraud Prevention, and Risk Assessment.


  FRISS''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 8.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Friss Domain Security
  slug: friss-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: friss
tags:
- Company
- Insurance
- Fraud Prevention
- Risk Assessment
website: https://www.friss.com
---
