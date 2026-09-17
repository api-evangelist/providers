---
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.2
  scored_at: '2026-09-16'
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
artifact_total: 13
asyncapis:
- description: ''
  name: Geocitation Webhooks
  slug: geocitation-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.geocitation.io
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/geocitation/refs/heads/main/agentic-access/geocitation-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/geocitation-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/geocitation/refs/heads/main/security/geocitation-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/geocitation-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/geocitation/refs/heads/main/security/geocitation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geocitation-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/geocitation/refs/heads/main/authentication/geocitation-authentication.yml
  title: ''
  type: Authentication
  url: authentication/geocitation-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/geocitation/refs/heads/main/errors/geocitation-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/geocitation-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/geocitation/refs/heads/main/rate-limits/geocitation-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/geocitation-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/geocitation/refs/heads/main/plans/geocitation-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/geocitation-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/geocitation/refs/heads/main/conventions/geocitation-conventions.yml
  title: ''
  type: Conventions
  url: conventions/geocitation-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/geocitation/refs/heads/main/lifecycle/geocitation-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/geocitation-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/geocitation/refs/heads/main/conformance/geocitation-conformance.yml
  title: ''
  type: Conformance
  url: conformance/geocitation-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.geocitation.io/en/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/geocitation/refs/heads/main/data-model/geocitation-data-model.yml
  title: ''
  type: DataModel
  url: data-model/geocitation-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/geocitation/refs/heads/main/asyncapi/geocitation-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/geocitation-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/geocitation/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/geocitation/refs/heads/main/llms/geocitation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/geocitation-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/geocitation/refs/heads/main/overlays/geocitation-openapi-overlay.yaml
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
image: https://www.geocitation.io/icon.svg
layout: provider
modified: '2026-09-10'
name: GEOCitation
nav: Providers
network: true
overview: 'GEOCitation publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Audits API, Gdpr API, Health API, and 3 more. Tagged areas include SEO, Geo, AEO, AI Search Visibility, and Content Intelligence.


  The GEOCitation catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GEOCitation''s developer surface includes authentication, documentation, getting-started guide, pricing, support, signup flow, and 19 more developer resources.'
plans:
- name: Geocitation Plans Pricing
  plan_count: 5
  slug: geocitation-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Geocitation Rate Limits
  slug: geocitation-rate-limits
score:
  band: strong
  composite: 55.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 52.7
    developer_ergonomics: 56.5
    discoverability: 68.5
    operational_transparency: 28.9
  previous_composite: 55.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
slug: geocitation
tags:
- SEO
- Geo
- AEO
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
