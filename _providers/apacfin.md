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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apacfin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apacfin.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apacfin.com/terms-and-condition
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apacfin.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://apacfin.com/contact_us
- group: company
  title: ''
  type: Blog
  url: https://apacfin.com/newsroom
- group: commercial
  title: ''
  type: Pricing
  url: https://apacfin.com/scheduleofcharge
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apacfin-llms.txt
coverage:
  checked: '2026-08-10'
  detail: APAC is an RBI-registered NBFC whose only software products are the APACM borrower app and an APAC Partner app; its website is fully open to crawlers (robots.txt allows everything) yet serves 404 at every developer, spec and .well-known path, and its five apacfin.in business systems (customerportal, partner, lms, crm, apps) are unmarketed internal applications that return a uniform AWS ALB 403 rather than any published contract.
  evidence:
  - status: 200
    url: https://apacfin.com/robots.txt
  - status: 404
    url: https://apacfin.com/developers
  - status: 404
    url: https://apacfin.com/openapi.json
  - status: 404
    url: https://apacfin.com/.well-known/security.txt
  - status: 404
    url: https://apacfin.com/.well-known/agent-card.json
  - status: 403
    url: https://customerportal.apacfin.in/
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: APAC Financial Services (Apacfin) is a Mumbai-based, Reserve Bank of India registered Non-Banking Financial Company (NBFC) that provides customized MSME business loans to underbanked and underserved micro, small, and medium enterprises across India. APAC offers tech-enabled, largely paperless digital onboarding, quick disbursal with minimal documentation, and a mobile app (APACM) for loan tracking, EMI payments, and service requests. The lender reports roughly Rs 2,479 Crore of assets under management across 226 branches in six states, serving more than 52,000 customers, and carries an ICRA A (Stable) credit rating. APAC is a portfolio company of Norwest Venture Partners. No public developer API, OpenAPI specification, or developer portal is published; customer and partner interaction is via the mobile app and hosted customer/complaint portals.
image: https://apacfin.com/media/logos/logo-1.jpg
layout: provider
modified: '2026-08-10'
name: APAC Financial Services
nav: Providers
network: true
overview: 'APAC Financial Services is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Fintech, Lending, and NBFC.


  APAC Financial Services'' developer surface includes support, engineering blog, pricing, and 5 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apacfin/refs/heads/main/screenshots/apacfin-2026-07-25T200536.png
security:
- kind: domain-security
  name: Apacfin Domain Security
  slug: apacfin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apacfin
tags:
- Company
- Financial-Services
- Fintech
- Lending
- NBFC
- MSME
- India
website: https://apacfin.com
---
