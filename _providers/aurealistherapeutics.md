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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aurealistherapeutics/refs/heads/main/llms/aurealistherapeutics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aurealistherapeutics-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aurealistherapeutics/refs/heads/main/hosts/aurealistherapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aurealistherapeutics-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aurealistherapeutics/refs/heads/main/security/aurealistherapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aurealistherapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aurealistherapeutics.com
- group: operate
  title: ''
  type: Support
  url: https://aurealistherapeutics.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://aurealistherapeutics.com/aurealis-news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aurealistherapeutics.com/cookie-policy/
coverage:
  checked: 2026-09-26
  detail: The provider's website does not expose any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications despite having a documentation site.
  evidence:
  - status: timeout
    url: https://api.aurealistherapeutics.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Aurealis Therapeutics is a biotechnology company focused on developing multi-target therapies for chronic wounds, diabetic foot ulcers, and cancer. The firm conducts clinical trials, publishes scientific research, and partners with healthcare organizations to bring innovative treatments to market. Their platform integrates advanced drug discovery with rigorous clinical validation to address unmet medical needs.
layout: provider
modified: '2026-09-26'
name: Aurealistherapeutics
nav: Providers
network: true
overview: 'Aurealistherapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Therapeutics, Clinical Trials, Medical Devices, and Company.


  Aurealistherapeutics'' developer surface includes support, engineering blog, and 5 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aurealistherapeutics Domain Security
  slug: aurealistherapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aurealistherapeutics
tags:
- Biotechnology
- Therapeutics
- Clinical Trials
- Medical Devices
- Company
website: https://aurealistherapeutics.com
---
