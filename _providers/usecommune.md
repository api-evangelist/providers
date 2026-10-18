---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Usecommune Agentic Access
  operation_count: 63
  slug: usecommune-agentic-access
  summary_line: 63 operations · 19 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.usecommune.com
  baseurl_source: declared
  description: 'An article is one thing a newsletter published: written in Commune and sent, or imported from the newsletter''s provider. Two rules gate every article read and are described on each operation. First, a'
  name: Commune Articles API
  slug: usecommune-articles-api
- baseURL: https://api.usecommune.com
  baseurl_source: declared
  description: 'What Commune knows about one subscriber that a newsletter''s email provider cannot answer: engagement scored across the inbox and the community together, and the raw event stream those scores are summe'
  name: Commune Engagement API
  slug: usecommune-engagement-api
- baseURL: https://api.usecommune.com
  baseurl_source: declared
  description: Where a newsletter's events go, and how a creator changes it. Commune hands every event it publishes to a delivery service that owns fan out, retries, signing and the delivery log, and a destination i
  name: Commune Event delivery API
  slug: usecommune-event-delivery-api
- baseURL: https://api.usecommune.com
  baseurl_source: declared
  description: A highlight is a passage of an article a reader marked. It anchors a comment to the exact sentence that prompted it.
  name: Commune Highlights API
  slug: usecommune-highlights-api
- baseURL: https://api.usecommune.com
  baseurl_source: declared
  description: A message is a reply inside a thread, up to two levels deep. Reactions hang off a message.
  name: Commune Messages API
  slug: usecommune-messages-api
- baseURL: https://api.usecommune.com
  baseurl_source: declared
  description: 'The rolled up numbers for a newsletter and for one article: headline stats for a period, acquisition attribution, bucketed series for charting, and one article''s email performance beside its community'
  name: Commune Metrics API
  slug: usecommune-metrics-api
- baseURL: https://api.usecommune.com
  baseurl_source: declared
  description: A newsletter is the top level object in Commune. It owns its articles, its chat, its subscribers and its team. Everything else in this API hangs off one.
  name: Commune Newsletters API
  slug: usecommune-newsletters-api
- baseURL: https://api.usecommune.com
  baseurl_source: declared
  description: 'The API''s own machinery rather than any newsletter''s data: the readiness probe, what a credential has left of its rate limit budgets, what its newsletter''s plan allows, and the newsletter''s API keys. '
  name: Commune Platform API
  slug: usecommune-platform-api
- baseURL: https://api.usecommune.com
  baseurl_source: declared
  description: One query across newsletters, articles, people and chat. Where a reader starts who does not yet have an identifier for any of them.
  name: Commune Search API
  slug: usecommune-search-api
- baseURL: https://api.usecommune.com
  baseurl_source: declared
  description: The addresses a newsletter sends from, and the state of the DNS that has to be in place for them to work. The sending half of the pair; Website domains is the other. Needs `sending`.
  name: Commune Senders API
  slug: usecommune-senders-api
- baseURL: https://api.usecommune.com
  baseurl_source: declared
  description: 'A send is one dispatch of one article to a newsletter''s list: when it started, when it finished, and the three numbers it finished on. Not to be confused with Senders, one heading below: a sender is t'
  name: Commune Sends API
  slug: usecommune-sends-api
- baseURL: https://api.usecommune.com
  baseurl_source: declared
  description: A tag segments a newsletter's audience. Sending an article to a tag stamps that article with an audience, which is what makes it invisible to everyone outside it. Named for the subscribers it is appli
  name: Commune Subscriber tags API
  slug: usecommune-subscriber-tags-api
- baseURL: https://api.usecommune.com
  baseurl_source: declared
  description: 'Who receives a newsletter. Needs `audience`, and never a public surface: a newsletter''s list belongs to its creator. `GET /subscriptions` is that edge read from the other end, the lists one account is'
  name: Commune Subscribers API
  slug: usecommune-subscribers-api
- baseURL: https://api.usecommune.com
  baseurl_source: declared
  description: 'Who may act on behalf of a newsletter: its owner, plus the members the owner added as admins, editors or guests. Both sides of that edge are here. A newsletter''s roster answers "who is on this team" a'
  name: Commune Team API
  slug: usecommune-team-api
- baseURL: https://api.usecommune.com
  baseurl_source: declared
  description: 'A thread is a conversation inside a newsletter''s community. Commune has no separate posts or comments stack: a creator''s broadcast, a reader''s question and the discussion under an article are all thre'
  name: Commune Threads API
  slug: usecommune-threads-api
- baseURL: https://api.usecommune.com
  baseurl_source: declared
  description: 'A person with a Commune account: the readers who join a community and the writers who are credited on an article. Looked up by identifier or by username, and only ever as a public profile: never an em'
  name: Commune Users API
  slug: usecommune-users-api
- baseURL: https://api.usecommune.com
  baseurl_source: declared
  description: The events Commune pushes to a consumer, rather than the resources a consumer pulls. Commune publishes state changes on 23 topics, each delivered as one HTTPS POST to an endpoint the consumer register
  name: Commune Webhooks API
  slug: usecommune-webhooks-api
