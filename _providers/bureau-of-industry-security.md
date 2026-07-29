---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bureau Of Industry Security Agentic Access
  operation_count: 1
  slug: bureau-of-industry-security-agentic-access
  summary_line: 1 operation
api_count: 3
apis:
- description: The Consolidated Screening List (CSL) API consolidates export screening lists from the Departments of Commerce, State, and Treasury. It includes the Entity List, Denied Persons List, Unverified List (
  name: Consolidated Screening List (CSL) API
  slug: consolidated-screening-list-api
- description: SNAP-R (Simplified Network Application Process Redesign) is the BIS online system for applying for export licenses, classifications, and authorizations under the Export Administration Regulations (EAR
  name: SNAP-R Export License Application System
  slug: snap-r
- description: Search the Consolidated Screening List
  name: Bureau of Industry Security Search API
  slug: bureau-of-industry-security-search-api
artifact_total: 10
collections:
- collection_type: open
  name: Consolidated Screening List (CSL) API
  slug: open-bureau-of-industry-security
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bureau-of-industry-security-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bureau-of-industry-security-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bureau-of-industry-security-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-industry-and-security-u-s-department-of-commerce
- group: company
  title: ''
  type: Website
  url: https://www.bis.gov
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bis.gov/privacy-policy
- group: other
  title: ''
  type: Consolidated Screening List
  url: https://www.trade.gov/consolidated-screening-list
- group: other
  title: ''
  type: Export Administration Regulations
  url: https://www.bis.gov/regulations/export-administration-regulations-ear
- group: other
  title: ''
  type: Commerce Control List
  url: https://www.bis.gov/regulations/commerce-control-list-ccl
created: '2024-12-25'
description: 'The Bureau of Industry and Security (BIS) is a division of the U.S. Department of Commerce that implements and enforces export control regulations to protect national security and prevent the proliferation of weapons of mass destruction. BIS reviews license applications for the export of sensitive goods and technologies, conducts outreach on compliance with export control laws, and maintains the Consolidated Screening List. Note: this entry is an alias for bureau-of-industry-and-security.'
finops:
- name: Bureau Of Industry Security Finops
  service_category: API
  slug: bureau-of-industry-security-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-industry-security.png
layout: provider
modified: '2026-04-21'
name: Bureau of Industry Security
nav: Providers
network: true
overview: 'Bureau of Industry Security publishes 1 API on the [APIs.io](https://apis.io/) network: Search API. Tagged areas include Compliance, Export Controls, Federal Government, Industries, and National Security.


  Bureau of Industry Security''s developer surface includes authentication and 8 more developer resources.'
plans:
- name: Bureau Of Industry Security Plans Pricing
  plan_count: 3
  slug: bureau-of-industry-security-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 5
  name: Bureau Of Industry Security Rate Limits
  slug: bureau-of-industry-security-rate-limits
score:
  band: thin
  composite: 38.2
  delta: -1.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.9
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bureau-of-industry-security/refs/heads/main/screenshots/bureau-of-industry-security-2026-06-20T173808.png
security:
- kind: authentication
  name: Bureau Of Industry Security Authentication
  slug: bureau-of-industry-security-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bureau Of Industry Security Domain Security
  slug: bureau-of-industry-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bureau-of-industry-security
tags:
- Compliance
- Export Controls
- Federal Government
- Industries
- National Security
- Screening Lists
- Security
website: https://www.bis.gov
---
