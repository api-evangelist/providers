---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: unknown
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 32
  human_in_the_loop: 4
  name: Adslighthouse Agentic Access
  operation_count: 88
  slug: adslighthouse-agentic-access
  summary_line: 88 operations · 32 acting · 4 human-in-the-loop
api_count: 2
apis:
- baseURL: https://adslighthouse.com/api/v1
  baseurl_source: declared
  description: The Account API from Ads Lighthouse — 6 operation(s) for account.
  name: Ads Lighthouse Account API
  slug: adslighthouse-account-api
- baseURL: https://adslighthouse.com/api/v1
  baseurl_source: declared
  description: The Alerts API from Ads Lighthouse — 6 operation(s) for alerts.
  name: Ads Lighthouse Alerts API
  slug: adslighthouse-alerts-api
- baseURL: https://adslighthouse.com/api/v1
  baseurl_source: declared
  description: The Checks API from Ads Lighthouse — 2 operation(s) for checks.
  name: Ads Lighthouse Checks API
  slug: adslighthouse-checks-api
- baseURL: https://adslighthouse.com/api/v1
  baseurl_source: declared
  description: The Google API from Ads Lighthouse — 4 operation(s) for google.
  name: Ads Lighthouse Google API
  slug: adslighthouse-google-api
- baseURL: https://adslighthouse.com/api/v1
  baseurl_source: declared
  description: The Keywords API from Ads Lighthouse — 4 operation(s) for keywords.
  name: Ads Lighthouse Keywords API
  slug: adslighthouse-keywords-api
- baseURL: https://adslighthouse.com/api/v1
  baseurl_source: declared
  description: Match an AI workload to the cheapest live GPU that can run it. No key required.
  name: Ads Lighthouse Matching API
  slug: adslighthouse-matching-api
- baseURL: https://adslighthouse.com/api/v1
  baseurl_source: declared
  description: The Observations API from Ads Lighthouse — 2 operation(s) for observations.
  name: Ads Lighthouse Observations API
  slug: adslighthouse-observations-api
- baseURL: https://adslighthouse.com/api/v1
  baseurl_source: declared
  description: The Policy API from Ads Lighthouse — 8 operation(s) for policy.
  name: Ads Lighthouse Policy API
  slug: adslighthouse-policy-api
- baseURL: https://adslighthouse.com/api/v1
  baseurl_source: declared
  description: Live GPU rental prices, cheapest first. /api/v1/gpus needs no key.
  name: Ads Lighthouse Prices API
  slug: adslighthouse-prices-api
- baseURL: https://adslighthouse.com/api/v1
  baseurl_source: declared
  description: The Projects API from Ads Lighthouse — 5 operation(s) for projects.
  name: Ads Lighthouse Projects API
  slug: adslighthouse-projects-api
- baseURL: https://adslighthouse.com/api/v1
  baseurl_source: declared
  description: The Redirect chains API from Ads Lighthouse — 2 operation(s) for redirect chains.
  name: Ads Lighthouse Redirect chains API
  slug: adslighthouse-redirect-chains-api
- baseURL: https://adslighthouse.com/api/v1
  baseurl_source: declared
  description: The Reports API from Ads Lighthouse — 25 operation(s) for reports.
  name: Ads Lighthouse Reports API
  slug: adslighthouse-reports-api
- baseURL: https://adslighthouse.com/api/v1
  baseurl_source: declared
  description: Launch and manage GPUs through FastGPU (API key required).
  name: Ads Lighthouse Router API
  slug: adslighthouse-router-api
- baseURL: https://adslighthouse.com/api/v1
  baseurl_source: declared
  description: The Team API from Ads Lighthouse — 5 operation(s) for team.
  name: Ads Lighthouse Team API
  slug: adslighthouse-team-api
