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
artifact_total: 2
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.levo.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.levo.ai/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.levo.ai/quickstart
- group: operate
  href: https://artifacts.apis.io/levo/changelog/levo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/levo-changelog.yml
- group: auth
  href: https://artifacts.apis.io/levo/authentication/levo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/levo-authentication.yml
- group: other
  href: https://artifacts.apis.io/levo/hosts/levo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/levo-hosts.yml
- group: other
  href: https://artifacts.apis.io/levo/vendors/levo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/levo-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/levoai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.levo.ai/changelog
- group: auth
  href: https://artifacts.apis.io/levo/security/levo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/levo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://levo.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.levo.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.levo.ai/resources/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.levo.ai/pricing
created: '2026-10-21'
description: Levo provides an AI‑powered API security platform that protects both traditional APIs and emerging AI‑driven services. The solution offers runtime visibility, threat detection, red‑teaming, and governance across the entire application stack, integrating with CI/CD pipelines and supporting compliance for industries such as banking, insurance, healthcare, and retail. Levo’s platform unifies API and AI security, delivering real‑time risk insights, automated policy enforcement, and detailed reporting to help organizations secure complex, dynamic micro‑service architectures and AI models.
image: https://cdn.prod.website-files.com/68d0ca01084046ac052b0d8d/68e354afe74b7b9c68f91e54_d5889fa56eef309d6a1e006a97e83701_Levo%27s%20Open%20Graph%20Logo.svg
layout: provider
modified: '2026-10-21'
name: Levo
nav: Providers
network: true
overview: 'Levo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, AI, API, and Platform.


  Levo''s developer surface includes getting-started guide, changelog, authentication, documentation, engineering blog, pricing, and 8 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 48.2
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Levo Authentication
  slug: levo-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Levo Domain Security
  slug: levo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: levo
tags:
- Company
- Security
- AI
- API
- Platform
website: https://levo.ai/
---
