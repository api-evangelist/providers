---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: The CDW Catalog API uses JSON to deliver customers real-time pricing and inventory status alongside any special pricing or catalog restrictions. It supports integration with eProcurement platforms for
  name: CDW Catalog API
  slug: cdw-catalog-api
- description: CDW eProcurement integration supports PunchOut and Roundtrip catalogs via cXML or OCI, electronic purchase order submission via cXML, EDI, or flat file, and electronic invoicing via XML or EDI. Orders
  name: CDW eProcurement Integration
  slug: cdw-eprocurement-api
artifact_total: 7
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cdw/refs/heads/main/plans/cdw-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cdw-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cdw/refs/heads/main/rate-limits/cdw-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cdw-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cdw/refs/heads/main/finops/cdw-finops.yml
  title: ''
  type: FinOps
  url: finops/cdw-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cdw/refs/heads/main/security/cdw-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cdw-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cdw/refs/heads/main/security/cdw-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cdw-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cdwlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cdw
- group: company
  title: ''
  type: Website
  url: https://www.cdw.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.cdw.com/content/cdw/en/services/eprocurement-and-custom-catalogs.html
- group: other
  title: ''
  type: Overview
  url: https://www.cdw.com/integrations/custompage/v2/6FB6697BBE2441968349584A24C5C459
created: '2024-01-15'
description: CDW is a leading multi-brand provider of information technology solutions to business, government, education, and healthcare customers. CDW offers eProcurement integration capabilities including a Catalog API, PunchOut (cXML/OCI), electronic purchase ordering, and electronic invoicing to enable procurement system integration with partners such as SAP Ariba, Coupa, Oracle, and Jaggaer.
finops:
- has_sources: true
  method: generated
  name: Cdw Finops
  primary_unit: ''
  service_category: IT Distribution + eProcurement
  slug: cdw-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cdw.png
layout: provider
modified: '2026-04-23'
name: CDW
nav: Providers
network: true
overview: 'CDW is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include B2B, Catalog, eProcurement, IT Distribution, and Punchout.


  CDW''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Cdw Plans Pricing
  plan_count: 1
  slug: cdw-plans-pricing
press:
- date: ''
  title: 2025 CDW AI Report
  url: https://www.cdw.com/content/cdw/en/solutions/artificial-intelligence-ai/2025-cdw-ai-report.html
- date: ''
  title: Lessons Learned From CDW's AI Research Report
  url: https://healthtechmagazine.net/article/2025/07/lessons-learned-cdws-ai-research-report
- date: ''
  title: Mission, a CDW Company, Achieves AWS Agentic AI ...
  url: https://www.prnewswire.com/news-releases/mission-a-cdw-company-achieves-aws-agentic-ai-specialization-expanding-enterprise-ai-capabilities-302626953.html
- date: ''
  title: CDW LLC - Financials - Quarterly Results
  url: https://investor.cdw.com/financials/quarterly-results/
- date: ''
  title: Artificial Intelligence (AI) Solutions
  url: https://www.cdw.com/content/cdw/en/solutions/ai-and-data/artificial-intelligence-ai.html
random_paper: 10
rate_limits:
- limit_count: 3
  name: Cdw Rate Limits
  slug: cdw-rate-limits
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 12.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/cdw/refs/heads/main/screenshots/cdw-2026-06-20T174108.png
security:
- kind: domain-security
  name: Cdw Domain Security
  slug: cdw-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Cdw Trust Center
  slug: cdw-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA
slug: cdw
tags:
- B2B
- Catalog
- eProcurement
- IT Distribution
- Punchout
- Technology
- Fortune 500
website: https://www.cdw.com
---
