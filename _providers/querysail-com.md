---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Hosted MCP servers exposing Google Search Console and Google Analytics 4 data to AI assistants.
  name: QuerySail MCP API
  slug: querysail-mcp-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/querysail-com/plans/querysail-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/querysail-com-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://querysail.com/support#security
- group: auth
  href: https://artifacts.apis.io/querysail-com/authentication/querysail-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/querysail-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/querysail-com/scopes/querysail-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/querysail-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/querysail-com/conformance/querysail-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/querysail-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/querysail-com/llms/querysail-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/querysail-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/querysail-com/well-known/querysail-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/querysail-com-security.txt
- group: auth
  href: https://artifacts.apis.io/querysail-com/well-known/querysail-com-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/querysail-com-mcp-security.txt
- group: agent
  href: https://artifacts.apis.io/querysail-com/well-known/querysail-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/querysail-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/querysail-com/hosts/querysail-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/querysail-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/querysail-com/vendors/querysail-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/querysail-com-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://querysail.com/google-search-console#connect
- group: auth
  href: https://artifacts.apis.io/querysail-com/security/querysail-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/querysail-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/querysail-com/security/querysail-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/querysail-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://querysail.com/
- group: docs
  title: ''
  type: Documentation
  url: https://querysail.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://querysail.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://querysail.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://querysail.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://querysail.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://querysail.com/api/auth/sign-in?screen=sign-up&returnPathname=%2Fonboarding
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/querysail
coverage:
  checked: '2026-10-30'
  detail: Provider documentation lists MCP endpoints but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://querysail.com/.well-known/ai-catalog.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: QuerySail provides hosted Managed Compute Platform (MCP) servers that expose Google Search Console and Google Analytics 4 data to AI assistants such as ChatGPT, Claude, and Codex. Users can connect their Google accounts without creating a Google Cloud project, enjoy a 7‑day free trial, and pay a simple monthly fee for unlimited property connections. The service includes a sign‑up flow, support resources, pricing details, and clear privacy and terms documentation, all hosted at querysail.com.
image: https://querysail.com/og.png
layout: provider
modified: '2026-10-30'
name: querysail-com
nav: Providers
network: true
overview: 'querysail-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include MCP, Google Search Console, Google Analytics, AI Assistants, and SaaS.


  querysail-com''s developer surface includes authentication, getting-started guide, documentation, pricing, support, signup flow, and 16 more developer resources.'
plans:
- name: Querysail Com Plans Pricing
  plan_count: 1
  slug: querysail-com-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Querysail Com Rate Limits
  slug: querysail-com-rate-limits
scopes:
- name: Querysail Com Scopes
  scope_count: 3
  slug: querysail-com-scopes
  summary_line: 3 scopes
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Querysail Com Authentication
  slug: querysail-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Querysail Com Domain Security
  slug: querysail-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Querysail Com Vulnerability Disclosure
  slug: querysail-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: querysail-com
tags:
- MCP
- Google Search Console
- Google Analytics
- AI Assistants
- SaaS
website: https://querysail.com/
---
