---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Certman is a cloud-based certificate authority management platform. This API allows you to manage Certificate Authorities and issue, renew, and revoke certificates programmatically.
  name: Certman API
  slug: certman-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: Security
  url: https://certman.app/en/security
- group: commercial
  href: https://artifacts.apis.io/certman-app/plans/certman-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/certman-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/certman-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/certman-app/conformance/certman-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/certman-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/certman-app/llms/certman-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/certman-app-llms.txt
- group: auth
  href: https://artifacts.apis.io/certman-app/well-known/certman-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/certman-app-security.txt
- group: agent
  href: https://artifacts.apis.io/certman-app/well-known/certman-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/certman-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/certman-app/hosts/certman-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/certman-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/certman-app/vendors/certman-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/certman-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://certman.app/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://certman.app/en/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://certman.app/en/pricing
- group: start
  title: ''
  type: Login
  url: https://certman.app/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/certman
- group: docs
  title: ''
  type: Documentation
  url: https://certman.app/en/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://certman.app/en/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/certman-app/security/certman-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/certman-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/certman-app/security/certman-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/certman-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://certman.app/
created: '2026-11-03'
description: Certman provides a scalable Certificate Authority platform that automates PKI management for developers and enterprises. It enables creation of root CAs, issuance of unlimited TLS certificates, and integration via API to streamline internal certificate workflows across home labs, DevOps pipelines, and large-scale production environments.
image: https://certman.app/og-image.png
layout: provider
modified: '2026-11-03'
name: Certman
nav: Providers
network: true
overview: 'Certman is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Certificate Authority, PKI, TLS, and Automation.


  Certman''s developer surface includes pricing, documentation, getting-started guide, and 16 more developer resources.'
plans:
- name: Certman App Plans Pricing
  plan_count: 3
  slug: certman-app-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 12.5
    discoverability: 57.1
    operational_transparency: 7.9
  provenance:
    conformance: derived
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Certman App Domain Security
  slug: certman-app-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Certman App Vulnerability Disclosure
  slug: certman-app-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: whoami
  slug: certman-app-whoami-skill
slug: certman-app
tags:
- Certificate Authority
- PKI
- TLS
- Automation
website: https://certman.app/
---
