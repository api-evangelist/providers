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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 82
  human_in_the_loop: 10
  name: Addy Io Agentic Access
  operation_count: 104
  slug: addy-io-agentic-access
  summary_line: 104 operations · 82 acting · 10 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.addy.io
  baseurl_source: declared
  description: The Account Details API from addy.io — 1 operation(s) for account details.
  name: addy.io Account Details API
  slug: addy-io-account-details-api
- baseURL: https://app.addy.io
  baseurl_source: declared
  description: The Account Notifications API from addy.io — 1 operation(s) for account notifications.
  name: addy.io Account Notifications API
  slug: addy-io-account-notifications-api
- baseURL: https://app.addy.io
  baseurl_source: declared
  description: The Alias Bulk Actions API from addy.io — 10 operation(s) for alias bulk actions.
  name: addy.io Alias Bulk Actions API
  slug: addy-io-alias-bulk-actions-api
- baseURL: https://app.addy.io
  baseurl_source: declared
  description: The Aliases API from addy.io — 12 operation(s) for aliases.
  name: addy.io Aliases API
  slug: addy-io-aliases-api
- baseURL: https://app.addy.io
  baseurl_source: declared
  description: The API Token API from addy.io — 1 operation(s) for api token.
  name: addy.io API Token API
  slug: addy-io-api-token-api
- baseURL: https://app.addy.io
  baseurl_source: declared
  description: The App Version API from addy.io — 1 operation(s) for app version.
  name: addy.io App Version API
  slug: addy-io-app-version-api
- baseURL: https://app.addy.io
  baseurl_source: declared
  description: The Blocklist API from addy.io — 4 operation(s) for blocklist.
  name: addy.io Blocklist API
  slug: addy-io-blocklist-api
- baseURL: https://app.addy.io
  baseurl_source: declared
  description: The Domain Options API from addy.io — 1 operation(s) for domain options.
  name: addy.io Domain Options API
  slug: addy-io-domain-options-api
- baseURL: https://app.addy.io
  baseurl_source: declared
  description: The Domains API from addy.io — 12 operation(s) for domains.
  name: addy.io Domains API
  slug: addy-io-domains-api
- baseURL: https://app.addy.io
  baseurl_source: declared
  description: The Endpoints API from addy.io — 1 operation(s) for endpoints.
  name: addy.io Endpoints API
  slug: addy-io-endpoints-api
- baseURL: https://app.addy.io
  baseurl_source: declared
  description: The Failed Deliveries API from addy.io — 5 operation(s) for failed deliveries.
  name: addy.io Failed Deliveries API
  slug: addy-io-failed-deliveries-api
- baseURL: https://app.addy.io
  baseurl_source: declared
  description: The Labels API from addy.io — 2 operation(s) for labels.
  name: addy.io Labels API
  slug: addy-io-labels-api
- baseURL: https://app.addy.io
  baseurl_source: declared
  description: The Recipients API from addy.io — 18 operation(s) for recipients.
  name: addy.io Recipients API
  slug: addy-io-recipients-api
- baseURL: https://app.addy.io
  baseurl_source: declared
  description: The Rules API from addy.io — 5 operation(s) for rules.
  name: addy.io Rules API
  slug: addy-io-rules-api
- baseURL: https://app.addy.io
  baseurl_source: declared
  description: The Usernames API from addy.io — 9 operation(s) for usernames.
  name: addy.io Usernames API
  slug: addy-io-usernames-api
artifact_total: 24
asyncapis:
- description: ''
  name: Addy Io Webhooks
  slug: addy-io-webhooks
common:
- group: other
  href: https://artifacts.apis.io/addy-io/capabilities/addy-io-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/addy-io-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/addy-io/agentic-access/addy-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/addy-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/addy-io/rules/addy-io-rules.yml
  title: ''
  type: Spectral
  url: rules/addy-io-rules.yml
- group: design
  href: https://artifacts.apis.io/addy-io/vocabulary/addy-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/addy-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/addy-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/addy-io/conformance/addy-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/addy-io-conformance.yml
- group: other
  href: https://artifacts.apis.io/addy-io/overlays/addy-io-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/addy-io-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/addy-io/well-known/addy-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/addy-io-security.txt
- group: agent
  href: https://artifacts.apis.io/addy-io/well-known/addy-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/addy-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/addy-io/hosts/addy-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/addy-io-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://addy.io/terms/
- group: operate
  title: ''
  type: Support
  url: https://addy.io/help/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.addy.io/
- group: auth
  title: ''
  type: Security
  url: https://addy.io/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://addy.io/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://addy.io/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.addy.io/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anonaddy
- group: operate
  title: ''
  type: ChangeLog
  url: https://addy.io/changelog/
- group: company
  title: ''
  type: Blog
  url: https://addy.io/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://addy.io/help/category/getting-started/
- group: docs
  title: ''
  type: APIReference
  url: https://app.addy.io/docs/
- group: auth
  href: https://artifacts.apis.io/addy-io/security/addy-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/addy-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://app.addy.io/
created: '2026-10-28'
description: Addy.io provides a web application that enables users to register, log in, and manage their personal account information. The platform includes a dashboard for account settings and integrates with payment services such as Stripe, offering a SaaS solution for address and email related workflows.
image: https://app.addy.io/og-image.png
layout: provider
modified: '2026-10-28'
name: addy.io
nav: Providers
network: true
overview: 'addy.io publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Details API, Account Notifications API, Alias Bulk Actions API, and 12 more. Tagged areas include Company, Email, Address, SaaS, and API.


  The addy.io catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  addy.io''s developer surface includes support, pricing, changelog, engineering blog, getting-started guide, API reference, and 18 more developer resources.'
plans:
- name: Addy Io Plans Pricing
  plan_count: 8
  slug: addy-io-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: addy.io API Rules
  rule_count: 13
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 4
  slug: addy-io-rules
scopes:
- name: Addy Io Scopes
  scope_count: 0
  slug: addy-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 54.7
    developer_ergonomics: 32.6
    discoverability: 66.1
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Addy Io Authentication
  slug: addy-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Addy Io Domain Security
  slug: addy-io-domain-security
  summary_line: DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Addy Io Vulnerability Disclosure
  slug: addy-io-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: get-account-details
  slug: addy-io-get-account-details
slug: addy-io
tags:
- Company
- Email
- Address
- SaaS
- API
- WebApp
website: https://app.addy.io/
---
