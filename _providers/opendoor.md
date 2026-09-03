---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
api_count: 1
apis:
- description: 'Opendoor for Agents is the partner program that lets licensed real-estate agents submit clients to Opendoor for a cash offer, list Opendoor-owned inventory, and earn referral commissions. Integration '
  name: Opendoor for Agents
  slug: opendoor-for-agents
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendoor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.opendoor.com
- group: company
  title: ''
  type: About
  url: https://www.opendoor.com/about
- group: company
  title: ''
  type: Partners
  url: https://www.opendoor.com/agents
- group: other
  title: ''
  type: Product
  url: https://www.opendoor.com/exclusives
- group: company
  title: ''
  type: Blog
  url: https://www.opendoor.com/articles
- group: operate
  title: ''
  type: Support
  url: https://www.opendoor.com/help
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.opendoor.com
- group: company
  title: ''
  type: Careers
  url: https://www.opendoor.com/careers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opendoor-labs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.opendoor.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opendoor.com/privacy
- group: other
  title: ''
  type: X
  url: https://x.com/Opendoor
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Opendoor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/opendoor
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/opendoor
created: '2024-01-01'
description: Opendoor is an iBuyer that lets U.S. homeowners request a near-instant cash offer on their home, sell directly to Opendoor, list with Opendoor through its agent network, or browse off-market inventory via Opendoor Exclusives. Founded in 2014 and publicly traded on NASDAQ as OPEN, the company runs buying, renovation, listing, and resale at scale and partners with third-party agents and brokerages through its Opendoor for Agents program and Opendoor Exclusives marketplace. Opendoor does not publish a self-serve public developer portal or open REST API; partner and agent integrations are arranged directly through Opendoor's business development and partnerships teams. This profile documents what is publicly findable on Opendoor's partner-facing surfaces.
finops:
- name: Opendoor Finops
  service_category: API
  slug: opendoor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendoor.png
layout: provider
modified: '2026-07-25'
name: Opendoor
nav: Providers
network: true
overview: 'Opendoor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agents, Cash Offer, Exclusives, Homes, and iBuyer.


  Opendoor''s developer surface includes engineering blog, support, and 14 more developer resources.'
plans:
- name: Opendoor Plans Pricing
  plan_count: 1
  slug: opendoor-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Opendoor Rate Limits
  slug: opendoor-rate-limits
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 6
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 26.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opendoor/refs/heads/main/screenshots/opendoor-2026-06-20T190956.png
security:
- kind: domain-security
  name: Opendoor Domain Security
  slug: opendoor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: opendoor
tags:
- Agents
- Cash Offer
- Exclusives
- Homes
- iBuyer
- Listings
- Partners
- Real-Estate
website: https://www.opendoor.com
---
