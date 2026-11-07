---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.4
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: Helpjuice provides a REST API for accessing knowledge base content such as articles, categories, and users.
  name: Helpjuice API
  slug: helpjuice-api
- description: The Categories API from Helpjuice — 1 operation(s) for categories.
  name: Helpjuice Categories API
  slug: helpjuice-categories-api
- description: The Questions API from Helpjuice — 3 operation(s) for questions.
  name: Helpjuice Questions API
  slug: helpjuice-questions-api
artifact_total: 9
asyncapis:
- description: ''
  name: Helpjuice Webhooks
  slug: helpjuice-webhooks
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.helpjuice.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://help.helpjuice.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://help.helpjuice.com/privacy-policy
- group: commercial
  href: https://artifacts.apis.io/helpjuice/plans/helpjuice-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/helpjuice-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/helpjuice/rules/helpjuice-rules.yml
  title: ''
  type: Spectral
  url: rules/helpjuice-rules.yml
- group: design
  href: https://artifacts.apis.io/helpjuice/asyncapi/helpjuice-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/helpjuice-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/helpjuice/authentication/helpjuice-authentication.yml
  title: ''
  type: Authentication
  url: authentication/helpjuice-authentication.yml
- group: design
  href: https://artifacts.apis.io/helpjuice/conformance/helpjuice-conformance.yml
  title: ''
  type: Conformance
  url: conformance/helpjuice-conformance.yml
- group: agent
  href: https://artifacts.apis.io/helpjuice/llms/helpjuice-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/helpjuice-llms.txt
- group: auth
  href: https://artifacts.apis.io/helpjuice/well-known/helpjuice-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/helpjuice-status-security.txt
- group: agent
  href: https://artifacts.apis.io/helpjuice/well-known/helpjuice-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/helpjuice-well-known.yml
- group: other
  href: https://artifacts.apis.io/helpjuice/hosts/helpjuice-hosts.yml
  title: ''
  type: Hosts
  url: hosts/helpjuice-hosts.yml
- group: other
  href: https://artifacts.apis.io/helpjuice/vendors/helpjuice-vendors.yml
  title: ''
  type: Vendors
  url: vendors/helpjuice-vendors.yml
- group: build
  href: https://artifacts.apis.io/helpjuice/packages/helpjuice-packages.yml
  title: ''
  type: SDKs
  url: packages/helpjuice-packages.yml
- group: build
  href: https://artifacts.apis.io/helpjuice/packages/helpjuice-packages.yml
  title: ''
  type: Packages
  url: packages/helpjuice-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.helpjuice.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.helpjuice.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Helpjuice
- group: auth
  href: https://artifacts.apis.io/helpjuice/security/helpjuice-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/helpjuice-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://helpjuice.com
- group: start
  title: ''
  type: GettingStarted
  url: https://helpjuice.com/signup
- group: company
  title: ''
  type: Blog
  url: https://helpjuice.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://helpjuice.com/pricing
coverage:
  checked: '2026-10-14'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found on the API host.
  evidence:
  - status: 404
    url: https://api.helpjuice.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Helpjuice provides knowledge base software that enables businesses to create, organize, and share internal and external documentation. Their platform offers AI-assisted content creation, customizable templates, and robust analytics to improve customer support efficiency. With features like article suggestions, multi‑language support, and integrations with popular tools, Helpjuice helps teams reduce repetitive inquiries and deliver consistent information across channels.
finops:
- has_sources: true
  method: derived
  name: Helpjuice Finops
  primary_unit: seat
  service_category: ''
  slug: helpjuice-finops
  template: false
image: https://helpjuice-static.s3.amazonaws.com/assets.helpjuice.com/meta-tag.png
layout: provider
modified: '2026-10-14'
name: Helpjuice
nav: Providers
network: true
overview: 'Helpjuice is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Questions API, and 1 more. Tagged areas include Knowledge Base, Software-as-a-Service, Customer Service, Artificial Intelligence, and Documentation.


  The Helpjuice catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Helpjuice''s developer surface includes support, authentication, documentation, getting-started guide, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Helpjuice Plans Pricing
  plan_count: 3
  slug: helpjuice-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Helpjuice API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: helpjuice-rules
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 54.5
    catalog_earned_first_party: 12.0
    catalog_gap: 60.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 55.3
    contract_governance: 31.8
    contract_quality: 18.5
    developer_ergonomics: 33.3
    discoverability: 69.6
    operational_transparency: 28.9
  previous_composite: 44.7
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/helpjuice/helpjuice-2026-11-03T133347.png
security:
- kind: authentication
  name: Helpjuice Authentication
  slug: helpjuice-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Helpjuice Domain Security
  slug: helpjuice-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: helpjuice
tags:
- Knowledge Base
- Software-as-a-Service
- Customer Service
- Artificial Intelligence
- Documentation
website: https://helpjuice.com
---
