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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Shipstar Ai Agentic Access
  operation_count: 30
  slug: shipstar-ai-agentic-access
  summary_line: 30 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.shipstar.ai/api/v1
  baseurl_source: declared
  description: The authentication API from shipstar-ai — 1 operation(s) for authentication.
  name: shipstar-ai Authentication API
  slug: shipstar-ai-authentication-api
- baseURL: https://api.shipstar.ai/api/v1
  baseurl_source: declared
  description: The banner API from shipstar-ai — 2 operation(s) for banner.
  name: shipstar-ai Banner API
  slug: shipstar-ai-banner-api
- baseURL: https://api.shipstar.ai/api/v1
  baseurl_source: declared
  description: The blog API from shipstar-ai — 4 operation(s) for blog.
  name: shipstar-ai Blog API
  slug: shipstar-ai-blog-api
- baseURL: https://api.shipstar.ai/api/v1
  baseurl_source: declared
  description: The changelog API from shipstar-ai — 4 operation(s) for changelog.
  name: shipstar-ai Changelog API
  slug: shipstar-ai-changelog-api
- baseURL: https://api.shipstar.ai/api/v1
  baseurl_source: declared
  description: The changelog-subscriptions API from shipstar-ai — 3 operation(s) for changelog-subscriptions.
  name: shipstar-ai Changelog Subscriptions API
  slug: shipstar-ai-changelog-subscriptions-api
- baseURL: https://api.shipstar.ai/api/v1
  baseurl_source: declared
  description: The Health API from shipstar-ai — 1 operation(s) for health.
  name: shipstar-ai Health API
  slug: shipstar-ai-health-api
- baseURL: https://api.shipstar.ai/api/v1
  baseurl_source: declared
  description: The kb API from shipstar-ai — 2 operation(s) for kb.
  name: shipstar-ai Kb API
  slug: shipstar-ai-kb-api
- baseURL: https://api.shipstar.ai/api/v1
  baseurl_source: declared
  description: The mailing-lists API from shipstar-ai — 7 operation(s) for mailing-lists.
  name: shipstar-ai Mailing Lists API
  slug: shipstar-ai-mailing-lists-api
- baseURL: https://api.shipstar.ai/api/v1
  baseurl_source: declared
  description: The team-invitations API from shipstar-ai — 1 operation(s) for team-invitations.
  name: shipstar-ai Team Invitations API
  slug: shipstar-ai-team-invitations-api
artifact_total: 22
common:
- group: docs
  title: ''
  type: APIReference
  url: https://docs.shipstar.ai/api-reference/overview
- group: agent
  href: https://artifacts.apis.io/shipstar-ai/agentic-access/shipstar-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/shipstar-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/shipstar-ai/plans/shipstar-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shipstar-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/shipstar-ai/rules/shipstar-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/shipstar-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/shipstar-ai/json-ld/shipstar-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/shipstar-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/shipstar-ai/vocabulary/shipstar-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/shipstar-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/shipstar-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/shipstar-ai/data-model/shipstar-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/shipstar-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/shipstar-ai/authentication/shipstar-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shipstar-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/shipstar-ai/errors/shipstar-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/shipstar-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/shipstar-ai/conformance/shipstar-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shipstar-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/shipstar-ai/llms/shipstar-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shipstar-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/shipstar-ai/a2a/shipstar-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/shipstar-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/shipstar-ai/well-known/shipstar-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shipstar-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/shipstar-ai/hosts/shipstar-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shipstar-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/shipstar-ai/vendors/shipstar-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shipstar-ai-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://shipstar.ai/integrations/webhooks
- group: start
  title: ''
  type: Login
  url: https://app.shipstar.ai/account/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shipstar
- group: operate
  title: ''
  type: ChangeLog
  url: https://shipstar.ai/changelog
- group: auth
  href: https://artifacts.apis.io/shipstar-ai/security/shipstar-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shipstar-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shipstar.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shipstar.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://shipstar.ai/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.shipstar.ai/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://shipstar.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shipstar.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shipstar.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://shipstar.ai/support
- group: company
  title: ''
  type: Blog
  url: https://shipstar.ai/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://shipstar.ai/status
created: '2026-10-31'
description: Shipstar AI provides automated marketing tools for developers, generating live, dismissable banner bars, changelogs, release notes, and social posts directly from GitHub commits. It offers a free plan with no credit card required, integrates with popular repositories, and supports multiple use‑cases such as product announcements and release‑note newsletters. The platform aims to streamline developer‑focused product marketing, allowing teams to focus on building while Shipstar handles the promotional content.
image: https://shipstar.ai/shipstar-opengraph.png
json_schemas:
- name: MailingListRead
  property_count: 7
  slug: shipstar-ai-mailing-list-read
- name: RecipientBulkAddResponse
  property_count: 3
  slug: shipstar-ai-recipient-bulk-add-response
- name: RecipientPage
  property_count: 2
  slug: shipstar-ai-recipient-page
- name: RecipientRemoveResponse
  property_count: 4
  slug: shipstar-ai-recipient-remove-response
- name: RecipientUpsertRequest
  property_count: 1
  slug: shipstar-ai-recipient-upsert-request
- name: RecipientUpsertResponse
  property_count: 7
  slug: shipstar-ai-recipient-upsert-response
jsonld:
- class_count: 17
  name: Shipstar Ai Context
  property_count: 39
  slug: shipstar-ai-context
layout: provider
modified: '2026-10-31'
name: shipstar-ai
nav: Providers
network: true
overview: 'shipstar-ai publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Banner API, Blog API, and 6 more. Tagged areas include Company, Marketing, Developer Tools, Automation, and Open Source.


  The shipstar-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  shipstar-ai''s developer surface includes API reference, authentication, changelog, documentation, getting-started guide, pricing, support, and 24 more developer resources.'
plans:
- name: Shipstar Ai Plans Pricing
  plan_count: 3
  slug: shipstar-ai-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: shipstar-ai API Rules
  rule_count: 57
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 5
  slug: shipstar-ai-rules
score:
  band: developing
  composite: 47.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 63.2
    developer_ergonomics: 39.9
    discoverability: 66.1
    operational_transparency: 22.4
  previous_composite: 57.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/shipstar-ai/shipstar-ai-2026-11-03T143131.png
security:
- kind: authentication
  name: Shipstar Ai Authentication
  slug: shipstar-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Shipstar Ai Domain Security
  slug: shipstar-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: shipstar-ai-subscribe-changelog
  slug: shipstar-ai-subscribe-changelog
slug: shipstar-ai
tags:
- Company
- Marketing
- Developer Tools
- Automation
- Open Source
website: https://shipstar.ai/
---
