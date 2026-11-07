---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 83
  human_in_the_loop: 10
  name: Dropto Run Agentic Access
  operation_count: 123
  slug: dropto-run-agentic-access
  summary_line: 123 operations · 83 acting · 10 human-in-the-loop
api_count: 1
apis:
- baseURL: https://dropto.run
  baseurl_source: declared
  description: 'Reporting a published site for phishing, malware or other misuse. Open to anybody with no account and no credential, deliberately: requiring one would cost more reports than it would gain in follow-up'
  name: Dropto Abuse API
  slug: dropto-run-abuse-api
- baseURL: https://dropto.run
  baseurl_source: declared
  description: The account a site belongs to, the people who can reach it, and the invitations that add them. An account is the unit everything else hangs from — sites, quota and billing are all per account rather t
  name: Dropto Account API
  slug: dropto-run-account-api
- baseURL: https://dropto.run
  baseurl_source: declared
  description: The Announcements API from Dropto — 1 operation(s) for announcements.
  name: Dropto Announcements API
  slug: dropto-run-announcements-api
- baseURL: https://dropto.run
  baseurl_source: declared
  description: 'Signing in: the browser''s redirect through Google, and the two flows a command line uses — one that can open a browser, and one that shows a code to approve from another machine. Sessions are cookies;'
  name: Dropto Auth API
  slug: dropto-run-auth-api
- baseURL: https://dropto.run
  baseurl_source: declared
  description: Subscriptions, seats and invoices, through the payment provider that is the merchant of record. Publishing is free with or without an account; what is bought here is room, a custom domain and a page w
  name: Dropto Billing API
  slug: dropto-run-billing-api
- baseURL: https://dropto.run
  baseurl_source: declared
  description: One publish, from asking for upload addresses to putting a version live. Versions are immutable and are never written over, so promoting an earlier one is a pointer moving rather than an upload repeat
  name: Dropto Deploys API
  slug: dropto-run-deploys-api
- baseURL: https://dropto.run
  baseurl_source: declared
  description: 'Liveness for the control plane, and the endpoint the browser reports its own errors to. Nothing here needs a credential, and nothing here touches a site: the data plane serves files whether or not the'
  name: Dropto Health API
  slug: dropto-run-health-api
- baseURL: https://dropto.run
  baseurl_source: declared
  description: The tiers and every ceiling they carry, read from the same table the server enforces against. The pricing page and the dashboard both read this, which is what stops a published limit and an enforced o
  name: Dropto Plans API
  slug: dropto-run-plans-api
- baseURL: https://dropto.run
  baseurl_source: declared
  description: The Promotions API from Dropto — 3 operation(s) for promotions.
  name: Dropto Promotions API
  slug: dropto-run-promotions-api
- baseURL: https://dropto.run
  baseurl_source: declared
  description: The Site folders API from Dropto — 3 operation(s) for site folders.
  name: Dropto Site folders API
  slug: dropto-run-site-folders-api
- baseURL: https://dropto.run
  baseurl_source: declared
  description: 'A site, its address, and everything that is true of it rather than of one publish: the subdomain, custom domains and their certificates, a password, an expiry date, and the traffic figures — which ide'
  name: Dropto Sites API
  slug: dropto-run-sites-api
- baseURL: https://dropto.run
  baseurl_source: declared
  description: The Support API from Dropto — 1 operation(s) for support.
  name: Dropto Support API
  slug: dropto-run-support-api
- baseURL: https://dropto.run
  baseurl_source: declared
  description: Long-lived credentials for publishing from a script, a CI job or an agent. A token is shown once when it is created and is recoverable nowhere afterwards, so what is listed here is a name and a prefix
  name: Dropto Tokens API
  slug: dropto-run-tokens-api
artifact_total: 31
common:
- group: agent
  href: https://artifacts.apis.io/dropto-run/agentic-access/dropto-run-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dropto-run-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/dropto-run/plans/dropto-run-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dropto-run-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dropto-run/rules/dropto-run-rules.yml
  title: ''
  type: Spectral
  url: rules/dropto-run-rules.yml
- group: design
  href: https://artifacts.apis.io/dropto-run/json-ld/dropto-run-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dropto-run-context.jsonld
- group: design
  href: https://artifacts.apis.io/dropto-run/vocabulary/dropto-run-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dropto-run-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dropto-run/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dropto-run/data-model/dropto-run-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dropto-run-data-model.yml
