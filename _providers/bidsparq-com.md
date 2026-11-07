---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://bidsparq.com/security
- group: agent
  href: https://artifacts.apis.io/bidsparq-com/llms/bidsparq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bidsparq-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/bidsparq-com/well-known/bidsparq-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bidsparq-com-security.txt
- group: agent
  href: https://artifacts.apis.io/bidsparq-com/well-known/bidsparq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bidsparq-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bidsparq-com/hosts/bidsparq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bidsparq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bidsparq-com/vendors/bidsparq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bidsparq-com-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.bidsparq.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bidsparq
- group: auth
  href: https://artifacts.apis.io/bidsparq-com/security/bidsparq-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bidsparq-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bidsparq-com/security/bidsparq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bidsparq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bidsparq.com/
coverage:
  checked: '2026-11-02'
  detail: Provider's documentation pages on dev.bidsparq.com contain no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL specifications.
  evidence:
  - status: 404
    url: https://dev.bidsparq.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BidSparq provides a SaaS platform that scans over 30,000 procurement sources daily, matching businesses with relevant government, education, and healthcare RFPs. Users can browse, filter, and receive alerts for opportunities that fit their criteria, helping them win more contracts efficiently. The service includes tools for managing bids, tracking competition, and analytics to improve win rates.
layout: provider
modified: '2026-11-02'
name: BidSparq
nav: Providers
network: true
overview: 'BidSparq is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Procurement, Software-as-a-Service, B2B, RFP, and Government.


  BidSparq''s developer surface includes documentation and 10 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 7.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bidsparq Com Domain Security
  slug: bidsparq-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bidsparq Com Vulnerability Disclosure
  slug: bidsparq-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bidsparq-com
tags:
- Procurement
- Software-as-a-Service
- B2B
- RFP
- Government
website: https://bidsparq.com/
---
