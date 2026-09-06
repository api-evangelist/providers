---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 22.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Qualcomm Agentic Access
  operation_count: 1
  slug: qualcomm-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://developer.qualcomm.com/api
  baseurl_source: declared
  description: Semiconductors operations
  name: qualcomm Semiconductors API
  slug: qualcomm-semiconductors-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Qualcomm Developer API
  slug: open-qualcomm-qualcomm-api
- collection_type: open
  name: Qualcomm Developer Semiconductors API
  slug: open-qualcomm-semiconductors-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qualcomm-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/qualcomm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qualcomm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qualcomm-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qualcomm
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qualcomm
- group: company
  title: ''
  type: Blog
  url: https://www.qualcomm.com/news
description: Qualcomm is a multinational semiconductor and telecommunications equipment company that creates intellectual property, semiconductors, software, and services related to wireless technology.
finops:
- name: Qualcomm Finops
  service_category: Semiconductors
  slug: qualcomm-finops
graphqls:
- description: This document describes the conceptual GraphQL schema for the Qualcomm Developer API, covering Snapdragon chipsets, AI inference, connectivity, software development kits, and device platform support.
  name: Qualcomm GraphQL Schema
  slug: qualcomm-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qualcomm.png
layout: provider
modified: '2026-05-19'
name: Qualcomm
nav: Providers
network: true
overview: 'Qualcomm publishes 1 API on the [APIs.io](https://apis.io/) network: Semiconductors API. Tagged areas include Fortune 500.


  Qualcomm''s developer surface includes authentication, engineering blog, and 5 more developer resources.'
plans:
- name: Qualcomm Plans Pricing
  plan_count: 1
  slug: qualcomm-plans-pricing
press:
- date: '2026-05-25'
  title: Qualcomm - News & Events - Press Releases
  url: https://investor.qualcomm.com/news-events/press-releases/default.aspx
- date: '2026-05-25'
  title: QUALCOMM Incorporated (QCOM) Latest Press Releases ...
  url: https://ca.finance.yahoo.com/quote/QCOM/press-releases/
- date: '2026-05-25'
  title: AI Research Areas | Intelligence on Devices
  url: https://www.qualcomm.com/research/artificial-intelligence
- date: '2026-05-25'
  title: Investor Events
  url: https://investor.qualcomm.com/news-events/investor-events/default.aspx
- date: '2026-05-25'
  title: Qualcomm Technologies, Inc. News and Press Releases
  url: https://www.prnewswire.com/news/qualcomm-technologies%2C-inc./
random_paper: 2
rate_limits:
- limit_count: 1
  name: Qualcomm Rate Limits
  slug: qualcomm-rate-limits
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 59.6
    developer_ergonomics: 14.3
    discoverability: 44.4
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 25.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qualcomm/refs/heads/main/screenshots/qualcomm-2026-06-20T192405.png
security:
- kind: authentication
  name: Qualcomm Authentication
  slug: qualcomm-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Qualcomm Domain Security
  slug: qualcomm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Qualcomm Vulnerability Disclosure
  slug: qualcomm-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: qualcomm
tags:
- Fortune 500
---
