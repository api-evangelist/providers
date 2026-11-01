---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Backend API for Manufact Cloud
  name: Manufact Cloud API
  slug: manufact-cloud-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/manufact/plans/manufact-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/manufact-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/manufact/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/manufact/cli/manufact-cli.yml
  title: ''
  type: CLI
  url: cli/manufact-cli.yml
- group: auth
  href: https://artifacts.apis.io/manufact/authentication/manufact-authentication.yml
  title: ''
  type: Authentication
  url: authentication/manufact-authentication.yml
- group: design
  href: https://artifacts.apis.io/manufact/conformance/manufact-conformance.yml
  title: ''
  type: Conformance
  url: conformance/manufact-conformance.yml
- group: agent
  href: https://artifacts.apis.io/manufact/llms/manufact-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/manufact-llms.txt
- group: agent
  href: https://artifacts.apis.io/manufact/well-known/manufact-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/manufact-well-known.yml
- group: other
  href: https://artifacts.apis.io/manufact/hosts/manufact-hosts.yml
  title: ''
  type: Hosts
  url: hosts/manufact-hosts.yml
- group: other
  href: https://artifacts.apis.io/manufact/vendors/manufact-vendors.yml
  title: ''
  type: Vendors
  url: vendors/manufact-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://manufact.com/signup
- group: auth
  title: ''
  type: Security
  url: https://manufact.com/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mcp-use
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.manufact.com/dashboard/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.manufact.com/dashboard/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://manufact.com/developers
- group: auth
  href: https://artifacts.apis.io/manufact/security/manufact-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/manufact-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/manufact/security/manufact-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/manufact-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://manufact.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.manufact.com
- group: commercial
  title: ''
  type: Pricing
  url: https://manufact.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://manufact.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://manufact.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://manufact.com/blog
- group: operate
  title: ''
  type: Support
  url: https://manufact.com/support
created: '2026-10-18'
description: Manufact (formerly mcp-use) is a company that provides manufacturing data APIs, enabling developers to integrate real‑time production metrics, inventory levels, and supply‑chain insights into their applications. The platform offers endpoints for retrieving factory performance, equipment status, and operational analytics, supporting JSON and CSV formats. It aims to streamline manufacturing workflows, improve visibility across production lines, and facilitate data‑driven decision making for enterprises seeking to optimize their operations and reduce downtime.
image: https://manufact.com/og-image.jpg
layout: provider
modified: '2026-10-18'
name: Manufact (formerly mcp-use)
nav: Providers
network: true
overview: 'Manufact (formerly mcp-use) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Data, and Supply Chain.


  Manufact (formerly mcp-use)''s developer surface includes CLI, authentication, signup flow, getting-started guide, changelog, API reference, documentation, and 17 more developer resources.'
plans:
- name: Manufact Plans Pricing
  plan_count: 5
  slug: manufact-plans-pricing
random_paper: 7
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 61.2
    discoverability: 57.1
    operational_transparency: 31.6
  previous_composite: 42.7
  provenance:
    conformance: first-party
    mcp: derived
    skills: unknown
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
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Manufact Authentication
  slug: manufact-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Manufact Domain Security
  slug: manufact-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Manufact Vulnerability Disclosure
  slug: manufact-vulnerability-disclosure
  summary_line: no policy recorded
slug: manufact
tags:
- Company
- Manufacturing
- Data
- Supply Chain
website: https://manufact.com/
---
