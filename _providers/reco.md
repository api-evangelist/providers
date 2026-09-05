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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Reco is a SaaS security platform using identity-centric analysis to detect threats, prevent data exposure, and manage access across SaaS applications.
  name: Reco
  slug: reco
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/reco-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reco-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/recolabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/recolabs
- group: company
  title: ''
  type: Website
  url: https://www.reco.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.reco.ai/resources
- group: agent
  title: ''
  type: LlmsText
  url: https://www.reco.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.reco.ai/blog/rss.xml
created: '2026-03-27'
description: Reco is a SaaS security platform using identity-centric analysis to detect threats, prevent data exposure, and manage access across SaaS applications.
finops:
- name: Reco Finops
  service_category: API
  slug: reco-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reco.png
layout: provider
modified: '2026-04-28'
name: Reco
nav: Providers
network: true
overview: 'Reco publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Identity Security and SaaS Security.


  Reco''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Reco Plans Pricing
  plan_count: 3
  slug: reco-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Reco Rate Limits
  slug: reco-rate-limits
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 7
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
    developer_ergonomics: 11.9
    discoverability: 48.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reco/refs/heads/main/screenshots/reco-2026-06-20T192700.png
security:
- kind: domain-security
  name: Reco Domain Security
  slug: reco-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Reco Trust Center
  slug: reco-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CSA STAR
slug: reco
tags:
- Identity Security
- SaaS Security
website: https://www.reco.ai
---