artifact_total: 22
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adslighthouse/refs/heads/main/agentic-access/adslighthouse-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adslighthouse-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/adslighthouse/refs/heads/main/plans/adslighthouse-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adslighthouse-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adslighthouse/refs/heads/main/rules/adslighthouse-rules.yml
  title: ''
  type: Spectral
  url: rules/adslighthouse-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adslighthouse/refs/heads/main/json-ld/adslighthouse-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/adslighthouse-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adslighthouse/refs/heads/main/vocabulary/adslighthouse-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/adslighthouse-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adslighthouse/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adslighthouse/refs/heads/main/data-model/adslighthouse-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adslighthouse-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adslighthouse/refs/heads/main/conventions/adslighthouse-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/adslighthouse-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adslighthouse/refs/heads/main/conventions/adslighthouse-conventions.yml
  title: ''
  type: Conventions
  url: conventions/adslighthouse-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://adslighthouse.com/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adslighthouse/refs/heads/main/errors/adslighthouse-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adslighthouse-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adslighthouse/refs/heads/main/conformance/adslighthouse-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adslighthouse-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adslighthouse/refs/heads/main/overlays/adslighthouse-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adslighthouse-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adslighthouse/refs/heads/main/llms/adslighthouse-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adslighthouse-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adslighthouse/refs/heads/main/well-known/adslighthouse-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adslighthouse-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adslighthouse/refs/heads/main/hosts/adslighthouse-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adslighthouse-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adslighthouse/refs/heads/main/vendors/adslighthouse-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adslighthouse-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://adslighthouse.com/integrations/webhooks
- group: auth
  title: ''
  type: Security
  url: https://adslighthouse.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://adslighthouse.com/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adslighthouse/refs/heads/main/authentication/adslighthouse-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adslighthouse-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adslighthouse/refs/heads/main/security/adslighthouse-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/adslighthouse-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adslighthouse/refs/heads/main/security/adslighthouse-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/adslighthouse-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adslighthouse/refs/heads/main/security/adslighthouse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adslighthouse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adslighthouse.com
- group: docs
  title: ''
  type: Documentation
  url: https://adslighthouse.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://adslighthouse.com/api/v1/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://adslighthouse.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://adslighthouse.com/help
- group: company
  title: ''
  type: Blog
  url: https://adslighthouse.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://adslighthouse.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://adslighthouse.com/signup
- group: start
  title: ''
  type: Login
  url: https://adslighthouse.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adslighthouse.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adslighthouse.com/privacy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://adslighthouse.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Ads Lighthouse provides brand search ad monitoring for Google and Bing, offering tools for advertisers, agencies, and affiliates to track brand appearances, compliance, and competition. The platform includes integrations with Slack, webhooks, email, and Google connections, delivering real‑time alerts, reports, and templates to help users manage paid‑search campaigns effectively.
image: https://adslighthouse.com/og-image.png
jsonld:
- class_count: 1
  name: Adslighthouse Context
  property_count: 2
  slug: adslighthouse-context
layout: provider
modified: '2026-10-12'
name: Ads Lighthouse
nav: Providers
network: true
overview: 'Ads Lighthouse publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Alerts API, Checks API, and 11 more. Tagged areas include Company, Advertising, Monitoring, and Brand Protection.


  The Ads Lighthouse catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ads Lighthouse''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 28 more developer resources.'
plans:
- name: Adslighthouse Plans Pricing
  plan_count: 5
  slug: adslighthouse-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Ads Lighthouse API Rules
  rule_count: 17
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 0
  slug: adslighthouse-rules
score:
  band: strong
  composite: 62.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 54.0
    catalog_earned_first_party: 12.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 19.7
    contract_quality: 57.3
    developer_ergonomics: 49.4
    discoverability: 64.3
    operational_transparency: 34.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 38.9
security:
- kind: authentication
  name: Adslighthouse Authentication
  slug: adslighthouse-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Adslighthouse Domain Security
  slug: adslighthouse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adslighthouse Vulnerability Disclosure
  slug: adslighthouse-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Adslighthouse Trust Center
  slug: adslighthouse-trust-center
  summary_line: SOC 2, ISO 27001
slug: adslighthouse
tags:
- Company
- Advertising
- Monitoring
- Brand Protection
website: https://adslighthouse.com
---
