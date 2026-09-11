---
access_model:
  confidence: medium
  label: Free and open — anonymous, unauthenticated public read API; no signup, no key, no plans
  onboarding: unknown
  pricing: free
  public: true
  source:
  - '{''url'': ''https://www.fmcs.gov/wp-json/wp/v2/posts?per_page=1'', ''status'': 200, ''note'': ''returns JSON anonymously with no credential of any kind (probed 2026-09-09)''}'
  - '{''url'': ''https://www.fmcs.gov/wp-json/wp/v2/settings'', ''status'': 401, ''note'': ''the administrative half of the same host refuses anonymous callers (rest_forbidden)''}'
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-09-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Federal Mediation And Conciliation Service Agentic Access
  operation_count: 31
  slug: federal-mediation-and-conciliation-service-agentic-access
  summary_line: 31 operations
api_count: 1
apis:
- baseURL: https://www.fmcs.gov/wp-json
  baseurl_source: declared
  description: The anonymous, read-only WordPress REST API behind www.fmcs.gov. Serves the agency's 117 programme and services pages, its 1,122-item document library (where the monthly F-7 collective bargaining noti
  name: FMCS Public Content API
  slug: fmcs-public-content-api
artifact_total: 9
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/federal-mediation-and-conciliation-service-wp-content-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/federal-mediation-and-conciliation-service-wp-content-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/federal-mediation-and-conciliation-service-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/federal-mediation-and-conciliation-service-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/federal-mediation-and-conciliation-service-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/federal-mediation-and-conciliation-service-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/federal-mediation-and-conciliation-service-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/federal-mediation-and-conciliation-service-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/federal-mediation-and-conciliation-service-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/federal-mediation-and-conciliation-service-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/federal-mediation-and-conciliation-service-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/federal-mediation-and-conciliation-service-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/federal-mediation-and-conciliation-service-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/federal-mediation-and-conciliation-service-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/federal-mediation-and-conciliation-service-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.fmcs.gov/vulnerability-disclosure-policy/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-mediation-and-conciliation-service-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/federal-mediation-and-conciliation-service
- group: company
  title: ''
  type: Website
  url: https://www.fmcs.gov/
- group: company
  title: ''
  type: Blog
  url: https://www.fmcs.gov/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.fmcs.gov/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fmcs.gov/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fmcs.gov/privacy-policy/
created: '2024-12-03'
description: The Federal Mediation and Conciliation Service (FMCS) is an independent United States federal agency created by the Taft-Hartley Act of 1947 to prevent, minimize and resolve work stoppages and labor disputes. It provides collective bargaining mediation, grievance and workplace mediation, arbitrator panel referral, facilitation, dispute-resolution systems design, regulatory negotiations and labor- management partnership services across seventeen published service lines. FMCS also administers the statutory F-7 notice under 29 U.S.C. 158(d) and publishes those notices monthly as Excel workbooks. FMCS publishes no developer programme and no specification of its own; its public website runs on WordPress and serves an anonymous, read-only REST API at https://www.fmcs.gov/wp-json over the agency's pages, document library, neutrals directory, training events and service taxonomy, which is catalogued here.
examples:
- key_count: 13
  name: Federal Mediation And Conciliation Service Taxonomies
  slug: federal-mediation-and-conciliation-service-taxonomies
- key_count: 16
  name: Federal Mediation And Conciliation Service Types
  slug: federal-mediation-and-conciliation-service-types
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-mediation-and-conciliation-service.png
layout: provider
modified: '2026-09-09'
name: Federal Mediation and Conciliation Service
nav: Providers
network: true
overview: 'Federal Mediation and Conciliation Service publishes 1 API on the [APIs.io](https://apis.io/) network: FMCS Public Content API. Tagged areas include Federal-Government, Labor, Mediation, Arbitration, and Dispute-Resolution.


  Federal Mediation and Conciliation Service''s developer surface includes authentication, engineering blog, support, and 21 more developer resources.'
plans:
- name: Federal Mediation And Conciliation Service Plans Pricing
  plan_count: 0
  slug: federal-mediation-and-conciliation-service-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Federal Mediation And Conciliation Service Rate Limits
  slug: federal-mediation-and-conciliation-service-rate-limits
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 24.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 16.5
    developer_ergonomics: 20.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 3.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-mediation-and-conciliation-service/refs/heads/main/screenshots/federal-mediation-and-conciliation-service-2026-06-20T181124.png
security:
- kind: authentication
  name: Federal Mediation And Conciliation Service Authentication
  slug: federal-mediation-and-conciliation-service-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Federal Mediation And Conciliation Service Domain Security
  slug: federal-mediation-and-conciliation-service-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Federal Mediation And Conciliation Service Vulnerability Disclosure
  slug: federal-mediation-and-conciliation-service-vulnerability-disclosure
  summary_line: contact published
slug: federal-mediation-and-conciliation-service
tags:
- Federal-Government
- Labor
- Mediation
- Arbitration
- Dispute-Resolution
- Government
- Public-Sector
- Content
website: https://www.fmcs.gov/
---
