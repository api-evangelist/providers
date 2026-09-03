---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The Capterra Click Report API allows software vendors to programmatically retrieve historical click data from their Capterra pay-per-click (PPC) advertising campaigns. Vendors can access click metrics
  name: Capterra Click Report API
  slug: click-report-api
artifact_total: 7
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/gartner/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/capterra-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/capterra-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/capterra-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/capterra-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/capterra-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/capterra-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/capterra-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/capterra-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/capterra-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/capterra-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/capterra-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/capterra-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/capterra-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/capterra-finops.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/capterra
- group: company
  title: ''
  type: Website
  url: https://www.capterra.com/
- group: start
  title: ''
  type: Portal
  url: https://www.capterra.com/vendors/
- group: start
  title: ''
  type: Login
  url: https://app.g2digitalmarkets.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.g2digitalmarkets.com/get-listed/start
- group: company
  title: ''
  type: Blog
  url: https://www.capterra.com/resources/
- group: docs
  title: ''
  type: Documentation
  url: https://www.capterra.com/legal/best-of-badges-methodologies_lessprioritymarkets/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.capterra.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PPC Terms
  url: https://www.capterra.com/legal/ppc-service-description/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.capterra.com/legal/privacy-policy/
- group: other
  title: ''
  type: G2 Digital Markets
  url: https://www.g2digitalmarkets.com/
- group: other
  title: ''
  type: X
  url: https://x.com/capterra
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/capterra
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Capterra
created: '2026-03-24'
description: Capterra is one of the largest software review and comparison marketplaces, helping business buyers discover, research, and select software across hundreds of categories through verified user reviews, feature comparisons, and pricing information. Founded in 1999 and acquired by Gartner in 2015, Capterra was sold to G2 alongside its sister sites GetApp and Software Advice in a deal that closed on 2026-02-05, and the three properties now operate as G2 Digital Markets — the vendor console has moved to app.g2digitalmarkets.com. For participating software vendors the properties run a pay-per-click lead-generation program, and the Capterra Click Report API lets those vendors programmatically retrieve historical click performance data across all mapped accounts. The API is credential-gated and its reference is published only inside the authenticated vendor console.
finops:
- name: Capterra Finops
  service_category: API
  slug: capterra-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/capterra.png
layout: provider
modified: '2026-08-12'
name: Capterra
nav: Providers
network: true
overview: 'Capterra publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, B2B, Click Reporting, G2 Digital Markets, and Gartner Digital Markets.


  Capterra''s developer surface includes authentication, developer portal, signup flow, engineering blog, documentation, and 24 more developer resources.'
plans:
- name: Capterra Plans Pricing
  plan_count: 0
  slug: capterra-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Capterra Rate Limits
  slug: capterra-rate-limits
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 13
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 26.6
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: authentication
  name: Capterra Authentication
  slug: capterra-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Capterra Domain Security
  slug: capterra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Capterra Vulnerability Disclosure
  slug: capterra-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: capterra
tags:
- Advertising
- B2B
- Click Reporting
- G2 Digital Markets
- Gartner Digital Markets
- Lead Generation
- Marketplace
- PPC
- Software Advice
- Software Comparison
- Software Reviews
website: https://www.capterra.com/
---
