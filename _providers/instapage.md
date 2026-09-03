---
access_model:
  confidence: high
  label: Self-serve signup, 14-day free trial, API included on every paid plan with a tiered daily call quota
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - https://instapage.com/plans
  - https://devdocs.instapage.com/
  trial: true
  try_now: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Instapage Agentic Access
  operation_count: 39
  slug: instapage-agentic-access
  summary_line: 39 operations · 23 acting
api_count: 11
apis:
- baseURL: https://api.instapage.com/v1
  baseurl_source: declared
  description: Create, read, rename and delete Instapage workspaces — the top-level tenant container that holds a customer's landing pages, integrations, domains and assets.
  name: Instapage Workspaces API
  slug: instapage-workspaces-api
- baseURL: https://api.instapage.com/v1
  baseurl_source: declared
  description: Bulk visit, conversion and lead statistics for pages and experiences.
  name: Instapage Analytics API
  slug: instapage-analytics-api
- baseURL: https://api.instapage.com/v1
  baseurl_source: declared
  description: Image asset folders and images inside a workspace.
  name: Instapage Assets API
  slug: instapage-assets-api
- baseURL: https://api.instapage.com/v1
  baseurl_source: declared
  description: Collections are groups of pages sharing one template with placeholder-driven content, plus the individual collection pages inside them.
  name: Instapage Collections API
  slug: instapage-collections-api
- baseURL: https://api.instapage.com/v1
  baseurl_source: declared
  description: Custom domains connected to a workspace.
  name: Instapage Domains API
  slug: instapage-domains-api
- baseURL: https://api.instapage.com/v1
  baseurl_source: declared
  description: A/B and AI experiments running against landing pages.
  name: Instapage Experiments API
  slug: instapage-experiments-api
- baseURL: https://api.instapage.com/v1
  baseurl_source: declared
  description: Retrieve and delete the lead data captured by landing page forms.
  name: Instapage Form Submissions API
  slug: instapage-form-submissions-api
- baseURL: https://api.instapage.com/v1
  baseurl_source: declared
  description: Groups (folders) organise landing pages inside a workspace.
  name: Instapage Groups API
  slug: instapage-groups-api
- baseURL: https://api.instapage.com/v1
  baseurl_source: declared
  description: Create, retrieve, update, publish, export and delete Instapage landing pages.
  name: Instapage Pages API
  slug: instapage-pages-api
- baseURL: https://api.instapage.com/v1
  baseurl_source: declared
  description: Personalized experiences attached to a landing page.
  name: Instapage Personalizations API
  slug: instapage-personalizations-api
- baseURL: https://api.instapage.com/v1
  baseurl_source: declared
  description: Manage the people who have access to a workspace and their access levels.
  name: Instapage Team Members API
  slug: instapage-team-members-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Instapage Analytics API
  slug: open-instapage-analytics
- collection_type: open
  name: Instapage Assets API
  slug: open-instapage-assets
- collection_type: open
  name: Instapage Collections API
  slug: open-instapage-collections
- collection_type: open
  name: Instapage Domains API
  slug: open-instapage-domains
- collection_type: open
  name: Instapage Experiments API
  slug: open-instapage-experiments
- collection_type: open
  name: Instapage Form Submissions API
  slug: open-instapage-form-submissions
- collection_type: open
  name: Instapage Groups API
  slug: open-instapage-groups
- collection_type: open
  name: Instapage Pages API
  slug: open-instapage-pages
- collection_type: open
  name: Instapage Personalizations API
  slug: open-instapage-personalizations
- collection_type: open
  name: Instapage Team Members API
  slug: open-instapage-team-members
- collection_type: open
  name: Instapage Workspaces API
  slug: open-instapage-workspaces-api
- collection_type: open
  name: Instapage API
  slug: open-instapage
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/instapage-team-members-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/instapage-pages-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/instapage-groups-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/instapage-personalizations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/instapage-collections-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/instapage-experiments-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/instapage-analytics-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/instapage-form-submissions-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/instapage-domains-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/instapage-assets-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/instapage-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/instapage-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instapage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/instapage-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Instapage
- group: company
  title: ''
  type: Website
  url: https://instapage.com
- group: docs
  title: ''
  type: Documentation
  url: https://devdocs.instapage.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://instapage.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.instapage.com/auth/signup
- group: company
  title: ''
  type: Blog
  url: https://instapage.com/blog
- group: operate
  title: ''
  type: Help Center
  url: https://help.instapage.com
- group: other
  title: ''
  type: API Overview
  url: https://instapage.com/api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/instapage
- group: build
  title: ''
  type: Packages
  url: packages/instapage-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/instapage-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/instapage-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/instapage-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/instapage-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/instapage-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/instapage-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/instapage-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/instapage-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/instapage-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/instapage-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.instapage.com/
- group: auth
  title: ''
  type: Security
  url: https://policies.airslate.com/bug-bounty-program
- group: auth
  title: ''
  type: Compliance
  url: https://instapage.com/security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devdocs.instapage.com/
- group: docs
  title: ''
  type: APIReference
  url: https://devdocs.instapage.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://devdocs.instapage.com/#getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.instapage.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://instapage.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://instapage.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://app.instapage.com/auth/signup
- group: start
  title: ''
  type: Login
  url: https://app.instapage.com/auth/login/
created: '2026-05-11'
description: Instapage is a landing page and post-click optimization platform that lets marketers build, personalize, A/B test, and analyze landing pages used in paid advertising and conversion campaigns. The platform includes a drag and drop builder, AdMap for ad-to-page connection, heatmaps, experiments, and AI-powered content generation, and integrates with major ad platforms, CRMs, and marketing automation tools. Instapage's REST API provides programmatic access to landing pages, leads, accounts, and team members using a Personal API Token for authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/instapage.png
layout: provider
modified: '2026-08-13'
name: Instapage
nav: Providers
network: true
overview: 'Instapage publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Workspaces API, Analytics API, Assets API, and 8 more. Tagged areas include Landing Pages, Conversion Optimization, Marketing, A/B Testing, and Post-Click Optimization.


  Instapage''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, changelog, API reference, and 39 more developer resources.'
plans:
- name: Instapage Plans Pricing
  plan_count: 3
  slug: instapage-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Instapage Rate Limits
  slug: instapage-rate-limits
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 21
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 17.8
    developer_ergonomics: 50.6
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 57.9
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instapage/refs/heads/main/screenshots/instapage-2026-06-20T183418.png
security:
- kind: authentication
  name: Instapage Authentication
  slug: instapage-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Instapage Domain Security
  slug: instapage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Instapage Vulnerability Disclosure
  slug: instapage-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Instapage Trust Center
  slug: instapage-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CCPA/CPRA
slug: instapage
tags:
- Landing Pages
- Conversion Optimization
- Marketing
- A/B Testing
- Post-Click Optimization
- Lead Generation
website: https://instapage.com
---
