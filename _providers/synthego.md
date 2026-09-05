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
  score: 23.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Synthego Agentic Access
  operation_count: 3
  slug: synthego-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.synthego.com/
  baseurl_source: declared
  description: The Order API from Synthego — 3 operation(s) for order.
  name: Synthego Order API
  slug: synthego-order-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Synthego Order API
  slug: open-synthego-order-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/synthego-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/synthego-order-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/synthego-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.synthego.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.synthego.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.synthego.com/
- group: company
  title: ''
  type: Blog
  url: https://www.synthego.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.synthego.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/synthego
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.synthego.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.synthego.com/legal/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.synthego.com/legal/iso-certification/
- group: auth
  title: ''
  type: Authentication
  url: authentication/synthego-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/synthego-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/synthego-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/synthego-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/synthego-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/synthego-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/synthego-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/synthego-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/synthego-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/synthego-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/synthego-place-order.md
created: '2026-07-17'
description: Synthego is a genome-engineering company that manufactures synthetic guide RNA (sgRNA, crRNA, trRNA), CRISPR kits, and engineered cells for research and cell/gene-therapy development. Its public Synthego Order API is a third-party integration API that lets partners retrieve current product pricing, generate a priced order preview from a list of guide-RNA sequences, and track an order through to checkout on Synthego's eCommerce site. Authentication is by an API key passed in the SYNTHEGOAPIKEY header. Synthego was surfaced as a portfolio company of SoftBank Vision Fund.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/synthego.png
layout: provider
modified: '2026-07-21'
name: Synthego
nav: Providers
network: true
overview: 'Synthego publishes 1 API on the [APIs.io](https://apis.io/) network: Order API. Tagged areas include Company, Health Tech, Genomics, CRISPR, and Biotechnology.


  Synthego''s developer surface includes documentation, API reference, engineering blog, support, authentication, and 18 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/synthego/refs/heads/main/screenshots/synthego-2026-09-02T161631.png
security:
- kind: authentication
  name: Synthego Authentication
  slug: synthego-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Synthego Domain Security
  slug: synthego-domain-security
  summary_line: TLSv1.2 · DMARC
slug: synthego
tags:
- Company
- Health Tech
- Genomics
- CRISPR
- Biotechnology
- Life Sciences
- Synthetic Biology
- Ordering
website: https://www.synthego.com/
---
