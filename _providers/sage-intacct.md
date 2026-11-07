---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'Modern REST API for Sage Intacct using OAuth 2.0 Bearer token authentication. Provides standard HTTP verbs for managing core financial objects (GL, AP, AR), dimensions, customers, vendors, and custom '
  name: Sage Intacct REST API
  slug: rest-api
- description: Legacy XML API providing programmatic access to general ledger, accounts payable, accounts receivable, order entry, purchasing, inventory, projects, and platform services. Uses session-based authentic
  name: Sage Intacct XML API
  slug: xml-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/sage-intacct/security/sage-intacct-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sage-intacct-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sage-intacct/security/sage-intacct-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sage-intacct-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/intacct
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sageintacct
- group: company
  title: ''
  type: Website
  url: https://www.sage.com/en-us/sage-business-cloud/intacct/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sage.com/intacct
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sage.com/intacct/docs/
- group: operate
  title: ''
  type: Community
  url: https://developer-community.sage.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sage.com/en-us/sage-business-cloud/intacct/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.sage.com/en-us/blog/feed/
created: '2026-05-11'
description: Sage Intacct is a cloud-based financial management and accounting platform built for growing and mid-market businesses, covering core financials, multi-entity consolidations, project and revenue accounting, and advanced reporting. Sage Intacct offers both a modern REST API (OAuth 2.0) and a long-standing XML API for programmatic access to general ledger, accounts payable, accounts receivable, cash management, order entry, purchasing, and custom dimensions.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sage-intacct.png
layout: provider
modified: '2026-05-11'
name: Sage Intacct
nav: Providers
network: true
overview: 'Sage Intacct is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including REST API, and 1 more. Tagged areas include Accounting, Financial Management, ERP, General Ledger, and Accounts Payable.


  Sage Intacct''s developer surface includes documentation, pricing, engineering blog, and 7 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 24.0
    developer_ergonomics: 47.6
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 26.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sage-intacct/sage-intacct-2026-06-20T193327.png
security:
- kind: domain-security
  name: Sage Intacct Domain Security
  slug: sage-intacct-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sage Intacct Vulnerability Disclosure
  slug: sage-intacct-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sage-intacct
tags:
- Accounting
- Financial Management
- ERP
- General Ledger
- Accounts Payable
- Accounts Receivable
- Mid-Market
website: https://www.sage.com/en-us/sage-business-cloud/intacct/
---
