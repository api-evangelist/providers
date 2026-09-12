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
  schema_version: 0.2
  score: 37.2
  scored_at: '2026-09-12'
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
  description: 'Asynchronous REST API to launch AEO/GEO audits (Market Intelligence and Gap Analysis), poll status, and retrieve structured JSON output. API-key auth via X-API-Key header; HMAC-SHA256 signed webhooks '
  name: GEOCitation Audit API
  slug: geocitation-audit-api
artifact_total: 8
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
  title: ''
  type: AgenticAccess
  url: agentic-access/geocitation-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/geocitation-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/geocitation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/geocitation-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/geocitation-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/geocitation-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/geocitation-plans-pricing.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/geocitation-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/geocitation-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/geocitation-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.geocitation.io/en/security
- group: design
  title: ''
  type: DataModel
  url: data-model/geocitation-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/geocitation-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/geocitation-llms.txt
- group: other
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
overview: 'GEOCitation publishes 1 API on the [APIs.io](https://apis.io/) network: Audit API. Tagged areas include SEO, GEO, AEO, AI Search Visibility, and Content Intelligence.


  The GEOCitation catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GEOCitation''s developer surface includes authentication, documentation, getting-started guide, pricing, support, signup flow, and 19 more developer resources.'
plans:
- name: Geocitation Plans Pricing
  plan_count: 5
  slug: geocitation-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Geocitation Rate Limits
  slug: geocitation-rate-limits
score:
  band: strong
  composite: 55.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 54.4
    developer_ergonomics: 56.5
    discoverability: 68.5
    operational_transparency: 28.9
  previous_composite: 55.4
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.21.0
  scored_at: '2026-09-12'
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
- GEO
- AEO
- AI Search Visibility
- Content Intelligence
- Competitive Intelligence
- Marketing
- MarTech
- White-label
- Agency Tooling
- Web Data & Analytics
website: https://www.geocitation.io
---
