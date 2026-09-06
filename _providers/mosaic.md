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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mosaic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mosaic.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mosaictech
- group: agent
  title: ''
  type: LlmsText
  url: https://www.mosaic.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mosaic-llms.txt
- group: company
  title: ''
  type: About
  url: https://www.mosaic.com/en/who-we-are/
- group: other
  title: ''
  type: Services
  url: https://www.mosaic.com/en/what-we-do/
- group: other
  title: ''
  type: Portfolio
  url: https://www.mosaic.com/en/our-work/
- group: company
  title: ''
  type: Blog
  url: https://www.mosaic.com/en/news/
- group: company
  title: ''
  type: Careers
  url: https://www.mosaic.com/en/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.mosaic.com/en/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acosta.group/terms-and-conditions-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acosta.group/privacy-policy/
- group: other
  title: ''
  type: Accessibility
  url: https://www.acosta.group/integrated-accessibility-standards-policy/
- group: auth
  title: ''
  type: Security
  url: https://www.acosta.group/security/
- group: auth
  title: ''
  type: Compliance
  url: https://www.acosta.group/security/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mosaic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mosaic-trust-center.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mosaic-plans-pricing.yml
coverage:
  checked: '2026-08-13'
  detail: 'Mosaic sells experiential marketing, corporate events, shopper programs and outsourced retail field labor — software is not the product, so there is nothing to expose: every OpenAPI/GraphQL/MCP/.well-known probe on www.mosaic.com returns the site''s Next.js 404, developer.mosaic.com and api.mosaic.com do not resolve, and the company''s own llms.txt indexes only company, service-line, case-study, office and policy pages.'
  evidence:
  - status: 200
    url: https://www.mosaic.com/llms.txt
  - status: 404
    url: https://www.mosaic.com/openapi.json
  - status: 404
    url: https://www.mosaic.com/.well-known/agent-card.json
  - status: 200
    url: https://www.mosaic.com/sitemap-0.xml
  - status: 0
    url: https://developer.mosaic.com
  reason: not-a-software-company
  state: none
created: '2026-03-21'
description: Mosaic is a North American brand experience agency with global reach, and one of the pillar agencies of Acosta Group. It works across four service lines — experiential marketing, B2B corporate experiences and events, integrated commerce and shopper programs, and field sales and marketing — plus third-party labor, assisted selling, retail merchandising, sales training, retail execution and surge staffing for retail, B2B and CPG environments. With roots in Toronto and Dallas and offices in Jacksonville, Mosaic says it has spent more than 35 years building brand experiences designed to drive awareness, engagement, conversion and behaviour change. Mosaic publishes no developer program, API documentation or machine-readable API contract.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mosaic.png
layout: provider
modified: '2026-08-13'
name: Mosaic
nav: Providers
network: true
overview: 'Mosaic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Marketing, Brand Experience, Agency, Fortune 500, and Experiential Marketing.


  Mosaic''s developer surface includes engineering blog and 18 more developer resources.'
plans:
- name: Mosaic Plans Pricing
  plan_count: 0
  slug: mosaic-plans-pricing
press:
- date: '2026-05-25'
  title: Mosaic Insurance and DXC Technology launch innovative ...
  url: https://www.mosaicinsurance.com/resources/press-releases/~/mosaic-insurance-and-dxc-technology-launch-innovative-technology-platform-for-specialty-insurance/
- date: '2026-05-25'
  title: Adtran launches Mosaic One Clarity to transform network ...
  url: https://www.adtran.com/en/newsroom/press-releases/20251014-adtran-launches-mosaic-one-clarity-to-transform-network-operations
- date: '2026-05-25'
  title: Databricks Unveils New Mosaic AI Capabilities to Help ...
  url: https://www.databricks.com/company/newsroom/press-releases/databricks-unveils-new-mosaic-ai-capabilities-help-customers-build
- date: '2026-05-25'
  title: Mosaic Raises $18M Series A To Build AI-Driven ...
  url: https://www.prnewswire.com/news-releases/mosaic-raises-18m-series-a-to-build-ai-driven-operating-system-for-deal-makers-302749548.html
- date: '2026-05-25'
  title: MOSAIC Coalition Launches to Operationalize AI Security ...
  url: https://www.cisecurity.org/about-us/media/press-release/mosaic-coalition-launches-to-operationalize-ai-security-standards-and-reduce-industry-fragmentation
random_paper: 6
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 14.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mosaic/refs/heads/main/screenshots/mosaic-2026-06-20T185813.png
security:
- kind: domain-security
  name: Mosaic Domain Security
  slug: mosaic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mosaic Vulnerability Disclosure
  slug: mosaic-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Mosaic Trust Center
  slug: mosaic-trust-center
  summary_line: SOC 2 Type II
slug: mosaic
tags:
- Marketing
- Brand Experience
- Agency
- Fortune 500
- Experiential Marketing
- Field Marketing
- Retail Merchandising
- Integrated Commerce
- Event
website: https://www.mosaic.com
---
