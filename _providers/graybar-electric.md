---
access_model:
  confidence: medium
  label: Gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://apiportal-snd.graybar.com/signin
  - https://apiportal-snd.graybar.com/developer/apis?api-version=2022-04-01-preview
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Graybar's Azure API Management developer portal. The portal is publicly reachable and serves a sign-in/sign-up flow and a single published product ("Starter", the Azure APIM default), but the anonymou
  name: Graybar API Portal
  slug: graybar-electric-api-portal
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.graybar.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/graybar
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/graybar
- group: operate
  title: ''
  type: Support
  url: https://www.graybar.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.graybar.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.graybar.com/website-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.graybar.com/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/graybar-electric-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/graybar-electric-llms.txt
coverage:
  checked: '2026-08-28'
  detail: Graybar runs its own Azure API Management developer portal at apiportal-snd.graybar.com, and search engines have indexed descriptions of real APIs on it (material availability by location, orders and quotes for a customer, frequently-purchased materials), but the portal's anonymous API catalog returns an empty list and /developer/identity returns 401 — every API definition, reference and specification sits behind a developer-account sign-in, so nothing is readable without credentials.
  evidence:
  - status: 200
    url: https://apiportal-snd.graybar.com/developer/apis?api-version=2022-04-01-preview
  - status: 401
    url: https://apiportal-snd.graybar.com/developer/identity?api-version=2022-04-01-preview
  - status: 200
    url: https://apiportal-snd.graybar.com/signin
  - status: 0
    url: https://b2b.graybar.com/
  reason: partner-login
  state: gated
created: '2026-03-21'
description: 'Graybar Electric Company is an employee-owned Fortune 500 distributor of electrical, communications, and data networking products and a provider of related supply chain management and logistics services. Graybar serves contractors, industrial plants, utilities, institutions and commercial customers across North America through a network of distribution centers and branches, and supports customer e-procurement through EDI, XML and PunchOut system-to-system integration. Graybar operates an Azure API Management developer portal at apiportal-snd.graybar.com, but publishes no API to anonymous visitors: the portal''s API catalog is empty without a sign-in.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/graybar-electric.png
layout: provider
modified: '2026-08-28'
name: Graybar Electric
nav: Providers
network: true
overview: 'Graybar Electric publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Distribution, Electrical, Data Networking, and Supply Chain.


  Graybar Electric''s developer surface includes support, engineering blog, and 7 more developer resources.'
plans:
- name: Graybar Electric Plans Pricing
  plan_count: 1
  slug: graybar-electric-plans-pricing
press:
- date: '2026-05-25'
  title: Graybar names a new executive for AI, digital transformation
  url: https://www.digitalcommerce360.com/2025/07/02/graybar-new-executive-ai-digital-transformation-ecommerce-growth/
- date: '2026-05-25'
  title: 2024 annual report
  url: https://www.sec.gov/Archives/edgar/data/205402/000020540225000017/Graybar_2024_ARS_Flatnd.pdf
- date: '2026-05-25'
  title: 'Graybar Electric: Seven Steps to Industry 4.0'
  url: https://www.proquest.com/docview/2333685394/2D3102A2EC9D415APQ/3
- date: '2026-05-25'
  title: Information Statement (Form DEF 14C)
  url: https://www.publicnow.com/view/4314BC4AFE8EA53637A0863B509C926C0645572D
- date: '2026-05-25'
  title: Explore how Graybar stays connected to customers
  url: https://www.sap.com/asset/dynamic/2025/03/febfef39-f87e-0010-bca6-c68f7e60039b.html
random_paper: 15
rate_limits:
- limit_count: 2
  name: Graybar Electric Rate Limits
  slug: graybar-electric-rate-limits
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 12
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 23.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Graybar Electric Domain Security
  slug: graybar-electric-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: graybar-electric
tags:
- Fortune 500
- Distribution
- Electrical
- Data Networking
- Supply Chain
- Logistics
- B2B eCommerce
- EDI
- Punchout
- Industrial
website: https://www.graybar.com
---
