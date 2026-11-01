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
  href: https://artifacts.apis.io/sweethawk/plans/sweethawk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sweethawk-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/sweethawk/security/sweethawk-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/sweethawk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sweethawk/authentication/sweethawk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sweethawk-authentication.yml
- group: design
  href: https://artifacts.apis.io/sweethawk/conformance/sweethawk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sweethawk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sweethawk/llms/sweethawk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sweethawk-llms.txt
- group: other
  href: https://artifacts.apis.io/sweethawk/hosts/sweethawk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sweethawk-hosts.yml
- group: other
  href: https://artifacts.apis.io/sweethawk/vendors/sweethawk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sweethawk-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.sweethawk.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sweethawk.com/terms
- group: operate
  title: ''
  type: Support
  url: https://support.sweethawk.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sweethawk.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://sweethawk.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.sweethawk.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://sweethawk.com/guides
- group: company
  title: ''
  type: Blog
  url: https://sweethawk.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://sweethawk.com/guides/how-to-automate-employee-onboarding-in-zendesk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SweetHawk
- group: auth
  href: https://artifacts.apis.io/sweethawk/security/sweethawk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sweethawk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sweethawk/security/sweethawk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sweethawk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sweethawk.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://support.sweethawk.com/mcp
  - status: 200
    url: https://sweethawk.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: SweetHawk offers a suite of Zendesk apps that add workflow capabilities such as multi‑step approvals, task and subticket management, scheduling, surveys, and visual ticket boards. The apps are designed for internal service desks that handle IT and HR processes, enabling teams to automate approvals, change management, onboarding, and recurring work within Zendesk. Customers include organizations that run employee service, ITSM, and HR service desks on the Zendesk platform.
layout: provider
modified: '2026-10-21'
name: Sweethawk
nav: Providers
network: true
overview: 'Sweethawk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Zendesk apps, IT service management, HR service, Employee service desk, and Workflow automation.


  Sweethawk''s developer surface includes authentication, support, pricing, documentation, engineering blog, getting-started guide, and 14 more developer resources.'
plans:
- name: Sweethawk Plans Pricing
  plan_count: 26
  slug: sweethawk-plans-pricing
random_paper: 19
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 44.6
    operational_transparency: 15.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Sweethawk Authentication
  slug: sweethawk-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sweethawk Domain Security
  slug: sweethawk-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Sweethawk Vulnerability Disclosure
  slug: sweethawk-vulnerability-disclosure
  summary_line: no policy recorded
slug: sweethawk
tags:
- Zendesk apps
- IT service management
- HR service
- Employee service desk
- Workflow automation
- Change management
website: https://sweethawk.com/
---
