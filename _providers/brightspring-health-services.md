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
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brightspring-health-services-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brightspringhealth
- group: company
  title: ''
  type: Website
  url: https://www.brightspringhealth.com
- group: start
  title: ''
  type: EmployeePortal
  url: https://reach.brightspringhealth.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.brightspringhealth.com
- group: agent
  title: ''
  type: LlmsText
  url: https://brightspringhealth.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.brightspringhealth.com/feed/
- group: design
  title: ''
  type: Conformance
  url: conformance/brightspring-health-services-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.brightspringhealth.com/compliance/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brightspringhealth.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brightspringhealth.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.brightspringhealth.com/contact-us/
coverage:
  checked: '2026-09-04'
  detail: BrightSpring's entire 633-URL corporate sitemap carries no developer, API or docs section, no api./developer./portal./fhir. subdomain resolves on brightspringhealth.com or pharmerica.com, and the one integration page any BrightSpring brand publishes (pharmerica.com/pccapi/) describes PharMerica CONSUMING PointClickCare's API rather than shipping one of its own.
  evidence:
  - status: 404
    url: https://www.brightspringhealth.com/openapi.json
  - status: 404
    url: https://www.brightspringhealth.com/.well-known/api-catalog
  - status: 200
    url: https://www.brightspringhealth.com/sitemap_index.xml
  - status: 200
    url: https://pharmerica.com/pccapi/
  reason: no-developer-program
  state: none
created: '2026-03-21'
description: 'BrightSpring Health Services is a leading Fortune 500 provider of comprehensive home and community-based health services for complex populations. The company operates across three primary service lines: Provider Services (home health, rehabilitation, neurorehabilitation, personal care), Pharmacy Services (specialty infusion, home and community-based pharmacy dispensing over 40 million prescriptions annually), and Managed Care (home-based primary care with demonstrated 44% reduction in hospitalizations). BrightSpring operates multiple clinical brands including Adoration Home Health, Amerita specialty infusion, and All Ways Caring.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brightspring-health-services.png
layout: provider
modified: '2026-09-04'
name: BrightSpring Health Services
nav: Providers
network: true
overview: 'BrightSpring Health Services is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Home Health, Healthcare, Pharmacy, Rehabilitation, and Managed Care.


  BrightSpring Health Services'' developer surface includes engineering blog, support, and 10 more developer resources.'
plans:
- name: Brightspring Health Services Plans Pricing
  plan_count: 0
  slug: brightspring-health-services-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Brightspring Health Services Rate Limits
  slug: brightspring-health-services-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/brightspring-health-services/refs/heads/main/screenshots/brightspring-health-services-2026-06-20T173702.png
security:
- kind: domain-security
  name: Brightspring Health Services Domain Security
  slug: brightspring-health-services-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brightspring-health-services
tags:
- Home Health
- Healthcare
- Pharmacy
- Rehabilitation
- Managed Care
- Fortune 500
website: https://www.brightspringhealth.com
---
