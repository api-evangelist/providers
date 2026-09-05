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
    agentic_access: derived
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
  score: 21.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Cachet Agentic Access
  operation_count: 4
  slug: cachet-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 3
apis:
- baseURL: https://platform-api.cachet.me
  baseurl_source: declared
  description: Endpoint where to send the connect request
  name: Cachet Connect API
  slug: cachet-connect-api
- baseURL: https://platform-api.cachet.me
  baseurl_source: declared
  description: Event actions which are sent by the platform to Cachet involving gig-workers tasks done on the platform
  name: Cachet Gig-Events API
  slug: cachet-gig-events-api
- baseURL: https://platform-api.cachet.me
  baseurl_source: declared
  description: User actions to send user-related data from platform to Cachet
  name: Cachet User API
  slug: cachet-user-api
- baseURL: https://platform-api.cachet.me
  baseurl_source: declared
  description: Used to notify Cachet about vehicle events
  name: Cachet Vehicle events API
  slug: cachet-vehicle-events-api
arazzos:
- description: Register a gig-worker on the Cachet Platform (Verify) API, then report a completed task event for that worker. Requires x-api-key and x-api-username headers issued by the Cachet IT team.
  name: Cachet gig-worker onboarding and task reporting
  slug: cachet-gig-onboarding
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cachet Parking Connect API
  slug: open-cachet-connect-api
- collection_type: open
  name: Cachet Parking Connect Gig-Events API
  slug: open-cachet-gig-events-api
- collection_type: open
  name: Cachet Parking Connect User API
  slug: open-cachet-user-api
- collection_type: open
  name: Cachet Parking Connect Vehicle events API
  slug: open-cachet-vehicle-events-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/cachet-parking-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://cachet.me/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cachet.me/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cachet.me/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cachet.me/
- group: operate
  title: ''
  type: Support
  url: https://help.cachet.me/en/
- group: company
  title: ''
  type: Blog
  url: https://cachet.me/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://cachet.me/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.cachet.me/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cachet.me/en/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cachet.me/en/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/cachet-authentication.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cachet-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cachet-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/cachet-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cachet-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cachet-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cachet-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cachet-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cachet-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cachet-gig-onboarding.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cachet-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cachet-agentic-access.yml
created: '2026-07-17'
description: 'Cachet OÜ is an Estonian InsurTech that provides adaptive, usage-based insurance for digital platforms and their users across new mobility, gig work, and car-sharing. Digital platforms integrate Cachet through three inbound event APIs: the Parking API (car-sharing fleets stream vehicle events so Cachet manages parking), the Verify / Platform API (gig-work platforms register workers and push task events to drive worker protection), and the Partners API (embed a prefilled Cachet onboarding link into a partner app). All three are OpenAPI 3.1 and authenticated with issued x-api-key and x-api-username headers. Cachet is backed by Techstars; notable platform clients include Bolt, Bird, Ryde, and TaskRabbit.'
image: https://cachet.me/assets/img/social_share.jpg
layout: provider
modified: '2026-07-18'
name: Cachet
nav: Providers
network: true
overview: 'Cachet publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Connect API, Gig-Events API, User API, and 1 more. Tagged areas include Company, Insurance, Insurtech, Mobility, and Gig Economy.


  Cachet''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 17 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 57.1
    developer_ergonomics: 54.2
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cachet/refs/heads/main/screenshots/cachet-2026-07-25T204205.png
security:
- kind: authentication
  name: Cachet Authentication
  slug: cachet-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Cachet Domain Security
  slug: cachet-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cachet
tags:
- Company
- Insurance
- Insurtech
- Mobility
- Gig Economy
- Car Sharing
- Embedded Insurance
- Event
website: https://cachet.me/
---
