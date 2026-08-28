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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Instapage Agentic Access
  operation_count: 39
  slug: instapage-agentic-access
  summary_line: 39 operations · 23 acting
api_count: 12
apis:
- description: The Instapage Public API is a REST API over the Instapage landing page and post-click optimization platform, exposing workspaces, team members, landing pages, page groups, personalized experiences, co
  name: Instapage Public API
  slug: public-api
- description: Create, read, rename and delete Instapage workspaces — the top-level tenant container that holds a customer's landing pages, integrations, domains and assets.
  name: Instapage Workspaces API
  slug: instapage-workspaces-api
- description: Bulk-invite, re-role and remove the people with access to an Instapage workspace, including the inheritOwnerContextInPublicApi flag that charges a member's API calls to the workspace owner's daily quo
  name: Instapage Team Members API
  slug: instapage-team-members
- description: List, search, update, delete, publish, unpublish, import and export Instapage landing pages, including Instapage-JSON round-tripping and published-URL changes.
  name: Instapage Pages API
  slug: instapage-pages
- description: Manage the groups (folders) that organise landing pages inside an Instapage workspace.
  name: Instapage Groups API
  slug: instapage-groups
- description: Retrieve the personalized experiences attached to an Instapage landing page, including which one is the default experience.
  name: Instapage Personalizations API
  slug: instapage-personalizations
- description: Read Instapage collections and their placeholder templates, and create, publish, unpublish and delete the individual collection pages inside them — the programmatic-SEO surface.
  name: Instapage Collections API
  slug: instapage-collections
- description: List the Manual and AI experiments running against Instapage landing pages, with their DRAFT / RUNNING / ENDED / ARCHIVED status and timing.
  name: Instapage Experiments API
  slug: instapage-experiments
- description: Retrieve bulk visit, conversion and lead statistics for Instapage pages and experiences, grouped by page or variation over hourly, daily, monthly or yearly UTC windows.
  name: Instapage Analytics API
  slug: instapage-analytics
- description: Retrieve and permanently delete the lead records captured by forms on Instapage landing pages, paged with an opaque nextPageToken cursor.
  name: Instapage Form Submissions API
  slug: instapage-form-submissions
- description: List the custom domains connected to an Instapage workspace, with connection status, SSL status and custom 404 configuration.
  name: Instapage Domains API
  slug: instapage-domains
- description: List Instapage image asset folders, list the images inside them, and upload new images via multipart/form-data.
  name: Instapage Assets API
  slug: instapage-assets
artifact_total: 32
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
overview: 'Instapage publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Public API, Workspaces API, Team Members API, and 9 more. Tagged areas include Landing Pages, Conversion Optimization, Marketing, A/B Testing, and Post-Click Optimization.


  Instapage''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, changelog, API reference, and 29 more developer resources.'
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
  composite: 46.4
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 16.7
    contract_quality: 17.8
    developer_ergonomics: 56.5
    discoverability: 74.1
    governance: 16.7
    operational_transparency: 65.8
  previous_composite: 46.4
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
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
