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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
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
- group: auth
  title: ''
  type: TrustCenter
  url: security/cdw-trust-center.yml
- group: auth
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
- name: Cdw Finops
  service_category: IT Distribution + eProcurement
  slug: cdw-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cdw.png
layout: provider
modified: '2026-04-23'
name: CDW
nav: Providers
network: true
overview: 'CDW publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include B2B, Catalog, eProcurement, IT Distribution, and Punchout.


  CDW''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Cdw Plans Pricing
  plan_count: 1
  slug: cdw-plans-pricing
press:
- date: '2026-05-25'
  title: 2025 CDW AI Report
  url: https://www.cdw.com/content/cdw/en/solutions/artificial-intelligence-ai/2025-cdw-ai-report.html
- date: '2026-05-25'
  title: Lessons Learned From CDW's AI Research Report
  url: https://healthtechmagazine.net/article/2025/07/lessons-learned-cdws-ai-research-report
- date: '2026-05-25'
  title: Mission, a CDW Company, Achieves AWS Agentic AI ...
  url: https://www.prnewswire.com/news-releases/mission-a-cdw-company-achieves-aws-agentic-ai-specialization-expanding-enterprise-ai-capabilities-302626953.html
- date: '2026-05-25'
  title: CDW LLC - Financials - Quarterly Results
  url: https://investor.cdw.com/financials/quarterly-results/
- date: '2026-05-25'
  title: Artificial Intelligence (AI) Solutions
  url: https://www.cdw.com/content/cdw/en/solutions/ai-and-data/artificial-intelligence-ai.html
random_paper: 3
rate_limits:
- limit_count: 3
  name: Cdw Rate Limits
  slug: cdw-rate-limits
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 9
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
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
