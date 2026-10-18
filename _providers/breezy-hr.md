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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-10-17'
api_count: 3
apis:
- description: Breezy HR provides a hiring software API documented at the Guides page.
  name: Breezy HR API
  slug: breezy-hr-api-2
- baseURL: https://api.breezy.hr
  baseurl_source: declared
  description: The Breezy HR API API from Breezy HR — 1 operation(s) for breezy hr api.
  name: Breezy HR Breezy HR API
  slug: breezy-hr-breezy-hr-api-api
- baseURL: https://api.breezy.hr
  baseurl_source: declared
  description: The Sign In API from Breezy HR — 1 operation(s) for sign in.
  name: Breezy HR Sign In API
  slug: breezy-hr-sign-in-api
artifact_total: 10
asyncapis:
- description: ''
  name: Breezy Hr Webhooks
  slug: breezy-hr-webhooks
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/breezy-hr/refs/heads/main/rate-limits/breezy-hr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/breezy-hr-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/breezy-hr/refs/heads/main/plans/breezy-hr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/breezy-hr-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/breezy-hr/refs/heads/main/rules/breezy-hr-rules.yml
  title: ''
  type: Spectral
  url: rules/breezy-hr-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/breezy-hr/refs/heads/main/asyncapi/breezy-hr-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/breezy-hr-webhooks.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/breezy-hr/refs/heads/main/changelog/breezy-hr-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/breezy-hr-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://ltgplc.com/trust-center/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/breezy-hr/refs/heads/main/authentication/breezy-hr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/breezy-hr-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/breezy-hr/refs/heads/main/conformance/breezy-hr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/breezy-hr-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/breezy-hr/refs/heads/main/llms/breezy-hr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/breezy-hr-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/breezy-hr/refs/heads/main/well-known/breezy-hr-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/breezy-hr-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/breezy-hr/refs/heads/main/well-known/breezy-hr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/breezy-hr-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/breezy-hr/refs/heads/main/hosts/breezy-hr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/breezy-hr-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/breezy-hr/refs/heads/main/vendors/breezy-hr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/breezy-hr-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://breezy.hr/policies/terms
- group: operate
  title: ''
  type: Support
  url: https://help.breezy.hr/en/
- group: start
  title: ''
  type: SignUp
  url: https://breezy.hr/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://breezy.hr/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://breezy.hr/pricing
- group: other
  title: ''
  type: Leadership
  url: https://breezy.hr/resources/interview-questions/leadership
- group: company
  title: ''
  type: Blog
  url: https://breezy.hr/blog/hr-memes
- group: start
  title: ''
  type: GettingStarted
  url: https://help.breezy.hr/en/articles/5578138-getting-started-with-breezy
- group: docs
  title: ''
  type: Documentation
  url: https://developer.breezy.hr/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/breezy-hr/refs/heads/main/security/breezy-hr-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/breezy-hr-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/breezy-hr/refs/heads/main/security/breezy-hr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/breezy-hr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://breezy.hr
coverage:
  checked: '2026-10-15'
  detail: Guides page returns 403, preventing access to API documentation.
  evidence:
  - status: 403
    url: https://breezy.hr/resources/guides
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: Breezy HR provides modern hiring software and an applicant tracking system designed to streamline recruitment. Their platform offers tools for job advertising, candidate management, automated workflows, interview scheduling, offer management, and HRIS integrations. Breezy HR aims to help companies attract, qualify, and hire talent efficiently, with analytics and reporting features to improve hiring outcomes.
image: https://cdn.prod.website-files.com/6127d83f257132e4fe0bddc6/679d163729b14e48b0984a3b_breezyhr-home.webp
layout: provider
modified: '2026-10-14'
name: Breezy HR
nav: Providers
network: true
overview: 'Breezy HR is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Breezy HR API, Sign In API, and 1 more. Tagged areas include Hiring, Applicant Tracking, Recruiting, Software-as-a-Service, and Human Resources.


  The Breezy HR catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Breezy HR''s developer surface includes changelog, authentication, support, signup flow, pricing, engineering blog, getting-started guide, and 18 more developer resources.'
plans:
- name: Breezy Hr Plans Pricing
  plan_count: 3
  slug: breezy-hr-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Breezy Hr Rate Limits
  slug: breezy-hr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Breezy HR API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: breezy-hr-rules
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 59.5
    catalog_earned_first_party: 20.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 19.8
    developer_ergonomics: 40.5
    discoverability: 71.4
    operational_transparency: 44.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Breezy Hr Authentication
  slug: breezy-hr-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Breezy Hr Domain Security
  slug: breezy-hr-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Breezy Hr Trust Center
  slug: breezy-hr-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: breezy-hr
tags:
- Hiring
- Applicant Tracking
- Recruiting
- Software-as-a-Service
- Human Resources
website: https://breezy.hr
---
