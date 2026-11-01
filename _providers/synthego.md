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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-10-31'
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
  name: Synthego Order API
  slug: open-synthego-order-api
common:
- group: company
  title: ''
  type: Blog
  url: https://www.synthego.com/press/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.synthego.com/feed/
- group: other
  href: https://artifacts.apis.io/synthego/capabilities/synthego-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/synthego-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/synthego/overlays/synthego-order-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/synthego-order-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/synthego/agentic-access/synthego-agentic-access.yml
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
  href: https://artifacts.apis.io/synthego/authentication/synthego-authentication.yml
  title: ''
  type: Authentication
  url: authentication/synthego-authentication.yml
- group: auth
  href: https://artifacts.apis.io/synthego/security/synthego-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/synthego-domain-security.yml
- group: design
  href: https://artifacts.apis.io/synthego/conventions/synthego-conventions.yml
  title: ''
  type: Conventions
  url: conventions/synthego-conventions.yml
- group: design
  href: https://artifacts.apis.io/synthego/errors/synthego-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/synthego-problem-types.yml
- group: design
  href: https://artifacts.apis.io/synthego/data-model/synthego-data-model.yml
  title: ''
  type: DataModel
  url: data-model/synthego-data-model.yml
- group: design
  href: https://artifacts.apis.io/synthego/lifecycle/synthego-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/synthego-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/synthego/conformance/synthego-conformance.yml
  title: ''
  type: Conformance
  url: conformance/synthego-conformance.yml
- group: agent
  href: https://artifacts.apis.io/synthego/well-known/synthego-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/synthego-well-known.yml
- group: agent
  href: https://artifacts.apis.io/synthego/mcp/synthego-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/synthego-mcp.yml
- group: agent
  href: https://artifacts.apis.io/synthego/llms/synthego-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/synthego-llms.txt
- group: agent
  href: https://artifacts.apis.io/synthego/skills/synthego-place-order.md
  title: ''
  type: AgentSkill
  url: skills/synthego-place-order.md
created: '2026-07-17'
description: Synthego is a genome-engineering company that manufactures synthetic guide RNA (sgRNA, crRNA, trRNA), CRISPR kits, and engineered cells for research and cell/gene-therapy development. Its public Synthego Order API is a third-party integration API that lets partners retrieve current product pricing, generate a priced order preview from a list of guide-RNA sequences, and track an order through to checkout on Synthego's eCommerce site. Authentication is by an API key passed in the SYNTHEGOAPIKEY header. Synthego was surfaced as a portfolio company of SoftBank Vision Fund.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/synthego.png
layout: provider
modified: '2026-10-06'
name: Synthego
nav: Providers
network: true
overview: 'Synthego publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Order API. Tagged areas include Company, Health Tech, Genomics, CRISPR, and Biotechnology.


  Synthego''s developer surface includes engineering blog, documentation, API reference, support, authentication, and 20 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 45.3
    developer_ergonomics: 37.5
    discoverability: 66.1
    operational_transparency: 5.3
  previous_composite: 33.6
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
    score: 23.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/synthego/synthego-2026-09-02T161631.png
security:
- kind: authentication
  name: Synthego Authentication
  slug: synthego-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Synthego Domain Security
  slug: synthego-domain-security
  summary_line: TLSv1.2 · DMARC
skill_count: 1
skills:
- name: Place a Synthego guide-RNA order
  slug: synthego-place-order
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
