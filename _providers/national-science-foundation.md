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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: National Science Foundation Agentic Access
  operation_count: 3
  slug: national-science-foundation-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://api.nsf.gov/services/v1/
  baseurl_source: declared
  description: The Awards API from National Science Foundation — 2 operation(s) for awards.
  name: National Science Foundation Awards API
  slug: national-science-foundation-awards-api
- baseURL: https://api.nsf.gov/services/v1/
  baseurl_source: declared
  description: The Awards.{format} API from National Science Foundation — 1 operation(s) for awards.{format}.
  name: National Science Foundation Awards.{format} API
  slug: national-science-foundation-awards-format-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: National Science Foundation Awards API
  slug: open-national-science-foundation-awards-api
- collection_type: open
  name: National Science Foundation Awards Awards.{format} API
  slug: open-national-science-foundation-awards-format-api
- collection_type: open
  name: National Science Foundation Awards API
  slug: open-national-science-foundation
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/national-science-foundation-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-science-foundation-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-science-foundation-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nsf-open
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-science-foundation
- group: company
  title: ''
  type: Website
  url: https://www.nsf.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.nsf.gov/developer
- group: company
  title: ''
  type: Blog
  url: https://www.nsf.gov/rss/rss_www_news.xml
created: '2024-12-03'
description: The National Science Foundation (NSF) is an independent federal agency that supports fundamental research and education in all the non-medical fields of science and engineering. NSF provides grants and funding to researchers and institutions to drive innovation, discovery, and progress.
finops:
- name: National Science Foundation Finops
  service_category: API
  slug: national-science-foundation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-science-foundation.png
layout: provider
modified: '2026-05-19'
name: National Science Foundation
nav: Providers
network: true
overview: 'National Science Foundation publishes 2 APIs on the [APIs.io](https://apis.io/) network: Awards API and Awards.{format} API. Tagged areas include Federal-Government, Research, and Science.


  National Science Foundation''s developer surface includes developer portal, engineering blog, and 6 more developer resources.'
plans:
- name: National Science Foundation Plans Pricing
  plan_count: 3
  slug: national-science-foundation-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: National Science Foundation Rate Limits
  slug: national-science-foundation-rate-limits
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 65.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 43.5
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 22.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-science-foundation/refs/heads/main/screenshots/national-science-foundation-2026-06-20T190040.png
security:
- kind: domain-security
  name: National Science Foundation Domain Security
  slug: national-science-foundation-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: national-science-foundation
tags:
- Federal-Government
- Research
- Science
website: https://www.nsf.gov/
---
