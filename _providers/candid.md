---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Candid Agentic Access
  operation_count: 7
  slug: candid-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 9
apis:
- description: Deep nonprofit profile data. Returns comprehensive records for a given organization including financials, programs, leadership, board, grants received and awarded, operating details, affiliations, and
  name: Candid Premier API
  slug: premier-api
- description: 'Real-time nonprofit verification and compliance screening used for due diligence, donation compliance, and tax-deductibility checks. Returns IRS 501(c)(3) status, revocation history, public-charity / '
  name: Candid Charity Check API
  slug: charity-check-api
- description: Structured demographic data voluntarily provided by nonprofits about their staff, board, and populations served. Enables funders and platforms to analyze equity, diversity, and inclusion across the so
  name: Candid Demographics API
  slug: demographics-api
- description: Access to Candid's global grants dataset — summary statistics, funders, recipients, and individual transaction records. Useful for philanthropic benchmarking, funder research, and grant-market intelli
  name: Candid Grants API
  slug: grants-api
- description: Search and retrieve philanthropic news content from Candid's curated news database covering funders, grantees, sector trends, and policy. Supports customizable parameters for date range, topic, geogra
  name: Candid News API
  slug: news-api
- description: 'Returns Candid''s philanthropic classification system (subject, population, support-strategy, and geographic area taxonomies) so integrators can consistently tag and query nonprofit, grant, and funder '
  name: Candid Taxonomy API
  slug: taxonomy-api
- description: Evaluates whether a given nonprofit is eligible to receive a grant or donation based on configurable rules — IRS status, country, OFAC, custom program criteria — to automate grantmaking and giving wor
  name: Candid Nonprofit Eligibility API
  slug: nonprofit-eligibility-api
- description: Operations for retrieving lookup values and filter metadata.
  name: Candid Lookup API
  slug: candid-lookup-api
- description: Operations for searching the Candid nonprofit database.
  name: Candid Search API
  slug: candid-search-api
artifact_total: 16
collections:
- collection_type: open
  name: Candid Essentials API
  slug: open-candid-essentials-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/candid-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/candid-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/candid-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CandidOrg
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/candiddotorg
- group: company
  title: ''
  type: Website
  url: https://candid.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.candid.org/
- group: start
  title: ''
  type: DataPortal
  url: https://data.candid.org/reference/welcome-to-candids-data-portal
- group: other
  title: ''
  type: APIsOverview
  url: https://candid.org/use-our-data
- group: commercial
  title: ''
  type: PricingAndAccess
  url: https://candid.org/use-our-data
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://candid.org/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://candid.org/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://help.candid.org/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.candid.org/llms.txt
created: '2025-03-01'
description: Candid (formed from the 2019 merger of Foundation Center and GuideStar) helps social sector organizations advance their missions by sharing information, breaking down barriers, and improving giving. Candid maintains the most comprehensive set of data on U.S. nonprofits, foundations, grants, and philanthropy, and exposes that data through a family of developer APIs — Essentials, Premier, Charity Check, Demographics, Grants, News, Taxonomy, Eligibility, and PDF/Bulk variants — available through the Candid Developer Portal.
finops:
- name: Candid Finops
  service_category: API
  slug: candid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/candid.png
layout: provider
modified: '2026-05-19'
name: Candid
nav: Providers
network: true
overview: 'Candid publishes 2 APIs on the [APIs.io](https://apis.io/) network: Lookup API and Search API. Tagged areas include Charities, Donations, Non-Profits, Philanthropy, and Foundations.


  Candid''s developer surface includes authentication, support, and 12 more developer resources.'
plans:
- name: Candid Plans Pricing
  plan_count: 3
  slug: candid-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 5
  name: Candid Rate Limits
  slug: candid-rate-limits
score:
  band: developing
  composite: 44.1
  delta: -2.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 60.2
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/candid/refs/heads/main/screenshots/candid-2026-06-20T173922.png
security:
- kind: authentication
  name: Candid Authentication
  slug: candid-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Candid Domain Security
  slug: candid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: candid
tags:
- Charities
- Donations
- Non-Profits
- Philanthropy
- Foundations
- Grants
- 990s
- Demographics
website: https://candid.org
---
