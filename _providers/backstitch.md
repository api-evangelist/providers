---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: RESTful JSON API to build and manage backstitch topics — content feeds assembled from social, RSS, video, deals, subreddit, and custom sources with include/exclude/NSFW filters — and to retrieve norma
  name: backstitch Content Curation API
  slug: backstitch-content-curation-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/backstitch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.backstitch.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.backstit.ch/api/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.backstit.ch/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/backstitch
- group: operate
  title: ''
  type: Support
  url: https://www.backstitch.io/help
- group: company
  title: ''
  type: Blog
  url: https://www.backstitch.io/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.backstitch.io/website-privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.backstitch.io/
- group: auth
  title: ''
  type: Authentication
  url: authentication/backstitch-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/backstitch-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/backstitch-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/backstitch-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/backstitch-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/backstitch-components.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/backstitch-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/backstitch-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.backstit.ch/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.backstitch.com/support-topic/getting-started/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.backstitch.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.backstitch.io/terms-of-service
- group: start
  title: ''
  type: Login
  url: https://studio.backstit.ch/
- group: design
  title: ''
  type: Conformance
  url: conformance/backstitch-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/backstitch-trust-center.yml
created: '2026-07-17'
description: backstitch is a Techstars-backed Kansas City company that operates an employee and total-rewards communications platform (drag-and-drop newsletters, a branded mobile employee app, and personalized total-compensation statements) alongside a developer-facing content-curation API. The backstitch API lets applications build and manage "topics" that aggregate and filter content from social, RSS, video, deals, and custom sources, then retrieve normalized result objects (articles, statuses, photos, videos, products, services, hotels) or embed them with a drop-in JavaScript widget. The API is offered in a legacy v1 and a recommended v2 over REST/JSON, authenticated with an Organization Key plus per-topic tokens.
image: https://www.backstitch.io/hs-fs/hubfs/backstitch_logo_purple_2020.png?width=170&height=36&name=backstitch_logo_purple_2020.png
layout: provider
modified: '2026-08-13'
name: backstitch
nav: Providers
network: true
overview: 'backstitch publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Content Curation, Employee Communications, Internal Communications, and Total Rewards.


  backstitch''s developer surface includes documentation, API reference, support, engineering blog, authentication, getting-started guide, and 18 more developer resources.'
plans:
- name: Backstitch Plans Pricing
  plan_count: 0
  slug: backstitch-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Backstitch Rate Limits
  slug: backstitch-rate-limits
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 30.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/backstitch/refs/heads/main/screenshots/backstitch-2026-07-25T202231.png
security:
- kind: authentication
  name: Backstitch Authentication
  slug: backstitch-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Backstitch Domain Security
  slug: backstitch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Backstitch Vulnerability Disclosure
  slug: backstitch-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Backstitch Trust Center
  slug: backstitch-trust-center
  summary_line: SOC for Service Organizations (AICPA)
slug: backstitch
tags:
- Company
- Content Curation
- Employee Communications
- Internal Communications
- Total Rewards
- Content Aggregation
- Newsletters
- Widgets
- REST
website: https://www.backstitch.io/
---
