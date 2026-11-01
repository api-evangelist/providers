---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 47
  human_in_the_loop: 1
  name: Forward Email Agentic Access
  operation_count: 76
  slug: forward-email-agentic-access
  summary_line: 76 operations · 47 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.forwardemail.net
  baseurl_source: declared
  description: Account management endpoints
  name: Forward Email Account API
  slug: forward-email-account-api
- baseURL: https://api.forwardemail.net
  baseurl_source: declared
  description: Domain alias management endpoints
  name: Forward Email Aliases API
  slug: forward-email-aliases-api
- baseURL: https://api.forwardemail.net
  baseurl_source: declared
  description: Alias calendar events management endpoints (CalDAV) >[!NOTE] > Unlike other API endpoints, these require [Authentication](#description/authentication) "username" equal to the alias username and "passw
  name: Forward Email Calendar Events API
  slug: forward-email-calendar-events-api
- baseURL: https://api.forwardemail.net
  baseurl_source: declared
  description: Alias calendars management endpoints (CalDAV) >[!NOTE] > Unlike other API endpoints, these require [Authentication](#description/authentication) "username" equal to the alias username and "password" e
  name: Forward Email Calendars API
  slug: forward-email-calendars-api
- baseURL: https://api.forwardemail.net
  baseurl_source: declared
  description: Alias contacts management endpoints (CardDAV) >[!NOTE] >Unlike other API endpoints, these require Authentication "username" equal to the alias username and "password" equal to the alias generated pass
  name: Forward Email Contacts API
  slug: forward-email-contacts-api
- baseURL: https://api.forwardemail.net
  baseurl_source: declared
  description: '> [!TIP] > Domain endpoints with a domain''s name <code>/v1/domains/:domain\_name</code> as their endpoint are interchangeable with a domain''s ID <code>:domain\_id</code>. This means you can refer to t'
  name: Forward Email Domains API
  slug: forward-email-domains-api
- baseURL: https://api.forwardemail.net
  baseurl_source: declared
  description: Email management endpoints
  name: Forward Email Emails API
  slug: forward-email-emails-api
- baseURL: https://api.forwardemail.net
  baseurl_source: declared
  description: Encryption endpoints
  name: Forward Email Encrypt API
  slug: forward-email-encrypt-api
- baseURL: https://api.forwardemail.net
  baseurl_source: declared
  description: Alias folders management endpoints (IMAP/POP3) >[!TIP] > Folder endpoints with a folder's path <code>/v1/folders/:path</code> as their endpoint are interchangeable with a folder's ID <code>:id</code>.
  name: Forward Email Folders API
  slug: forward-email-folders-api
- baseURL: https://api.forwardemail.net
  baseurl_source: declared
  description: Domain invite management endpoints
  name: Forward Email Invites API
  slug: forward-email-invites-api
- baseURL: https://api.forwardemail.net
  baseurl_source: declared
  description: Log management endpoints
  name: Forward Email Logs API
  slug: forward-email-logs-api
- baseURL: https://api.forwardemail.net
  baseurl_source: declared
  description: Domain member management endpoints
  name: Forward Email Members API
  slug: forward-email-members-api
- baseURL: https://api.forwardemail.net
  baseurl_source: declared
  description: Alias messages management endpoints (IMAP/POP3) >[!NOTE] > Unlike other API endpoints, these require [Authentication](#description/authentication) "username" equal to the alias username and "password"
  name: Forward Email Messages API
  slug: forward-email-messages-api
- baseURL: https://api.forwardemail.net
  baseurl_source: declared
  description: Register and manage push notification tokens for APNs, FCM, UnifiedPush, and Web Push. Tokens are scoped to an alias and used to deliver notifications when the app is backgrounded or closed.
  name: Forward Email Push Tokens API
  slug: forward-email-push-tokens-api
- baseURL: https://api.forwardemail.net
  baseurl_source: declared
  description: Sieve script management endpoints >[!NOTE] > Sieve is a powerful email filtering language defined in RFC 5228. Scripts are executed on incoming mail to automatically organize, filter, and respond to m
  name: Forward Email Sieve Scripts API
  slug: forward-email-sieve-scripts-api
- baseURL: https://api.forwardemail.net
  baseurl_source: declared
  description: 'Real-time push notifications via WebSocket. Connect to the /v1/ws endpoint to receive live events. Authentication is optional: authenticated clients receive per-alias events (IMAP, CalDAV, CardDAV) an'
  name: Forward Email WebSockets API
  slug: forward-email-websockets-api
artifact_total: 32
asyncapis:
- description: ''
  name: Forward Email Webhooks
  slug: forward-email-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/forward-email/agentic-access/forward-email-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/forward-email-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/forward-email/plans/forward-email-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/forward-email-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/forward-email/rules/forward-email-rules.yml
  title: ''
  type: Spectral
  url: rules/forward-email-rules.yml
- group: design
  href: https://artifacts.apis.io/forward-email/json-ld/forward-email-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/forward-email-context.jsonld
- group: design
  href: https://artifacts.apis.io/forward-email/vocabulary/forward-email-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/forward-email-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/forward-email/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/forward-email/asyncapi/forward-email-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/forward-email-webhooks.yml
- group: design
  href: https://artifacts.apis.io/forward-email/data-model/forward-email-data-model.yml
  title: ''
  type: DataModel
  url: data-model/forward-email-data-model.yml
- group: design
  href: https://artifacts.apis.io/forward-email/errors/forward-email-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/forward-email-problem-types.yml
- group: design
  href: https://artifacts.apis.io/forward-email/conformance/forward-email-conformance.yml
  title: ''
  type: Conformance
  url: conformance/forward-email-conformance.yml
- group: agent
  href: https://artifacts.apis.io/forward-email/llms/forward-email-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/forward-email-llms.txt
- group: agent
  href: https://artifacts.apis.io/forward-email/mcp/forward-email-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/forward-email-mcp.yml
- group: auth
  href: https://artifacts.apis.io/forward-email/well-known/forward-email-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/forward-email-security.txt
- group: agent
  href: https://artifacts.apis.io/forward-email/well-known/forward-email-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/forward-email-well-known.yml
- group: other
  href: https://artifacts.apis.io/forward-email/hosts/forward-email-hosts.yml
  title: ''
  type: Hosts
  url: hosts/forward-email-hosts.yml
- group: build
  href: https://artifacts.apis.io/forward-email/packages/forward-email-packages.yml
  title: ''
  type: SDKs
  url: packages/forward-email-packages.yml
- group: build
  href: https://artifacts.apis.io/forward-email/packages/forward-email-packages.yml
  title: ''
  type: Packages
  url: packages/forward-email-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://forwardemail.net/en/terms
- group: operate
  title: ''
  type: Support
  url: https://forwardemail.net/en/help
- group: operate
  title: ''
  type: StatusPage
  url: https://status.forwardemail.net/
- group: auth
  title: ''
  type: Security
  url: https://forwardemail.net/en/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://forwardemail.net/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://forwardemail.net/en/press
- group: start
  title: ''
  type: Login
  url: https://forwardemail.net/en/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/isaacs
- group: docs
  title: ''
  type: Documentation
  url: https://forwardemail.net/en/guides
- group: company
  title: ''
  type: Blog
  url: https://forwardemail.net/blog/feed/atom
- group: start
  title: ''
  type: GettingStarted
  url: https://forwardemail.net/en/faq#how-do-i-get-started-and-set-up-email-forwarding
- group: docs
  title: ''
  type: APIReference
  url: https://forwardemail.net/en/email-api
- group: auth
  href: https://artifacts.apis.io/forward-email/authentication/forward-email-authentication.yml
  title: ''
  type: Authentication
  url: authentication/forward-email-authentication.yml
- group: auth
  href: https://artifacts.apis.io/forward-email/security/forward-email-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/forward-email-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/forward-email/security/forward-email-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/forward-email-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://forwardemail.net/
created: '2026-10-26'
description: Forward Email provides free email forwarding for custom domains with an open-source, privacy‑focused service. It offers API access to manage domains, aliases, messages, calendars, contacts and webhooks, supports SMTP, IMAP, POP3, CalDAV and CardDAV, and includes features like encrypted SQLite mailboxes, DKIM, SPF, DMARC, and detailed analytics. The platform serves over 1.6 million domains, offers unlimited aliases, and provides SDKs and client apps for desktop, mobile and terminal environments.
image: https://forwardemail.net/en/index.png?v=1793035193245
json_schemas:
- name: AliasAccount
  property_count: 18
  slug: forward-email-alias-account
- name: AliasInput
  property_count: 21
  slug: forward-email-alias-input
- name: Domain
  property_count: 53
  slug: forward-email-domain
- name: Message
  property_count: 32
  slug: forward-email-message
- name: SMTP
  property_count: 26
  slug: forward-email-smtp
- name: UpdateDomainInput
  property_count: 20
  slug: forward-email-update-domain-input
jsonld:
- class_count: 37
  name: Forward Email Context
  property_count: 216
  slug: forward-email-context
layout: provider
mcp_servers:
- description: ''
  name: Forward Email MCP Server
  slug: forward-email-mcp-yml
modified: '2026-10-26'
name: Forward Email
nav: Providers
network: true
overview: 'Forward Email publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Aliases API, Calendar Events API, and 13 more. Tagged areas include Email Forwarding, Email Hosting, Open Source, API, and Secure Email.


  The Forward Email catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Forward Email''s developer surface includes support, documentation, engineering blog, getting-started guide, API reference, authentication, and 27 more developer resources.'
plans:
- name: Forward Email Plans Pricing
  plan_count: 4
  slug: forward-email-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Forward Email API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 6
  slug: forward-email-rules
score:
  band: strong
  composite: 60.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 71.7
    developer_ergonomics: 61.2
    discoverability: 66.7
    operational_transparency: 39.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Forward Email Authentication
  slug: forward-email-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Forward Email Domain Security
  slug: forward-email-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Forward Email Vulnerability Disclosure
  slug: forward-email-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: getting-started
  slug: forward-email-getting_started
slug: forward-email
tags:
- Email Forwarding
- Email Hosting
- Open Source
- API
- Secure Email
website: https://forwardemail.net/
---