- baseURL: https://api.usecommune.com
  baseurl_source: declared
  description: A creator's own domain pointed at their Commune site, so their community lives at their address rather than at ours. The same prove you own this hostname flow as Senders, pointed at the site rather th
  name: Commune Website domains API
  slug: usecommune-website-domains-api
artifact_total: 34
asyncapis:
- description: ''
  name: Usecommune Webhooks
  slug: usecommune-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/mcp/usecommune-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/usecommune-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/llms/usecommune-api-reference-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usecommune-api-reference-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/agentic-access/usecommune-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/usecommune-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/rate-limits/usecommune-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/usecommune-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/plans/usecommune-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/usecommune-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/rules/usecommune-rules.yml
  title: ''
  type: Spectral
  url: rules/usecommune-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/json-ld/usecommune-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/usecommune-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/vocabulary/usecommune-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/usecommune-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/asyncapi/usecommune-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/usecommune-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/data-model/usecommune-data-model.yml
  title: ''
  type: DataModel
  url: data-model/usecommune-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/changelog/usecommune-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/usecommune-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/conventions/usecommune-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/usecommune-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/conventions/usecommune-conventions.yml
  title: ''
  type: Conventions
  url: conventions/usecommune-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/lifecycle/usecommune-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/usecommune-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/errors/usecommune-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/usecommune-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/conformance/usecommune-conformance.yml
  title: ''
  type: Conformance
  url: conformance/usecommune-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/overlays/usecommune-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/usecommune-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/llms/usecommune-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usecommune-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/llms/usecommune-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usecommune-dev-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/well-known/usecommune-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/usecommune-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/hosts/usecommune-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usecommune-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/vendors/usecommune-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usecommune-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/authentication/usecommune-authentication.yml
  title: ''
  type: Authentication
  url: authentication/usecommune-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/scopes/usecommune-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/usecommune-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://usecommune.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://usecommune.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://usecommune.dev/guides
- group: docs
  title: ''
  type: APIReference
  url: https://api-reference.usecommune.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://usecommune.dev/guides/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://api-reference.usecommune.dev/changes
- group: commercial
  title: ''
  type: Pricing
  url: https://usecommune.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://usecommune.com/register
- group: start
  title: ''
  type: Login
  url: https://usecommune.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usecommune.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usecommune.com/privacy
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/P6FtchV5e
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/security/usecommune-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usecommune-domain-security.yml
created: '2026-10-07'
description: 'Commune turns newsletters into communities: each newsletter has an archive of articles and every article carries a threaded chat, with engagement insights, subscriber analytics, growth tracking and superfan identification on top. The Commune API (63 operations, 23 webhook topics, contract version 2026-08-26) exposes newsletters, articles, threads, messages, subscribers, tags, senders, domains, metrics, sends and event delivery over a cursor-paginated REST surface at api.usecommune.com, authenticated with bearer API keys or OAuth 2.1 (PKCE, dynamic client registration, RFC 9728 protected-resource metadata), versioned by a Commune-Version date header, with a required Idempotency-Key on every write and a hosted MCP server at api.usecommune.com/mcp.'
image: https://usecommune.com/favicon.ico
json_schemas:
- name: ApiKey
  property_count: 15
  slug: usecommune-api-key
- name: ArticlePerformance
  property_count: 4
  slug: usecommune-article-performance
- name: Article
  property_count: 18
  slug: usecommune-article
- name: DeliveryAttempt
  property_count: 13
  slug: usecommune-delivery-attempt
- name: NewsletterStats
  property_count: 8
  slug: usecommune-newsletter-stats
- name: Send
  property_count: 10
  slug: usecommune-send
jsonld:
- class_count: 107
  name: Usecommune Context
  property_count: 243
  slug: usecommune-context
layout: provider
mcp_servers:
- description: Commune ships a hosted, remote MCP server at https://api.usecommune.com/mcp (Streamable HTTP). The guide describes job-shaped tools (for example 'which readers am I about to lose', draft/test/schedule
  name: Commune MCP Server
  slug: commune
modified: '2026-10-07'
name: Commune
nav: Providers
network: true
overview: 'Commune publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Articles API, Engagement API, Event delivery API, and 15 more. Tagged areas include Newsletters, Email, Community, Publishing, and Creator Economy.


  The Commune catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Commune''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Usecommune Plans Pricing
  plan_count: 3
  slug: usecommune-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Usecommune Rate Limits
  slug: usecommune-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Commune API Rules
  rule_count: 18
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 2
  slug: usecommune-rules
scopes:
- name: Usecommune Scopes
  scope_count: 14
  slug: usecommune-scopes
  summary_line: 14 scopes · authorizationCode
score:
  band: strong
  composite: 63.9
  coverage:
    artifact_dirs: 28
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 74.2
    developer_ergonomics: 56.5
    discoverability: 75.0
    operational_transparency: 55.3
  previous_composite: 63.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 35.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/usecommune/refs/heads/main/screenshots/usecommune-2026-10-11T131538.png
security:
- kind: authentication
  name: Usecommune Authentication
  slug: usecommune-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Usecommune Domain Security
  slug: usecommune-domain-security
  summary_line: TLSv1.3 · DMARC
slug: usecommune
tags:
- Newsletters
- Email
- Community
- Publishing
- Creator Economy
- Subscribers
- Webhook
- MCP
- Analytics
- Content
website: https://usecommune.com
---
