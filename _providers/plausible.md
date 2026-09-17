---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Plausible Agentic Access
  operation_count: 18
  slug: plausible-agentic-access
  summary_line: 18 operations · 12 acting
api_count: 3
apis:
- baseURL: https://plausible.io/api/v1
  baseurl_source: declared
  description: The CustomProps API from Plausible — 2 operation(s) for customprops.
  name: Plausible CustomProps API
  slug: plausible-customprops-api
- baseURL: https://plausible.io/api
  baseurl_source: declared
  description: Submit pageviews and custom events.
  name: Plausible Events API
  slug: plausible-events-api
- baseURL: https://plausible.io/api/v1
  baseurl_source: declared
  description: The Goals API from Plausible — 2 operation(s) for goals.
  name: Plausible Goals API
  slug: plausible-goals-api
- baseURL: https://plausible.io/api/v1
  baseurl_source: declared
  description: The Guests API from Plausible — 2 operation(s) for guests.
  name: Plausible Guests API
  slug: plausible-guests-api
- baseURL: https://plausible.io/api/v2
  baseurl_source: declared
  description: Run analytics queries against site data.
  name: Plausible Query API
  slug: plausible-query-api
- baseURL: https://plausible.io/api/v1
  baseurl_source: declared
  description: The Sites API from Plausible — 2 operation(s) for sites.
  name: Plausible Sites API
  slug: plausible-sites-api
- baseURL: https://plausible.io/api/v1
  baseurl_source: declared
  description: The Teams API from Plausible — 1 operation(s) for teams.
  name: Plausible Teams API
  slug: plausible-teams-api
- baseURL: https://plausible.io/api/v1
  baseurl_source: declared
  description: The Shared Links API from Plausible — 1 operation(s) for shared links.
  name: Plausible Shared Links API
  slug: plausible-shared-links-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Plausible Events CustomProps API
  slug: open-plausible-customprops-api
- collection_type: open
  name: Plausible CustomProps Events API
  slug: open-plausible-events-api
- collection_type: open
  name: Plausible Events API
  slug: open-plausible-events
- collection_type: open
  name: Plausible Events CustomProps Goals API
  slug: open-plausible-goals-api
- collection_type: open
  name: Plausible Events CustomProps Guests API
  slug: open-plausible-guests-api
- collection_type: open
  name: Plausible Events CustomProps Query API
  slug: open-plausible-query-api
- collection_type: open
  name: Plausible Events CustomProps SharedLinks API
  slug: open-plausible-sharedlinks-api
- collection_type: open
  name: Plausible Events CustomProps Sites API
  slug: open-plausible-sites-api
- collection_type: open
  name: Plausible Sites API
  slug: open-plausible-sites
- collection_type: open
  name: Plausible Stats API
  slug: open-plausible-stats
- collection_type: open
  name: Plausible Events CustomProps Teams API
  slug: open-plausible-teams-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/overlays/plausible-sharedlinks-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/plausible-sharedlinks-api-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://github.com/plausible/analytics/blob/master/LICENSE
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/packages/plausible-packages.yml
  title: ''
  type: Packages
  url: packages/plausible-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/packages/plausible-packages.yml
  title: ''
  type: SDKs
  url: packages/plausible-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/mcp/plausible-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/plausible-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/llms/plausible-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/plausible-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/conformance/plausible-conformance.yml
  title: ''
  type: Conformance
  url: conformance/plausible-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://plausible.io/compliance
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/errors/plausible-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/plausible-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/lifecycle/plausible-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/plausible-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://plausible.io/status
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/conventions/plausible-conventions.yml
  title: ''
  type: Conventions
  url: conventions/plausible-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/changelog/plausible-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/plausible-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/components/plausible-components.yml
  title: ''
  type: Components
  url: components/plausible-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/data-model/plausible-data-model.yml
  title: ''
  type: DataModel
  url: data-model/plausible-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/sandbox/plausible-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/plausible-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/security/plausible-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/plausible-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://plausible.io/vulnerability-disclosure-program
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/plans/plausible-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/plausible-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/rate-limits/plausible-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/plausible-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/finops/plausible-finops.yml
  title: ''
  type: FinOps
  url: finops/plausible-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/mcp/plausible-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/plausible-mcp.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://plausible.io/roadmap
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/plausible
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/plausible/analytics
- group: docs
  title: ''
  type: APIReference
  url: https://plausible.io/docs/stats-api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://plausible.io/docs/data-access
