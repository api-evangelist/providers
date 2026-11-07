---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
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
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Geocitation Agentic Access
  operation_count: 17
  slug: geocitation-agentic-access
  summary_line: 17 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.geocitation.io/v1
  baseurl_source: declared
  description: The audits API from GEOCitation — 8 operation(s) for audits.
  name: GEOCitation Audits API
  slug: geocitation-audits-api
- baseURL: https://api.geocitation.io/v1
  baseurl_source: declared
  description: The gdpr API from GEOCitation — 1 operation(s) for gdpr.
  name: GEOCitation Gdpr API
  slug: geocitation-gdpr-api
- baseURL: https://api.geocitation.io/v1
  baseurl_source: declared
  description: The health API from GEOCitation — 2 operation(s) for health.
  name: GEOCitation Health API
  slug: geocitation-health-api
- baseURL: https://api.geocitation.io/v1
  baseurl_source: declared
  description: The meta API from GEOCitation — 3 operation(s) for meta.
  name: GEOCitation Meta API
  slug: geocitation-meta-api
- baseURL: https://api.geocitation.io/v1
  baseurl_source: declared
  description: The opt-out API from GEOCitation — 1 operation(s) for opt-out.
  name: GEOCitation Opt Out API
  slug: geocitation-opt-out-api
- baseURL: https://api.geocitation.io/v1
  baseurl_source: declared
  description: The usage API from GEOCitation — 1 operation(s) for usage.
  name: GEOCitation Usage API
  slug: geocitation-usage-api
- baseURL: https://api.geocitation.io/v1
  baseurl_source: declared
  description: The agent-tasks API from GEOCitation — 1 operation(s) for agent-tasks.
  name: GEOCitation Agent Tasks API
  slug: geocitation-agent-tasks-api
- baseURL: https://api.geocitation.io/v1
  baseurl_source: declared
  description: The agents API from GEOCitation — 9 operation(s) for agents.
  name: GEOCitation Agents API
  slug: geocitation-agents-api
- baseURL: https://api.geocitation.io/v1
  baseurl_source: declared
  description: The campaigns API from GEOCitation — 8 operation(s) for campaigns.
  name: GEOCitation Campaigns API
  slug: geocitation-campaigns-api
- baseURL: https://api.geocitation.io/v1
  baseurl_source: declared
  description: The crawler-traffic API from GEOCitation — 3 operation(s) for crawler-traffic.
  name: GEOCitation Crawler Traffic API
  slug: geocitation-crawler-traffic-api
- baseURL: https://api.geocitation.io/v1
  baseurl_source: declared
  description: The google-auth API from GEOCitation — 4 operation(s) for google-auth.
  name: GEOCitation Google Auth API
  slug: geocitation-google-auth-api
- baseURL: https://api.geocitation.io/v1
  baseurl_source: declared
  description: The report-pptx API from GEOCitation — 4 operation(s) for report-pptx.
  name: GEOCitation Report Pptx API
  slug: geocitation-report-pptx-api
- baseURL: https://api.geocitation.io/v1
  baseurl_source: declared
  description: The user-agents API from GEOCitation — 2 operation(s) for user-agents.
  name: GEOCitation User Agents API
  slug: geocitation-user-agents-api
artifact_total: 25
asyncapis:
- description: ''
  name: Geocitation Webhooks
  slug: geocitation-webhooks
common:
- group: other
  href: https://artifacts.apis.io/geocitation/capabilities/geocitation-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/geocitation-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.geocitation.io
- group: agent
  href: https://artifacts.apis.io/geocitation/agentic-access/geocitation-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/geocitation-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/geocitation/security/geocitation-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/geocitation-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/geocitation/security/geocitation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geocitation-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/geocitation/authentication/geocitation-authentication.yml
  title: ''
  type: Authentication
  url: authentication/geocitation-authentication.yml
