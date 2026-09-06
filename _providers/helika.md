---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 19.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://events.analytics.helika.io
  baseurl_source: declared
  description: The Events API from Helika — 1 operation(s) for events.
  name: Helika Events API
  slug: helika-events-api
artifact_total: 5
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Helika Analytics Service Events API
  slug: open-helika-events-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/helika-events-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.helika.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.helika.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.helika.io/docs/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.helika.io/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.helika.io/reference/create_event_v1_events_post
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getlidar
- group: start
  title: ''
  type: Login
  url: https://platform.helika.io/
- group: operate
  title: ''
  type: Support
  url: https://www.helika.io/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.helika.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.helika.io/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/helika-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/helika-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/helika-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/helika-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/helika-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/helika-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/helika-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/helika-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/helika-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/helika-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/helika-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Helika is a game and brand analytics platform, originally built for web3 and blockchain games, that helps studios, sports teams, and entertainment brands collect, unify, and act on player and community engagement data. Its Analytics Service API ingests gameplay and engagement events through a single events endpoint authenticated with an x-api-key header, and is instrumented by first-party Unity, Unreal Engine, and Web SDKs. Helika has since expanded into Helika Evolve, an AI-character platform that lets IP owners deploy brand-safe interactive characters across Discord, web, and social channels. Helika is a Pantera Capital portfolio company operating in the crypto and gaming sector.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/helika.png
layout: provider
modified: '2026-07-19'
name: Helika
nav: Providers
network: true
overview: 'Helika publishes 1 API on the [APIs.io](https://apis.io/) network: Events API. Tagged areas include Company, Crypto, Gaming, Analytics, and Game Analytics.


  Helika''s developer surface includes documentation, getting-started guide, API reference, support, authentication, and 18 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 47.6
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 34.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/helika/refs/heads/main/screenshots/helika-2026-07-25T220913.png
security:
- kind: authentication
  name: Helika Authentication
  slug: helika-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Helika Domain Security
  slug: helika-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: helika
tags:
- Company
- Crypto
- Gaming
- Analytics
- Game Analytics
- Web3
- Event
- Artificial Intelligence
- SDK
- Player Data
website: https://www.helika.io/
---
