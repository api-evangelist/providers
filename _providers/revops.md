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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/revops/plans/revops-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/revops-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/revops/changelog/revops-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/revops-changelog.yml
- group: start
  href: https://artifacts.apis.io/revops/sandbox/revops-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/revops-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/revops/authentication/revops-authentication.yml
  title: ''
  type: Authentication
  url: authentication/revops-authentication.yml
- group: auth
  href: https://artifacts.apis.io/revops/well-known/revops-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/revops-status-security.txt
- group: agent
  href: https://artifacts.apis.io/revops/well-known/revops-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/revops-well-known.yml
- group: other
  href: https://artifacts.apis.io/revops/hosts/revops-hosts.yml
  title: ''
  type: Hosts
  url: hosts/revops-hosts.yml
- group: other
  href: https://artifacts.apis.io/revops/vendors/revops-vendors.yml
  title: ''
  type: Vendors
  url: vendors/revops-vendors.yml
- group: build
  href: https://artifacts.apis.io/revops/packages/revops-packages.yml
  title: ''
  type: SDKs
  url: packages/revops-packages.yml
- group: build
  href: https://artifacts.apis.io/revops/packages/revops-packages.yml
  title: ''
  type: Packages
  url: packages/revops-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.revops.io
- group: auth
  title: ''
  type: Security
  url: https://www.revops.io/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.revops.io/release-notes
- group: auth
  href: https://artifacts.apis.io/revops/security/revops-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/revops-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/revops/security/revops-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/revops-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.revops.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.revops.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.revops.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.revops.io/guides/quick-start/
- group: operate
  title: ''
  type: Support
  url: mailto:support@revops.io
- group: company
  title: ''
  type: Blog
  url: https://www.revops.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.revops.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.revops.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.revops.io/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.revops.io/cookie-policy
- group: other
  title: ''
  type: Disclaimer
  url: https://www.revops.io/disclaimer
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/revops/workspace
- group: start
  title: ''
  type: SignUp
  url: https://app.revops.io/signup
coverage:
  checked: '2026-10-23'
  detail: Docs site returns HTML shells and no OpenAPI spec at known paths.
  evidence:
  - status: 404
    url: https://docs.revops.io/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: RevOps provides a modern CPQ and deal desk platform that streamlines revenue operations for SaaS and enterprise businesses. The solution offers configurable approval workflows, integration with HubSpot, Salesforce, DocuSign, Maxio, Chargebee, Slack, and Google Workspace, enabling teams to create, manage, and close deals efficiently. Acquired by Maxio, RevOps continues to expand its feature set with advanced pricing tables, contract templates, and real‑time collaboration tools, positioning itself as a comprehensive revenue operations hub.
image: https://www.revops.io/design-assets/logos/Logomark-Gradient-no-bg.svg
layout: provider
modified: '2026-10-22'
name: RevOps
nav: Providers
network: true
overview: 'RevOps is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include CPQ, Revenue-Operations, SaaS, Integrations, and Deal-Desk.


  RevOps'' developer surface includes changelog, sandbox, authentication, documentation, getting-started guide, support, engineering blog, and 21 more developer resources.'
plans:
- name: Revops Plans Pricing
  plan_count: 3
  slug: revops-plans-pricing
random_paper: 23
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 48.2
    operational_transparency: 42.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Revops Authentication
  slug: revops-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Revops Domain Security
  slug: revops-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Revops Vulnerability Disclosure
  slug: revops-vulnerability-disclosure
  summary_line: no policy recorded
slug: revops
tags:
- CPQ
- Revenue-Operations
- SaaS
- Integrations
- Deal-Desk
website: https://www.revops.io/
---
