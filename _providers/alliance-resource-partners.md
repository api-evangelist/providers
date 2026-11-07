---
access_model:
  confidence: high
  label: Anonymous public read - no key, no registration, no plans
  onboarding: unknown
  pricing: free
  public: true
  source:
  - https://www.arlp.com/wp-json/
  - plans
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Alliance Resource Partners website at www.arlp.com: the route index of the site''s content management system, catalogued as one site surface rather than a'
  name: Alliance Resource Partners Website (WordPress REST)
  slug: arlp-com-website-wordpress-rest
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://www.arlp.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alliance-resource-partners-lp
- group: operate
  title: ''
  type: Support
  url: https://www.arlp.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arlp.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arlp.com/privacy-statement/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.arlp.com/overview/default.aspx
- group: auth
  href: https://artifacts.apis.io/alliance-resource-partners/authentication/alliance-resource-partners-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alliance-resource-partners-authentication.yml
- group: design
  href: https://artifacts.apis.io/alliance-resource-partners/conventions/alliance-resource-partners-conventions.yml
  title: ''
  type: Conventions
  url: conventions/alliance-resource-partners-conventions.yml
- group: design
  href: https://artifacts.apis.io/alliance-resource-partners/errors/alliance-resource-partners-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/alliance-resource-partners-problem-types.yml
- group: design
  href: https://artifacts.apis.io/alliance-resource-partners/data-model/alliance-resource-partners-data-model.yml
  title: ''
  type: DataModel
  url: data-model/alliance-resource-partners-data-model.yml
- group: design
  href: https://artifacts.apis.io/alliance-resource-partners/lifecycle/alliance-resource-partners-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/alliance-resource-partners-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/alliance-resource-partners/conformance/alliance-resource-partners-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alliance-resource-partners-conformance.yml
- group: build
  href: https://artifacts.apis.io/alliance-resource-partners/packages/alliance-resource-partners-packages.yml
  title: ''
  type: Packages
  url: packages/alliance-resource-partners-packages.yml
- group: agent
  href: https://artifacts.apis.io/alliance-resource-partners/mcp/alliance-resource-partners-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/alliance-resource-partners-mcp.yml
- group: agent
  href: https://artifacts.apis.io/alliance-resource-partners/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/alliance-resource-partners/llms/alliance-resource-partners-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alliance-resource-partners-llms.txt
- group: other
  href: https://artifacts.apis.io/alliance-resource-partners/overlays/alliance-resource-partners-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/alliance-resource-partners-content-overlay.yaml
- group: build
  href: https://artifacts.apis.io/alliance-resource-partners/examples/_index.yml
  title: ''
  type: Examples
  url: examples/_index.yml
- group: operate
  href: https://artifacts.apis.io/alliance-resource-partners/rate-limits/alliance-resource-partners-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/alliance-resource-partners-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/alliance-resource-partners/plans/alliance-resource-partners-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alliance-resource-partners-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/alliance-resource-partners/finops/alliance-resource-partners-finops.yml
  title: ''
  type: FinOps
  url: finops/alliance-resource-partners-finops.yml
- group: auth
  href: https://artifacts.apis.io/alliance-resource-partners/security/alliance-resource-partners-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alliance-resource-partners-domain-security.yml
created: '2026-04-19'
description: 'Alliance Resource Partners, L.P. (NASDAQ: ARLP) is a diversified energy and natural-resource partnership headquartered in Tulsa, Oklahoma. It is the largest coal producer in the eastern United States, operating underground and surface mines across the Illinois Basin and Appalachia, and it holds an oil and gas mineral and royalty portfolio alongside a growth-investment arm covering other energy and infrastructure ventures. ARLP runs no developer program: it publishes no API documentation, no OpenAPI, no SDK, no API pricing and no developer portal, and the api.arlp.com and developer.arlp.com hosts once listed here do not resolve in DNS. The only machine-readable interface the company serves is the read-only WordPress REST API behind its corporate site at www.arlp.com, which returns ARLP''s own published corporate content - business segments, sustainability posture, careers, contact and legal pages, media, taxonomy and cross-content search - anonymously as JSON. Any operational
  data exchange with ARLP (customer contracts, rail and barge logistics, mine reporting, royalty statements) is a bilateral commercial agreement, not a published API product.'
examples:
- key_count: 13
  name: Alliance Resource Partners Content Types
  slug: alliance-resource-partners-content-types
- key_count: 11
  name: Alliance Resource Partners Oembed
  slug: alliance-resource-partners-oembed
- key_count: 2
  name: Alliance Resource Partners Statuses
  slug: alliance-resource-partners-statuses
- key_count: 5
  name: Alliance Resource Partners Taxonomies
  slug: alliance-resource-partners-taxonomies
finops:
- has_sources: true
  method: generated
  name: Alliance Resource Partners Finops
  primary_unit: ''
  service_category: Energy / Mining Data
  slug: alliance-resource-partners-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alliance-resource-partners.png
layout: provider
modified: '2026-09-01'
name: Alliance Resource Partners
nav: Providers
network: true
overview: 'Alliance Resource Partners publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Website (WordPress REST). Tagged areas include Coal, Mining, Energy, Royalties, and Natural Resources.


  The Alliance Resource Partners catalog on APIs.io includes 1 Spectral governance ruleset.


  Alliance Resource Partners'' developer surface includes support, authentication, code examples, and 19 more developer resources.'
plans:
- name: Alliance Resource Partners Plans Pricing
  plan_count: 0
  slug: alliance-resource-partners-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Alliance Resource Partners Rate Limits
  slug: alliance-resource-partners-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Alliance Resource Partners API Rules
  rule_count: 63
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 4
  slug: alliance-resource-partners-rules
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 30.5
    developer_ergonomics: 23.2
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 23.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 17.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/alliance-resource-partners/alliance-resource-partners-2026-06-20T171531.png
security:
- kind: authentication
  name: Alliance Resource Partners Authentication
  slug: alliance-resource-partners-authentication
  summary_line: none/http · 2 schemes
- kind: domain-security
  name: Alliance Resource Partners Domain Security
  slug: alliance-resource-partners-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Research Alliance Resource Partners corporate content
  slug: alliance-resource-partners-corporate-content-research
- name: Monitor Alliance Resource Partners page changes
  slug: alliance-resource-partners-page-change-monitoring
slug: alliance-resource-partners
tags:
- Coal
- Mining
- Energy
- Royalties
- Natural Resources
- Corporate
website: https://www.arlp.com
---
