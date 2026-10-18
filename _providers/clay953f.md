---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.2
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API documentation is available but machine‑readable specifications were not found.
  name: Clay API
  slug: clay-api
- baseURL: https://api.clay.com/public/v0
  baseurl_source: spec
  description: Workspace credit balances.
  name: Clay953f Credits API
  slug: clay953f-credits-api
- baseURL: https://api.clay.com/public/v0
  baseurl_source: spec
  description: Authenticated user and workspace endpoints.
  name: Clay953f Me API
  slug: clay953f-me-api
- baseURL: https://api.clay.com/public/v0
  baseurl_source: spec
  description: Routine discovery and execution endpoints.
  name: Clay953f Routines API
  slug: clay953f-routines-api
- baseURL: https://api.clay.com/public/v0
  baseurl_source: spec
  description: Search creation and pagination endpoints.
  name: Clay953f Search API
  slug: clay953f-search-api
- baseURL: https://api.clay.com/public/v0
  baseurl_source: spec
  description: Structured table query endpoints.
  name: Clay953f Tables API
  slug: clay953f-tables-api
- baseURL: https://api.clay.com/public/v0
  baseurl_source: spec
  description: Search workflow runs by query.
  name: Clay953f Workflows Runs API
  slug: clay953f-workflowsruns-api
artifact_total: 13
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/plans/clay953f-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clay953f-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/rules/clay953f-rules.yml
  title: ''
  type: Spectral
  url: rules/clay953f-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/json-ld/clay953f-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clay953f-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/vocabulary/clay953f-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clay953f-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/data-model/clay953f-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clay953f-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/changelog/clay953f-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/clay953f-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/conventions/clay953f-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clay953f-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.clay.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/authentication/clay953f-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clay953f-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/errors/clay953f-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clay953f-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/conformance/clay953f-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clay953f-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/llms/clay953f-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clay953f-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/a2a/clay953f-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/clay953f-a2a.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/well-known/clay953f-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clay953f-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/well-known/clay953f-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clay953f-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/well-known/clay953f-community-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clay953f-community-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/well-known/clay953f-clay-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clay953f-clay-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/well-known/clay953f-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clay953f-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/hosts/clay953f-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clay953f-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/vendors/clay953f-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clay953f-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.clay.com/glossary/webhooks
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.clay.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clay.com/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clay.com/
- group: start
  title: ''
  type: Sandbox
  url: https://www.clay.com/fr/glossary/sandbox
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clay.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.clay.com/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.clay.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.clay.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.clay.com/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://developers.clay.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/security/clay953f-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clay953f-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clay953f/refs/heads/main/security/clay953f-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clay953f-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clay.com
coverage:
  checked: '2026-10-08'
  detail: Developers portal returns HTML pages rendered via JavaScript, no OpenAPI or other machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://developers.clay.com/quickstart
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-08'
description: Clay is a data infrastructure platform that aggregates over 150 premium data sources and AI research agents into a single system, enabling users to run agentic workflows and launch go‑to‑market (GTM) plays that turn insights into revenue. It offers a 14‑day free trial with no credit card required, targeting marketers, sales teams, and product managers seeking automated growth workflows.
image: https://cdn.prod.website-files.com/61477f2c24a826836f969afe/6a3ab15061812432ead96f56_Clay_Homepage_og-image%201000.png
jsonld:
- class_count: 48
  name: Clay953F Context
  property_count: 89
  slug: clay953f-context
layout: provider
modified: '2026-10-08'
name: Clay953f
nav: Providers
network: true
overview: 'Clay953f publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Credits API, Me API, Routines API, and 4 more. Tagged areas include Data Marketplace, CRM Enrichment, and AI Agents.


  The Clay953f catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clay953f''s developer surface includes changelog, authentication, sandbox, pricing, engineering blog, getting-started guide, API reference, and 28 more developer resources.'
plans:
- name: Clay953F Plans Pricing
  plan_count: 3
  slug: clay953f-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Clay953f API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: clay953f-rules
score:
  band: developing
  composite: 53.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 55.8
    catalog_earned_first_party: 12.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 35.6
    contract_quality: 56.9
    developer_ergonomics: 42.3
    discoverability: 57.1
    operational_transparency: 50.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Clay953F Authentication
  slug: clay953f-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Clay953F Domain Security
  slug: clay953f-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Clay953F Vulnerability Disclosure
  slug: clay953f-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: clay953f
tags:
- Data Marketplace
- CRM Enrichment
- AI Agents
website: https://www.clay.com
---
