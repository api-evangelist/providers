---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 12.9
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Build hybrid smart contracts with Chainlink
  name: Chainlink
  slug: chainlink
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chainlink-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chainlink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chain.link/developer-resources
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Build hybrid smart contracts with Chainlink
graphqls:
- description: Chainlink exposes a GraphQL API as part of its node operator interface — the same API powering the Chainlink Operator UI (formerly Chainlink Dashboard). It provides programmatic access to node managem
  name: Chainlink GraphQL API
  slug: chainlink-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chainlink.png
layout: provider
modified: '2026-05-28'
name: Chainlink
nav: Providers
network: true
overview: Chainlink publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain and Public APIs.
random_paper: 0
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chainlink/refs/heads/main/screenshots/chainlink-2026-06-20T174200.png
security:
- kind: domain-security
  name: Chainlink Domain Security
  slug: chainlink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chainlink Vulnerability Disclosure
  slug: chainlink-vulnerability-disclosure
  summary_line: Hackerone
slug: chainlink
tags:
- Blockchain
- Public APIs
website: https://chain.link/developer-resources
---
