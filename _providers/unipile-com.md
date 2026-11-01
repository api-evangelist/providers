---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
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
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 63.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 45
  human_in_the_loop: 45
  name: Unipile Com Agentic Access
  operation_count: 98
  slug: unipile-com-agentic-access
  summary_line: 98 operations · 45 acting · 45 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api1.unipile.com:13111
  baseurl_source: declared
  description: Accounts management
  name: unipile-com Accounts API
  slug: unipile-com-accounts-api
- baseURL: https://api1.unipile.com:13111
  baseurl_source: declared
  description: Calendars management
  name: unipile-com Calendars API
  slug: unipile-com-calendars-api
- baseURL: https://api1.unipile.com:13111
  baseurl_source: declared
  description: Emails management
  name: unipile-com Emails API
  slug: unipile-com-emails-api
- baseURL: https://api1.unipile.com:13111
  baseurl_source: declared
  description: Linkedin specific use cases
  name: unipile-com LinkedIn Specific API
  slug: unipile-com-linkedin-specific-api
- baseURL: https://api1.unipile.com:13111
  baseurl_source: declared
  description: Messaging management
  name: unipile-com Messaging API
  slug: unipile-com-messaging-api
- baseURL: https://api1.unipile.com:13111
  baseurl_source: declared
  description: Posts features
  name: unipile-com Posts API
  slug: unipile-com-posts-api
- baseURL: https://api1.unipile.com:13111
  baseurl_source: declared
  description: Users features
  name: unipile-com Users API
  slug: unipile-com-users-api
- baseURL: https://api1.unipile.com:13111
  baseurl_source: declared
  description: Webhooks management
  name: unipile-com Webhooks API
  slug: unipile-com-webhooks-api
artifact_total: 15
common:
- group: docs
  title: ''
  type: Documentation
  url: https://developer.unipile.com/
- group: agent
  href: https://artifacts.apis.io/unipile-com/agentic-access/unipile-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/unipile-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/unipile-com/plans/unipile-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/unipile-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/unipile-com/rules/unipile-com-rules.yml
  title: ''
  type: Spectral
  url: rules/unipile-com-rules.yml
- group: design
  href: https://artifacts.apis.io/unipile-com/vocabulary/unipile-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/unipile-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/unipile-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/unipile-com/conventions/unipile-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/unipile-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/unipile-com/conventions/unipile-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/unipile-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/unipile-com/authentication/unipile-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/unipile-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/unipile-com/errors/unipile-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/unipile-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/unipile-com/conformance/unipile-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/unipile-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/unipile-com/llms/unipile-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/unipile-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/unipile-com/mcp/unipile-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/unipile-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/unipile-com/well-known/unipile-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/unipile-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/unipile-com/hosts/unipile-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/unipile-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/unipile-com/vendors/unipile-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/unipile-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/unipile-com/packages/unipile-com-packages.yml
  title: ''
  type: SDKs
  url: packages/unipile-com-packages.yml
- group: build
  href: https://artifacts.apis.io/unipile-com/packages/unipile-com-packages.yml
  title: ''
  type: Packages
  url: packages/unipile-com-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.unipile.com/mcp/webhooks/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.unipile.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.unipile.com/changelog
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.unipile.com/signup
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.unipile.com/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/unipile-com/security/unipile-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unipile-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unipile.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.unipile.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.unipile.com/v2.0/reference/api-usage
- group: commercial
  title: ''
  type: Pricing
  url: https://www.unipile.com/pricing-api/
- group: company
  title: ''
  type: Blog
  url: https://www.unipile.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.unipile.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unipile.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unipile.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unipile
created: '2026-10-31'
description: Unipile provides a unified API platform that enables developers to integrate multi-channel messaging services such as LinkedIn, WhatsApp, Instagram, Facebook Messenger, Gmail, and Outlook into their applications. By offering a single REST and real‑time API, Unipile abstracts the complexities of each provider, delivering consistent endpoints, authentication on behalf, and built‑in account protection. The service includes detailed documentation, pricing plans, and a developer portal, and it complies with GDPR and SOC 2 standards.
image: https://www.unipile.com/wp-content/uploads/2026/09/unipile-one-api-multi-channel-messaging-social.png
layout: provider
mcp_servers:
- description: Remote MCP server at developer.unipile.com.
  name: unipile-com MCP Server
  slug: unipile-com-mcp-yml
modified: '2026-10-31'
name: unipile-com
nav: Providers
network: true
overview: 'unipile-com publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Calendars API, Emails API, and 5 more. Tagged areas include Messaging, API, Integration, Multi-Channel, and Communication.


  The unipile-com catalog on APIs.io includes 1 Spectral governance ruleset.


  unipile-com''s developer surface includes documentation, authentication, changelog, signup flow, getting-started guide, API reference, pricing, and 26 more developer resources.'
plans:
- name: Unipile Com Plans Pricing
  plan_count: 6
  slug: unipile-com-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: unipile-com API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: unipile-com-rules
score:
  band: strong
  composite: 63.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 68.5
    catalog_earned_first_party: 0.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 44.6
    developer_ergonomics: 70.7
    discoverability: 65.0
    operational_transparency: 44.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Unipile Com Authentication
  slug: unipile-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Unipile Com Domain Security
  slug: unipile-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: list-accounts
  slug: unipile-com-list-accounts
slug: unipile-com
tags:
- Messaging
- API
- Integration
- Multi-Channel
- Communication
website: https://unipile.com/
---
