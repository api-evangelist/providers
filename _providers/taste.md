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
    error_semantics: verified
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
  score: 22.1
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://api.tastelabs.com
  baseurl_source: declared
  description: The health API from Taste — 2 operation(s) for health.
  name: Taste health API
  slug: taste-health-api
- baseURL: https://api.tastelabs.com
  baseurl_source: declared
  description: The Prompt Enhancement API from Taste — 2 operation(s) for prompt enhancement.
  name: Taste Prompt Enhancement API
  slug: taste-prompt-enhancement-api
- baseURL: https://api.tastelabs.com
  baseurl_source: declared
  description: The Taste Engine API API from Taste — 1 operation(s) for taste engine api.
  name: Taste Taste Engine API API
  slug: taste-taste-engine-api-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Taste Engine health API
  slug: open-taste-health-api
- collection_type: open
  name: Taste Engine health Prompt Enhancement API
  slug: open-taste-prompt-enhancement-api
- collection_type: open
  name: Taste Engine health Taste Engine API API
  slug: open-taste-taste-engine-api-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/taste-taste-engine-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taste-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tastelabs.com/
- group: company
  title: ''
  type: Blog
  url: https://tastelabs.com/blog
- group: auth
  title: ''
  type: Authentication
  url: authentication/taste-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/taste-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/taste-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/taste-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/taste-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/taste-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/taste-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/taste-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/taste-lifecycle.yml
created: '2026-07-17'
description: Taste Labs is a San Francisco research lab and infrastructure company building "the taste layer for AI" — decoding subjective design domains to end AI slop. Its Taste Engine API extracts brand and design guidelines from a reference site or a prior submission and enhances website and slide-deck prompts so AI generation stays on-brand, returning an enhanced prompt plus structured brand context and reasoning. The company is backed by CRV and Amplify Partners and runs the TasteMakers community program. This profile was enriched from the provider's live public surface, including the Taste Engine API OpenAPI.
image: https://cdn.prod.website-files.com/6a1d5baf94efef5f7c435fc3/6a306ae79b1ce1b28e27e16b_taste_Logo.png
layout: provider
modified: '2026-07-21'
name: Taste
nav: Providers
network: true
overview: 'Taste publishes 3 APIs on the [APIs.io](https://apis.io/) network: health API, Prompt Enhancement API, and Taste Engine API API. Tagged areas include Company, Artificial Intelligence, Design, Machine-Learning, and Developer Tools.


  Taste''s developer surface includes engineering blog, authentication, and 12 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 49.4
    developer_ergonomics: 16.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 23.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/taste/refs/heads/main/screenshots/taste-2026-09-02T162559.png
security:
- kind: authentication
  name: Taste Authentication
  slug: taste-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Taste Domain Security
  slug: taste-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: taste
tags:
- Company
- Artificial Intelligence
- Design
- Machine-Learning
- Developer Tools
- Prompt Engineering
- Content Generation
website: https://tastelabs.com/
---
