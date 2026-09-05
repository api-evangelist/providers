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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'Anixter (now part of Wesco International) provides B2B eCommerce integration services including EDI (Electronic Data Interchange) for purchase orders, invoices, and shipping notices, punchout catalog '
  name: Anixter eCommerce Integration API
  slug: anixter-ecommerce-integration-api
artifact_total: 5
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/wesco-international/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anixter-international-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wescoanixter
- group: company
  title: ''
  type: Website
  url: https://www.anixter.com/en_us.html
- group: company
  title: ''
  type: Website
  url: https://www.wesco.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.anixter.com/en_us/services-and-solutions/supply-chain-services/ecommerce/integrations.html
- group: start
  title: ''
  type: Portal
  url: https://www.anixter.com/en_us/services-and-solutions/supply-chain-services/ecommerce.html
- group: other
  title: ''
  type: Announcement
  url: https://www.wesco.com/us/en/our-company/news-and-insights/press-releases/new-wesco-anixter-brand-underscores-commitment-to-innovation.html
- group: other
  title: ''
  type: Announcement
  url: https://www.anixter.com/en_mx/about-us/news-and-events/news/wesco-international-announces-completion-of-merger-with-anixter-.html
- group: operate
  title: ''
  type: Contact
  url: https://www.anixter.com/en_us/about-us/contact.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anixter-international-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/anixter-international-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/anixter-international-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/anixter-international-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/anixter-international-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/anixter-international-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/anixter-international-packages.yml
coverage:
  checked: '2026-09-02'
  detail: Anixter runs a real MuleSoft Anypoint API platform — api.wesco.com resolves to api-wesco.lb.anypointdns.net and the Anypoint Exchange organization domain "anixter" has its public portal switched on — but that portal publishes zero public assets, so every API asset sits behind an Anypoint login, and the eCommerce integrations page that describes the EDI and punchout surface answers 403 behind a Cloudflare managed challenge on top of it.
  evidence:
  - status: 200
    url: https://anypoint.mulesoft.com/exchange/api/v2/portals/anixter
  - status: 200
    url: https://anypoint.mulesoft.com/exchange/api/v2/assets?domain=anixter&limit=50
  - status: 404
    url: https://anypoint.mulesoft.com/exchange/api/v2/portals/zzznotarealportal12345
  - status: 403
    url: https://www.anixter.com/en_us/services-and-solutions/supply-chain-services/ecommerce/integrations.html
  - status: 404
    url: https://api.wesco.com/.well-known/api-catalog
  reason: partner-login
  state: gated
created: '2026-03-23'
description: Anixter International was a leading global distributor of network and security solutions, electrical and electronic solutions, and utility power solutions. In June 2020, Anixter was acquired by Wesco International for approximately $4.5 billion, creating a combined company with over $17 billion in annual revenue. Anixter now operates as Wesco Anixter, providing B2B distribution, supply chain services, and digital integration capabilities including EDI, punchout catalogs, and procurement system integrations.
finops:
- name: Anixter International Finops
  service_category: API
  slug: anixter-international-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/anixter-international.png
layout: provider
modified: '2026-09-02'
name: Anixter International
nav: Providers
network: true
overview: 'Anixter International publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include B2B Commerce, Cables, Data Communications, Distribution, and Electrical.


  Anixter International''s developer surface includes documentation, developer portal, and 15 more developer resources.'
plans:
- name: Anixter International Plans Pricing
  plan_count: 0
  slug: anixter-international-plans-pricing
press:
- date: '2026-05-25'
  title: WESCO International and Anixter ...
  url: https://www.prnewswire.com/news-releases/wesco-international-and-anixter-international-announce-merger-agreement-to-create-a-premier-electrical-and-data-communications-distribution-and-supply-chain-services-company-300985474.html
- date: '2026-05-25'
  title: What's New
  url: https://www.anixter.com/en_gb/about-us/news-and-events/news.html
- date: '2026-05-25'
  title: WESCO International Announces Completion of Merger ...
  url: https://www.sdmmag.com/articles/98194-wesco-international-announces-completion-of-merger-with-anixter
- date: '2026-05-25'
  title: XBRL Viewer
  url: https://www.sec.gov/ix?doc=/Archives/edgar/data/52795/000119312519324432/d860223d8k.htm
- date: '2026-05-25'
  title: Anixter International Inc. Announces the Acquisition of Tri-Ed
  url: https://securitytoday.com/articles/2014/08/11/anixter-international-inc-announces-the-acquisition-of-tri-ed.aspx?admgarea=ht.accesscontrol
random_paper: 3
rate_limits:
- limit_count: 0
  name: Anixter International Rate Limits
  slug: anixter-international-rate-limits
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 14.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anixter-international/refs/heads/main/screenshots/anixter-international-2026-06-20T172016.png
security:
- kind: domain-security
  name: Anixter International Domain Security
  slug: anixter-international-domain-security
  summary_line: TLSv1.2 · DMARC
slug: anixter-international
tags:
- B2B Commerce
- Cables
- Data Communications
- Distribution
- Electrical
- Industrial
- Network Infrastructure
- Security Solutions
- Supply Chain
- Wesco
- Fortune 500
website: https://www.anixter.com/en_us.html
---
