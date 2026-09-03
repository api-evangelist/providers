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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 12.9
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lvmh-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lvmh-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lvmh-group
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lvmh
- group: company
  title: ''
  type: Website
  url: https://www.lvmh.com/
- group: company
  title: ''
  type: AboutUs
  url: https://www.lvmh.com/en/our-group
- group: other
  title: ''
  type: Brands
  url: https://www.lvmh.com/en/our-maisons
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.lvmh.com/en/investors
- group: company
  title: ''
  type: News
  url: https://www.lvmh.com/en/news-documents
- group: other
  title: ''
  type: Sustainability
  url: https://www.lvmh.com/en/our-commitments
- group: company
  title: ''
  type: Careers
  url: https://www.lvmhcareers.com/
- group: other
  title: ''
  type: Innovation
  url: https://www.lvmh.com/en/news-documents/lvmh-innovation
- group: other
  title: ''
  type: BlockchainConsortium
  url: https://auraconsortium.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://www.lvmh.com/llms.txt
- group: docs
  title: ''
  type: GraphQL
  url: graphql/lvmh-graphql.md
created: '2026-05-05'
description: LVMH Moët Hennessy Louis Vuitton is the world's largest luxury goods conglomerate, headquartered in Paris and operating over 75 prestigious brands. Its portfolio spans fashion and leather goods (Louis Vuitton, Christian Dior, Fendi, Loewe, Celine), wines and spirits (Moët & Chandon, Hennessy, Veuve Clicquot), perfumes and cosmetics (Givenchy, Guerlain), watches and jewelry (Tiffany & Co., Bulgari, TAG Heuer), and selective retailing (Sephora, DFS). LVMH does not currently publish a public developer API or developer portal at the group level; technical and partner integrations are handled brand-by-brand and through closed innovation partnerships such as the Aura Blockchain Consortium.
graphqls:
- description: This document describes a conceptual GraphQL schema for LVMH Moet Hennessy Louis Vuitton, the world's largest luxury goods conglomerate. LVMH does not currently publish a public developer API at the g
  name: LVMH GraphQL Schema
  slug: lvmh-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lvmh.png
layout: provider
modified: '2026-05-16'
name: LVMH
nav: Providers
network: true
overview: 'LVMH is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cosmetics, Fashion, Jewelry, Luxury, and Retail.


  LVMH''s developer surface includes product news and 14 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 15.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lvmh/refs/heads/main/screenshots/lvmh-2026-07-25T225802.png
security:
- kind: domain-security
  name: Lvmh Domain Security
  slug: lvmh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lvmh Vulnerability Disclosure
  slug: lvmh-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lvmh
tags:
- Cosmetics
- Fashion
- Jewelry
- Luxury
- Retail
- Wine and Spirits
website: https://www.lvmh.com/
---
