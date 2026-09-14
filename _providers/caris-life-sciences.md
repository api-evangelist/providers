---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Caris Life Sciences Agentic Access
  operation_count: 3
  slug: caris-life-sciences-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://portal.caris.ai
  baseurl_source: declared
  description: Public informational pages for ordering and integration partners.
  name: Caris Life Sciences Information API
  slug: caris-life-sciences-information-api
- baseURL: https://portal.caris.ai
  baseurl_source: declared
  description: Browser-based Caris+Portal landing surface.
  name: Caris Life Sciences Portal API
  slug: caris-life-sciences-portal-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Caris Life Sciences (Public Surface) Information API
  slug: open-caris-life-sciences-information-api
- collection_type: open
  name: Caris Life Sciences (Public Surface) Information Portal API
  slug: open-caris-life-sciences-portal-api
- collection_type: open
  name: Caris Life Sciences (Public Surface)
  slug: open-caris-life-sciences
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/caris-life-sciences-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/caris-life-sciences-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/caris-life-sciences
- group: company
  title: ''
  type: Website
  url: https://www.carislifesciences.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.carislifesciences.com/partners/ehr-integrations/
- group: commercial
  title: ''
  type: Plans
  url: plans/caris-life-sciences-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/caris-life-sciences-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/caris-life-sciences-finops.yml
created: '2026-06-20'
description: Caris Life Sciences is a molecular science and precision oncology company that delivers comprehensive tumor profiling (Caris Molecular Intelligence / MI Profiling) and a clinico-genomic real-world data platform (CODEai). Clinician access is through the Caris+Portal and partner-provisioned EHR integrations (Epic Orders and Results Anywhere, OncoEMR/Flatiron, iKnowMed, and other CMS-certified systems). Caris does not publish a public, self-serve developer API; integration is partner- and contract-based.
finops:
- name: Caris Life Sciences Finops
  service_category: Healthcare and Life Sciences
  slug: caris-life-sciences-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/caris-life-sciences.png
layout: provider
modified: '2026-06-20'
name: Caris Life Sciences
nav: Providers
network: true
overview: 'Caris Life Sciences publishes 2 APIs on the [APIs.io](https://apis.io/) network: Information API and Portal API. Tagged areas include Precision Oncology, Molecular Profiling, Genomics, Healthcare, and EHR Integration.


  Caris Life Sciences'' developer surface includes documentation and 7 more developer resources.'
plans:
- name: Caris Life Sciences Plans Pricing
  plan_count: 2
  slug: caris-life-sciences-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Caris Life Sciences Rate Limits
  slug: caris-life-sciences-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/caris-life-sciences/refs/heads/main/screenshots/caris-life-sciences-2026-06-20T174006.png
security:
- kind: domain-security
  name: Caris Life Sciences Domain Security
  slug: caris-life-sciences-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: caris-life-sciences
tags:
- Precision Oncology
- Molecular Profiling
- Genomics
- Healthcare
- EHR Integration
- Real-World Data
website: https://www.carislifesciences.com
---
