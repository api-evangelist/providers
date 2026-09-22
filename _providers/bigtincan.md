---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 28.6
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 36
  human_in_the_loop: 1
  name: Bigtincan Agentic Access
  operation_count: 69
  slug: bigtincan-agentic-access
  summary_line: 69 operations · 36 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://pubapi.bigtincan.com
  baseurl_source: declared
  description: The Admin API from Bigtincan — 10 operation(s) for admin.
  name: Bigtincan Admin API
  slug: bigtincan-admin-api
- baseURL: https://pubapi.bigtincan.com
  baseurl_source: declared
  description: The Bookmark API from Bigtincan — 1 operation(s) for bookmark.
  name: Bigtincan Bookmark API
  slug: bigtincan-bookmark-api
- baseURL: https://pubapi.bigtincan.com
  baseurl_source: declared
  description: The Channel API from Bigtincan — 7 operation(s) for channel.
  name: Bigtincan Channel API
  slug: bigtincan-channel-api
- baseURL: https://pubapi.bigtincan.com
  baseurl_source: declared
  description: The CRM API from Bigtincan — 1 operation(s) for crm.
  name: Bigtincan CRM API
  slug: bigtincan-crm-api
- baseURL: https://pubapi.bigtincan.com
  baseurl_source: declared
  description: The Event API from Bigtincan — 1 operation(s) for event.
  name: Bigtincan Event API
  slug: bigtincan-event-api
- baseURL: https://pubapi.bigtincan.com
  baseurl_source: declared
  description: The File API from Bigtincan — 4 operation(s) for file.
  name: Bigtincan File API
  slug: bigtincan-file-api
- baseURL: https://pubapi.bigtincan.com
  baseurl_source: declared
  description: The Form API from Bigtincan — 5 operation(s) for form.
  name: Bigtincan Form API
  slug: bigtincan-form-api
- baseURL: https://pubapi.bigtincan.com
  baseurl_source: declared
  description: The Group API from Bigtincan — 5 operation(s) for group.
  name: Bigtincan Group API
  slug: bigtincan-group-api
- baseURL: https://pubapi.bigtincan.com
  baseurl_source: declared
  description: The History API from Bigtincan — 1 operation(s) for history.
  name: Bigtincan History API
  slug: bigtincan-history-api
- baseURL: https://pubapi.bigtincan.com
  baseurl_source: declared
  description: The Links API from Bigtincan — 1 operation(s) for links.
  name: Bigtincan Links API
  slug: bigtincan-links-api
- baseURL: https://pubapi.bigtincan.com
  baseurl_source: declared
  description: The Public File Share API from Bigtincan — 3 operation(s) for public file share.
  name: Bigtincan Public File Share API
  slug: bigtincan-public-file-share-api
- baseURL: https://pubapi.bigtincan.com
  baseurl_source: declared
  description: The Search API from Bigtincan — 2 operation(s) for search.
  name: Bigtincan Search API
  slug: bigtincan-search-api
- baseURL: https://pubapi.bigtincan.com
  baseurl_source: declared
  description: The Settings API from Bigtincan — 1 operation(s) for settings.
  name: Bigtincan Settings API
  slug: bigtincan-settings-api
- baseURL: https://pubapi.bigtincan.com
  baseurl_source: declared
  description: The Story API from Bigtincan — 11 operation(s) for story.
  name: Bigtincan Story API
  slug: bigtincan-story-api
- baseURL: https://pubapi.bigtincan.com
  baseurl_source: declared
  description: The Tab API from Bigtincan — 7 operation(s) for tab.
  name: Bigtincan Tab API
  slug: bigtincan-tab-api
- baseURL: https://pubapi.bigtincan.com
  baseurl_source: declared
  description: The Tag API from Bigtincan — 1 operation(s) for tag.
  name: Bigtincan Tag API
  slug: bigtincan-tag-api
- baseURL: https://pubapi.bigtincan.com
  baseurl_source: declared
  description: The User API from Bigtincan — 6 operation(s) for user.
  name: Bigtincan User API
  slug: bigtincan-user-api
