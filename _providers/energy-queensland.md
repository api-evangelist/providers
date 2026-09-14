---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Energy Queensland Agentic Access
  operation_count: 27
  slug: energy-queensland-agentic-access
  summary_line: 27 operations
api_count: 2
apis:
- baseURL: https://cdr.energymadeeasy.gov.au/ergon/cds-au/v1
  baseurl_source: declared
  description: Data Holder Customer endpoints
  name: Energy Queensland Data Holder Customers API
  slug: energy-queensland-data-holder-customers-api
- baseURL: https://cdr.energymadeeasy.gov.au/ergon/cds-au/v1
  baseurl_source: declared
  description: Data Holder Operations endpoints
  name: Energy Queensland Data Holder Operations API
  slug: energy-queensland-data-holder-operations-api
- baseURL: https://cdr.energymadeeasy.gov.au/ergon/cds-au/v1
  baseurl_source: declared
  description: Distributed Energy Resource endpoints
  name: Energy Queensland Distributed Energy Resources API
  slug: energy-queensland-distributed-energy-resources-api
- baseURL: https://cdr.energymadeeasy.gov.au/ergon/cds-au/v1
  baseurl_source: declared
  description: Electricity Service Point endpoints
  name: Energy Queensland Electricity Service Points API
  slug: energy-queensland-electricity-service-points-api
- baseURL: https://cdr.energymadeeasy.gov.au/ergon/cds-au/v1
  baseurl_source: declared
  description: Electricity Usage endpoints
  name: Energy Queensland Electricity Usage API
  slug: energy-queensland-electricity-usage-api
- baseURL: https://cdr.energymadeeasy.gov.au/ergon/cds-au/v1
  baseurl_source: declared
  description: Energy Account Balance endpoints
  name: Energy Queensland Energy Account Balances API
  slug: energy-queensland-energy-account-balances-api
- baseURL: https://cdr.energymadeeasy.gov.au/ergon/cds-au/v1
  baseurl_source: declared
  description: Energy Account Billing endpoints
  name: Energy Queensland Energy Account Billing API
  slug: energy-queensland-energy-account-billing-api
- baseURL: https://cdr.energymadeeasy.gov.au/ergon/cds-au/v1
  baseurl_source: declared
  description: Energy Account endpoints
  name: Energy Queensland Energy Accounts API
  slug: energy-queensland-energy-accounts-api
- baseURL: https://cdr.energymadeeasy.gov.au/ergon/cds-au/v1
  baseurl_source: declared
  description: Energy Plan endpoints
  name: Energy Queensland Energy Plans API
  slug: energy-queensland-energy-plans-api
artifact_total: 16
collections:
- collection_type: open
  name: CDR Common API
  slug: open-energy-queensland-cds-common
- collection_type: open
  name: CDR Energy API
  slug: open-energy-queensland-cds-energy
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/energy-queensland-read-ergon-tariff-plans.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/energy-queensland-check-cdr-availability.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/energy-queensland-consume-accredited-energy-data.md
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/energy-queensland-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/energy-queensland-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/energy-queensland-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/energy-queensland-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/energy-queensland-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/energy-queensland-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/energy-queensland-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/energy-queensland-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://public.cdr.ergonretail.com.au/cds-au/v1/discovery/status
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/includes/endpoint-version-schedule/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/energy-queensland-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/energy-queensland-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/energy-queensland-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/energy-queensland-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/energy-queensland-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/energy-queensland-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/energy-queensland-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/energy-queensland-cds-energy-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/energy-queensland-cds-common-overlay.yaml
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#energy-apis
- group: company
  title: ''
  type: Website
  url: https://www.energyq.com.au/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Energy-Queensland
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/company/energyq
- group: operate
  title: ''
  type: Status
  url: https://public.cdr.ergonretail.com.au/cds-au/v1/discovery/status
- group: start
  title: ''
  type: Registry
  url: https://api.cdr.gov.au/cdr-register/v1/energy/data-holders/brands/summary
- group: docs
  title: ''
  type: Documentation
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: other
  title: ''
  type: Data
  url: https://www.data.qld.gov.au/dataset/ergon-energy-electrical-distribution-network-series
- group: other
  title: ''
  type: Regulatory
  url: https://www.accc.gov.au/public-registers/exemption-for-ergon-energy-queensland-pty-ltd
created: '2026-07-27'
description: 'Energy Queensland Limited is the Queensland Government-owned corporation formed on 30 June 2016 by merging Ergon Energy and Energex. It is the whole Queensland electricity value chain below transmission in a single holding company: Energex distributes to roughly 1.5 million connections across South East Queensland, Ergon Energy Network distributes across regional Queensland, Ergon Energy Retail is the notified-price retailer for about 760,000 regional customers, Yurika sells energy services and telecommunications, and SPARQ Solutions provides group ICT. That dual role is what makes its API posture worth recording precisely, because the two halves of the business sit on opposite sides of a statutory line. The RETAIL half is a designated Consumer Data Right energy data holder and its implementation is verified live, not claimed: "Ergon Energy Retail" (ABN 11121177802) is listed on the ACCC CDR Register with publicBaseUri https://public.cdr.ergonretail.com.au and productBaseUri
  https://cdr.energymadeeasy.gov.au/ergon, both of which answered HTTP 200 to anonymous, standards-conformant calls on 2026-07-27, returning 36 REGULATED electricity plans and a CDS discovery status of OK. The DISTRIBUTION half - the poles and wires - is not a CDR data holder at all, publishes no developer portal, no open-data API and no machine-readable contract, and has no developer., developers., api., docs. or data. subdomain in DNS on energyq.com.au, ergon.com.au or energex.com.au. Its network data reaches the public as PDF and XLSX planning reports, registration-free but non-programmatic map viewers, and exactly one open-licensed spatial dataset deposited on the Queensland Government''s CKAN portal. The split is the finding: a mandate transplanted from banking produced a real, anonymous, standardised API on the regulated retail side and changed nothing whatsoever on the network side it never touched.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/energy-queensland.png
layout: provider
modified: '2026-07-27'
name: Energy Queensland
nav: Providers
network: true
overview: 'Energy Queensland publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Data Holder Customers API, Data Holder Operations API, Distributed Energy Resources API, and 6 more. Tagged areas include Energy, Australia, Utilities, Electricity, and Grid.


  Energy Queensland''s developer surface includes authentication, changelog, API reference, status page, documentation, and 27 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 15
  name: Energy Queensland Rate Limits
  slug: energy-queensland-rate-limits
scopes:
- name: Energy Queensland Scopes
  scope_count: 13
  slug: energy-queensland-scopes
  summary_line: 13 scopes · authorizationCode
screenshot: https://raw.githubusercontent.com/api-evangelist/energy-queensland/refs/heads/main/screenshots/energy-queensland-2026-08-07T164903.png
security:
- kind: authentication
  name: Energy Queensland Authentication
  slug: energy-queensland-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Energy Queensland Domain Security
  slug: energy-queensland-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: energy-queensland
tags:
- Energy
- Australia
- Utilities
- Electricity
- Grid
- Distribution Network
- Energy Retail
- Consumer Data Right
- CDR
- Product Reference Data
- Queensland
- Smart Metering
- Solar
- DER
- Open Data
website: https://www.energyq.com.au/
---
