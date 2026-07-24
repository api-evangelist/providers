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
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Chief Financial Officers Council Agentic Access
  operation_count: 14
  slug: chief-financial-officers-council-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 13
apis:
- description: The cfo.gov public website is the official portal for the federal CFO Council, hosting member rosters, council news, working-group outputs, financial-management policy guidance, and links to companion
  name: CFO Council Website
  slug: cfoc-website
- description: The CFO Council operates topical working groups covering areas such as financial systems, internal control, grants management, payment integrity, financial reporting, and data analytics. Working-group
  name: CFO Council Working Groups
  slug: cfoc-working-groups
- description: PaymentAccuracy.gov is the OMB-maintained transparency site for reporting government-wide improper payments and payment-integrity activities. The site publishes downloadable agency-level payment accur
  name: PaymentAccuracy.gov (Payment Integrity)
  slug: cfoc-payment-integrity
- description: USAspending.gov is the Treasury-operated public source of accountable federal spending data, exposing a comprehensive REST API for federal awards, contracts, grants, sub-awards, and agency budget data
  name: USAspending.gov API (Treasury)
  slug: usaspending
- description: Performance.gov is the OMB-administered public site for federal cross-agency priority goals, agency strategic plans, and performance reports. The CFO Council collaborates with OMB on financial-managem
  name: MAX.gov / Performance.gov
  slug: max-gov
- description: The Agencies API from Chief Financial Officers Council — 2 operation(s) for agencies.
  name: Chief Financial Officers Council Agencies API
  slug: chief-financial-officers-council-agencies-api
- description: The Awards API from Chief Financial Officers Council — 3 operation(s) for awards.
  name: Chief Financial Officers Council Awards API
  slug: chief-financial-officers-council-awards-api
- description: The Downloads API from Chief Financial Officers Council — 1 operation(s) for downloads.
  name: Chief Financial Officers Council Downloads API
  slug: chief-financial-officers-council-downloads-api
- description: The Federal Accounts API from Chief Financial Officers Council — 1 operation(s) for federal accounts.
  name: Chief Financial Officers Council Federal Accounts API
  slug: chief-financial-officers-council-federal-accounts-api
- description: The Recipients API from Chief Financial Officers Council — 2 operation(s) for recipients.
  name: Chief Financial Officers Council Recipients API
  slug: chief-financial-officers-council-recipients-api
- description: The References API from Chief Financial Officers Council — 2 operation(s) for references.
  name: Chief Financial Officers Council References API
  slug: chief-financial-officers-council-references-api
- description: The Search API from Chief Financial Officers Council — 3 operation(s) for search.
  name: Chief Financial Officers Council Search API
  slug: chief-financial-officers-council-search-api
- description: The Subawards API from Chief Financial Officers Council — 1 operation(s) for subawards.
  name: Chief Financial Officers Council Subawards API
  slug: chief-financial-officers-council-subawards-api
artifact_total: 19
collections:
- collection_type: open
  name: USAspending.gov API (CFO Council context)
  slug: open-chief-financial-officers-council
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chief-financial-officers-council-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chief-financial-officers-council-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cfo.gov/
- group: company
  title: ''
  type: About
  url: https://www.cfo.gov/about-the-council/
- group: other
  title: ''
  type: Resources
  url: https://www.cfo.gov/resources/
- group: other
  title: ''
  type: WorkingGroups
  url: https://www.cfo.gov/working-groups/
- group: company
  title: ''
  type: News
  url: https://www.cfo.gov/news/
- group: other
  title: ''
  type: Events
  url: https://www.cfo.gov/events/
- group: other
  title: ''
  type: Members
  url: https://www.cfo.gov/members/
- group: operate
  title: ''
  type: Contact
  url: mailto:CFOC.support@gsa.gov
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cfo.gov/privacy-policy/
- group: other
  title: ''
  type: AccessibilityStatement
  url: https://www.cfo.gov/accessibility/
- group: other
  title: ''
  type: USAspending
  url: https://www.usaspending.gov/
- group: other
  title: ''
  type: PaymentAccuracy
  url: https://www.paymentaccuracy.gov/
- group: other
  title: ''
  type: PerformanceGov
  url: https://www.performance.gov/
- group: other
  title: ''
  type: OMB
  url: https://www.whitehouse.gov/omb/
- group: other
  title: ''
  type: Treasury
  url: https://home.treasury.gov/
- group: other
  title: ''
  type: GSA
  url: https://www.gsa.gov/
- group: other
  title: ''
  type: ProgramAreas
  url: ''
- group: other
  title: ''
  type: WorkingGroups
  url: ''
created: '2024-12-03'
description: The Chief Financial Officers Council (CFOC) was established by the Chief Financial Officers (CFO) Act of 1990 (Public Law 101-576) and is composed of the CFOs and Deputy CFOs of the 24 largest federal departments and agencies, along with senior officials from the Office of Management and Budget (OMB) and the Department of the Treasury. The Council works collaboratively to improve federal financial management through shared guidance, working groups, and inter-agency standards. While the CFO Council itself does not operate a developer API program, its remit is closely tied to the larger ecosystem of federal financial management data and APIs administered by Treasury (USAspending.gov, Fiscal Service), OMB (PaymentAccuracy.gov, MAX.gov), and GSA (Performance.gov, SAM.gov).
finops:
- name: Chief Financial Officers Council Finops
  service_category: API
  slug: chief-financial-officers-council-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chief-financial-officers-council.png
layout: provider
modified: '2026-04-23'
name: Chief Financial Officers Council
nav: Providers
network: true
overview: 'Chief Financial Officers Council publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Agencies API, Awards API, Downloads API, and 5 more. Tagged areas include Federal Financial Management, Federal Government, Finance, Government, and OMB.


  Chief Financial Officers Council''s developer surface includes product news and 17 more developer resources.'
plans:
- name: Chief Financial Officers Council Plans Pricing
  plan_count: 3
  slug: chief-financial-officers-council-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Chief Financial Officers Council Rate Limits
  slug: chief-financial-officers-council-rate-limits
score:
  band: thin
  composite: 30.6
  delta: -1.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 45.1
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 32.1
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 21.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Chief Financial Officers Council Domain Security
  slug: chief-financial-officers-council-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chief-financial-officers-council
tags:
- Federal Financial Management
- Federal Government
- Finance
- Government
- OMB
- Treasury
website: https://www.cfo.gov/
---
