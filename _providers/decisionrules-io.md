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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Management API for DecisionRules.io platform
  name: DecisionRules Management API
  slug: decisionrules-management-api
artifact_total: 4
asyncapis:
- description: ''
  name: Decisionrules Io Webhooks
  slug: decisionrules-io-webhooks
common:
- group: design
  href: https://artifacts.apis.io/decisionrules-io/asyncapi/decisionrules-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/decisionrules-io-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/decisionrules-io/authentication/decisionrules-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/decisionrules-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/decisionrules-io/conformance/decisionrules-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/decisionrules-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/decisionrules-io/llms/decisionrules-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/decisionrules-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/decisionrules-io/well-known/decisionrules-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/decisionrules-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/decisionrules-io/hosts/decisionrules-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/decisionrules-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/decisionrules-io/vendors/decisionrules-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/decisionrules-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.decisionrules.io/doc/terms-and-conditions/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.decisionrules.io/doc/terms-and-conditions/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.decisionrules.io/doc/product-updates/release-notes
- group: auth
  href: https://artifacts.apis.io/decisionrules-io/security/decisionrules-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/decisionrules-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://decisionrules.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.decisionrules.io/en/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.decisionrules.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.decisionrules.io/doc/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.decisionrules.io/en/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://www.decisionrules.io/en/support/
- group: company
  title: ''
  type: Blog
  url: https://www.decisionrules.io/en/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/decisionrules
- group: commercial
  title: ''
  type: Pricing
  url: https://www.decisionrules.io/en/pricing/public-cloud/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://decisionrules.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DecisionRules provides an AI‑powered business rules engine that lets enterprises model, automate and scale decision logic across finance, insurance, e‑commerce, healthcare and more. The platform offers a versatile toolbox, integrations, templates and professional services, with enterprise‑grade security and compliance. It supports developers via extensive documentation, SDKs and a developer hub, and offers cloud‑hosted and on‑premise deployments.
image: https://www.decisionrules.io/og_image_en.png
layout: provider
modified: '2026-11-05'
name: DecisionRules
nav: Providers
network: true
overview: 'DecisionRules is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Business Rules, Artificial Intelligence, Enterprise, Integration, and Low-Code.


  The DecisionRules catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DecisionRules'' developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 13 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 57.1
    discoverability: 66.1
    operational_transparency: 28.9
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Decisionrules Io Authentication
  slug: decisionrules-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Decisionrules Io Domain Security
  slug: decisionrules-io-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: decisionrules-io
tags:
- Business Rules
- Artificial Intelligence
- Enterprise
- Integration
- Low-Code
website: https://decisionrules.io/
---
