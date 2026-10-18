---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.4
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: BracketView provides a privacy‑first online JSON workspace with features like viewing, formatting, validating, querying, diffing, and schema generation via a web app.
  name: BracketView API
  slug: bracketview-api
artifact_total: 4
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bracketview/refs/heads/main/plans/bracketview-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bracketview-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bracketview/refs/heads/main/changelog/bracketview-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bracketview-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://bracketview.in/privacy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bracketview/refs/heads/main/llms/bracketview-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bracketview-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bracketview/refs/heads/main/well-known/bracketview-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bracketview-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bracketview/refs/heads/main/well-known/bracketview-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bracketview-app-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bracketview/refs/heads/main/well-known/bracketview-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bracketview-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bracketview/refs/heads/main/hosts/bracketview-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bracketview-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bracketview/refs/heads/main/vendors/bracketview-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bracketview-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://app.bracketview.in/webhooks
- group: operate
  title: ''
  type: ChangeLog
  url: https://bracketview.in/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bracketview/refs/heads/main/security/bracketview-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bracketview-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bracketview/refs/heads/main/security/bracketview-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bracketview-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bracketview.in/
- group: commercial
  title: ''
  type: Pricing
  url: https://bracketview.in/pricing
- group: company
  title: ''
  type: Blog
  url: https://bracketview.in/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bracketview.in/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bracketview.in/privacy
- group: operate
  title: ''
  type: Support
  url: https://bracketview.in/contact
coverage:
  checked: '2026-10-16'
  detail: BracketView's public site provides documentation but no machine‑readable OpenAPI, GraphQL, AsyncAPI, or other contract.
  evidence:
  - status: 200
    url: https://bracketview.in/
  - status: 404
    url: https://api.bracketview.in/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: BracketView provides a privacy‑first online JSON workspace that lets users view, format, validate, query (JSONPath + jq), diff, and generate schemas directly in the browser. It offers multiple visualizations such as tree, graph, node cards, and nested tables, supporting nine UI languages. Optional AI‑assisted fixes, encrypted snapshots, and a webhook tester are available as paid features. The service also includes a downloadable Windows and Linux desktop app for offline use, ensuring data never leaves the user's device unless explicitly chosen.
image: https://bracketview.in/og-image.webp
layout: provider
modified: '2026-10-16'
name: BracketView
nav: Providers
network: true
overview: 'BracketView is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include JSON, Workspace, Formatter, Viewer, and Privacy.


  BracketView''s developer surface includes changelog, pricing, engineering blog, support, and 15 more developer resources.'
plans:
- name: Bracketview Plans Pricing
  plan_count: 2
  slug: bracketview-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 64.3
    operational_transparency: 34.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bracketview Domain Security
  slug: bracketview-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bracketview Vulnerability Disclosure
  slug: bracketview-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bracketview
tags:
- JSON
- Workspace
- Formatter
- Viewer
- Privacy
website: https://bracketview.in/
---
