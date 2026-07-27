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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: The Environmental Conservation Online System (ECOS) is the USFWS portal for threatened and endangered species data, critical habitat designations, recovery plans, and Section 7 consultations. ECOS exp
  name: USFWS Environmental Conservation Online System (ECOS)
  slug: ecos
- description: The Service Catalog (ServCat) is the USFWS reference library for reports, datasets, and other documents produced by or for the agency. ServCat is backed by an internal services layer; while the catalo
  name: USFWS Service Catalog (ServCat)
  slug: servcat
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fish-and-wildlife-service-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/USFWS
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usfws
- group: company
  title: ''
  type: Website
  url: https://www.fws.gov
- group: other
  title: ''
  type: Data
  url: https://www.fws.gov/library/collections/data
- group: other
  title: ''
  type: ECOS
  url: https://ecos.fws.gov/ecp/
- group: other
  title: ''
  type: IPaC
  url: https://ipac.ecosphere.fws.gov/
- group: other
  title: ''
  type: ServCat
  url: https://ecos.fws.gov/ServCat/
created: '2024-12-03'
description: The U.S. Fish and Wildlife Service (USFWS) is the federal agency responsible for conserving, protecting, and enhancing fish, wildlife, plants, and their habitats for the continuing benefit of the American people. USFWS programs cover migratory birds, endangered species, interjurisdictional fish and marine mammals, and inland sport fisheries. Public-facing data is shared primarily through web tools and downloadable datasets such as the Environmental Conservation Online System (ECOS), Information for Planning and Consultation (IPaC), and the Service Catalog (ServCat) rather than a consolidated public API program.
finops:
- name: Fish And Wildlife Service Finops
  service_category: API
  slug: fish-and-wildlife-service-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fish-and-wildlife-service.png
layout: provider
modified: '2026-07-25'
name: U.S. Fish and Wildlife Service
nav: Providers
network: true
overview: U.S. Fish and Wildlife Service publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Conservation, Endangered Species, Federal Government, Fisheries, and Wildlife.
plans:
- name: Fish And Wildlife Service Plans Pricing
  plan_count: 3
  slug: fish-and-wildlife-service-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Fish And Wildlife Service Rate Limits
  slug: fish-and-wildlife-service-rate-limits
score:
  band: emerging
  composite: 20.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 20.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fish-and-wildlife-service/refs/heads/main/screenshots/fish-and-wildlife-service-2026-06-20T181254.png
security:
- kind: domain-security
  name: Fish And Wildlife Service Domain Security
  slug: fish-and-wildlife-service-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: fish-and-wildlife-service
tags:
- Conservation
- Endangered Species
- Federal Government
- Fisheries
- Wildlife
website: https://www.fws.gov
---
