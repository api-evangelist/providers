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
  schema_version: '0.2'
  score: 32.1
  scored_at: '2026-09-16'
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
  description: The published neutrals directory and site author list. Personal data.
  name: Federal Mediation and Conciliation Service Directory API
  slug: federal-mediation-and-conciliation-service-directory-api
- baseURL: https://www.fmcs.gov/wp-json
  baseurl_source: declared
  description: Registered content types, taxonomies, statuses and oEmbed.
  name: Federal Mediation and Conciliation Service Discovery API
  slug: federal-mediation-and-conciliation-service-discovery-api
- baseURL: https://www.fmcs.gov/wp-json
  baseurl_source: declared
  description: The media library — F-7 notice workbooks, FOIA reports, audit reports and programme PDFs.
  name: Federal Mediation and Conciliation Service Documents API
  slug: federal-mediation-and-conciliation-service-documents-api
- baseURL: https://www.fmcs.gov/wp-json
  baseurl_source: declared
  description: FMCS training and convening announcements and their registration taxonomies.
  name: Federal Mediation and Conciliation Service Events API
  slug: federal-mediation-and-conciliation-service-events-api
- baseURL: https://www.fmcs.gov/wp-json
  baseurl_source: declared
  description: The FAQ post type classified by the FMCS service taxonomy.
  name: Federal Mediation and Conciliation Service FAQ API
  slug: federal-mediation-and-conciliation-service-faq-api
- baseURL: https://www.fmcs.gov/wp-json
  baseurl_source: declared
  description: Posts published to www.fmcs.gov, including the agency history timeline.
  name: Federal Mediation and Conciliation Service News API
  slug: federal-mediation-and-conciliation-service-news-api
- baseURL: https://www.fmcs.gov/wp-json
  baseurl_source: declared
  description: Programme, services and administrative pages.
  name: Federal Mediation and Conciliation Service Pages API
  slug: federal-mediation-and-conciliation-service-pages-api
- baseURL: https://www.fmcs.gov/wp-json
  baseurl_source: declared
  description: Cross-type site search.
  name: Federal Mediation and Conciliation Service Search API
  slug: federal-mediation-and-conciliation-service-search-api
- baseURL: https://www.fmcs.gov/wp-json
  baseurl_source: declared
  description: Categories, tags and the FMCS service taxonomy.
  name: Federal Mediation and Conciliation Service Taxonomy API
  slug: federal-mediation-and-conciliation-service-taxonomy-api
artifact_total: 17
common:
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/federal-mediation-and-conciliation-service/refs/heads/main/openapi/_original/federal-mediation-and-conciliation-service-wp-content-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/federal-mediation-and-conciliation-service-wp-content-openapi.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/federal-mediation-and-conciliation-service/refs/heads/main/overlays/federal-mediation-and-conciliation-service-wp-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/federal-mediation-and-conciliation-service-wp-content-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/federal-mediation-and-conciliation-service/refs/heads/main/authentication/federal-mediation-and-conciliation-service-authentication.yml
  title: ''
  type: Authentication
  url: authentication/federal-mediation-and-conciliation-service-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/federal-mediation-and-conciliation-service/refs/heads/main/conventions/federal-mediation-and-conciliation-service-conventions.yml
  title: ''
  type: Conventions
  url: conventions/federal-mediation-and-conciliation-service-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/federal-mediation-and-conciliation-service/refs/heads/main/errors/federal-mediation-and-conciliation-service-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/federal-mediation-and-conciliation-service-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/federal-mediation-and-conciliation-service/refs/heads/main/lifecycle/federal-mediation-and-conciliation-service-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/federal-mediation-and-conciliation-service-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/federal-mediation-and-conciliation-service/refs/heads/main/conformance/federal-mediation-and-conciliation-service-conformance.yml
  title: ''
  type: Conformance
  url: conformance/federal-mediation-and-conciliation-service-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/federal-mediation-and-conciliation-service/refs/heads/main/data-model/federal-mediation-and-conciliation-service-data-model.yml
  title: ''
  type: DataModel
  url: data-model/federal-mediation-and-conciliation-service-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/federal-mediation-and-conciliation-service/refs/heads/main/rate-limits/federal-mediation-and-conciliation-service-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/federal-mediation-and-conciliation-service-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/federal-mediation-and-conciliation-service/refs/heads/main/plans/federal-mediation-and-conciliation-service-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/federal-mediation-and-conciliation-service-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/federal-mediation-and-conciliation-service/refs/heads/main/packages/federal-mediation-and-conciliation-service-packages.yml
  title: ''
  type: Packages
  url: packages/federal-mediation-and-conciliation-service-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/federal-mediation-and-conciliation-service/refs/heads/main/mcp/federal-mediation-and-conciliation-service-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/federal-mediation-and-conciliation-service-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/federal-mediation-and-conciliation-service/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/federal-mediation-and-conciliation-service/refs/heads/main/llms/federal-mediation-and-conciliation-service-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/federal-mediation-and-conciliation-service-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/federal-mediation-and-conciliation-service/refs/heads/main/agentic-access/federal-mediation-and-conciliation-service-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/federal-mediation-and-conciliation-service-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/federal-mediation-and-conciliation-service/refs/heads/main/security/federal-mediation-and-conciliation-service-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/federal-mediation-and-conciliation-service-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.fmcs.gov/vulnerability-disclosure-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/federal-mediation-and-conciliation-service/refs/heads/main/security/federal-mediation-and-conciliation-service-domain-security.yml
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
modified: '2026-09-16'
name: Federal Mediation and Conciliation Service
nav: Providers
network: true
overview: 'Federal Mediation and Conciliation Service publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Directory API, Discovery API, Documents API, and 6 more. Tagged areas include Federal-Government, Labor, Mediation, Arbitration, and Dispute Resolution.


  Federal Mediation and Conciliation Service''s developer surface includes authentication, engineering blog, support, and 21 more developer resources.'
plans:
- name: Federal Mediation And Conciliation Service Plans Pricing
  plan_count: 0
  slug: federal-mediation-and-conciliation-service-plans-pricing
random_paper: 13
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
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 16.5
    developer_ergonomics: 20.8
    discoverability: 68.5
    operational_transparency: 10.5
  previous_composite: 28.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
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
- Dispute Resolution
- Government
- Public Sector
- Content
website: https://www.fmcs.gov/
---
