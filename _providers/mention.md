---
access_model:
  confidence: high
  label: Contact Sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://mention.com/en/pricing/
  - https://en.support.mention.com/en/articles/1904644-api-access-explained
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
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Mention Agentic Access
  operation_count: 36
  slug: mention-agentic-access
  summary_line: 36 operations · 19 acting
api_count: 9
apis:
- baseURL: https://api.mention.net/api
  baseurl_source: declared
  description: The Accounts API from Mention — 5 operations for account CRUD and identity resolution — createAccount, getAccount, updateAccount, deleteAccount and getMe. An access token can only act on its own accou
  name: Mention Accounts API
  slug: mention-accounts-api
- baseURL: https://api.mention.net/api
  baseurl_source: declared
  description: The Alerts API from Mention — 8 operations for the standing keyword queries Mention crawls the web and social media for — list, create, read, update, pause and unpause an alert, plus the per-account n
  name: Mention Alerts API
  slug: mention-alerts-api
- baseURL: https://api.mention.net/api
  baseurl_source: declared
  description: The Authors API from Mention — 1 operation. listAuthors returns the authors and influencers behind an alert’s mentions with influence score, reach and the underlying social profile, filterable by kind
  name: Mention Authors API
  slug: mention-authors-api
- baseURL: https://api.mention.net/api
  baseurl_source: declared
  description: The Mentions API from Mention — 6 operations over the results an alert collects — list with an extensive filter surface, read one, read its grouped children, curate folder/tone/tags/read state, mark a
  name: Mention Mentions API
  slug: mention-mentions-api
- baseURL: https://api.mention.net/api
  baseurl_source: declared
  description: 'The Shares API from Mention — 5 operations over the join between an account and an alert. Share is the authorization primitive AND the lifecycle owner of an alert: deleting the last share deletes the '
  name: Mention Shares API
  slug: mention-shares-api
- baseURL: https://api.mention.net/api
  baseurl_source: declared
  description: The Stats API from Mention — 1 operation. getStats returns aggregate counters alert by alert over a date range and interval, with week-day, per-interval tone, country and influencer breakdowns, all ex
  name: Mention Stats API
  slug: mention-stats-api
- baseURL: https://api.mention.net/api
  baseurl_source: declared
  description: 'The Tags API from Mention — 4 operations for the labels scoped to an alert, including up to five auto-tagging keywords per tag that label incoming mentions automatically. Limits: 100 tags per alert, 2'
  name: Mention Tags API
  slug: mention-tags-api
- baseURL: https://api.mention.net/api
  baseurl_source: declared
  description: 'The Tasks API from Mention — 5 operations for the assignments created on a mention for team mates. assigned_to_account_id is fixed at creation; type, comment and done are updatable. A mention returns '
  name: Mention Tasks API
  slug: mention-tasks-api
- baseURL: https://api.mention.net/api
  baseurl_source: declared
  description: 'The App API from Mention — 1 operation. GET /app/data returns the reference vocabularies every other Mention endpoint resolves its enumerated values against: alert sources, alert languages and countri'
  name: Mention App API
  slug: mention-app-api
artifact_total: 27
collections:
- collection_type: open
  name: Mention Accounts API
  slug: open-mention-accounts-api
- collection_type: open
  name: Mention Alerts API
  slug: open-mention-alerts-api
- collection_type: open
  name: Mention App API
  slug: open-mention-app-api
- collection_type: open
  name: Mention Authors API
  slug: open-mention-authors-api
- collection_type: open
  name: Mention Mentions API
  slug: open-mention-mentions-api
- collection_type: open
  name: Mention Shares API
  slug: open-mention-shares-api
- collection_type: open
  name: Mention Stats API
  slug: open-mention-stats-api
- collection_type: open
  name: Mention Tags API
  slug: open-mention-tags-api
- collection_type: open
  name: Mention Tasks API
  slug: open-mention-tasks-api
- collection_type: open
  name: Mention API
  slug: open-mention
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.mention.com/current/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.mention.com/current/src/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://dev.mention.com/current/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.mention.com/current/src/guidelines/Clients.html
- group: start
  title: ''
  type: Portal
  url: https://mention.com/en/media-monitoring-api/
- group: company
  title: ''
  type: Website
  url: https://mention.com/
- group: operate
  title: ''
  type: Support
  url: https://en.support.mention.com/
- group: company
  title: ''
  type: Blog
  url: https://mention.com/en/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mentionapp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mention
- group: commercial
  title: ''
  type: Pricing
  url: https://mention.com/en/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://social.agorapulse.com/mention-trial
- group: start
  title: ''
  type: Login
  url: https://web.mention.com/#login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mention.com/en/terms-and-conditions/#general-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mention.com/en/terms-and-conditions/#privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://mention.com/en/terms-and-conditions/#security-policy
- group: auth
  title: ''
  type: Compliance
  url: https://mention.com/en/terms-and-conditions/#security-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mention.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mention-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mention-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mention-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mention-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mention-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mention-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mention-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mention-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mention-finops.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mention-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mention-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/mention-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mention-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mention-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mention-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mention-vulnerability-disclosure.yml
created: '2026-03-16'
description: Mention is a media monitoring and social listening platform that watches over one billion sources in real time across 42 languages, covering social networks, news, blogs, forums, video and 75+ review sites. Its JSON-based RESTful API, documented at dev.mention.com, gives developers programmatic access to alerts (the standing keyword queries Mention crawls for), the mentions those alerts collect, curation by folder/tone/tag, mention tasks assigned to team mates, alert sharing and permissions, authors and influencer scoring, aggregate statistics, and a long-lived streaming endpoint for real-time delivery. Authentication is a bearer token obtained from a registered app or through an OAuth2 authorization-code flow, and the API version is selected per request with an Accept-Version header. Mention is sold by Agorapulse SAS; API access is a paid add-on rather than an included capability of the published plan.
finops:
- name: Mention Finops
  service_category: API
  slug: mention-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mention.png
layout: provider
modified: '2026-08-13'
name: Mention
nav: Providers
network: true
overview: 'Mention publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Alerts API, Authors API, and 6 more. Tagged areas include Alerts, Brand Monitoring, Media Monitoring, Social Listening, and Social-Media.


  Mention''s developer surface includes documentation, API reference, getting-started guide, developer portal, support, engineering blog, pricing, and 28 more developer resources.'
plans:
- name: Mention Plans Pricing
  plan_count: 1
  slug: mention-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Mention Rate Limits
  slug: mention-rate-limits
scopes:
- name: Mention Scopes
  scope_count: 0
  slug: mention-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 59.0
    catalog_earned_first_party: 16.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 3.4
    developer_ergonomics: 58.9
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 50.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mention/refs/heads/main/screenshots/mention-2026-06-20T185146.png
security:
- kind: authentication
  name: Mention Authentication
  slug: mention-authentication
  summary_line: http/apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Mention Domain Security
  slug: mention-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mention Vulnerability Disclosure
  slug: mention-vulnerability-disclosure
  summary_line: Hackerone
slug: mention
tags:
- Alerts
- Brand Monitoring
- Media Monitoring
- Social Listening
- Social-Media
- Sentiment Analysis
- Reputation Management
- Influencer Marketing
- Competitive Intelligence
- Streaming
- Marketing
website: https://mention.com/
---
