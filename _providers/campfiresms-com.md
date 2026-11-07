---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 33
  human_in_the_loop: 1
  name: Campfiresms Com Agentic Access
  operation_count: 42
  slug: campfiresms-com-agentic-access
  summary_line: 42 operations · 33 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.campfiresms.com
  baseurl_source: declared
  description: The Auth API from Campfire SMS — 4 operation(s) for auth.
  name: Campfire SMS Auth API
  slug: campfiresms-com-auth-api
- baseURL: https://api.campfiresms.com
  baseurl_source: declared
  description: The Bridges API from Campfire SMS — 6 operation(s) for bridges.
  name: Campfire SMS Bridges API
  slug: campfiresms-com-bridges-api
- baseURL: https://api.campfiresms.com
  baseurl_source: declared
  description: The Credential API from Campfire SMS — 1 operation(s) for credential.
  name: Campfire SMS Credential API
  slug: campfiresms-com-credential-api
- baseURL: https://api.campfiresms.com
  baseurl_source: declared
  description: The Enrollment API from Campfire SMS — 7 operation(s) for enrollment.
  name: Campfire SMS Enrollment API
  slug: campfiresms-com-enrollment-api
- baseURL: https://api.campfiresms.com
  baseurl_source: declared
  description: The Health API from Campfire SMS — 1 operation(s) for health.
  name: Campfire SMS Health API
  slug: campfiresms-com-health-api
- baseURL: https://api.campfiresms.com
  baseurl_source: declared
  description: The Installations API from Campfire SMS — 2 operation(s) for installations.
  name: Campfire SMS Installations API
  slug: campfiresms-com-installations-api
- baseURL: https://api.campfiresms.com
  baseurl_source: declared
  description: The Join API from Campfire SMS — 1 operation(s) for join.
  name: Campfire SMS Join API
  slug: campfiresms-com-join-api
- baseURL: https://api.campfiresms.com
  baseurl_source: declared
  description: The Login API from Campfire SMS — 1 operation(s) for login.
  name: Campfire SMS Login API
  slug: campfiresms-com-login-api
- baseURL: https://api.campfiresms.com
  baseurl_source: declared
  description: The Public API from Campfire SMS — 2 operation(s) for public.
  name: Campfire SMS Public API
  slug: campfiresms-com-public-api
- baseURL: https://api.campfiresms.com
  baseurl_source: declared
  description: The Setup API from Campfire SMS — 15 operation(s) for setup.
  name: Campfire SMS Setup API
  slug: campfiresms-com-setup-api
- baseURL: https://api.campfiresms.com
  baseurl_source: declared
  description: The Webhooks API from Campfire SMS — 2 operation(s) for webhooks.
  name: Campfire SMS Webhooks API
  slug: campfiresms-com-webhooks-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/campfiresms-com/agentic-access/campfiresms-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/campfiresms-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/campfiresms-com/rules/campfiresms-com-rules.yml
  title: ''
  type: Spectral
  url: rules/campfiresms-com-rules.yml
- group: design
  href: https://artifacts.apis.io/campfiresms-com/json-ld/campfiresms-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/campfiresms-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/campfiresms-com/vocabulary/campfiresms-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/campfiresms-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/campfiresms-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/campfiresms-com/data-model/campfiresms-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/campfiresms-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/campfiresms-com/security/campfiresms-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/campfiresms-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/campfiresms-com/authentication/campfiresms-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/campfiresms-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/campfiresms-com/errors/campfiresms-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/campfiresms-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/campfiresms-com/conformance/campfiresms-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/campfiresms-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/campfiresms-com/llms/campfiresms-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/campfiresms-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/campfiresms-com/well-known/campfiresms-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/campfiresms-com-security.txt
- group: agent
  href: https://artifacts.apis.io/campfiresms-com/well-known/campfiresms-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/campfiresms-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/campfiresms-com/hosts/campfiresms-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/campfiresms-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/campfiresms-com/vendors/campfiresms-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/campfiresms-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://campfiresms.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://campfiresms.com/privacy.html
- group: start
  title: ''
  type: Login
  url: https://api.campfiresms.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://campfiresms.com/install.html#local-agents
- group: docs
  title: ''
  type: APIReference
  url: https://campfiresms.com/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/campfiresms
- group: auth
  href: https://artifacts.apis.io/campfiresms-com/security/campfiresms-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/campfiresms-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/campfiresms-com/security/campfiresms-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/campfiresms-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://campfiresms.com/
- group: docs
  title: ''
  type: Documentation
  url: https://campfiresms.com/guides/
- group: commercial
  title: ''
  type: Pricing
  url: https://campfiresms.com/
created: '2026-11-04'
description: Campfire SMS provides a two-way SMS bridge that connects your phone with AI coding agents. It enables agents like ChatGPT, Grok Bot, Codex, Claude Code, and others to send and receive messages via SMS, allowing continuous task execution even when your computer is off. The platform offers phone verification, message queuing, routing, and integration with various AI tools, plus a free tier of 20 messages for new users.
image: https://campfiresms.com/assets/campfiresms-social-card-v3.png
json_schemas:
- name: Body_configure_account_grok_wake_v1_setup_grok_wake_post
  property_count: 3
  slug: campfiresms-com-body-configure-account-grok-wake-v1-setup-grok-wake-post
- name: Body_configure_grok_wake_v1_setup_credentials__credential_id__grok_wake_post
  property_count: 2
  slug: campfiresms-com-body-configure-grok-wake-v1-setup-credentials-credential-id-grok-wake-post
- name: Body_set_setup_pin_v1_setup_pin_post
  property_count: 2
  slug: campfiresms-com-body-set-setup-pin-v1-setup-pin-post
- name: Body_update_setup_pin_v1_setup_pin_update_post
  property_count: 3
  slug: campfiresms-com-body-update-setup-pin-v1-setup-pin-update-post
- name: OpenBridgeRequest
  property_count: 3
  slug: campfiresms-com-open-bridge-request
- name: SetPinRequest
  property_count: 2
  slug: campfiresms-com-set-pin-request
jsonld:
- class_count: 23
  name: Campfiresms Com Context
  property_count: 24
  slug: campfiresms-com-context
layout: provider
modified: '2026-11-04'
name: Campfire SMS
nav: Providers
network: true
overview: 'Campfire SMS publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Bridges API, Credential API, and 8 more. Tagged areas include SMS, Artificial Intelligence, Automation, Messaging, and Integration.


  The Campfire SMS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Campfire SMS''s developer surface includes authentication, getting-started guide, API reference, documentation, pricing, and 21 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Campfire SMS API Rules
  rule_count: 37
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 2
  slug: campfiresms-com-rules
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 49.8
    developer_ergonomics: 32.6
    discoverability: 66.1
    operational_transparency: 13.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 21.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Campfiresms Com Authentication
  slug: campfiresms-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Campfiresms Com Domain Security
  slug: campfiresms-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Campfiresms Com Vulnerability Disclosure
  slug: campfiresms-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: enrollment
  slug: campfiresms-com-enrollment-skill
slug: campfiresms-com
tags:
- SMS
- Artificial Intelligence
- Automation
- Messaging
- Integration
website: https://campfiresms.com/
---