- group: design
  href: https://artifacts.apis.io/geocitation/errors/geocitation-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/geocitation-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/geocitation/rate-limits/geocitation-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/geocitation-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/geocitation/plans/geocitation-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/geocitation-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/geocitation/conventions/geocitation-conventions.yml
  title: ''
  type: Conventions
  url: conventions/geocitation-conventions.yml
- group: design
  href: https://artifacts.apis.io/geocitation/lifecycle/geocitation-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/geocitation-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/geocitation/conformance/geocitation-conformance.yml
  title: ''
  type: Conformance
  url: conformance/geocitation-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.geocitation.io/en/security
- group: design
  href: https://artifacts.apis.io/geocitation/data-model/geocitation-data-model.yml
  title: ''
  type: DataModel
  url: data-model/geocitation-data-model.yml
- group: design
  href: https://artifacts.apis.io/geocitation/asyncapi/geocitation-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/geocitation-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/geocitation/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/geocitation/llms/geocitation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/geocitation-llms.txt
- group: other
  href: https://artifacts.apis.io/geocitation/overlays/geocitation-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/geocitation-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.geocitation.io/en
- group: docs
  title: ''
  type: Documentation
  url: https://www.geocitation.io/en/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://www.geocitation.io/en/documentation/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.geocitation.io/en/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.geocitation.io/en/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.geocitation.io/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.geocitation.io/en/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.geocitation.io/en/login
created: '2026-09-10'
description: White-label AEO/GEO (Answer Engine / Generative Engine Optimization) audit API for SEO agencies and SaaS platforms. A single async REST API that runs AI-visibility/citation-gap audits and returns structured JSON with citation probabilities, entity/semantic-cluster data, E-E-A-T scores, and content recommendations.
finops:
- has_sources: true
  method: derived
  name: Geocitation Finops
  primary_unit: seat
  service_category: ''
  slug: geocitation-finops
  template: false
image: https://www.geocitation.io/icon.svg
layout: provider
modified: '2026-09-10'
name: GEOCitation
nav: Providers
network: true
overview: 'GEOCitation publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audits API, Gdpr API, Health API, and 10 more. Tagged areas include SEO, Geo, Answer Engine Optimization, AI Search Visibility, and Content Intelligence.


  The GEOCitation catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  GEOCitation''s developer surface includes authentication, documentation, getting-started guide, pricing, support, signup flow, and 20 more developer resources.'
plans:
- name: Geocitation Plans Pricing
  plan_count: 6
  slug: geocitation-plans-pricing
- name: Geocitation Price Estimates
  plan_count: 0
  slug: geocitation-price-estimates
random_paper: 22
rate_limits:
- limit_count: 2
  name: Geocitation Rate Limits
  slug: geocitation-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: GEOCitation API Rules
  rule_count: 50
  severity_counts:
    error: 38
    hint: 0
    info: 4
    warn: 8
  slug: geocitation-rules
score:
  band: strong
  composite: 60.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 52.5
    developer_ergonomics: 56.5
    discoverability: 66.1
    operational_transparency: 28.9
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 68.4
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/geocitation/geocitation-2026-10-11T104807.png
security:
- kind: authentication
  name: Geocitation Authentication
  slug: geocitation-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Geocitation Domain Security
  slug: geocitation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Geocitation Trust Center
  slug: geocitation-trust-center
  summary_line: SOC 2, GDPR
skill_count: 2
skills:
- name: Run a GEOCitation Gap-Analysis audit for a URL
  slug: geocitation-run-gap-audit
- name: Run a GEOCitation Market audit and retrieve the report
  slug: geocitation-run-market-audit
slug: geocitation
tags:
- SEO
- Geo
- Answer Engine Optimization
- AI Search Visibility
- Content Intelligence
- Competitive Intelligence
- Marketing
- MarTech
- White Label
- Agency Tooling
- Web Data & Analytics
website: https://www.geocitation.io
---
