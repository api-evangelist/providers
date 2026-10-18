---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 3.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Kissflow low-code platform
  name: Kissflow API
  slug: kissflow-api
artifact_total: 4
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/kissflow/refs/heads/main/changelog/kissflow-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/kissflow-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://kissflow.com/compliance/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kissflow/refs/heads/main/conformance/kissflow-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kissflow-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kissflow/refs/heads/main/llms/kissflow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kissflow-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kissflow/refs/heads/main/well-known/kissflow-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kissflow-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kissflow/refs/heads/main/well-known/kissflow-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kissflow-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kissflow/refs/heads/main/hosts/kissflow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kissflow-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kissflow/refs/heads/main/vendors/kissflow-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kissflow-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kissflow/refs/heads/main/packages/kissflow-packages.yml
  title: ''
  type: SDKs
  url: packages/kissflow-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kissflow/refs/heads/main/packages/kissflow-packages.yml
  title: ''
  type: Packages
  url: packages/kissflow-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://kissflow.com/workflow/glossary/webhooks/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kissflow.com/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://help.kissflow.com/en/
- group: auth
  title: ''
  type: Security
  url: https://kissflow.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kissflow.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://kissflow.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://community.kissflow.com/login
- group: other
  title: ''
  type: Leadership
  url: https://kissflow.com/project/team/how-to-delegate-tasks-effectively/
- group: start
  title: ''
  type: GettingStarted
  url: https://kissflow.com/get-started/
- group: operate
  title: ''
  type: ChangeLog
  url: https://kissflow.com/whats-new
- group: company
  title: ''
  type: Blog
  url: https://kissflow.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://developers.kissflow.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kissflow
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kissflow/refs/heads/main/security/kissflow-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/kissflow-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kissflow/refs/heads/main/security/kissflow-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kissflow-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kissflow/refs/heads/main/security/kissflow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kissflow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kissflow.com
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://academy.kissflow.com/api/graphql
  - status: 403
    url: https://kissflow.com/mcp
  - status: 403
    url: https://careers.kissflow.com/mcp
  - status: 200
    url: https://kissflow.com
  reason: partner-login
  state: gated
created: '2026-10-13'
description: Kissflow provides a low-code platform that enables enterprises to build custom applications, automate workflows, and integrate with existing systems using AI-driven tools. The solution supports rapid digital transformation across industries such as finance, healthcare, manufacturing, and retail, offering features like governance, security compliance, and a marketplace of pre-built apps. It aims to empower citizen developers and IT leaders to create end‑to‑end processes without extensive coding.
image: https://kissflow.com/hubfs/OG%20Homepage.webp
layout: provider
modified: '2026-10-13'
name: Kissflow
nav: Providers
network: true
overview: 'Kissflow is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Low-Code, Workflow Automation, enterprise-apps, Integration, and digital-transformation.


  Kissflow''s developer surface includes changelog, support, pricing, getting-started guide, engineering blog, documentation, and 21 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 66.1
    operational_transparency: 39.5
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kissflow Domain Security
  slug: kissflow-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kissflow Vulnerability Disclosure
  slug: kissflow-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Kissflow Trust Center
  slug: kissflow-trust-center
  summary_line: SOC 2, ISO 27001
slug: kissflow
tags:
- Low-Code
- Workflow Automation
- enterprise-apps
- Integration
- digital-transformation
- Company
website: https://kissflow.com
---
