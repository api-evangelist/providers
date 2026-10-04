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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Ascend Advanced Therapies website at www.ascend-adv.com: the route index of the site''s content management system, catalogued as one site surface rather t'
  name: Ascend Advanced Therapies Website (WordPress REST)
  slug: ascend-adv-com-website-wordpress-rest
artifact_total: 4
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ascend-advanced-therapies/refs/heads/main/capabilities/ascend-advanced-therapies-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ascend-advanced-therapies-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ascend-advanced-therapies/refs/heads/main/skills/ascend-advanced-therapies-monitor-news-insights.md
  title: ''
  type: AgentSkill
  url: skills/ascend-advanced-therapies-monitor-news-insights.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ascend-advanced-therapies/refs/heads/main/mcp/ascend-advanced-therapies-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ascend-advanced-therapies-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ascend-advanced-therapies/refs/heads/main/overlays/ascend-advanced-therapies-wp-rest-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ascend-advanced-therapies-wp-rest-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.ascend-adv.com/
- group: company
  title: ''
  type: About
  url: https://www.ascend-adv.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.ascend-adv.com/news-insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.ascend-adv.com/feed/
- group: operate
  title: ''
  type: Contact
  url: https://www.ascend-adv.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://www.ascend-adv.com/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ascend-adv.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ascend-adv.com/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.ascend-adv.com/cookie-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ascend-advanced-therapies/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ascend-advanced-therapies/refs/heads/main/well-known/ascend-advanced-therapies-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ascend-advanced-therapies-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ascend-advanced-therapies/refs/heads/main/security/ascend-advanced-therapies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ascend-advanced-therapies-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ascend-advanced-therapies/refs/heads/main/llms/ascend-advanced-therapies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ascend-advanced-therapies-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ascend-advanced-therapies/refs/heads/main/authentication/ascend-advanced-therapies-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ascend-advanced-therapies-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ascend-advanced-therapies/refs/heads/main/errors/ascend-advanced-therapies-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ascend-advanced-therapies-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ascend-advanced-therapies/refs/heads/main/conventions/ascend-advanced-therapies-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ascend-advanced-therapies-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ascend-advanced-therapies/refs/heads/main/data-model/ascend-advanced-therapies-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ascend-advanced-therapies-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ascend-advanced-therapies/refs/heads/main/conformance/ascend-advanced-therapies-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ascend-advanced-therapies-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ascend-advanced-therapies/refs/heads/main/lifecycle/ascend-advanced-therapies-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ascend-advanced-therapies-lifecycle.yml
created: '2026-07-17'
description: Ascend Advanced Therapies is a gene-to-GMP contract development and manufacturing organization (CDMO) for advanced therapies, specializing in adeno-associated virus (AAV) vector development and manufacture for gene therapies, immunotherapies, oncolytics, and vaccines. Formed in 2023 when expert teams merged behind more than $130M of funding, and aligned with ABL, Inc. since late 2024, Ascend operates GMP manufacturing, aseptic fill-finish, and analytical facilities in Rockville, Maryland and Alachua, Florida alongside European capacity. Services span process development, gene therapy formulation, scalable manufacturing, in-house fill-finish, GMP QC testing, long-read NGS for viral vectors, and potency assay development, built on its EpyQ production system and proprietary AAV yield enhancers. Ascend is a life-science manufacturer rather than a software vendor and publishes no commercial product API; the only machine-readable interface it exposes is the WordPress REST content
  API behind its corporate website, captured here for discovery.
image: https://www.ascend-adv.com/wp-content/uploads/2025/02/cropped-favicon-192x192.png
layout: provider
modified: '2026-07-19'
name: Ascend Advanced Therapies
nav: Providers
network: true
overview: 'Ascend Advanced Therapies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Gene Therapy, Cell Therapy, and Contract Manufacturing.


  Ascend Advanced Therapies'' developer surface includes engineering blog, authentication, and 21 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 25.6
    discoverability: 64.3
    operational_transparency: 0.0
  previous_composite: 17.4
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/ascend-advanced-therapies/refs/heads/main/screenshots/ascend-advanced-therapies-2026-07-25T201402.png
security:
- kind: authentication
  name: Ascend Advanced Therapies Authentication
  slug: ascend-advanced-therapies-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ascend Advanced Therapies Domain Security
  slug: ascend-advanced-therapies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ascend-advanced-therapies
tags:
- Company
- Biotechnology
- Gene Therapy
- Cell Therapy
- Contract Manufacturing
- Life Sciences
- Pharmaceuticals
- CDMO
- AAV
website: https://www.ascend-adv.com/
---
