---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-09-05'
api_count: 2
apis:
- baseURL: https://api.cmp.optimizely.com/v3
  baseurl_source: declared
  description: The Assets API from Newscred — 1 operation(s) for assets.
  name: Newscred Assets API
  slug: newscred-assets-api
- baseURL: https://api.cmp.optimizely.com/v3
  baseurl_source: declared
  description: The Brand Compliance API from Newscred — 2 operation(s) for brand compliance.
  name: Newscred Brand Compliance API
  slug: newscred-brand-compliance-api
- baseURL: https://api.cmp.optimizely.com/v3
  baseurl_source: declared
  description: The Campaigns API from Newscred — 7 operation(s) for campaigns.
  name: Newscred Campaigns API
  slug: newscred-campaigns-api
- baseURL: https://api.cmp.optimizely.com/v3
  baseurl_source: declared
  description: The Events API from Newscred — 3 operation(s) for events.
  name: Newscred Events API
  slug: newscred-events-api
- baseURL: https://api.cmp.optimizely.com/v3
  baseurl_source: declared
  description: The Fields API from Newscred — 4 operation(s) for fields.
  name: Newscred Fields API
  slug: newscred-fields-api
- baseURL: https://api.cmp.optimizely.com/v3
  baseurl_source: declared
  description: The Labels API from Newscred — 1 operation(s) for labels.
  name: Newscred Labels API
  slug: newscred-labels-api
- baseURL: https://api.cmp.optimizely.com/v3
  baseurl_source: declared
  description: The Library API from Newscred — 24 operation(s) for library.
  name: Newscred Library API
  slug: newscred-library-api
- baseURL: https://api.cmp.optimizely.com/v3
  baseurl_source: declared
  description: The Milestones API from Newscred — 2 operation(s) for milestones.
  name: Newscred Milestones API
  slug: newscred-milestones-api
- baseURL: https://api.cmp.optimizely.com/v3
  baseurl_source: declared
  description: The Publishing API from Newscred — 4 operation(s) for publishing.
  name: Newscred Publishing API
  slug: newscred-publishing-api
- baseURL: https://api.cmp.optimizely.com/v3
  baseurl_source: declared
  description: The Settings API from Newscred — 1 operation(s) for settings.
  name: Newscred Settings API
  slug: newscred-settings-api
- baseURL: https://api.cmp.optimizely.com/v3
  baseurl_source: declared
  description: The Structured Contents API from Newscred — 11 operation(s) for structured contents.
  name: Newscred Structured Contents API
  slug: newscred-structured-contents-api
- baseURL: https://api.cmp.optimizely.com/v3
  baseurl_source: declared
  description: The Task Step API from Newscred — 1 operation(s) for task step.
  name: Newscred Task Step API
  slug: newscred-task-step-api
- baseURL: https://api.cmp.optimizely.com/v3
  baseurl_source: declared
  description: 'Facilitates the integration of external systems with Optimizely CMP through the following use cases: 1. **External Work Management** – Use the endpoints to link Optimizely CMP with an external system '
  name: Newscred Tasks API
  slug: newscred-tasks-api
- baseURL: https://api.cmp.optimizely.com/v3
  baseurl_source: declared
  description: The Teams API from Newscred — 2 operation(s) for teams.
  name: Newscred Teams API
  slug: newscred-teams-api
- baseURL: https://api.cmp.optimizely.com/v3
  baseurl_source: declared
  description: The Templates API from Newscred — 2 operation(s) for templates.
  name: Newscred Templates API
  slug: newscred-templates-api
- baseURL: https://api.cmp.optimizely.com/v3
  baseurl_source: declared
  description: The Uploader API from Newscred — 4 operation(s) for uploader.
  name: Newscred Uploader API
  slug: newscred-uploader-api
- baseURL: https://api.cmp.optimizely.com/v3
  baseurl_source: declared
  description: The Users API from Newscred — 3 operation(s) for users.
  name: Newscred Users API
  slug: newscred-users-api
