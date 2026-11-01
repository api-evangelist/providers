---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.2
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: ''
  name: Crispy MCP API
  slug: crispy-mcp-api
- description: 'crispy-sh API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: crispy-sh API
  slug: crispy-sh-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/crispy-sh/plans/crispy-sh-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crispy-sh-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/crispy-sh/rules/crispy-sh-rules.yml
  title: ''
  type: Spectral
  url: rules/crispy-sh-rules.yml
- group: design
  href: https://artifacts.apis.io/crispy-sh/json-ld/crispy-sh-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/crispy-sh-context.jsonld
- group: design
  href: https://artifacts.apis.io/crispy-sh/vocabulary/crispy-sh-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crispy-sh-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/crispy-sh/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/crispy-sh/data-model/crispy-sh-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crispy-sh-data-model.yml
- group: build
  href: https://artifacts.apis.io/crispy-sh/cli/crispy-sh-cli.yml
  title: ''
  type: CLI
  url: cli/crispy-sh-cli.yml
- group: operate
  href: https://artifacts.apis.io/crispy-sh/changelog/crispy-sh-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/crispy-sh-changelog.yml
- group: design
  href: https://artifacts.apis.io/crispy-sh/errors/crispy-sh-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crispy-sh-problem-types.yml
- group: design
  href: https://artifacts.apis.io/crispy-sh/conformance/crispy-sh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crispy-sh-conformance.yml
- group: agent
  href: https://artifacts.apis.io/crispy-sh/llms/crispy-sh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crispy-sh-llms.txt
- group: auth
  href: https://artifacts.apis.io/crispy-sh/well-known/crispy-sh-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/crispy-sh-security.txt
- group: agent
  href: https://artifacts.apis.io/crispy-sh/well-known/crispy-sh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crispy-sh-well-known.yml
- group: other
  href: https://artifacts.apis.io/crispy-sh/hosts/crispy-sh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crispy-sh-hosts.yml
- group: other
  href: https://artifacts.apis.io/crispy-sh/vendors/crispy-sh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crispy-sh-vendors.yml
- group: build
  href: https://artifacts.apis.io/crispy-sh/packages/crispy-sh-packages.yml
  title: ''
  type: SDKs
  url: packages/crispy-sh-packages.yml
- group: build
  href: https://artifacts.apis.io/crispy-sh/packages/crispy-sh-packages.yml
  title: ''
  type: Packages
  url: packages/crispy-sh-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://crispy.sh/help/webhooks
- group: operate
  title: ''
  type: Support
  url: https://crispy.sh/help
- group: operate
  title: ''
  type: StatusPage
  url: https://crispy.sh/status
- group: auth
  title: ''
  type: Security
  url: https://crispy.sh/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://crispy.sh/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://crispy.sh/docs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://crispy.sh/docs/integrations/invitation-not-accepted-after
- group: auth
  href: https://artifacts.apis.io/crispy-sh/security/crispy-sh-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/crispy-sh-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/crispy-sh/security/crispy-sh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crispy-sh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crispy.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://crispy.sh/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://crispy.sh/pricing
- group: company
  title: ''
  type: Blog
  url: https://crispy.sh/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crispy.sh/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crispy.sh/privacy
- group: start
  title: ''
  type: SignUp
  url: https://crispy.sh/signup?journey_source=home
- group: start
  title: ''
  type: Login
  url: https://crispy.sh/login
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://crispy.sh/api/mcp
  - status: 200
    url: https://crispy.sh/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Content, outreach, inbox and signals for founders on LinkedIn. All in one place. The LinkedIn tool for founders. Post, find the right conversations, reach out, follow up and keep track of every contact, from Claude or ChatGPT.
image: https://crispy.sh/opengraph-image
json_schemas:
- name: PostApiMcpRequest
  property_count: 4
  slug: crispy-sh-post-api-mcp-request
- name: PostApiV1SubscriptionsRequest
  property_count: 3
  slug: crispy-sh-post-api-v1-subscriptions-request
jsonld:
- class_count: 2
  name: Crispy Sh Context
  property_count: 7
  slug: crispy-sh-context
layout: provider
modified: '2026-10-30'
name: crispy-sh
nav: Providers
network: true
overview: 'crispy-sh is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include LinkedIn, Founders, Outreach, Automation, and SaaS.


  The crispy-sh catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  crispy-sh''s developer surface includes CLI, changelog, support, API reference, getting-started guide, documentation, pricing, and 27 more developer resources.'
plans:
- name: Crispy Sh Plans Pricing
  plan_count: 1
  slug: crispy-sh-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Crispy Sh Rate Limits
  slug: crispy-sh-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: crispy-sh API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: crispy-sh-rules
score:
  band: strong
  composite: 59.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 73.9
    catalog_earned_first_party: 0.0
    catalog_gap: 41.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.7
    contract_governance: 79.1
    contract_quality: 46.8
    developer_ergonomics: 56.4
    discoverability: 57.1
    operational_transparency: 50.0
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
- kind: domain-security
  name: Crispy Sh Domain Security
  slug: crispy-sh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Crispy Sh Vulnerability Disclosure
  slug: crispy-sh-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: crispy-sh-main
  slug: crispy-sh-main-skill
slug: crispy-sh
tags:
- LinkedIn
- Founders
- Outreach
- Automation
- SaaS
website: https://crispy.sh/
---
