---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.1
  scored_at: '2026-10-03'
api_count: 3
apis:
- description: API for Ambition's revenue operations platform, referenced in help articles.
  name: Ambition API
  slug: ambition-api
- baseURL: https://SUBDOMAIN.ambition.com
  baseurl_source: declared
  description: The Account API from Ambitioninc — 1 operation(s) for account.
  name: Ambitioninc Account API
  slug: ambitioninc-account-api
- baseURL: https://SUBDOMAIN.ambition.com
  baseurl_source: declared
  description: The Data API from Ambitioninc — 1 operation(s) for data.
  name: Ambitioninc Data API
  slug: ambitioninc-data-api
artifact_total: 8
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ambitioninc/refs/heads/main/plans/ambitioninc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ambitioninc-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ambitioninc/refs/heads/main/rules/ambitioninc-rules.yml
  title: ''
  type: Spectral
  url: rules/ambitioninc-rules.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ambitioninc/refs/heads/main/changelog/ambitioninc-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ambitioninc-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.ambition.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ambitioninc/refs/heads/main/authentication/ambitioninc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ambitioninc-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ambitioninc/refs/heads/main/conformance/ambitioninc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ambitioninc-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ambitioninc/refs/heads/main/llms/ambitioninc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ambitioninc-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ambitioninc/refs/heads/main/well-known/ambitioninc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ambitioninc-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ambitioninc/refs/heads/main/hosts/ambitioninc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ambitioninc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ambitioninc/refs/heads/main/vendors/ambitioninc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ambitioninc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ambition.com/terms
- group: operate
  title: ''
  type: Support
  url: https://help.ambition.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ambition.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://ambition.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://ambition.com/blog/we-do-coaching
- group: start
  title: ''
  type: GettingStarted
  url: https://help.ambition.com/articles/4369357246-how-do-i-set-up-the-coaching-quickstart-and-access-check-in-visualizations-within-domo
- group: docs
  title: ''
  type: Documentation
  url: https://help.ambition.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ambitioninc/refs/heads/main/security/ambitioninc-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ambitioninc-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ambitioninc/refs/heads/main/security/ambitioninc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ambitioninc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ambition.com
coverage:
  checked: 2026-09-24
  detail: Documentation pages are JavaScript‑rendered and no OpenAPI spec is discoverable.
  evidence:
  - status: 200
    url: https://help.ambition.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-24'
description: Ambitioninc provides a revenue operations platform that helps sales teams improve performance through AI‑driven coaching, real‑time analytics, and workflow automation. The solution integrates with CRM and communication tools, offering dashboards, gamification, and data‑driven insights to boost productivity and align revenue goals across the organization.
image: https://cdn.prod.website-files.com/6984499d58b4a2c470a1db24/699e04a5d021c325fc2db81f_OG.png
layout: provider
modified: '2026-09-24'
name: Ambitioninc
nav: Providers
network: true
overview: 'Ambitioninc publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Account API, Data API, and 1 more. Tagged areas include Software-as-a-Service, Revenue Operations, Sales Enablement, Artificial Intelligence, and Platform.


  The Ambitioninc catalog on APIs.io includes 1 Spectral governance ruleset.


  Ambitioninc''s developer surface includes changelog, authentication, support, pricing, engineering blog, getting-started guide, documentation, and 13 more developer resources.'
plans:
- name: Ambitioninc Plans Pricing
  plan_count: 3
  slug: ambitioninc-plans-pricing
random_paper: 21
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Ambitioninc API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: ambitioninc-rules
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 51.5
    catalog_earned_first_party: 12.0
    catalog_gap: 63.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 11.9
    developer_ergonomics: 40.5
    discoverability: 69.6
    operational_transparency: 15.8
  previous_composite: 48.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: falling
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Ambitioninc Authentication
  slug: ambitioninc-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ambitioninc Domain Security
  slug: ambitioninc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ambitioninc Trust Center
  slug: ambitioninc-trust-center
  summary_line: SOC 2
slug: ambitioninc
tags:
- Software-as-a-Service
- Revenue Operations
- Sales Enablement
- Artificial Intelligence
- Platform
website: https://ambition.com
---
