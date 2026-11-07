---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: unknown
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 41
  human_in_the_loop: 1
  name: Eusend Dev Agentic Access
  operation_count: 67
  slug: eusend-dev-agentic-access
  summary_line: 67 operations · 41 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.eusend.dev
  baseurl_source: declared
  description: Mint and revoke credentials, including send-only and domain-scoped keys.
  name: eusend-dev API keys API
  slug: eusend-dev-api-keys-api
- baseURL: https://api.eusend.dev
  baseurl_source: declared
  description: Named contact lists a broadcast can be sent to.
  name: eusend-dev Audiences API
  slug: eusend-dev-audiences-api
- baseURL: https://api.eusend.dev
  baseurl_source: declared
  description: One message sent to a whole audience.
  name: eusend-dev Broadcasts API
  slug: eusend-dev-broadcasts-api
- baseURL: https://api.eusend.dev
  baseurl_source: declared
  description: The custom fields contacts carry, and the fallbacks they render with.
  name: eusend-dev Contact properties API
  slug: eusend-dev-contact-properties-api
- baseURL: https://api.eusend.dev
  baseurl_source: declared
  description: The people in an audience, and their subscription state.
  name: eusend-dev Contacts API
  slug: eusend-dev-contacts-api
- baseURL: https://api.eusend.dev
  baseurl_source: declared
  description: Register sending domains and verify their DKIM, SPF and DMARC records.
  name: eusend-dev Domains API
  slug: eusend-dev-domains-api
- baseURL: https://api.eusend.dev
  baseurl_source: declared
  description: Send, schedule, inspect and cancel individual messages.
  name: eusend-dev Emails API
  slug: eusend-dev-emails-api
- baseURL: https://api.eusend.dev
  baseurl_source: declared
  description: Addresses this organization will not send to.
  name: eusend-dev Suppressions API
  slug: eusend-dev-suppressions-api
- baseURL: https://api.eusend.dev
  baseurl_source: declared
  description: Unauthenticated liveness and readiness checks.
  name: eusend-dev System API
  slug: eusend-dev-system-api
- baseURL: https://api.eusend.dev
  baseurl_source: declared
  description: Stored HTML bodies with variable placeholders.
  name: eusend-dev Templates API
  slug: eusend-dev-templates-api
- baseURL: https://api.eusend.dev
  baseurl_source: declared
  description: Kinds of email a contact can subscribe to and leave independently, so an unsubscribe can be a preference change.
  name: eusend-dev Topics API
  slug: eusend-dev-topics-api
- baseURL: https://api.eusend.dev
  baseurl_source: declared
  description: HTTP callbacks for delivery, bounce, complaint, open and click events.
  name: eusend-dev Webhooks API
  slug: eusend-dev-webhooks-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/eusend-dev/agentic-access/eusend-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/eusend-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/eusend-dev/plans/eusend-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/eusend-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/eusend-dev/rules/eusend-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/eusend-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/eusend-dev/json-ld/eusend-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/eusend-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/eusend-dev/vocabulary/eusend-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/eusend-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/eusend-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/eusend-dev/data-model/eusend-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/eusend-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/eusend-dev/errors/eusend-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/eusend-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/eusend-dev/conformance/eusend-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/eusend-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/eusend-dev/mcp/eusend-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/eusend-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/eusend-dev/well-known/eusend-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/eusend-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/eusend-dev/hosts/eusend-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eusend-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/eusend-dev/vendors/eusend-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eusend-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/eusend-dev/packages/eusend-dev-packages.yml
  title: ''
  type: Packages
  url: packages/eusend-dev-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://eusend.dev/features/webhooks
- group: auth
  title: ''
  type: Security
  url: https://eusend.dev/legal/security
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@eusend_dev/sdk
- group: start
  title: ''
  type: Login
  url: https://eusend.dev/login
- group: start
  title: ''
  type: GettingStarted
  url: https://eusend.dev/docs/dashboard/domain-setup
- group: auth
  href: https://artifacts.apis.io/eusend-dev/security/eusend-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eusend-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eusend.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://eusend.dev/docs
- group: company
  title: ''
  type: Blog
  url: https://eusend.dev/blog
- group: operate
  title: ''
  type: Changelog
  url: https://eusend.dev/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://eusend.dev/pricing
- group: operate
  title: ''
  type: Support
  url: https://eusend.dev/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eusend.dev/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eusend.dev/legal/terms
- group: docs
  title: ''
  type: APIReference
  url: https://eusend.dev/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eusend-dev
created: '2026-10-30'
description: eusend is an EU‑native transactional and marketing email API. It processes, stores, and delivers email entirely within the European Union, offering GDPR‑friendly alternatives to Resend, SendGrid, and Postmark. The service provides robust features like DKIM signing, SPF alignment, detailed delivery events, and a developer‑focused dashboard, all hosted on EU data centres.
image: https://eusend.dev/opengraph-image.jpg
json_schemas:
- name: BatchContactsRequest
  property_count: 1
  slug: eusend-dev-batch-contacts-request
- name: Broadcast
  property_count: 23
  slug: eusend-dev-broadcast
- name: Domain
  property_count: 11
  slug: eusend-dev-domain
- name: Email
  property_count: 16
  slug: eusend-dev-email
- name: SendEmailRequest
  property_count: 16
  slug: eusend-dev-send-email-request
- name: UpdateBroadcastRequest
  property_count: 13
  slug: eusend-dev-update-broadcast-request
jsonld:
- class_count: 75
  name: Eusend Dev Context
  property_count: 125
  slug: eusend-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.eusend.dev.
  name: eusend-dev MCP Server
  slug: eusend-dev-mcp-yml
modified: '2026-10-30'
name: eusend-dev
nav: Providers
network: true
overview: 'eusend-dev publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including API keys API, Audiences API, Broadcasts API, and 9 more. Tagged areas include Email, Transactional, Marketing, EU, and GDPR.


  The eusend-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  eusend-dev''s developer surface includes getting-started guide, documentation, engineering blog, changelog, pricing, support, API reference, and 23 more developer resources.'
plans:
- name: Eusend Dev Plans Pricing
  plan_count: 9
  slug: eusend-dev-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: eusend-dev API Rules
  rule_count: 19
  severity_counts:
    error: 13
    hint: 0
    info: 3
    warn: 3
  slug: eusend-dev-rules
scopes:
- name: Eusend Dev Scopes
  scope_count: 0
  slug: eusend-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.2
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 65.8
    developer_ergonomics: 31.4
    discoverability: 65.0
    operational_transparency: 11.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 55.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/eusend-dev/eusend-dev-2026-11-03T131844.png
security:
- kind: authentication
  name: Eusend Dev Authentication
  slug: eusend-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Eusend Dev Domain Security
  slug: eusend-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: send-email
  slug: eusend-dev-send-email
slug: eusend-dev
tags:
- Email
- Transactional
- Marketing
- EU
- GDPR
website: https://eusend.dev/
---