- baseURL: https://api.cmp.optimizely.com/v3
  baseurl_source: declared
  description: The Work Requests API from Newscred — 13 operation(s) for work requests.
  name: Newscred Work Requests API
  slug: newscred-work-requests-api
- baseURL: https://api.cmp.optimizely.com/v3
  baseurl_source: declared
  description: The Workflows API from Newscred — 2 operation(s) for workflows.
  name: Newscred Workflows API
  slug: newscred-workflows-api
artifact_total: 27
asyncapis:
- description: ''
  name: Newscred Cmp Webhooks
  slug: newscred-cmp-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/newscred-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/newscred-cmp-open-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/newscred-welcome-open-api-overlay.yaml
- group: auth
  title: ''
  type: Security
  url: security/newscred-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/newscred-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newscred-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.optimizely.com/campaigns/acquisition/newscred
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.newscred.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.developers.optimizely.com/content-marketing-platform/docs/open-api-introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.developers.optimizely.com/content-marketing-platform/reference/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.developers.optimizely.com/content-marketing-platform/reference/get-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/newscred-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/newscred-scopes.yml
- group: operate
  title: ''
  type: Support
  url: https://support.optimizely.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.optimizely.com/field-notes/articles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/newscred
- group: commercial
  title: ''
  type: Pricing
  url: https://www.optimizely.com/plans
- group: commercial
  title: ''
  type: Plans
  url: plans/newscred-plans-pricing.yml
- group: start
  title: ''
  type: Login
  url: https://cmp.optimizely.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.optimizely.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.optimizely.com/legal/privacy-notice
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.optimizely.com/trust-center
- group: auth
  title: ''
  type: Compliance
  url: conformance/newscred-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/newscred-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/newscred-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/newscred-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.optimizely.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/newscred-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/newscred-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/newscred-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/newscred-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/newscred-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/newscred-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/newscred-packages.yml
- group: design
  title: ''
  type: Components
  url: components/newscred-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/newscred-llms.txt
created: '2026-08-26'
description: 'Newscred is the content marketing platform company that began as a licensed-content syndication API and grew into an enterprise Content Marketing Platform (CMP), Marketing Resource Management and Digital Asset Management suite. The company rebranded to Welcome in 2020 after Industry Dive acquired its content-services business, and Optimizely acquired Welcome in December 2021, where the product now ships as Optimizely Content Marketing Platform. The API lineage is continuous and the vendor documents it: the Open API base URL moved from https://api.newscred.com/v3 to https://api.welcomesoftware.com/v3 (28 March 2021) to https://api.cmp.optimizely.com/v3, and CMP still requires customers to allowlist *.newscred.com. The public contract is a 170-operation OAuth 2.0 REST API published by the newscred GitHub organization, covering library and digital asset management, tasks and workflows, campaigns, publishing, structured content, work requests, templates, teams and settings, plus
  a webhook event surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/newscred.png
layout: provider
modified: '2026-08-26'
name: Newscred
nav: Providers
network: true
overview: 'Newscred publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Brand Compliance API, Campaigns API, and 16 more. Tagged areas include Company, Content Marketing, Content Management, Digital Asset Management, and Marketing.


  The Newscred catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Newscred''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 30 more developer resources.'
plans:
- name: Newscred Plans Pricing
  plan_count: 0
  slug: newscred-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Newscred Rate Limits
  slug: newscred-rate-limits
scopes:
- name: Newscred Scopes
  scope_count: 3
  slug: newscred-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 57.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 64.8
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 81.6
  previous_composite: 57.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/newscred/refs/heads/main/screenshots/newscred-2026-09-02T150743.png
security:
- kind: authentication
  name: Newscred Authentication
  slug: newscred-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Newscred Domain Security
  slug: newscred-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Newscred Vulnerability Disclosure
  slug: newscred-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Newscred Trust Center
  slug: newscred-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA
slug: newscred
tags:
- Company
- Content Marketing
- Content Management
- Digital Asset Management
- Marketing
- Marketing Resource Management
- Workflows
- Publishing
- Webhook
- Acquired
website: https://www.optimizely.com/campaigns/acquisition/newscred
---
