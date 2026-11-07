---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Read-only public JSON and feed surface documented in Okapi''s llms.txt: one provider''s tracked breaking changes as JSON at https://www.okapi.bot/api/v1/providers/<provider>.json (title, kind, model, st'
  name: Okapi Breaking Changes Data
  slug: okapi-breaking-changes-data
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/okapi-bot/plans/okapi-bot-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/okapi-bot-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/okapi-bot/conventions/okapi-bot-conventions.yml
  title: ''
  type: Conventions
  url: conventions/okapi-bot-conventions.yml
- group: design
  href: https://artifacts.apis.io/okapi-bot/lifecycle/okapi-bot-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/okapi-bot-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/okapi-bot/llms/okapi-bot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/okapi-bot-llms.txt
- group: other
  href: https://artifacts.apis.io/okapi-bot/hosts/okapi-bot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/okapi-bot-hosts.yml
- group: build
  href: https://artifacts.apis.io/okapi-bot/integrations/okapi-bot-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/okapi-bot-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/okapi-bot/vendors/okapi-bot-vendors.yml
  title: ''
  type: Vendors
  url: vendors/okapi-bot-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.okapi.bot/providers/category/media/
- group: auth
  href: https://artifacts.apis.io/okapi-bot/security/okapi-bot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/okapi-bot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.okapi.bot/
- group: company
  title: ''
  type: Blog
  url: https://www.okapi.bot/blog/
- group: start
  title: ''
  type: SignUp
  url: https://github.com/apps/okapi-agent
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.okapi.bot/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.okapi.bot/privacy/
created: '2026-11-05'
description: 'Okapi (okapi.bot) bills itself as "Dependabot for APIs": a free GitHub App that finds the third-party APIs an application and its AI agents call, tracks those providers'' changes, and opens a pull request with the code fix before a deprecation or breaking change lands. Its site reports reading 1,173 API providers'' own pages and tracking 841 upcoming breaking changes, and it publishes a public breaking-changes feed and provider directory. Its terms say automated use of this data goes through Okapi''s check API, which is available by emailing hello@okapi.bot. The product is in early access.'
image: https://www.okapi.bot/og.png
layout: provider
modified: '2026-11-05'
name: Okapi
nav: Providers
network: true
overview: 'Okapi is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API Change Management, Breaking Changes, Deprecation, and GitHub App.


  Okapi''s developer surface includes engineering blog, signup flow, and 12 more developer resources.'
plans:
- name: Okapi Bot Plans Pricing
  plan_count: 1
  slug: okapi-bot-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Okapi Bot Rate Limits
  slug: okapi-bot-rate-limits
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 67.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Okapi Bot Authentication
  slug: okapi-bot-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Okapi Bot Domain Security
  slug: okapi-bot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: okapi-bot
tags:
- Company
- API Change Management
- Breaking Changes
- Deprecation
- GitHub App
- Developer Tools
- API Monitoring
- AI Agents
website: https://www.okapi.bot/
---