- baseURL: https://pubapi.bigtincan.com
  baseurl_source: declared
  description: The User Metadata API from Bigtincan — 2 operation(s) for user metadata.
  name: Bigtincan User Metadata API
  slug: bigtincan-user-metadata-api
artifact_total: 26
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/capabilities/bigtincan-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bigtincan-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/agentic-access/bigtincan-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bigtincan-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/scopes/bigtincan-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/bigtincan-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/authentication/bigtincan-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bigtincan-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/security/bigtincan-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bigtincan-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/security/bigtincan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bigtincan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bigtincan.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pubapi.bigtincan.com/doc/interactive/
- group: docs
  title: ''
  type: APIReference
  url: https://pubapi.bigtincan.com/doc/interactive/
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/openapi/_original/bigtincan-hub-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/bigtincan-hub-api-openapi.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/overlays/bigtincan-hub-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bigtincan-hub-api-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/conventions/bigtincan-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bigtincan-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/errors/bigtincan-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bigtincan-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/data-model/bigtincan-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bigtincan-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/lifecycle/bigtincan-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bigtincan-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/changelog/bigtincan-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bigtincan-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/conformance/bigtincan-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bigtincan-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/conformance/bigtincan-conformance.yml
  title: ''
  type: Compliance
  url: conformance/bigtincan-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/packages/bigtincan-packages.yml
  title: ''
  type: Packages
  url: packages/bigtincan-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/packages/bigtincan-packages.yml
  title: ''
  type: SDKs
  url: packages/bigtincan-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/mcp/bigtincan-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bigtincan-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/llms/bigtincan-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bigtincan-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.bigtincan.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bigtincan.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bigtincan.com/
- group: start
  title: ''
  type: SignUp
  url: https://identity.bigtincan.com
- group: start
  title: ''
  type: Login
  url: https://identity.bigtincan.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bigtincan.com/eula/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bigtincan.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.bigtincan.com/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.bigtincan.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bigtincan
- group: other
  title: ''
  type: X
  url: https://x.com/bigtincan
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/plans/bigtincan-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bigtincan-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/rate-limits/bigtincan-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bigtincan-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/finops/bigtincan-finops.yml
  title: ''
  type: FinOps
  url: finops/bigtincan-finops.yml
created: '2026-06-13'
description: Bigtincan is an industry-leading sales enablement automation platform providing a REST API for managing sales content, training and coaching programs, buyer engagement analytics, digital sales rooms, and CRM content sync. The platform combines AI-powered content management, sales readiness tools, and buyer engagement capabilities to help revenue teams close deals faster.
finops:
- name: Bigtincan Finops
  service_category: ''
  slug: bigtincan-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bigtincan.png
layout: provider
modified: '2026-09-16'
name: Bigtincan
nav: Providers
network: true
overview: 'Bigtincan publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Bookmark API, Channel API, and 15 more. Tagged areas include Sales Enablement, Content Management, Training, Coaching, and Buyer Engagement.


  Bigtincan''s developer surface includes authentication, documentation, API reference, changelog, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Bigtincan Plans Pricing
  plan_count: 5
  slug: bigtincan-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Bigtincan Rate Limits
  slug: bigtincan-rate-limits
scopes:
- name: Bigtincan Scopes
  scope_count: 0
  slug: bigtincan-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 54.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 48.2
    developer_ergonomics: 44.6
    discoverability: 68.5
    operational_transparency: 31.6
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/screenshots/bigtincan-2026-06-20T173235.png
security:
- kind: authentication
  name: Bigtincan Authentication
  slug: bigtincan-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Bigtincan Domain Security
  slug: bigtincan-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bigtincan Trust Center
  slug: bigtincan-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001, ISO/IEC 27701
slug: bigtincan
tags:
- Sales Enablement
- Content Management
- Training
- Coaching
- Buyer Engagement
- Analytics
- CRM Integration
- Digital Sales Rooms
website: https://www.bigtincan.com/
---