- group: build
  href: https://artifacts.apis.io/dropto-run/cli/dropto-run-cli.yml
  title: ''
  type: CLI
  url: cli/dropto-run-cli.yml
- group: operate
  href: https://artifacts.apis.io/dropto-run/changelog/dropto-run-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dropto-run-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://dropto.run/contact
- group: auth
  href: https://artifacts.apis.io/dropto-run/authentication/dropto-run-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dropto-run-authentication.yml
- group: design
  href: https://artifacts.apis.io/dropto-run/errors/dropto-run-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dropto-run-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dropto-run/conformance/dropto-run-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dropto-run-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dropto-run/llms/dropto-run-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dropto-run-llms.txt
- group: auth
  href: https://artifacts.apis.io/dropto-run/well-known/dropto-run-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dropto-run-security.txt
- group: auth
  href: https://artifacts.apis.io/dropto-run/well-known/dropto-run-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dropto-run-app-security.txt
- group: agent
  href: https://artifacts.apis.io/dropto-run/well-known/dropto-run-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dropto-run-well-known.yml
- group: other
  href: https://artifacts.apis.io/dropto-run/hosts/dropto-run-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dropto-run-hosts.yml
- group: other
  href: https://artifacts.apis.io/dropto-run/vendors/dropto-run-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dropto-run-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dropto.run/terms
- group: operate
  title: ''
  type: ChangeLog
  url: https://dropto.run/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://dropto.run/llms.txt
- group: auth
  href: https://artifacts.apis.io/dropto-run/security/dropto-run-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dropto-run-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dropto-run/security/dropto-run-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dropto-run-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dropto.run/
- group: docs
  title: ''
  type: Documentation
  url: https://dropto.run/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://dropto.run/pricing
- group: company
  title: ''
  type: Blog
  url: https://dropto.run/blog
- group: operate
  title: ''
  type: Support
  url: https://dropto.run/faq
created: '2026-11-06'
description: Dropto provides instant static site hosting powered by AI. Users can drop a folder, markdown, PDF, Word, or Excel files and have them published as a live site on a global edge network without sign‑up, build steps, or configuration. The platform offers a Docs section, pricing details, and various hosting options like markdown, Vite, and forms. It also features AI‑generated content publishing, password protection, and a feedback system, aiming to simplify website deployment for developers and creators.
image: https://dropto.run/og.png
json_schemas:
- name: MeResponse
  property_count: 13
  slug: dropto-run-me-response
- name: SiteDetail
  property_count: 39
  slug: dropto-run-site-detail
- name: SiteDomainResponse
  property_count: 16
  slug: dropto-run-site-domain-response
- name: SiteSettingsResponse
  property_count: 14
  slug: dropto-run-site-settings-response
- name: SiteTrafficOverview
  property_count: 19
  slug: dropto-run-site-traffic-overview
- name: UpdateSiteSettingsRequest
  property_count: 11
  slug: dropto-run-update-site-settings-request
jsonld:
- class_count: 120
  name: Dropto Run Context
  property_count: 277
  slug: dropto-run-context
layout: provider
modified: '2026-11-06'
name: Dropto
nav: Providers
network: true
overview: 'Dropto publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Abuse API, Account API, Announcements API, and 10 more. Tagged areas include Hosting, Artificial Intelligence, Static Sites, Developer Tools, and Cloud.


  The Dropto catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dropto''s developer surface includes CLI, changelog, authentication, API reference, documentation, pricing, engineering blog, and 22 more developer resources.'
plans:
- name: Dropto Run Plans Pricing
  plan_count: 4
  slug: dropto-run-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Dropto API Rules
  rule_count: 52
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 14
  slug: dropto-run-rules
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 35.6
    contract_quality: 59.1
    developer_ergonomics: 44.6
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dropto Run Authentication
  slug: dropto-run-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dropto Run Domain Security
  slug: dropto-run-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dropto Run Vulnerability Disclosure
  slug: dropto-run-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: dropto-run-cli-device-signin
  slug: dropto-run-cli-device-signin
- name: dropto-run-create-site-with-domain
  slug: dropto-run-create-site-with-domain
- name: dropto-run-invite-account-member
  slug: dropto-run-invite-account-member
- name: dropto-run-token-rotate
  slug: dropto-run-token-rotate
- name: dropto-run-update-subscription-plan
  slug: dropto-run-update-subscription-plan
slug: dropto-run
tags:
- Hosting
- Artificial Intelligence
- Static Sites
- Developer Tools
- Cloud
website: https://dropto.run/
---
