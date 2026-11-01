---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: unknown
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 69.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 28
  human_in_the_loop: 2
  name: Openmail Sh Agentic Access
  operation_count: 47
  slug: openmail-sh-agentic-access
  summary_line: 47 operations · 28 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.openmail.sh
  baseurl_source: declared
  description: Downloading and extracting text from attachments
  name: openmail-sh Attachments API
  slug: openmail-sh-attachments-api
- baseURL: https://api.openmail.sh
  baseurl_source: declared
  description: 'Custom domains: add your own sending/receiving domain, publish DNS, and verify it'
  name: openmail-sh Domains API
  slug: openmail-sh-domains-api
- baseURL: https://api.openmail.sh
  baseurl_source: declared
  description: Reporting bugs, friction, and feature requests to the OpenMail team
  name: openmail-sh Feedback API
  slug: openmail-sh-feedback-api
- baseURL: https://api.openmail.sh
  baseurl_source: declared
  description: Email inboxes and their webhook configuration
  name: openmail-sh Inboxes API
  slug: openmail-sh-inboxes-api
- baseURL: https://api.openmail.sh
  baseurl_source: declared
  description: 'Sending limits: today''s cold outreach caps on new recipients, per account, inbox, and domain, and what raises them'
  name: openmail-sh Limits API
  slug: openmail-sh-limits-api
- baseURL: https://api.openmail.sh
  baseurl_source: declared
  description: Sending and listing messages
  name: openmail-sh Messages API
  slug: openmail-sh-messages-api
- baseURL: https://api.openmail.sh
  baseurl_source: declared
  description: Domains your organisation controls but does not send from. Prove ownership with one TXT record and mail to their addresses stops counting toward the cold outreach limits.
  name: openmail-sh Owned Domains API
  slug: openmail-sh-owned-domains-api
- baseURL: https://api.openmail.sh
  baseurl_source: declared
  description: Isolated sub-accounts for your end users or tenants
  name: openmail-sh Pods API
  slug: openmail-sh-pods-api
- baseURL: https://api.openmail.sh
  baseurl_source: declared
  description: Correspondent policy — provider-enforced allow/block rules and allowlist mode, scoped per account, pod, or inbox. Account-wide key only.
  name: openmail-sh Policy API
  slug: openmail-sh-policy-api
- baseURL: https://api.openmail.sh
  baseurl_source: declared
  description: Conversation threads and read status
  name: openmail-sh Threads API
  slug: openmail-sh-threads-api
artifact_total: 29
asyncapis:
- description: ''
  name: Openmail Sh Webhooks
  slug: openmail-sh-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/openmail-sh/agentic-access/openmail-sh-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/openmail-sh-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/openmail-sh/rate-limits/openmail-sh-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/openmail-sh-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/openmail-sh/plans/openmail-sh-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/openmail-sh-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/openmail-sh/rules/openmail-sh-rules.yml
  title: ''
  type: Spectral
  url: rules/openmail-sh-rules.yml
- group: design
  href: https://artifacts.apis.io/openmail-sh/json-ld/openmail-sh-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/openmail-sh-context.jsonld
- group: design
  href: https://artifacts.apis.io/openmail-sh/vocabulary/openmail-sh-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/openmail-sh-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/openmail-sh/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/openmail-sh/asyncapi/openmail-sh-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/openmail-sh-webhooks.yml
- group: design
  href: https://artifacts.apis.io/openmail-sh/data-model/openmail-sh-data-model.yml
  title: ''
  type: DataModel
  url: data-model/openmail-sh-data-model.yml
- group: build
  href: https://artifacts.apis.io/openmail-sh/cli/openmail-sh-cli.yml
  title: ''
  type: CLI
  url: cli/openmail-sh-cli.yml
- group: design
  href: https://artifacts.apis.io/openmail-sh/conventions/openmail-sh-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/openmail-sh-conventions.yml
- group: design
  href: https://artifacts.apis.io/openmail-sh/conventions/openmail-sh-conventions.yml
  title: ''
  type: Conventions
  url: conventions/openmail-sh-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://openmail.sh/terms
- group: auth
  href: https://artifacts.apis.io/openmail-sh/authentication/openmail-sh-authentication.yml
  title: ''
  type: Authentication
  url: authentication/openmail-sh-authentication.yml
- group: design
  href: https://artifacts.apis.io/openmail-sh/errors/openmail-sh-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/openmail-sh-problem-types.yml