- group: other
  title: ''
  type: Playground
  url: https://plausible.io/docs/stats-api-playground
- group: start
  title: ''
  type: Demo
  url: https://plausible.io/plausible.io
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://plausible.io/dpa
- group: other
  title: ''
  type: Imprint
  url: https://plausible.io/imprint
- group: company
  title: ''
  type: Bluesky
  url: https://bsky.app/profile/plausible.io
- group: company
  title: ''
  type: Mastodon
  url: https://fosstodon.org/@plausible
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/agentic-access/plausible-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/plausible-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/security/plausible-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/plausible-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/authentication/plausible-authentication.yml
  title: ''
  type: Authentication
  url: authentication/plausible-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/plausible-analytics
- group: company
  title: ''
  type: Website
  url: https://plausible.io
- group: docs
  title: ''
  type: Documentation
  url: https://plausible.io/docs
- group: docs
  title: ''
  type: APIDocumentation
  url: https://plausible.io/docs/stats-api
- group: start
  title: ''
  type: GettingStarted
  url: https://plausible.io/docs/add-website
- group: company
  title: ''
  type: Blog
  url: https://plausible.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://plausible.io/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/plausible/analytics
- group: start
  title: ''
  type: Login
  url: https://plausible.io/login
- group: start
  title: ''
  type: Signup
  url: https://plausible.io/register
- group: operate
  title: ''
  type: Support
  url: https://plausible.io/contact
- group: other
  title: ''
  type: SelfHosted
  url: https://plausible.io/self-hosted-web-analytics
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/plausible/analytics/releases
- group: commercial
  title: ''
  type: TermsOfService
  url: https://plausible.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://plausible.io/privacy
- group: other
  title: ''
  type: DataPolicy
  url: https://plausible.io/data-policy
created: '2026-03-26'
description: Plausible is an open source, privacy-friendly web analytics platform designed as a lightweight alternative to Google Analytics. It provides essential website traffic metrics without using cookies or collecting personal data, making it compliant with GDPR, CCPA, and other privacy regulations out of the box. It can be self-hosted or used as a cloud service.
finops:
- name: Plausible Finops
  service_category: Analytics
  slug: plausible-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plausible.png
layout: provider
modified: '2026-08-13'
name: Plausible
nav: Providers
network: true
overview: 'Plausible publishes 8 APIs on the [APIs.io](https://apis.io/) network, including CustomProps API, Events API, Goals API, and 5 more. Tagged areas include Analytics, Cookie-Free, Event Tracking, GDPR, and Goal Conversions.


  Plausible''s developer surface includes changelog, sandbox, API reference, authentication, documentation, getting-started guide, engineering blog, and 46 more developer resources.'
plans:
- name: Plausible Plans Pricing
  plan_count: 4
  slug: plausible-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Plausible Rate Limits
  slug: plausible-rate-limits
score:
  band: strong
  composite: 61.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 67.0
    catalog_earned_first_party: 24.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 75.0
    contract_governance: 18.2
    contract_quality: 53.5
    developer_ergonomics: 69.6
    discoverability: 74.1
    operational_transparency: 81.6
  previous_composite: 60.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/screenshots/plausible-2026-06-20T191759.png
security:
- kind: authentication
  name: Plausible Authentication
  slug: plausible-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Plausible Domain Security
  slug: plausible-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Plausible Vulnerability Disclosure
  slug: plausible-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: plausible
tags:
- Analytics
- Cookie-Free
- Event Tracking
- GDPR
- Goal Conversions
- Open-Source
- Privacy
- Self-Hosted
- Site Management
- Web Analytics
website: https://plausible.io
---
