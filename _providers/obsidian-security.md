---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Obsidian Security is a SaaS security platform providing threat detection, posture management, and compliance monitoring for cloud applications.
  name: Obsidian Security
  slug: obsidian-security
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/obsidian-security-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/obsidian-security-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/obsidian-security
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/obsidiansecurity
- group: company
  title: ''
  type: Website
  url: https://www.obsidiansecurity.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.obsidiansecurity.com/resources
- group: company
  title: ''
  type: Blog
  url: https://www.obsidiansecurity.com/blog
created: '2026-03-27'
description: Obsidian Security is a SaaS security platform providing threat detection, posture management, and compliance monitoring for cloud applications.
finops:
- name: Obsidian Security Finops
  service_category: API
  slug: obsidian-security-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/obsidian-security.png
layout: provider
modified: '2026-04-28'
name: Obsidian Security
nav: Providers
network: true
overview: 'Obsidian Security publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SaaS Security and Threat Detection.


  Obsidian Security''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Obsidian Security Plans Pricing
  plan_count: 3
  slug: obsidian-security-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Obsidian Security Rate Limits
  slug: obsidian-security-rate-limits
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 10.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/obsidian-security/refs/heads/main/screenshots/obsidian-security-2026-06-20T190555.png
security:
- kind: domain-security
  name: Obsidian Security Domain Security
  slug: obsidian-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Obsidian Security Trust Center
  slug: obsidian-security-trust-center
  summary_line: SOC 2, ISO 27001
slug: obsidian-security
tags:
- SaaS Security
- Threat Detection
website: https://www.obsidiansecurity.com
---
