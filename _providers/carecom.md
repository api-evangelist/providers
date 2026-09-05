---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carecom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.care.com
- group: company
  title: ''
  type: CorporateWebsite
  url: https://www.care.com/about/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/care-com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/caredotcom
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.care.com
- group: commercial
  title: ''
  type: Plans
  url: https://www.care.com/hiw/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.iac.com
created: '2026-07-03'
description: Care.com is a two-sided online marketplace that connects families with caregivers across childcare, senior care, pet care, housekeeping, tutoring, and special-needs care, plus a "Care for Business" employer benefit used by companies such as Google, Starbucks, and Best Buy. Founded in 2007 by Sheila Lirio Marcelo, the company went public on the NYSE (CRCM) in 2014 and was acquired by IAC (IAC Inc.) in February 2020 for approximately $500 million, taking it private. Care.com is consumer- and enterprise-facing and does NOT publish a documented public developer API - there is no developer portal, no public API reference, and no self-service API keys. Its GitHub organization (github.com/caredotcom) contains only internal DevOps/infra tooling, not customer-facing API libraries. The only partner-facing programmatic surface is a private job-import integration inside Care.com Recruiting Solutions / Care for Business, used to sync job postings from an employer ATS; it is provisioned through
  a partnership agreement rather than openly documented. Note - Care.com is frequently confused with Caring.com (a separate senior-care directory owned by Caring, Inc. that DOES publish a JSON API at docs.caring.com); this entry is about care.com only. Access to the marketplace itself is via paid Basic and Premium memberships; there is no published API pricing.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carecom.png
layout: provider
modified: '2026-07-03'
name: Care.com
nav: Providers
network: true
overview: Care.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Care, Childcare, Senior Care, Pet Care, and Housekeeping.
random_paper: 16
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 6.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carecom/refs/heads/main/screenshots/carecom-2026-07-25T204535.png
security:
- kind: domain-security
  name: Carecom Domain Security
  slug: carecom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carecom
tags:
- Care
- Childcare
- Senior Care
- Pet Care
- Housekeeping
- Marketplace
- Caregivers
- Two-Sided Marketplace
- IaC
- No Public API
website: https://www.care.com
---
