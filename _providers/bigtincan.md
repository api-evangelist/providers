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
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-03'
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
artifact_total: 27
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/bigtincan-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bigtincan-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bigtincan-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bigtincan-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bigtincan-trust-center.yml
- group: auth
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
  title: ''
  type: OpenAPI
  url: openapi/bigtincan-hub-api-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/bigtincan-hub-api-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/bigtincan-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bigtincan-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bigtincan-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bigtincan-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bigtincan-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bigtincan-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/bigtincan-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/bigtincan-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bigtincan-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bigtincan-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
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
  title: ''
  type: Plans
  url: plans/bigtincan-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bigtincan-rate-limits.yml
- group: commercial
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
mcp_servers:
- description: Bigtincan ships NO Model Context Protocol server. A search of the provider's site, the MCP ecosystem and the public registries found no hosted endpoint and no stdio package, and no /.well-known/ai-plu
  name: Bigtincan Hub MCP Server (candidate)
  slug: bigtincan-hub-mcp-server-candidate
modified: '2026-08-14'
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
  band: developing
  composite: 52.6
  coverage:
    artifact_dirs: 24
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 48.6
    developer_ergonomics: 44.6
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 52.6
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
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