- group: design
  href: https://artifacts.apis.io/openmail-sh/conformance/openmail-sh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/openmail-sh-conformance.yml
- group: agent
  href: https://artifacts.apis.io/openmail-sh/llms/openmail-sh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/openmail-sh-llms.txt
- group: other
  href: https://artifacts.apis.io/openmail-sh/a2a/openmail-sh-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/openmail-sh-a2a.yml
- group: auth
  href: https://artifacts.apis.io/openmail-sh/well-known/openmail-sh-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/openmail-sh-security.txt
- group: agent
  href: https://artifacts.apis.io/openmail-sh/well-known/openmail-sh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/openmail-sh-well-known.yml
- group: other
  href: https://artifacts.apis.io/openmail-sh/hosts/openmail-sh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openmail-sh-hosts.yml
- group: other
  href: https://artifacts.apis.io/openmail-sh/vendors/openmail-sh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/openmail-sh-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://openmail.sh/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openmailsh
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.openmail.sh/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.openmail.sh${path}`
- group: docs
  title: ''
  type: APIReference
  url: https://docs.openmail.sh/api-reference/introduction
- group: auth
  href: https://artifacts.apis.io/openmail-sh/security/openmail-sh-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/openmail-sh-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/openmail-sh/security/openmail-sh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openmail-sh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openmail.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openmail.sh/
- group: company
  title: ''
  type: Blog
  url: https://openmail.sh/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://openmail.sh/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.openmail.sh/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openmail.sh/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://openmail.sh/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.openmail.sh
created: '2026-10-30'
description: Openmail.sh is a developer-focused email service platform that provides programmable email sending, inbound routing, and webhook notifications. It enables applications to integrate email capabilities via simple RESTful APIs, offering features such as template management, analytics, and domain authentication. The service targets SaaS developers, marketers, and enterprises seeking to automate transactional and marketing communications while maintaining deliverability and compliance.
image: https://openmail.sh/og-image.png
json_schemas:
- name: ApiKey
  property_count: 8
  slug: openmail-sh-api-key
- name: ColdCapLimits
  property_count: 9
  slug: openmail-sh-cold-cap-limits
- name: Domain
  property_count: 9
  slug: openmail-sh-domain
- name: Inbox
  property_count: 10
  slug: openmail-sh-inbox
- name: Message
  property_count: 17
  slug: openmail-sh-message
- name: OwnedDomain
  property_count: 7
  slug: openmail-sh-owned-domain
jsonld:
- class_count: 13
  name: Openmail Sh Context
  property_count: 60
  slug: openmail-sh-context
layout: provider
modified: '2026-10-30'
name: openmail-sh
nav: Providers
network: true
overview: 'openmail-sh publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Attachments API, Domains API, Feedback API, and 7 more. Tagged areas include Company, Email, API, AI, and Developer.


  The openmail-sh catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  openmail-sh''s developer surface includes CLI, authentication, getting-started guide, API reference, documentation, engineering blog, pricing, and 30 more developer resources.'
plans:
- name: Openmail Sh Plans Pricing
  plan_count: 3
  slug: openmail-sh-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 12
  name: Openmail Sh Rate Limits
  slug: openmail-sh-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: openmail-sh API Rules
  rule_count: 15
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 0
  slug: openmail-sh-rules
score:
  band: exemplar
  composite: 70.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 96.6
    catalog_earned_first_party: 0.0
    catalog_gap: 18.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 70.9
    contract_quality: 65.8
    developer_ergonomics: 66.0
    discoverability: 67.9
    operational_transparency: 67.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Openmail Sh Authentication
  slug: openmail-sh-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Openmail Sh Domain Security
  slug: openmail-sh-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Openmail Sh Vulnerability Disclosure
  slug: openmail-sh-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: openmail-sh-add-and-verify-owned-domain
  slug: openmail-sh-add-and-verify-owned-domain
- name: openmail-sh-create-and-retrieve-pod
  slug: openmail-sh-create-and-retrieve-pod
- name: openmail-sh-manage-inboxes
  slug: openmail-sh-manage-inboxes
- name: openmail-sh-send-email-and-list-messages
  slug: openmail-sh-send-email-and-list-messages
slug: openmail-sh
tags:
- Company
- Email
- API
- AI
- Developer
website: https://openmail.sh/
---
